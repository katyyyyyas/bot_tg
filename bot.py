import logging #standart bibl
import asyncio 
from aiogram import Bot, Dispatcher, types #то что мы сами скачиваем
from config import TOKEN #то что мы сами создали
from aiogram.filters import CommandStart
from transcript import transcriptor
from anectod import tell_joke


logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(msg:types.Message):
    await msg.answer(text='Привет, напиши своё имя на кириллице:')

@dp.message()
async def send_func (msg:types.Message):
    user_name = msg.from_user.first_name
    answ_to_user = transcriptor(msg.text)
    await msg.answer(text=f'В общем, {user_name}, заграницей ты был(-а) бы {answ_to_user} :)')
    await msg.answer(text=f'Хочешь шутку?')

# @dp.message() ***прости Марк, ты сегодня без шуток, мы с Сашей не вспомнили аргумент***,
#  но смотри anecdot.py, там шутка-прибаутка
# async def send_func (msg:types.Message):
#     user_name = msg.from_user.first_name
#     answ_to_user = tell_joke(msg.text)
#     if answ_to_user == 'ну ок':
#         await msg.answer(text = f'{answ_to_user},сегодня ты без шутки, пока')
#     else: 
#         await msg.answer(text=f'Конечно, {user_name}, вот твоя шутка: {answ_to_user} ')

async def main() -> None:
    bot = Bot(token = TOKEN)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

