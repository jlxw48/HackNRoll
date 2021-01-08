from flask import request
# from api.dialogflow_api import detect_intent_via_text
from beans.session import Session
from beans.user import User
from cache import get_current_session
from intent_handlers import INTENT_HANDLERS, handle_invalid_intent
from main import app
from utils import \
    get_user_from_request, \
    get_user_input_from_request, default_if_blank, is_not_blank, \
    get_user_command_from_request
import os
import psycopg2

from api.telegram_api import send_message
from command_handlers import COMMAND_HANDLERS, handle_invalid_command

DATABASE_URL = os.environ["DATABASE_URL"]
conn = psycopg2.connect(DATABASE_URL, sslmode="require")
cursor = conn.cursor()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/webhook', methods=['POST'])
def webhook():
    req_body = request.get_json()

    if req_body is None:
        return "ERROR: No request body", 400

    user = get_user_from_request(req_body)
    session = get_current_session(user)
    user_input = get_user_input_from_request(req_body)
    commands = get_user_command_from_request(req_body)  # new

    if is_not_blank(user.id, user_input):
        __process_request(user, session, user_input, commands)

    __process_input(user, session, 'TESTING')


    # # Original working code
    # if is_not_blank(user.id, user_input):
    #     __process_input(user, session, user_input)

    return 'This works!'


# Process incoming request as either one with commands or one for Dialogflow
def __process_request(user: User, session: Session, user_input, commands):
    __process_telegram_commands(user, session, commands)


# Processes all individual commands found in user input, concatenating them into a single response for user
# Does not support options for individual commands since we are responding to potentially multiple commands in input
def __process_telegram_commands(user: User, session: Session, commands):
    individual_responses = filter(is_not_blank, map(__process_individual_telegram_command, commands))
    response = "\n---\n".join(individual_responses)

    send_message(user, ", ".join(commands), session.id, response)


def __process_individual_telegram_command(command):
    if is_not_blank(command):
        return COMMAND_HANDLERS.get(command, handle_invalid_command)(command)
    else:
        return 'Error in processing individual telegram command'


# def __process_dialogflow_input(user: User, session: Session, user_input):
#     intent_result = detect_intent_via_text(session.id, user_input)
#
#     intent_action = default_if_blank(intent_result.action, '')
#
#     if is_not_blank(intent_action):
#         INTENT_HANDLERS.get(intent_action, handle_invalid_intent)(user, intent_result, session.id)

def __process_input(user: User, session: Session, user_input):
    intent_action = 'TESTING'   # testing default

    #intent_action = default_if_blank(user_input, 'UPDATE_PARTICULARS')

    if is_not_blank(intent_action):
        INTENT_HANDLERS.get(intent_action, handle_invalid_intent)(user, intent_action, session.id)
