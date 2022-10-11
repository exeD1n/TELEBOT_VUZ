from cgitb import text
from auth import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, reply_keyboard
from database import name_group, name_subject


API_TOKEN = TOKEN
# я изменил
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

# # Кнопка 'Учитель' 
# @dp.message_handler(text = "Учитель")
# async def command_teacher(message: types.Message):   
    
#     kb_teacher = [
#             [
#             types.KeyboardButton(text = 'Практические'),
#             types.KeyboardButton(text='Лабораторные')
#             ],
#             [
#             types.KeyboardButton(text = 'Лекционные'),
#             types.KeyboardButton(text='Оценки')
#             ],
#             [
#             types.KeyboardButton(text='Меню')
#             ]
#     ]   
        
#     keyboardTeacher = types.ReplyKeyboardMarkup(
#         keyboard=kb_teacher,
#         resize_keyboard=True
#     )
#     await message.answer('Что вас интересует?', reply_markup=keyboardTeacher) 

# #Кнопка 'Практические'
# @dp.message_handler(text= "Практические")
# async def command_praktic(message:types.Message):
#     kb_prak = [
#         [
#             types.KeyboardButton(text="Добавить практическую")  #Здесь добавить еще что-то нужно
#         ],
#         [
#             types.KeyboardButton(text='Меню')
#         ]
#     ]
#     keyboardPraktic = types.ReplyKeyboardMarkup(
#         keyboard=kb_prak,
#         resize_keyboard=True
#     )
#     await message.answer('Что вы хотите сделать?', reply_markup=keyboardPraktic)

# #Кнопка 'Лабораторные'
# @dp.message_handler(text= "Лабораторные")
# async def command_lekc(message:types.Message):
#     kb_lekc = [
#         [
#             types.KeyboardButton(text="Добавить лабораторную")  #Здесь добавить еще что-то нужно
#         ],
#         [
#              types.KeyboardButton(text='Меню')
#         ]
#     ]
#     keyboardLekc = types.ReplyKeyboardMarkup(
#         keyboard=kb_lekc,
#         resize_keyboard=True
#     )
#     await message.answer('Что вы хотите сделать?', reply_markup=keyboardLekc)  

# #Кнопка 'Лекционные'
# @dp.message_handler(text= "Лекционные")
# async def command_lek(message:types.Message):
#     kb_lek = [
#         [
#             types.KeyboardButton(text="Добавить лекцию")  #Здесь добавить еще что-то нужно
#         ],
#         [
#              types.KeyboardButton(text='Меню')
#         ]
#     ]
#     keyboardLek = types.ReplyKeyboardMarkup(
#         keyboard=kb_lek,
#         resize_keyboard=True
#     )
#     await message.answer('Что вы хотите сделать?', reply_markup=keyboardLek)

# #Кнопка 'Оценки'
# @dp.message_handler(text= "Оценки")
# async def command_ocenki(message:types.Message):
#     kb_ocenki = [
#         [
#             types.KeyboardButton(text="Выставить оценку")  #Здесь добавить еще что-то нужно
#         ],
#         [
#              types.KeyboardButton(text='Меню')
#         ]
#     ]
#     keyboardOcenki = types.ReplyKeyboardMarkup(
#         keyboard=kb_ocenki,
#         resize_keyboard=True
#     )
#     await message.answer('Что вы хотите сделать?', reply_markup=keyboardOcenki)    

# Кнопка 'Студент' 
@dp.message_handler(text = "Студент")
async def command_student(message:types.Message):   
    builder = ReplyKeyboardMarkup()
    for i in name_group:
        builder.add(types.KeyboardButton(text=str(i)))
    builder.add(types.KeyboardButton(text='Меню'))
        
    # kb_student = [
    #         [
    #         types.KeyboardButton(text = 'Мои практические'),
    #         types.KeyboardButton(text='Мои лабораторные')
    #         ],
    #         [
    #         types.KeyboardButton(text = 'Список лекций'),
    #         types.KeyboardButton(text='Мои оценки')
    #         ],
    #         [
    #         types.KeyboardButton(text='Меню')
    #         ]
    # ]   
    # keyboardStudent = types.ReplyKeyboardMarkup(
    #     keyboard=kb_student,
    #     resize_keyboard=True
    # )
    await message.answer('В какой группе вы учитесь?', reply_markup=builder)

