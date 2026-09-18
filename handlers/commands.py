from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from config import bot
from database import db
from handlers import buttons

router_commands = Router()

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(text=f'Привет, твой id {message.from_user.id}')

@router_commands.message(Command('help'))
async def help_handler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Первый бот группы 69-2')


@router_commands.message(F.text == 'привет')
async def hello_text_handler(message: Message):
    await message.answer('hello')


@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo_mem = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_mem)


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMjapbjokNBT2YjOMt9wh5q_5HZtpIAAuMAA1eEbA_LD3f9g8IMvD0E')

    await message.answer_sticker('CAACAgIAAxkBAAMnapbkCM4uItEY8u7AtfAwChFY6Z0AAiqNAAJBuqlLZqmYVBFV9sw9BA')


@router_commands.message(F.sticker)
async def get_sticker_id_handler(message: Message):
    await message.answer(f'ID - этого стикера - {message.sticker.file_id}')


@router_commands.message(Command('products'))
async def get_products(message: Message):
    products = await db.get_products_db()

    if not products:
        await message.answer('В базе данных товаров нет!')
        return
    else:
        for name, price, description, category, product_id, photo in products:
            await message.answer_photo(photo=photo, 
                                       caption=f'Название - {name} \nЦена - {price} \nОписание - {description} \nКатегория - {category} \nАртикул - {product_id}', 
                                       reply_markup=buttons.product_actions(product_id=product_id))