# -*- coding: utf-8 -*-
import os
import telebot
from django.conf import settings

from .models import Respondent


bot = telebot.TeleBot(settings.TOKEN, num_threads=5)
