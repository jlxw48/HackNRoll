import telebot
from telebot import types

from beans.user import User
from constants import TELEGRAM_API_TOKEN

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


# Send a message to Telegram chat without options
def send_message(user: User, state, session_id, response):
    print("Sending response '{}' for user {} session {} state '{}'"
          .format(response, user.id, session_id, state))

    return bot.send_message(user.id, response)


# Send a message to Telegram chat with options, with two options in a row by default
def send_message_with_options(user: User, state, session_id, response, *options, row_width=2):
    print("Sending response '{}' with options '{}' for user {} session {} state '{}'"
          .format(response, options, user.id, session_id, state))

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=row_width)
    markup.add(*options)

    return bot.send_message(user.id, response, reply_markup=markup)


def force_reply_after_name(user: User, state, session_id, response):
    # ForceReply: forces a user to reply to a message
    # Takes an optional selective argument (True/False, default False)
    msg = "Name received\nPlease input your gender now:"
    markup = types.ForceReply(selective=False)
    bot.send_message(user.id, response, reply_markup=markup)
    force_reply_after_gender(user, state, session_id, "gender")


def force_reply_after_gender(user: User, state, session_id, response):
    # ForceReply: forces a user to reply to a message
    # Takes an optional selective argument (True/False, default False)
    msg = "Gender received\nPlease input your year now:"
    markup = types.ForceReply(selective=False)
    bot.send_message(user.id, msg, reply_markup=markup)
    force_reply_after_year(user, state, session_id, "year")


def force_reply_after_year(user: User, state, session_id, response):
    # ForceReply: forces a user to reply to a message
    # Takes an optional selective argument (True/False, default False)
    msg = "Year received\nPlease input your faculty now:"
    markup = types.ForceReply(selective=False)
    return bot.send_message(user.id, msg, reply_markup=markup)



# import telebot
# from telebot import types
#
# from user import User
# from constants import TELEGRAM_API_TOKEN
#
# bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
#
#
#
# # Send a message to Telegram chat without options
# def send_message(user: User, state, session_id, response):
#     print("Sending response '{}' for user {} session {} state '{}'"
#           .format(response, user.id, session_id, state))
#     return bot.send_message(user.id, response)
#
#
# #Send a message to Telegram chat with options, with two options in a row by default
# def send_message_with_options(user: User, state, session_id, response, *options, row_width=2):
#     print("Sending response '{}' with options '{}' for user {} session {} state '{}'"
#           .format(response, options, user.id, session_id, state))
#
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=row_width)
#     markup.add(*options)
#
#     return bot.send_message(user.id, response, reply_markup=markup)
#
# def send_message_with_keyboard(user: User, state, session_id, response, keyboard):
#     print("Sending response '{}' with keyboard".format(response))
#     return bot.send_message(user.id, response, reply_markup=keyboard)
