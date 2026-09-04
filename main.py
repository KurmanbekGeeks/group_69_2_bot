import asyncio
import logging
from config import bot, dp
from handlers import commands, echo, fsm_add_products


dp.include_router(router=commands.router_commands)

dp.include_router(router=echo.router_echo)

dp.include_router(router=fsm_add_products.router_addproduct)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
