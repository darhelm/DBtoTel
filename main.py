from telebot.async_telebot import AsyncTeleBot
from os import getenv
import asyncio

API_KEY = getenv("API_KEY")
bot = AsyncTeleBot(API_KEY)

@bot.message_handler(command=['start'])
async def welcome(message):
    await bot.reply_to(message, ".به ربات نمایش حجم خوش آمدید")

asyncio.run(bot.polling())