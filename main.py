from flask import Flask, request
from threading import Thread
from telethon.sync import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline
from datetime import datetime
import time
import gspread
import pytz
from oauth2client.service_account import ServiceAccountCredentials
import logging

# --- Логирование ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

# --- Flask для 24/7 ---
app = Flask('')

@app.route('/')
def home():
    logging.info(f"Получен запрос от {request.remote_addr}")
    return "Бот работает!"

def run():
    logging.info("Запуск Flask-сервера на 0.0.0.0:8080")
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()

# --- Настройки Telegram ---
api_id = 24429810
api_hash = 'e9b149a28c3c0e928f1f68f897aa412c'
phone = '+37379104005'
username = 'ddddddddddddddddddddddddddddd2'  # Telegram username или ID

# --- Настройки Google Sheets ---
sheet_name = 'tgstatuslogin'
cred_file = 'credentials.json'

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
client_gsheets = gspread.authorize(creds)
sheet = client_gsheets.open(sheet_name).sheet1

# Если таблица пустая, добавляем заголовки
if sheet.row_count == 0:
    sheet.append_row(["Время", "Статус"])

# Авторизация Telegram
client = TelegramClient('session_data', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    code = input('Введи код из Telegram: ')
    client.sign_in(phone, code)

tz = pytz.timezone('Europe/Chisinau')
user = client.get_entity(username)
last_status = None

# Запускаем Flask сервер для keep-alive
keep_alive()

logging.info(f"🟢 Отслеживаю статус пользователя: {username}")

while True:
    try:
        status = client.get_entity(user).status
        now = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')

        if isinstance(status, UserStatusOnline):
            current = 'онлайн'
        elif isinstance(status, UserStatusOffline):
            was_online = status.was_online.astimezone(tz)
            current = f'оффлайн (был {was_online.strftime("%Y-%m-%d %H:%M:%S")})'
        else:
            current = 'недоступно'

        if current != last_status:
            logging.info(f"[{now}] {current}")
            sheet.append_row([now, current])
            last_status = current

    except Exception as e:
        logging.error(f"Ошибка при получении статуса или записи в Google Sheets: {e}")

    time.sleep(3)
