from aiogram import types


#@dp.message_handler(commands="menu")
#async def show_menu(message: types.Message):
    #buttons = [
        #types.InlineKeyboardButton(text="vk", url="https://vk.com/papatvoeipodrugi"),
        #types.InlineKeyboardButton(text="trello", url="https://trello.com/")
    #]
    #keyboard = types.InlineKeyboardMarkup(row_width=1)
    #keyboard.add(*buttons)
    #await message.answer("Кнопки-ссылки", reply_markup=keyboard)


choice = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="vk", url="https://vk.com/papatvoeipodrugi"),
            types.InlineKeyboardButton(text="trello", url="https://trello.com/"),
        ]
])
