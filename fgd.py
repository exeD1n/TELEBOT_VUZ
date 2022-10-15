from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pymysql
from auth import TOKEN


"""Информация для подлкючения к базам данных"""
mySQLServer = 'localhost'
myDataBase = 'PgutyBot'
user = 'root'
passwodr = ''


"""Индификация бота"""
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

"""Подключение к базе данных"""
try:
    connection = pymysql.connect(host = mySQLServer,port = 3306,database = myDataBase,user = user,password = passwodr,cursorclass = pymysql.cursors.DictCursor)
    print('<<<<<< БАЗА ДАННЫХ УСПЕШНО РАБОТАЕТ >>>>>>')

    
    with connection.cursor() as cursor:
        select_name_grup = "SELECT * FROM Subject;"
        cursor.execute(select_name_grup)
        rows = cursor.fetchall()            
        name_subject = {}
        for row in rows:
            key, value = row['idSubject'], row['Subject']
            name_subject[key] = value   

    """БОТ ТЕЛЕГРАМ"""
    class InputData(StatesGroup):
        input_group = State()
        input_subject = State()

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

    @dp.message_handler(text="Студент")
    async def students(message: types.Message):
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Введите название группы", callback_data="group_input"))
        await message.answer("Нажмите на кнопку\nчто бы вписать группу", reply_markup=markup)

    @dp.callback_query_handler(text="group_input")
    async def group_call(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer("Напишите группу текстом", reply_markup=types.ReplyKeyboardRemove())
        await InputData.input_group.set()
        
    @dp.message_handler(state=InputData.input_group)
    async def group_input(message: types.Message):
        markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Перейти к выбору предмета", callback_data="subject_input"))
        await message.answer(f"Ваша группа - {message.text.lower()}", reply_markup=markup)
    
    @dp.callback_query_handler(text="subject_input")
    async def subject_call(call: types.CallbackQuery):
        await call.answer()
        
        await call.message.answer("Выберете интересующий вас предмет", reply_markup=types.ReplyKeyboardRemove())
        await InputData.input_group.set()
    
    
    """Обработчик запуска бота"""   
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
    
#При возникновении ошибки к подключении к базе данных
except Exception as ex:
    print('Connection refused')
    print('ex')     
    

