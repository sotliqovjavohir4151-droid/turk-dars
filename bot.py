from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

TOKEN = "8564026272:AAGFcUZO7hK8OhX4RIZoy4Ap8be5eYa-6PI"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ODDIY TUGMALAR
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    KeyboardButton("📘 Ma'lumot"),
    KeyboardButton("📞 Aloqa")
)

# INLINE WEB TUGMA
web = InlineKeyboardMarkup()
web.add(
    InlineKeyboardButton(
        "🌐 Darslarni ochish",
        web_app=WebAppInfo(url="https://sotliqovjavohir4151-droid.github.io/turk-dars/web/")
    )
)

# START
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Salom! Tugmani tanlang 👇", reply_markup=keyboard)
    await message.answer("Turk tili darslarini ochish:", reply_markup=web)

# MA'LUMOT
@dp.message_handler(lambda m: m.text == "📘 Ma'lumot")
async def info(message: types.Message):
    await message.answer("Bu turk tili o‘rganish mini ilovasi.")

# ALOQA
@dp.message_handler(lambda m: m.text == "📞 Aloqa")
async def contact(message: types.Message):
    await message.answer("Admin: @sotliqov")

# ISHGA TUSHIRISH
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
