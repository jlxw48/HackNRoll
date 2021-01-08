from flask import request

from api.dialogflow_api import detect_intent_via_text, detect_intent_via_event
from api.telegram_api import send_message
from beans.session import Session
from beans.user import User
from cache import get_current_session
from command_handlers import COMMAND_HANDLERS, handle_invalid_command
from intent_handlers import INTENT_HANDLERS, handle_invalid_intent
from main import app
from utils import \
    get_user_from_request, \
    get_user_input_from_request, \
    default_if_blank, \
    is_not_blank, \
    get_user_command_from_request


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Validates incoming webhook request to make sure required fields are present, before processing
@app.route('/webhook', methods=['POST'])
def webhook():
    req_body = request.get_json()

    if req_body is None:
        return "ERROR: No request body", 400

    user = get_user_from_request(req_body)
    session = get_current_session(user)
    user_input = get_user_input_from_request(req_body)
    commands = get_user_command_from_request(req_body)

    if is_not_blank(user.id, user_input):
        __process_request(user, session, user_input, commands)

    return 'OK'


# Process incoming request as either one with commands or one for Dialogflow
def __process_request(user: User, session: Session, user_input, commands):
    if len(commands) == 0:
        send_message(user, "", session.id, "Please enter a command e.g. /help")
    elif len(commands) == 1:
        __process_individual_telegram_command(user, list(commands)[0], user_input, session)
    else:
        send_message(user, "", session.id, "Please use only 1 command at a time.")


def __process_individual_telegram_command(user, command, user_input, session):
    if is_not_blank(command):
        send_message(user, "", session.id, COMMAND_HANDLERS.get(command, handle_invalid_command)(user, user_input))

    return ''


