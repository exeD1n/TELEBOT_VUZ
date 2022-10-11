from cgitb import text
from auth import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard
from database import name_group, name_subject

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
    await message.answer(f'Привет {message.from_user.full_name} 👋\nКем вы являетесь?', reply_markup=keyboardStart)
    
    
# Выбор кнопки для студента
@dp.message_handler(text = "Студент")
async def echo(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Успеваемость"),
            types.KeyboardButton(text="Лобораторные")
        ],
        [
            types.KeyboardButton(text = 'Меню'),
        ]
    ]
    keyboardStudChek = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer(f'Выберите что вы хотите узнать', reply_markup=keyboardStudChek)
        
# Выбор студентом успеваемости
@dp.message_handler(text='Успеваемость')
async def echo(message: types.Message):
    builder = ReplyKeyboardMarkup()
    for i in name_group:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.add(types.KeyboardButton(text='Меню'))
    await message.answer('В какой группе вы учитесь?', reply_markup=builder) 
    
@dp.message_handler()
async def echo(message: types.Message):
    builder = ReplyKeyboardMarkup()
    for i in name_group:
        if message.text == i:
            builder = ReplyKeyboardMarkup()
            for k, j in name_subject.items():        
                builder.add(types.KeyboardButton(text=str(j)))
            builder.add(types.KeyboardButton(text='Меню'))
            await message.reply('Выберете предмет', reply_markup=builder)           
    # for k, j in name_subject.items():        
    #      if message.text == j:
    #         kb = [
    #             [types.KeyboardButton(text="хуй")],
    #             [types.KeyboardButton(text="хуй2")]
    #         ]
    #         keyboardChek = types.ReplyKeyboardMarkup(
    #             keyboard=kb,
    #             resize_keyboard=True
    #         )
    #         await message.reply('Вsfdsfsdfsf', reply_markup=keyboardChek)  
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    