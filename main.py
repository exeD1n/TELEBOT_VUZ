from auth import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard

API_TOKEN = TOKEN

# Инициальзация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Приветствие пользователя
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Учитель")],
        [types.KeyboardButton(text="Студент")]
    ]
    keyboardStart = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.reply("Привет👋\nКем вы являетесь?", reply_markup=keyboardStart)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)