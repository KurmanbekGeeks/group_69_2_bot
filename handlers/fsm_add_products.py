from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import db

class AddProduct(StatesGroup):
    name = State()
    price = State()
    description = State()
    product_id = State()    #артикул
    category = State()
    photo = State()


router_addproduct = Router()


@router_addproduct.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):

    staff = await db.get_staff_list_db()
    staff_ids = [user_id for user_id, full_name in staff]

    if message.from_user.id in staff_ids:
        await message.answer('Введите название товара:')
        await state.set_state(AddProduct.name)
    else: 
         await message.answer('У вас нет доступов к этой команде!')


@router_addproduct.message(AddProduct.name)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара:')
    await state.set_state(AddProduct.price)


@router_addproduct.message(AddProduct.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Напишите описание товара:")
    await state.set_state(AddProduct.description)


@router_addproduct.message(AddProduct.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Введите артикул для товара. Он должен быть уникальным!')
    await state.set_state(AddProduct.product_id)


@router_addproduct.message(AddProduct.product_id)
async def add_product_id(message: Message, state: FSMContext):
    await state.update_data(product_id=message.text)
    await message.answer('Введите категорию')
    await state.set_state(AddProduct.category)

@router_addproduct.message(AddProduct.category)
async def add_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.answer('Отправьте фото товара')
    await state.set_state(AddProduct.photo)

@router_addproduct.message(AddProduct.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)

    data = await state.get_data()

    await message.answer_photo(photo=data['photo'], 
                               caption=f"Данные товара: "
                                f"\nНазвание - {data['name']}"
                                f"\nЦена - {data['price']} "
                                f"\nОписание - {data['description']}" 
                                f"\nАртикул - {data['product_id']}"
                                f"\nКатегория - {data['category']}")

    await db.add_product_db(name=data['name'], price=data['price'], description=data['description'], 
                         product_id=data['product_id'], category=data['category'], photo=data['photo'])
    
    await state.clear()