@dp.message_handler()
async def echo(message: types.Message):
    builder = ReplyKeyboardMarkup()
    for i in name_group:
        if message.text == i:
            for k, v in name_subject:
                builder.add(types.KeyboardButton(text=str(v)))
            builder.add(types.KeyboardButton(text='Меню'))
            await message.reply('Выберете предмет', reply_markup=builder)

    # elif message.text == 'Студент':
    #     await message.reply("", reply_markup=types.ReplyKeyboardRemove())
    
#Кнопка Мои практические    
# @dp.message_handler(text = stay)
# async def command_praks(message: types.Message):
#         kb_praktics = [
#             [
#                 types.KeyboardButton(text='Список работ')
#             ],
#             [
#             types.KeyboardButton(text='Меню')    
#             ]
#         ]
#         keyboardPaktics = types.ReplyKeyboardMarkup(
#             keyboard=kb_praktics,
#             resize_keyboard=True
#         )
#         await message.answer('Что вы хотите сделать', reply_markup=keyboardPaktics)
# #Кнопка Мои лабораторные    
# @dp.message_handler(text = 'Мои лабораторные')
# async def command_labs(message: types.Message):
#         kb_labs = [
#             [
#             types.KeyboardButton(text='Список работ')
#             ],
#             [
#             types.KeyboardButton(text='Меню')    
#             ]
#         ]
#         keyboardLabs = types.ReplyKeyboardMarkup(
#             keyboard=kb_labs,
#             resize_keyboard=True
#         )
#         await message.answer('Что вы хотите сделать', reply_markup=keyboardLabs) 
# #Кнопка Список лекций    
# @dp.message_handler(text = 'Список лекций')
# async def command_lekcs(message: types.Message):
        
#         kb_lekcs = [
#             [
#                 types.KeyboardButton(text='Математика'),
#                 types.KeyboardButton(text='Русский язык'), 
#                 types.KeyboardButton(text='Программирование')
#             ],
#             [
#                 types.KeyboardButton(text='Информатика'),
#                 types.KeyboardButton(text='1С'),
#                 types.KeyboardButton(text='Базы данных')
#             ],
#             [
#             types.KeyboardButton(text='Меню')    
#             ]
#         ]
#         keyboardLekcs = types.ReplyKeyboardMarkup(
#             keyboard=kb_lekcs,
#             resize_keyboard=True
#         )
#         await message.answer('Выберите предмет', reply_markup=keyboardLekcs)
# #Кнопка Мои оценки    
# @dp.message_handler(text = 'Мои оценки')
# async def command_ocenki(message: types.Message):
        
#         kb_ocenki = [
#             [
#                 types.KeyboardButton(text='Математика'),
#                 types.KeyboardButton(text='Русский язык'), 
#                 types.KeyboardButton(text='Программирование')
#             ],
#             [
#                 types.KeyboardButton(text='Информатика'),
#                 types.KeyboardButton(text='1С'),
#                 types.KeyboardButton(text='Базы данных')
#             ],
#             [
#             types.KeyboardButton(text='Меню')    
#             ]
#         ]
#         keyboardOcenki = types.ReplyKeyboardMarkup(
#             keyboard=kb_ocenki,
#             resize_keyboard=True
#         )
#         await message.answer('Выберите предмет', reply_markup=keyboardOcenki)                       
# # Кнопка меню
@dp.message_handler(text = 'Меню')
async def menu(message:types.Message):
    kb = [
        [types.KeyboardButton(text="Учитель")],
        [types.KeyboardButton(text="Студент")]
    ]
    keyboardStart = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True
    )
    await message.answer('Возвращаю в основное меню', reply_markup=keyboardStart)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)