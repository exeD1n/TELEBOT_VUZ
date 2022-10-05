from auth import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard

#Семихвостов

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


@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Учитель':
        check_lab_teatcher = KeyboardButton('Просмотр лабораторных работ')
        change_lab_teatcher = KeyboardButton('Изменение лабораторных работ')
        add_evaluation_teatcher = KeyboardButton('Добавить (изменить) оценку ученику')
        back = KeyboardButton('Назад')
        button_teatcher = ReplyKeyboardMarkup().add(check_lab_teatcher).add(change_lab_teatcher).add(add_evaluation_teatcher).add(back)
        await message.reply("", reply_markup=button_teatcher)

    elif message.text == 'Студент':
        await message.reply("", reply_markup=types.ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)