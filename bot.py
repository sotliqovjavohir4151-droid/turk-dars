from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8564026272:AAGFcUZO7hK8OhX4RIZoy4Ap8be5eYa-6PI"

bot = Bot("8564026272:AAGFcUZO7hK8OhX4RIZoy4Ap8be5eYa-6PI")
dp = Dispatcher(bot)

# ====== ODDIY TUGMALAR ======
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

btn1 = KeyboardButton("📘 Ma'lumot")
btn2 = KeyboardButton("📞 Aloqa")

keyboard.add(btn1, btn2)

# ====== INLINE WEB TUGMA (MINI APP) ======
web = InlineKeyboardMarkup()
web.add(
    InlineKeyboardButton(
        "🌐 Darslarni ochish",
        web_app=WebAppInfo(url="https://sotliqovjavohir4151-droid.github.io/turk-dars/")
    )
)

# ====== /START ======
@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("Salom! Tugmani tanlang 👇", reply_markup=keyboard)
    await msg.answer("Turk tili darslarini ochish:", reply_markup=web)

# ====== XABARLAR ======
@dp.message_handler()
async def echo(msg: types.Message):
    if msg.text == "📘 Ma'lumot":
        await msg.answer("Bu turk tili o‘rgatuvchi bot 📚")

    elif msg.text == "📞 Aloqa":
        await msg.answer("Admin: @username")

# ====== ISHGA TUSHIRISH ======
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)






