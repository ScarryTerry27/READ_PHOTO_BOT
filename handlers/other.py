import json
import string
from aiogram import Dispatcher
from aiogram.types import Message


async def echo_send(message: Message):
    # цензура
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split()}\
            .intersection(set(json.load(open('mat.json')))):
        await message.reply('Не ругайся')
        await message.delete()


def registers_handlers_other(dp: Dispatcher):  # регистрируем хендлеры
    dp.register_message_handler(echo_send)
