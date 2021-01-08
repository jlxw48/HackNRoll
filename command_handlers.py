from constants import MENU_CODES_TO_OPTIONS, DEFAULT_GREETING
import psycopg2
import requests
import os

DATABASE_URL = os.environ.get("DATABASE_URL")
conn = psycopg2.connect(DATABASE_URL, sslmode="require")


# Returns an error message stating that command is invalid
def handle_invalid_command(user, user_input):
    return "Sorry, your command is invalid"


def query_user_exists(user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM soscoders.users WHERE telegram_id = %s;", [user_id])
    result = cursor.fetchall()
    print(result)
    if len(result) == 1:
        cursor.close()
        return True
    else:
        cursor.close()
        return False


def add_new_user(user_id, user_username, faculty, year, gender):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO soscoders.users VALUES(%s, %s, %s, %s, %s);", [user_id, user_username, faculty, year, gender])
    cursor.close()


# Returns a greeting message with instructions on how to get started
def __show_default_greeting(user, user_input):
    if query_user_exists(user.id):
        return "You have already been registered before, use /find to find module mates!"
    else:
        if len(user_input.split()) != 2:
            return "You have not been registered: please enter /start faculty,study year,gender"
        fields = user_input.split()[1]
        fields_split = fields.split(',')
        if len(fields_split) != 3:
            return"You have not been registered: please enter /start faculty,study year,gender"
        else:
            # Need add fields check later
            add_new_user(user.id, user.username, fields_split[0], fields_split[1], fields_split[2])
            return "Adding you to our database. You may now use the /find feature to find module mates!"


# Returns a bulleted list of features the bot offers
def __show_help_menu(user, user_input):
    response = "Use /start faculty,study year,gender to register if you haven't done so.\n"
    response += "Use /find moduleCode,Faculty,year,gender e.g. /find CS2105,Computing,4,male to find only year 4 " \
                "computing male group mates for that module. Enter / for each of the filters that are to be ignored.\n"

    return response


def check_module_valid(module_code: str) -> bool:
    acad_year = "2020-2021"
    get_url = f"https://api.nusmods.com/v2/{acad_year}/moduleList.json"
    modules_get = requests.get(get_url)
    modules_objects = modules_get.json()
    modules_list = [module["moduleCode"] for module in modules_objects]
    return module_code in modules_list

# def add_user_to_request(user, module_code):
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO ")


# Can add flexibility to include multiple options within same filter
def __find_mod(user, user_input):
    if not query_user_exists(user.id):
        return "You have not been registered, please use /start faculty,study year,gender to register."
    fields = user_input.split()
    if len(fields) != 2:
        return "To find module mates please enter /find module code,faculty,year,gender. Use /help for an example."
    else:
        user_input = fields[1]
        input_split = user_input.split(',')
        module_code = input_split[0]
        if check_module_valid(str(module_code)):
            query_str = "SELECT * FROM soscoders.request R INNER JOIN soscoders.users U ON R.id = U.telegram_id " \
                        "WHERE R.module = %s"
            if input_split[1] != '/':
                query_str += "AND U.faculty = %s"
            if input_split[2] != '/':
                input_split[2] = int(input_split[2])
                query_str += "AND U.study_year = %s"
            if input_split[3] != '/':
                query_str += "AND U.gender = %s"
            query_str += f"AND R.id != {user.id};"
            cursor = conn.cursor()
            cursor.execute(query_str, [x for x in input_split if x != '/'])
            # Return all that fulfilled criteria
            query_result = cursor.fetchall()
            returnText = "We have found the following top 5 users fulfilling your filters:\n"
            print(query_result)
            for i in range(5):
                if i < len(query_result):
                    returnText += f"@{query_result[i][1]}\n"
            returnText += "\nWe have also added you to the database to be searched by other users for this module."

            cursor.execute("INSERT INTO soscoders.request VALUES (%s, %s);", [user.id, module_code])
            cursor.close()
            return returnText
        else:
            return f"Invalid module code, {module_code} does not exist."


# Dictionary of command actions mapped to a corresponding function that will be executed when user submits said command
COMMAND_HANDLERS = {
    'start': lambda user, user_input: __show_default_greeting(user, user_input),
    'help': lambda user, user_input: __show_help_menu(user, user_input),
    'find': lambda user, user_input: __find_mod(user, user_input)
}
