from constants import UPDATE_PARTICULARS_SUGGESTIONS, DEFAULT_GREETING, MAIN_SUGGESTIONS
from api.telegram_api import send_message_with_options

from beans.user import User

# Returns an error message stating that command is invalid
def handle_invalid_command(user: User, command, session_id):
    return "Sorry, your command '{}' is invalid".format(command)


# Returns a greeting message with instructions on how to get started
def __show_default_greeting(user: User, command, session_id):
    # return DEFAULT_GREETING
    return send_message_with_options(user, command, session_id, DEFAULT_GREETING,
                                     *MAIN_SUGGESTIONS, row_width=1)

# Returns a bulleted list of features the bot offers
def __show_help_menu(user: User, command, session_id):
    response = "Hello there! I'm the bot for Ninja Cafe. Feel free to:\n\n"
    response += "- Order something from our menu\n"
    response += "- Ask about what's available on the menu (or use '/menu')\n"
    response += "- Check on your current orders with us\n"
    response += "- Enquire about where your order is\n"

    return response


# Returns a response string with menu items offered as a bulleted list
def __show_particular_fields_for_command(user: User, command, session_id):
    response = "Please choose one of these particulars to update:\n"
    # for x in range(1, len(list(UPDATE_PARTICULARS_SUGGESTIONS.values())) + 1):
    #     response += "{}: {}\n".format(x, list(UPDATE_PARTICULARS_SUGGESTIONS.values())[x - 1])
    # response += "\nWhich would you like to update?\n"
    #
    # return response

    return send_message_with_options(user, command, session_id, response,
                                     *UPDATE_PARTICULARS_SUGGESTIONS, row_width=1)


# Dictionary of command actions mapped to a corresponding function that will be executed when user submits said command
# COMMAND_HANDLERS = {
#     'start': lambda ignored: __show_default_greeting(),
#     'help': lambda ignored: __show_help_menu(),
#     'update': lambda ignored: __show_particular_fields_for_command()
# }
COMMAND_HANDLERS = {
    'start': __show_default_greeting,
    'help':  __show_help_menu,
    'update':  __show_particular_fields_for_command
}


# from telebot import types
#
#
# # Returns an error message stating that command is invalid
# def handle_invalid_command(command):
#     return "Sorry, your command '{}' is invalid".format(command)
#
#
# # Returns a greeting message with instructions on how to get started
# def __show_default_greeting():
#     response = "Select one of the options to get started! :)"
#     return response
#
#
# COMMAND_HANDLERS = {
#     '/start': lambda ignored: __show_default_greeting()
# }
#
# keyboard_greeting = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
# itembtn1 = types.KeyboardButton('Looking for friends!')
# itembtn2 = types.KeyboardButton('Looking for module mates!')
# keyboard_greeting.add(itembtn1, itembtn2)
# KEYBOARDS = {
#     '/start': lambda ignored: keyboard_greeting
# }