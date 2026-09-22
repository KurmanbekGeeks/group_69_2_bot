from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database import db
from config import staff_code

router_staff = Router()


class RegisterStaff(StatesGroup):
    code = State()


@router_staff.message(Command('register_staff'))
async def register_start(message: Message, state: FSMContext):
    if await db.is_staff_db(message.from_user.id):
        await message.answer('Вы уже зарегистрированы как сотрудник.')
        return
    else: 
        await message.answer('Введите код регистрации:')
        await state.set_state(RegisterStaff.code)


@router_staff.message(RegisterStaff.code, F.text)
async def register_check_code(message: Message, state: FSMContext):
    if message.text.strip() == staff_code:
        await db.add_staff_db(
            user_id=message.from_user.id,
            full_name=message.from_user.full_name
        )
        await message.answer('Готово! Теперь доступны добавление и редактирование товаров. ')
    else:
        await message.answer('Неверный код. Попробуйте снова: /register')

    await state.clear()

