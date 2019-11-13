# -*- coding: utf-8 -*-
import telebot
from django.conf import settings

from survey.questions import QUESTIONS
from .models import Respondent

bot = telebot.TeleBot(settings.TOKEN, num_threads=5)
number_of_questions = len(QUESTIONS)


def markup_choices(choices):
    if not choices:
        return telebot.types.ReplyKeyboardRemove(selective=False)

    markup = telebot.types.ReplyKeyboardMarkup(True, False)
    for choice in choices:
        markup.add(telebot.types.KeyboardButton(choice))

    return markup


@bot.message_handler()
def handler(message):
    registrant, _ = Respondent.objects.get_or_create(
        user_id=message.from_user.id,
        defaults={
            "first_name": message.from_user.first_name or "",
            "last_name": message.from_user.last_name or "",
            "username": message.from_user.username or "",
            "step": 0,
        }
    )

    if number_of_questions >= registrant.step >= 1:
        prev_question = QUESTIONS[registrant.step - 1]["text"]
        registrant.details[prev_question] = message.text
        registrant.save(update_fields=["details"])

    if registrant.step >= number_of_questions:
        bot.send_message(registrant.user_id, "Готово. Спасибо за участие.", reply_markup=markup_choices([]))
        return

    question = QUESTIONS[registrant.step]
    text = question["text"]
    choices = question.get("choices") or []

    bot.send_message(registrant.user_id, text, reply_markup=markup_choices(choices))

    registrant.step += 1
    registrant.save(update_fields=["step"])
