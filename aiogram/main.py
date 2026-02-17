from aiogram import Bot, Dispatcher
from handlers import main_router
import asyncio, logging


bot = Bot(token="")
dp = Dispatcher()

dp.include_router(main_router)


async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Bot stopped with error: {e}")


if __name__ == '__main__':
    asyncio.run(main())