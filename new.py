from cgitb import text
from auth import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard
import pymysql

# Инициализация DataBase
mySQLServer = 'localhost'
myDataBase = 'PgutyBot'
user = 'root'
passwodr = ''


# Инициальзация бота
API_TOKEN = TOKEN
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

'''Конект к базе данных'''
try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('succesfully conneted')
    
    # Старт бота и его выбор кнопок
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
    
    '''Студент выбран и все от него'''
    # Если выбран студент
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
        try:
            with connection.cursor() as cursor:
                select_name_grup = "SELECT * FROM Rating;"
                cursor.execute(select_name_grup)
                rows = cursor.fetchall()
                all_name_group = [] # Список всех групп
                for row in rows:
                    all_name_group.append(row['name_group'])
                name_group = [] # Список групп без повторений
                for i in all_name_group:
                    if i not in name_group:
                        name_group.append(i)
        finally:
            connection.close() 
        builder = ReplyKeyboardMarkup()
        for i in name_group:
            builder.add(types.KeyboardButton(text=str(i)))
        builder.add(types.KeyboardButton(text='Меню'))
        await message.answer('В какой группе вы учитесь?', reply_markup=builder)
    
except Exception as ex:
    print('Connection refused')
    print('ex')     
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)