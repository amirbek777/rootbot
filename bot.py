from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import Message
# from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
import config
import redis
import random
import logging
import timedelta
import time
import datetime
from datetime import datetime
import requests
from aiogram import Bot, types
from aiogram import types
from aiogram.dispatcher import filters

bot = Bot(token="1765481474:AAFT9SFN4gSCyxCB0CjO3ue2CB_ge2tGTQA")
dp = Dispatcher(bot)
#group = -1001189644764

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(f"""
Команды бота:
/ban - заблокировать пользователя,
/unban - разблокировать пользователя,
/admins - Список персонала,
/kick - Выкинуть пользователя из группы,
/rules - Правила чата,
/myid - Получить свой id,
/chatid - Получить id чата,
/del - Удалить сообщение (укажите ссылку на сообщение),
/support - Поддержка бота.""")

@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply
@dp.message_handler(commands=['chatid'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('Получить ID', callback_data= 'chat_id')
    keyboard_markup.row(user_id_btn)
    
    await message.answer(f"ID чата: {message.chat.id}", reply_markup=keyboard_markup)
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(f"""
Привет, я чат-менеджер, могу ли я чем нибудь помочь?

Напишите /help для просмотра команд бота""")

#@dp.message_handler(commands=['admins'])
#async def process_admin_command(message: types.Message):
#    chat_admins = await bot.get_chat_administrators.(group)
#    await message.reply(f"Список админов и модераторов: {chat_admins}")

@dp.message_handler(commands='reload', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_reload_command(message: types.Message):
    await message.reply("Бот перезагружен!")
    if not message.reply_to_message:
        await message.reply("Эту команду нужно использовать ответом на сообщение!")
        return

@dp.message_handler(commands='del', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_help_command(message: types.Message):
    await bot.delete_message(message.chat.id, message.reply)
@dp.message_handler(commands=['myid'])
async def alarm(message: types.Message):
    keyboard_markup = types.InlineKeyboardMarkup()
    user_id_btn = types.InlineKeyboardButton('Получить ID', callback_data= 'user_id')
    keyboard_markup.row(user_id_btn)
    await message.answer(f"Ваш ID: {message.from_user.id}", reply_markup=keyboard_markup)

@dp.message_handler(commands='ban', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_help_command(message: types.Message): 
    await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(f"Пользователь заблокирован!")
    if not message.reply_to_message:
        await message.reply("Эту команду нужно использовать ответом на сообщение!")
        return

@dp.message_handler(commands='unban', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_help_command(message: types.Message):
    me = await bot.get_me() 
    await message.bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(f"Пользователь {me.first_name} разблокирован!")
    if not message.reply_to_message:
        await message.reply("Эту команду нужно использовать ответом на сообщение!")
        return

@dp.message_handler(commands='mute', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_help_command(message: types.Message):
    flood = await bot.get_me()
    await message.bot.mute_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(f'Пользователь был заглушен')

@dp.message_handler(commands='kick', is_chat_admin=True)
@dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
async def process_help_command(message: types.Message):
    me = await bot.get_me()
    await message.bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await message.reply(f"Пользователь выброшен из группы!")
    if not message.reply_to_message:
        await message.reply("Эту команду нужно использовать ответом на сообщение!")
        return
        
@dp.message_handler(commands=['support'])
async def support_command(message: types.Message):
    await message.reply(f"""
Со всеми вопросами обращаться:

@rootWin""")

@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    ran = '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Отправить радомное число", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)
    await message.reply(random.randint())
@dp.message_handler(commands=['admins'])
async def cmd_admin(message: types.Message):
    await message.reply("""
Список админов/модеров группы:

Главный суперпользователь:
@rootWin

Гл.Модер:
@moonlighted

Модер:
@Milky_Weey

Главный терминатор:
@Ban_Root_bot


Для ознакомления с правилами отправьте:
/rules
        """)
@dp.message_handler(commands=['rules'])
async def process_help_command(message: types.Message):
    await message.reply("""
Правила чата: 
 
1. Уважайте друг друга 
                 
2. Не обсуждать способы мошеничества и скама 
             
3. Любой контент 18+ запрещен. 
 
4. Не флудить и спамить 
 
5. Не обсуждать про то что связано с политикой 
 
6. Не ругаться на админов и модераторов 
 
7. Запрещен деанон пользователей которые в чате и вне чата 
 
8. Запрещено оскорблять чужую религию 
 
9. Запрщенно рекламировать свой проект кроме того который на github 
 
10. Не попрошайничать 
 
За нарушения правил администраторы и модераторы группы могут заглушить или же заблокировать нарушителя.
""")
def log(message):
    print("<!------!>")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id), message.text))
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = False)
    executor.start_polling(dp)