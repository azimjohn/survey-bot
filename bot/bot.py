# -*- coding: utf-8 -*-
import os

import telebot
import bot.responses as R
from .models import StepInfo, Post


TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN, threaded=False) # PythonAnywhere doesn't allong threading


def get_chat_step(chat_id):
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    return step_info.step


@bot.message_handler(commands=['start'])
def ask_language(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 0
    step_info.username = message.from_user.username
    step_info.user_id = message.from_user.id
    step_info.first_name = message.from_user.first_name
    step_info.last_name = message.from_user.last_name

    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.add(
        telebot.types.KeyboardButton(R.UZBEK),
        telebot.types.KeyboardButton(R.RUSSIAN)
    )

    step_info.save()
    bot.send_message(chat_id, R.WELCOME)
    bot.send_message(chat_id, R.ENTER_LANGUAGE, reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 0)
def ask_type(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 1

    if message.text == R.UZBEK:
        step_info.language = 'UZ'
    else:
        step_info.language = 'RU'

    lang = step_info.language

    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    markup.add(
        telebot.types.KeyboardButton(R.MESSAGES[lang]['STUDENT']),
        telebot.types.KeyboardButton(R.MESSAGES[lang]['TEACHER'])
    )

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['WHO_ARE_YOU'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 1)
def ask_subject(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 2

    lang = step_info.language or 'RU'
    markup = telebot.types.ReplyKeyboardMarkup(True, False)

    subjects = R.MESSAGES[lang]['SUBJECTS']
    for subject in subjects:
        markup.add(
            telebot.types.KeyboardButton(subject)
        )

    if message.text == R.MESSAGES[lang]["TEACHER"]:
        step_info.type = 'teacher'
    elif message.text == R.MESSAGES[lang]["STUDENT"]:
        step_info.type = 'student'

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['SUBJECT'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 2)
def ask_region(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 3

    lang = step_info.language or 'RU'

    step_info.subject = message.text

    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    regions = R.MESSAGES[lang]['REGIONS']
    for region in regions:
        markup.add(
            telebot.types.KeyboardButton(region['NAME'])
        )

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['CHOOSE_REGION'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 3)
def ask_district(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 4

    lang = step_info.language or 'RU'

    step_info.region = message.text

    markup = telebot.types.ReplyKeyboardMarkup(True, False)

    regions = R.MESSAGES[lang]['REGIONS']
    for region in regions:
        if region['NAME'] == message.text:
            for district in region['DISTRICTS']:
                markup.add(
                    telebot.types.KeyboardButton(district)
                )

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['CHOOSE_DISTRICT'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 4)
def ask_price(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 5

    lang = step_info.language or 'RU'

    markup = telebot.types.ReplyKeyboardMarkup(True, False)

    step_info.district = message.text

    prices = R.MESSAGES[lang]['PRICES']
    for price in prices:
        markup.add(
            telebot.types.KeyboardButton(price)
        )

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['PRICE'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 5)
def ask_phone(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 6

    lang = step_info.language or 'RU'

    step_info.price = message.text
    markup = telebot.types.ReplyKeyboardRemove(selective=False)

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['PHONE'], reply_markup=markup)


@bot.message_handler(func=lambda message: get_chat_step(message.chat.id) == 6)
def finish(message):
    chat_id = message.chat.id
    step_info, _ = StepInfo.objects.get_or_create(chat_id=chat_id)
    step_info.step = 7

    lang = step_info.language or 'RU'

    step_info.phone = message.text
    markup = telebot.types.ReplyKeyboardRemove(selective=False)

    Post.objects.create(
        type=step_info.type,
        language=step_info.language,
        subject=step_info.subject,
        region=step_info.region,
        district=step_info.district,
        price=step_info.price,
        phone=step_info.phone,
        userid=step_info.user_id,
        username=step_info.username
    )

    step_info.save()
    bot.send_message(chat_id, R.MESSAGES[lang]['FINISHED'], reply_markup=markup)

