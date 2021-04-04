from aiogram import executor



from loader import dp

from handlers.users.start import bot_start
from handlers.users.help import bot_help
from handlers.users.menu import show_menu
#from keyboards.inline.button1 import process_start_command

#async def process_start_command(dispatcher):
   # await process_start_command (dispatcher)

async def menu(dispatcher):
    # Выполняет команду /admins
    await show_menu(dispatcher)

async def start(dispatcher):
    # Выполняет команду /start
    await bot_start(dispatcher)


async def helping(dispatcher):
    # Выполняет команду /help
    await bot_help(dispatcher)



if __name__ == '__main__':
    executor.start_polling(dp)
