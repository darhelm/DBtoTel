from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


from read_db import findEmail, findId

with open("secrets.txt", "r", encoding="UTF-8") as f:
    TOKEN = f.read().strip()

BOT_USERNAME : Final = "@traffic_mp_bot"

# commands

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("به ربات نمایش حجم Eternal VPN خوش امدید")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
/id  خود را اینجا وارد کنید id
/email  خود را اینجا وارد کنید email

لینک اموزش ها: link
""")

async def id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = context.args[0]
    array = findId(id)
    if type(array) == list:
        await update.message.reply_text(f"""
                email: {array[0]}
                download: {array[1]} GB
                upload: {array[2]} GB
                traffic sum: {array[3]} GB
                expiry time: {array[4]}
""")
    
    await update.message.reply_text(" وجود ندارد Id")

async def email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    array = findEmail(context.args[0])
    if type(array) == list:
        await update.message.reply_text(f"""
                email: {array[0]}
                download: {array[1]} GB
                upload: {array[2]} GB
                traffic sum: {array[3]} GB
                expiry time: {array[4]}
""")
    
    await update.message.reply_text(" وجود ندارد Email")


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("id", id))
    app.add_handler(CommandHandler("email", email))

    # Poll the bot
    app.run_polling()