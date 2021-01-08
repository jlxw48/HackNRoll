from api import order_api
# from api.dialogflow_api import detect_intent_via_event
from api.telegram_api import send_message, send_message_with_options
from beans.user import User
from cache import get_current_order, add_to_order, clear_from_order
from constants import *
import requests
from utils import default_if_blank, is_not_blank, get_items_from_response
import psycopg2

DATABASE_URL = "postgres://wetquihchacmku:139b7d3f9599dbd0e1af9191d9cbafccf47bf5c152dacbd25ad72a55ff2b758b@ec2-35-168-54-239.compute-1.amazonaws.com:5432/dcdivls3vthr4q"
conn = psycopg2.connect(DATABASE_URL, sslmode="require")


#
# # Displays the response found in the intent result as is, with no options
# def __display_default_response(user: User, intent_result, session_id):
#     response = default_if_blank(intent_result.fulfillment_text, DEFAULT_ERROR_MESSAGE)
#
#     return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Displays the response found in the intent result formatted with the user's name, with main menu suggestions
# def __display_main_greeting(user: User, intent_result, session_id):
#     response = intent_result.fulfillment_text.format(default_if_blank(user.name, 'Customer'))
#
#     return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                      *MAIN_SUGGESTIONS, row_width=1)
#
#
# # Displays response with menu items offered as a bulleted list
# def __show_menu_response(user: User, intent_result, session_id):
#     response = "Glad you asked! Here's what we offer:\n"
#     for x in range(1, len(list(MENU_CODES_TO_OPTIONS.values())) + 1):
#         response += "{}: {}\n".format(x, list(MENU_CODES_TO_OPTIONS.values())[x - 1])
#     response += "\nWhat would you like?\n"
#
#     return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Displays response in intent result with a list of menu items as Telegram buttons
# def __show_menu_options(user: User, intent_result, session_id):
#     response = intent_result.fulfillment_text
#     if is_not_blank(response):
#         return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                          *list(MENU_CODES_TO_OPTIONS.values()))
#     else:
#         return send_message(user, intent_result.intent.display_name, session_id, DEFAULT_ERROR_MESSAGE)
#
#
# # Calls Order API to fetch user's current orders and formats them in the response
# # If no orders are found, an appropriate message is shown accordingly
# def __show_orders(user: User, intent_result, session_id):
#     orders = order_api.list_orders(user)
#
#     if len(orders) > 0:
#         response = "Here are your current orders:\n"
#         for x in range(1, len(orders) + 1):
#             response += "{}. {}\n<Placed @ {}>\n\n" \
#                 .format(x, orders[x - 1]['order_description'], orders[x - 1]['timestamp'])
#         response += "\nHow else can I help you?"
#
#         return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                          *MAIN_SUGGESTIONS, row_width=1)
#     else:
#         response = "You have no orders yet. Let me know if you wanna order something!"
#         return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Updates the session cache with the items captured in the response from user, includes "I'm done" option
# def __update_order(user: User, intent_result, session_id):
#     order_items = get_items_from_response(intent_result)
#
#     if len(order_items) > 0:
#         response = intent_result.fulfillment_text
#         add_to_order(user, session_id, order_items)
#         return send_message_with_options(user, intent_result.intent.display_name, session_id, response, "I'm done!")
#     else:
#         response = "Sorry, I wasn't able to detect your order. Could you repeat yourself?"
#         return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Clears the menu items from the session cache for the user
# def __cancel_order(user: User, intent_result, session_id):
#     response = intent_result.fulfillment_text
#     clear_from_order(user, session_id)
#     return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Formats the list of menu items for the user's order in session cache, with options to submit or cancel the order
# # Triggers an event call to Dialogflow to reset contexts to main menu if no menu items found
# def __confirm_order(user: User, intent_result, session_id):
#     order_items = get_current_order(user, session_id)
#
#     if len(order_items) > 0:
#         response = "Here are the items in your order:\n"
#         for name, count in order_items.items():
#             response += "- {}x {}\n".format(count,
#                                             default_if_blank(MENU_CODES_TO_OPTIONS[name], 'N.A.'))
#         response += "\nSubmit?"
#
#         return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                          "Yes, submit my order!", "Nah, cancel it")
#     else:
#         # detect_intent_via_event(session_id, 'NINJA_CAFE_MAIN_EVENT')
#
#         response = "Oops, you don't have any items in your order. Let me know how else I can help you!"
#
#         return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Calls Order API to create a new order with the user's given menu items in session cache
# # Clears the cache after creating the order
# def __submit_order(user: User, intent_result, session_id):
#     order_items = get_current_order(user, session_id)
#
#     response = intent_result.fulfillment_text
#
#     order_api.create_order(user, order_items)
#     clear_from_order(user, session_id)
#
#     return send_message(user, intent_result.intent.display_name, session_id, response)
#
#
# # Displays suggested inputs user can raise to the bot after hitting a fallback in the main menu
# def __show_main_suggestions(user: User, intent_result, session_id):
#     response = intent_result.fulfillment_text
#
#     return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                      *MAIN_SUGGESTIONS, row_width=1)
#
#
# # Displays suggested inputs user can raise to the bot after hitting a fallback in the process of creating an order
# def __show_ongoing_order_suggestions(user: User, intent_result, session_id):
#     response = intent_result.fulfillment_text
#
#     return send_message_with_options(user, intent_result.intent.display_name, session_id, response,
#                                      *UPDATE_PARTICULARS_SUGGESTIONS, row_width=1)

