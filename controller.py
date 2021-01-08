from flask import request

from api import telegram_api
from api.telegram_api import *
from main import app
from utils import get_user_from_request, get_user_input_from_request, is_not_blank, get_user_command_from_request, User, \
    get_user_text_from_request
from command_handlers import COMMAND_HANDLERS, handle_invalid_command, KEYBOARDS
from text_handler import TEXTKEYBOARDS


def __process_request(user: User, session, user_input, commands):
    if len(commands) > 0:
        __process_telegram_commands(user, session, commands)


# Processes all individual commands found in user input, concatenating them into a single response for user
# Does not support options for individual commands since we are responding to potentially multiple commands in input
def __process_telegram_commands(user: User, session, commands):
    response = __process_individual_telegram_command(commands)
    markup = KEYBOARDS.get(commands)(commands)
    send_message_with_keyboard(user, ", ".join(commands), 12345, response, markup)


def __process_individual_telegram_command(command):
    if is_not_blank(command):
        return COMMAND_HANDLERS.get(command, handle_invalid_command)(command)
    else:
        return ''


def process_text(user: User, text):
    if is_not_blank(text):
        return telegram_api.send_message_with_keyboard(user, text, 12345, "Select", TEXTKEYBOARDS.get(text)(text))
    else:
        return ''


@app.route('/webhook', methods=['POST'])
def webhook():
    req_body = request.get_json()
    print(req_body)
    user = get_user_from_request(req_body)
    user_input = get_user_input_from_request(req_body)
    commands = get_user_command_from_request(req_body)
    if "/" in commands:
        if is_not_blank(user.id, user_input):
            __process_request(user, 12, user_input, commands)
    else:
        user_text = get_user_text_from_request(req_body)
        process_text(user, user_text)
    return ''
