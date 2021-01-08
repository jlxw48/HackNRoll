from telebot import types


# Returns an error message stating that command is invalid
def handle_invalid_command(command):
    return "Sorry, your command '{}' is invalid".format(command)


# Returns a greeting message with instructions on how to get started
def __show_default_greeting():
    response = "Select one of the options to get started! :)"
    return response


COMMAND_HANDLERS = {
    '/start': lambda ignored: __show_default_greeting()
}

keyboard_greeting = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
itembtn1 = types.KeyboardButton('Looking for friends!')
itembtn2 = types.KeyboardButton('Looking for module mates!')
keyboard_greeting.add(itembtn1, itembtn2)
KEYBOARDS = {
    '/start': lambda ignored: keyboard_greeting
}


