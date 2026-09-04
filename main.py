import asyncio
import logging
from config import bot, dp, Admin
from handlers import commands, echo, fsm_add_products
from aiogram.types import BotCommand



async def set_commands():
    commands = [
        BotCommand(command='start', description='Старт бота'),
        BotCommand(command='help', description='helper'),
        BotCommand(command='mem', description='фотка мема'),
        BotCommand(command='sticker', description='отправка стикеров'),
        BotCommand(command='add_product', description='заполнения нового товара'),
    ]
    await bot.set_my_commands(commands)

async def on_startup():
    await set_commands()
    for admin_id in Admin:
        await bot.send_message(chat_id=admin_id, text='Бот включен!')

dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm_add_products.router_addproduct)
dp.include_router(router=echo.router_echo)


dp.startup.register(on_startup)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
