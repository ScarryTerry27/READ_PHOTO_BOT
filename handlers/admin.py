from config import admin_ids
from create_bot import bot


async def message_admins(dp):
    print('Бот запущен')
    for ad in admin_ids:
        await bot.send_message(int(ad), text='Бот онлайн')



