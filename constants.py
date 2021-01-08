# DEFAULT_DIALOGFLOW_LANGUAGE_CODE = "en"
MENU_CODES_TO_OPTIONS = {
    "MENU_ITEM_BREAD": "Rye Sourdough Bread",
    "MENU_ITEM_DONUT": "Blueberry Jelly Donut",
    "MENU_ITEM_COOKIE": "Almond Crunch Cookie",
    "MENU_ITEM_SANDWICH": "BLT Sandwich",
    "MENU_ITEM_BURGER": "Teriyaki Chicken Burger",
    "MENU_ITEM_SPAGHETTI": "Spaghetti Aglio Olio",
    "MENU_ITEM_MACARONI": "Macaroni Mac and Cheese",
    "MENU_ITEM_STEAK": "Minute Steak Frites",
    "MENU_ITEM_SALAD": "Caesar Salad"
}
DEFAULT_GREETING = "Hello! Please start by updating your particulars :) \n (Separate each information using ';')"
DEFAULT_ERROR_MESSAGE = 'Sorry, something went wrong. Please try again later!'
START_OPTIONS = (
    "Please update your name:",
    "Please update your gender:",
    "Please update your year of study:",
    "Please update your faculty:"
)
NEW_OPTIONS = (
    "Looking for module mates!",
)
UPDATE_OPTIONS = (
    "Update my particulars",
)
UPDATE_PARTICULARS_OPTIONS = (
    "Name",
    "Gender",
    "Year of Study",
    "Faculty",
    "Module",
)
HELP_OPTIONS = (
    "Help 1",
    "Help 2",
    "Help 3",
    "Help 4",
    "Help 5"
)
QUERIES = {
    "GET_ALL_USERS": "SELECT * FROM soscoders.users;",
    "GET_5_USERS_NO_PREF": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE module = %s LIMIT 5;",
    "GET_5_USERS_FAC": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE faculty = %s LIMIT 5;",
    "GET_5_USERS_YEAR": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE study_year = %s LIMIT 5;",
    "GET_5_USERS_GENDER": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE gender = %s LIMIT 5;",
    "GET_5_USERS_FAC_YEAR": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE faculty = %s AND study_year = %s LIMIT 5;",
    "GET_5_USERS_FAC_GENDER": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE faculty = %s AND gender = %s LIMIT 5;",
    "GET_5_USERS_YEAR_GENDER": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE study_year = %s AND gender = %s LIMIT 5;",
    "GET_5_USERS_FAC_YEAR_GENDER": "SELECT * FROM soscoders.request INNER JOIN soscoders.users ON soscoders.request.id = soscoders.users.telegram_id WHERE faculty = %s AND study_year = %s AND gender = %s LIMIT 5;",
    "INSERT_USER": "INSERT INTO soscoders.users(telegram_id, telegram_username, faculty, study_year, gender) VALUES(%s, %s, %s, %s, %s);",
    "INSERT_REQUEST": "INSERT INTO soscoders.request(id, module) VALUES(%s, %s);"
}

# Change the following to suit your project
# DIALOGFLOW_PROJECT_ID = "ninja-van-dialogflow-devmy"
# GOOGLE_SERVICE_ACCOUNT_FILE_PATH = "ninja-van-dialogflow-devmy.json"
TELEGRAM_API_TOKEN = "1535611773:AAFom07aPMU66l7DgYqNjUK8K9UZhbKCoQo"
