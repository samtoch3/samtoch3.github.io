# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 14:14:53 2022

@author: Samson Thibaut

"""

from telegram.bot import Bot
from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram.chataction import ChatAction
from time import sleep
from telegram import *
from telegram.ext import *
from requests import *

token = '5434468014:AAHHtgNIeC_F0hKULu_KZSFDEmgX_VA1hvY'
updater = Updater(token, use_context=True)


def start(update: Update, context: CallbackContext):
    context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    sleep(1)
    update.message.reply_text(text=f"""Bonjour {update.effective_user.first_name} {update.effective_user.last_name},
Je suis Samson, l'assistant intelligent de l'Institut Universitaire de la Cote. Que puis-je faire pour vous ?""")

def message(update: Update, context: CallbackContext):
    if("litteraire" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super {update.effective_user.first_name}, les cursus litteraires que nous proposons sont en lien avec les metiers de journalisme, (...).")

    if("scientifique" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super {update.effective_user.first_name}, nos cursus scientifiques sont en lien avec les metiers d'ingenierie, de mecatronique, (...).")

    if("technique" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super {update.effective_user.first_name}, les cursus techniques que nous proposons sont en lien avec les metiers de mecanique, (...).")

    if("formations" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text="Nos programmes de formations sont sur notre site web a cette adresse : https://myiuc.com/nos-formations/tous-programmes/")
        
    if("admissions" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text('les conditions d\'admission dependent de la formation que vous souhaitez. Pour commencer, laissez moi pour poser quelques questions concernant vos choix')
        update.message.reply_text('Ete-vous etudiant/futur etudiant ou parent ?')

    if("etudiant" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super {update.effective_user.first_name}, etes vous issue d’une serie littéraire, scientifique ou technique ?")
        
    if("parent" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super M. {update.effective_user.first_name}. votre enfant, est-il issue d’une serie littéraire, scientifique ou technique ?")

    if("call center" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"Super {update.effective_user.first_name}, vous pouvez entrer en contact avec le call center via ce numero : +237 699684612")
        update.message.reply_text(text=f"Vous pouvez contacter le call center sur WhatsApp via ce lien : https://wa.me/+237699684612")
        update.message.reply_text(text=f"Merci pour l'echange {update.effective_user.first_name}, et au plaisir...")

    if("au revoir" in update.message.text):
        context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
        sleep(2)
        update.message.reply_text(text=f"A bientot {update.effective_user.first_name}. Passez une agréable journée !")


print('Conversation started')
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, message))
updater.start_polling()
print('Conversation running')


