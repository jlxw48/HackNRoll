from user import *


# Extracts user id from Telegram request
def get_user_from_request(req_body):
    if 'message' in req_body:
        req_from = req_body.get('message', {}).get('from', {})
        return User(req_from.get('id', ''), __get_req_from_name(req_from))
    else:
        return ''

# Extracts user's name from Telegram request
def __get_req_from_name(req_from):
    first_name = req_from.get('first_name')
    last_name = req_from.get('last_name')
    if is_not_blank(first_name, last_name):
        return first_name + ' ' + last_name
    elif is_not_blank(first_name):
        return first_name # Return only first name if last name is not available
    else:
        return ''

# Extracts user's input (text or button click) from Telegram request
def get_user_input_from_request(req_body):
    if 'message' in req_body:
        return req_body.get('message', {}).get('text', '')
    else:
        return ''

# Checks where one or more string params provided are None or blank
def is_not_blank(*string):
    return all(s is not None and s for s in string)


# Extracts user's commands from Telegram request
def get_user_command_from_request(req_body):
    if 'message' in req_body and 'entities' in req_body['message']:
        text = req_body.get('message').get('text')
        return text
    else:
        return ''


def get_user_text_from_request(req_body):
    if 'message' in req_body:
        text = req_body.get('message').get('text')
        return text
    else:
        return ''
