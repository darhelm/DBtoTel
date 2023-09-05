#!/usr/bin/env python3

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from dotenv import dotenv_values


from read_db import findEmail, findId, findConfig


# Load the secrets to a variable as a dictionary "key, value pair"

SECRET = dotenv_values(".env")

BOT_USERNAME : Final = SECRET["USR_NAME"]

# Commands

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به ربات نمایش حجم Eternal VPN خوش امدید")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
/id  خود را اینجا وارد کنید id
/email  خود را اینجا وارد کنید email

لینک اموزش ها: link
""")

async def id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id: str = context.args[0]
    array = findId(id)

    if type(array) == list:
        await update.message.reply_text(f"""
email: {array[0]}
id: {array[5]}
download: {array[1]} GB
upload: {array[2]} GB
traffic sum: {array[3]} GB
expiry time: {array[4]}
""")
    
    else:
        await update.message.reply_text(f" وجود ندارد Id: {id}")

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    email: str = context.args[0]
    array = findEmail(context.args[0])
    if type(array) == list:
        await update.message.reply_text(f"""
email: {array[0]}
download: {array[1]} GB
upload: {array[2]} GB
traffic sum: {array[3]} GB
expiry time: {array[4]}
""")
    elif type(array) != list:
        await update.message.reply_text(f" وجود ندارد Email: {email}")

async def config(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config : str = context.args[0]
    array = findConfig(config)

    if type(array) == list:
        await update.message.reply_text(f"""
email: {array[0]}
id: {array[5]}
download: {array[1]} GB
upload: {array[2]} GB
traffic sum: {array[3]} GB
expiry time: {array[4]}
""")
    
    else:
        await update.message.reply_text(f" وجود ندارد Config: {config}")


if __name__ == "__main__":
    app = Application.builder().token(SECRET["API_TOKEN"]).build()

    # Command Handler
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("id", id))
    app.add_handler(CommandHandler("email", email))
    app.add_handler(CommandHandler("config", config))

    # Poll the bot
    app.run_polling()