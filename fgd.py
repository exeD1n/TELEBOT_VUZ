from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import pymysql
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard
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
        
    """БОТ ТЕЛЕГРАМ"""
    class InputData(StatesGroup):
        input_group = State()
        input_subject = State()
        input_lab = State()
        input_teacher_add = State()

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

    @dp.message_handler()
    async def students(message: types.Message):
        if message.text == "Студент":
            markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Успеваемость", callback_data="group_input")).add(InlineKeyboardButton("Практика", callback_data="lab_input"))
            await message.answer("Выберет что вам нужно", reply_markup=markup)
        if message.text == "Учитель":
            markup = InlineKeyboardMarkup().add(InlineKeyboardButton("Посмотреть\изменить успеваемость", callback_data="group_input")).add(InlineKeyboardButton("Изменить лабораторную работу", callback_data="lab_input_teacher_change")).add(InlineKeyboardButton("Добавить лабораторную работу", callback_data="lab_input_teacher_add"))
            await message.answer("Выберет что вам нужно", reply_markup=markup)

    # 1 Call
    @dp.callback_query_handler(text="group_input")
    async def group_call(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer("Напишите группу и предмет \n\nПример: Ивт26у Математика", reply_markup=types.ReplyKeyboardRemove())
        await InputData.input_group.set()
        
    # 2 Call    
    @dp.callback_query_handler(text="lab_input")
    async def group_call(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer("Напишите нужный вам предмет\nи название работы\nПример: Русский практика", reply_markup=types.ReplyKeyboardRemove())
        await InputData.input_lab.set()
        
    # 3 Call
    @dp.callback_query_handler(text="lab_input_teacher_add")
    async def add_lab_call(call: types.CallbackQuery):
        await call.answer()
        await call.message.answer("Напишите нужный что вы хотите добавить\n\nПример: Математика, Решение массивных уравнений, практика", reply_markup=types.ReplyKeyboardRemove())
        await InputData.input_teacher_add.set()
    
    # 1 Input    
    @dp.message_handler(state=InputData.input_group)
    async def group_input(message: types.Message):
        group_subject_info = message.text.lower().split(" ")
        
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Subject;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()            
            name_subject = {}
            for row in rows:
                key, value = row['idSubject'], row['Subject']
                name_subject[key] = value  
        
        for k, j in name_subject.items():
            if j == group_subject_info[1]:
                idsubject = k
        
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Rating;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()            
            name_subject = {}
            for row in rows:
                if row['idSubject']==idsubject and row['name_group']==str(group_subject_info[0]):
                    link_rating = row['link_rating']
                
        await message.answer(f"Ваша группа - {group_subject_info[0]}\nВыбранный вами предмет - {group_subject_info[1]}\n\nВаша успеваемость доступна по ссылке: {link_rating}")
    
    # 2 Input    
    @dp.message_handler(state=InputData.input_lab)
    async def lab_input(message: types.Message):
        subject_lab_info = message.text.lower().split(" ")
        
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Subject;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()            
            name_subject = {}
            for row in rows:
                key, value = row['idSubject'], row['Subject']
                name_subject[key] = value  
        
        for k, j in name_subject.items():
            if j == subject_lab_info[0]:
                idsubject = k
        
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM LabPractick;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()            
            dict_lab = {}
            for row in rows:
                if row['idSubject']==idsubject and row['LabOrPrack']==str(subject_lab_info[1]):
                    key, value = row['namePractick'], row['linkPractick']
                    dict_lab[key] = value
                    
        for k, j in dict_lab.items():
            name_prack = k
            linkPractick = j
            await message.answer(f"Выбранный вами предмет - {subject_lab_info[0]}\n\nНазвание данной работы: {str(name_prack).title()}\n\n{subject_lab_info[1].title()} по ссылке: {linkPractick}")
    
    # 3 Input
    @dp.message_handler(state=InputData.input_teacher_add)
    async def add_lab_input(message: types.Message):
        # Взяли данные и разделили по запятой
        # 0-Математика 1-Решение массивных уравнений 2-практика 3-Ссылка
        group_subject_info = message.text.lower().split(",")
        with connection.cursor() as cursor:
            select_name_grup = "SELECT * FROM Subject;"
            cursor.execute(select_name_grup)
            rows = cursor.fetchall()            
            name_subject = {}
            for row in rows:
                key, value = row['idSubject'], row['Subject']
                name_subject[key] = value  
        
        for k, j in name_subject.items():
            if j == group_subject_info[0]:
                idsubject = k
               
        with connection.cursor() as cursor:
            add_record = f"INSERT INTO `LabPractick` (`idSubject`, `LabOrPrack`, `namePractick`, `linkPractick`) VALUES ('{idsubject}', '{group_subject_info[2]}', '{group_subject_info[1]}', '{group_subject_info[3]}');"
            cursor.execute(add_record)
            connection.commit()
        # await message.answer(f"Предмет - {group_subject_info[0]}\n\nНазвание работы - {group_subject_info[1]}\n\nЗначение работы - {group_subject_info[2]}\n\nСсылка на работу - {group_subject_info[3]}\n\nВы добавили новую работу для студента")
    
    """Обработчик запуска бота"""   
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True)
    
#При возникновении ошибки к подключении к базе данных
except Exception as ex:
    print('Connection refused')
    print('ex')     
    

