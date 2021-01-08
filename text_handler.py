from telebot import types

keyboard_module = types.ReplyKeyboardMarkup(one_time_keyboard=True)
itembtn1 = types.KeyboardButton('Module')
itembtn2 = types.KeyboardButton('Name')
itembtn3 = types.KeyboardButton('Age')
itembtn4 = types.KeyboardButton('Year of Study')
itembtn5 = types.KeyboardButton('Major')
keyboard_module.add(itembtn1)
keyboard_module.add(itembtn2, itembtn3)
keyboard_module.add(itembtn4, itembtn5)
TEXTKEYBOARDS = {
    "Looking for module mates!": lambda ignored: keyboard_module
}