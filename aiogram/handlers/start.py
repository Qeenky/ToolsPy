from aiogram import types
from aiogram import Router
from aiogram.filters import Command


user_router = Router()

@user_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.first_name}! Вы успешно зарегистрированы.")