# Returns a generic fallback message
def handle_invalid_intent(user: User, intent_action, session_id, user_input):
    response = "Sorry, I did not understand you. What were you saying?"

    return send_message(user, intent_action, session_id, response)


def __display_test(user: User, intent_action, session_id, user_input):
    response = "display_test function"

    query = "SELECT * FROM test;"
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    if row is not None:
        while row is not None:
            print(row)
            row = cursor.fetchone()
    else:
        print("no users in database")
    cursor.close()

    return send_message(user, intent_action, session_id, response)


def __show_update_particulars_suggestions(user: User, intent_action, session_id, user_input):
    response = "Please choose one of these particulars to update:\n"

    return send_message_with_options(user, intent_action, session_id, response,
                                     *UPDATE_PARTICULARS_OPTIONS, row_width=1)


def __update_name(user: User, intent_action, session_id, user_input):
    response = "Updating name:\n"

    return send_message(user, intent_action, session_id, response)


def __update_gender(user: User, intent_action, session_id, user_input):
    response = "Updating gender:\n"

    return send_message(user, intent_action, session_id, response)


def __update_year(user: User, intent_action, session_id, user_input):
    response = "Updating year:\n"

    return send_message(user, intent_action, session_id, response)


def __update_faculty(user: User, intent_action, session_id, user_input):
    response = "Updating faculty:\n"

    return send_message(user, intent_action, session_id, response)


def __update_module(user: User, intent_action, session_id, user_input):
    response = "Updating module:\n"

    return send_message(user, intent_action, session_id, response)


# Fetches module list from NUSMODS then check if provided module_code is in the list
def check_module_valid(module_code: str) -> bool:
    acad_year = "2020-2021"
    get_url = f"https://api.nusmods.com/v2/{acad_year}/moduleList.json"
    modules_get = requests.get(get_url)
    modules_objects = modules_get.json()
    modules_list = [module["moduleCode"] for module in modules_objects]
    return module_code in modules_list


def __create_user(user: User, intent_action, session_id, lst):
    query = QUERIES.get("INSERT_USER")

    cursor = conn.cursor()
    print(lst)
    new_lst = [int(lst[i]) if (i == 0 or i == 3) else lst[i] for i in range(len(lst))]
    cursor.execute(query, )  # need to pass in the data here in the 2nd param
    conn.commit()
    cursor.close()

    response = "Profile created!"
    return send_message(user, intent_action, session_id, response)


def __get_friends(user: User, intent_action, session_id, user_input):
    response = "hi!"

    query = QUERIES.get("GET_5_USERS_NO_PREF")
    cursor = conn.cursor()
    cursor.execute(query, ()) # pass module here
    row = cursor.fetchone()
    if row is not None:
        while row is not None:
            print(row)
            row = cursor.fetchone()
    else:
        print("no users in database")
    cursor.close()

    return send_message(user, intent_action, session_id, response)


# Dictionary of intent actions mapped to a corresponding function that will be executed when the intent is matched
INTENT_HANDLERS = {
    'DEFAULT': __display_test,
    'Update my particulars': __show_update_particulars_suggestions,
    'Please update your name:': __update_name,
    'Please update your gender:': __update_gender,
    "Please update your year of study:": __update_year,
    "Please update your faculty:": __update_faculty,
    "Name": __update_name,
    "Gender": __update_gender,
    "Year of Study": __update_year,
    "Faculty": __update_faculty,
    "Module": __update_module,
    'start': __create_user,
    'TESTING': __get_friends,
    'UPDATE_PARTICULARS': __show_update_particulars_suggestions
}
