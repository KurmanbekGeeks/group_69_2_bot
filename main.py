from aiogram import F, Bot, Dispatcher, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from decouple import config
import asyncio
import logging

token_bot = config("TOKEN")
# print(token_bot)

bot = Bot(token=token_bot)
dp = Dispatcher()

router_main = Router()

dp.include_router(router=router_main)

@router_main.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(text='Привет')

@router_main.message(Command('help'))
async def help_handler(message: Message):
    await bot.send_message(chat_id=message.chat.id, text='Первый бот группы 69-2')


@router_main.message(F.text == 'привет')
async def hello_text_handler(message: Message):
    await message.answer('hello')


@router_main.message(Command('mem'))
async def mem_handler(message: Message):
    photo_mem = FSInputFile('media/mem.png')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_mem)


@router_main.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker('CAACAgIAAxkBAAMjapbjokNBT2YjOMt9wh5q_5HZtpIAAuMAA1eEbA_LD3f9g8IMvD0E')

    await message.answer_sticker('CAACAgIAAxkBAAMnapbkCM4uItEY8u7AtfAwChFY6Z0AAiqNAAJBuqlLZqmYVBFV9sw9BA')


@router_main.message(F.sticker)
async def get_sticker_id_handler(message: Message):
    await message.answer(f'ID - этого стикера - {message.sticker.file_id}')


@router_main.message(F.text)
async def echo_handler(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))