import os
from PIL import Image
from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, ContentTypes
from create_bot import bot, dp
import pytesseract


# commands=['start']
async def command_start(message: Message):
    try:
        text = '''Данный бот считывает текст на фото или картинке.
        Обратите внимание на качество фотографии. Чем выше качество фотографии, 
        тем больше шансов правильно считать с него текст'''
        await bot.send_message(message.from_user.id,
                               text=text)
    except:
        await message.reply('Сначала напиши в лс боту\nhttps://t.me/ScaryTerryBot')


async def working_pytesseract(image):
    pytesseract.pytesseract.tesseract_cmd = r'.\Tesseract-OCR\tesseract.exe'
    tessdata_dir_config = r'--tessdata-dir ".\Tesseract-OCR\tessdata"'
    text = pytesseract.image_to_string(image, lang='rus', config=tessdata_dir_config)
    if not text:
        text = 'Что-то пошло не так, попробуйте снова'
    return text


@dp.message_handler(content_types=ContentTypes.PHOTO)
async def read_photo(message: Message):

    src = f'photos/{message.photo[-1].file_id}.jpg'
    await message.photo[-1].download(src)
    text = await working_pytesseract(Image.open(src))

    os.remove(src)
    await bot.send_message(message.from_user.id, text)


def registers_handlers_clients(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
