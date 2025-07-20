
# 🟢 Telegram Online Status Tracker 📊

A simple Python program to track the **online/offline status** of a Telegram user in real-time and log it to a **Google Sheet**.  
Includes a built-in Flask server to keep the script alive on platforms like Heroku or Replit.

---

## 📁 Project Description

### 🔍 Features

- ⏱️ Tracks Telegram user's online status every 3 seconds
- 📉 Logs status history to Google Sheets with timestamps
- 🌍 Timezone support
- 🌐 Flask server for keep-alive

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-username/telegram-status-tracker.git
cd telegram-status-tracker
```

### 2. Install dependencies

Create a virtual environment and install the requirements:

```bash
pip install -r requirements.txt
```

### 3. Configure Telegram API

Register your app at [my.telegram.org](https://my.telegram.org):

- Get `api_id` and `api_hash`
- Enter your phone number

🔐 **Example (replace in `main.py`)**:

```python
api_id = 12345678
api_hash = 'your_api_hash_here'
phone = '+1234567890'
username = 'example_user_or_id'  # Telegram username or ID
```

### 4. Configure Google Sheets Access

- Create a service account in Google Cloud
- Share your sheet with its email
- Download `credentials.json` and place in project root

🛡️ **IMPORTANT**: Do **not** publish your real credentials. Use `.gitignore`.

**Example (`credentials.json`)**:
```json
{
  "type": "service_account",
  "project_id": "example-project-id",
  ...
}
```

### 5. Create your Google Sheet

- Name it `tgstatuslogin`
- Update the `main.py` if needed:
```python
sheet_name = 'tgstatuslogin'
```

---

## 🖥️ Run

```bash
python main.py
```

You'll be asked for a Telegram code during the first run.

---

## 🌐 Flask Web Server

- Flask runs on `0.0.0.0:8080`
- Access via [http://localhost:8080](http://localhost:8080)

Response:
```
Bot is running!
```

---

## 🛠 Project Structure

```
📁 telegram-status-tracker/
├── main.py
├── credentials.json    # 🔐 Do not publish!
├── requirements.txt
├── Procfile
└── README.md
```

---

## 📦 Dependencies

Key libraries (in `requirements.txt`):

- `Telethon` — Telegram API
- `gspread` + `oauth2client` — Google Sheets
- `Flask` — HTTP server
- `pytz` — timezone support
- `logging` — log status changes

---

## 🧠 How It Works

Every 3 seconds:

1. Fetches user's status from Telegram
2. Converts it to: `online`, `offline (was ...)`, or `unavailable`
3. If changed, appends it to Google Sheet
4. Logs changes to console

---

## ⚠️ Security

- All **real data is replaced** with examples
- Use `.env` for secrets in production
- Never publish `credentials.json` or `session_data.session`

Recommended `.gitignore`:
```
credentials.json
session_data.session*
```

---

## 🧪 Example Output

| Time                  | Status                        |
|----------------------|-------------------------------|
| 2025-07-20 17:03:12  | online                        |
| 2025-07-20 17:05:44  | offline (was 2025-07-20 17:04:10) |

---

## 🤝 Contribute

- Fork it
- Create branches
- Open PRs

---

## 📄 License

MIT License

---

# 🇷🇺 Telegram Online Status Tracker 📊

Простая Python-программа, отслеживающая **статус Telegram-пользователя** (онлайн/оффлайн) в реальном времени и записывающая его в **Google Таблицу**.  
Также реализован встроенный Flask-сервер для поддержания активности на хостингах вроде Heroku или Replit.

---

## 📁 Описание проекта

### 🔍 Возможности

- ⏱️ Проверка статуса указанного Telegram-пользователя каждые 3 секунды
- 📉 Запись истории статуса в Google Sheets с временной меткой
- 🌍 Поддержка часового пояса
- 🌐 Flask-сервер для keep-alive

---

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий:

```bash
git clone https://github.com/your-username/telegram-status-tracker.git
cd telegram-status-tracker
```

### 2. Установите зависимости

```bash
pip install -r requirements.txt
```

### 3. Настройте Telegram API

- Получите `api_id` и `api_hash` на [my.telegram.org](https://my.telegram.org)
- Укажите номер телефона

🔐 **Пример (в `main.py`)**:

```python
api_id = 12345678
api_hash = 'your_api_hash_here'
phone = '+1234567890'
username = 'example_user_or_id'
```

### 4. Настройте доступ к Google Sheets

- Создайте сервисный аккаунт
- Дайте ему доступ к таблице
- Поместите `credentials.json` в корень проекта

🛡️ **Важно**: не публикуйте реальные ключи.

**Пример (`credentials.json`)**:
```json
{
  "type": "service_account",
  "project_id": "example-project-id",
  ...
}
```

### 5. Создайте Google Таблицу

Назовите её, например: `tgstatuslogin`

---

## 🖥️ Запуск

```bash
python main.py
```

---

## 🌐 Веб-сервер Flask

Flask работает на `0.0.0.0:8080`, доступ: [http://localhost:8080](http://localhost:8080)

Ответ:
```
Бот работает!
```

---

## 🛠 Структура проекта

```
📁 telegram-status-tracker/
├── main.py
├── credentials.json
├── requirements.txt
├── Procfile
└── README.md
```

---

## 📦 Зависимости

- `Telethon`, `gspread`, `oauth2client`, `flask`, `pytz`, `logging`

---

## 🧠 Как это работает?

1. Получает статус пользователя из Telegram
2. Форматирует: `онлайн`, `оффлайн (был ...)`, `недоступно`
3. Если изменился — записывает в Google Таблицу
4. Выводит в лог

---

## ⚠️ Безопасность

- Все реальные данные заменены на примеры
- Не публикуйте `credentials.json` и `session_data`

`.gitignore`:
```
credentials.json
session_data.session*
```

---

## 🧪 Пример результата

| Время                 | Статус                               |
|-----------------------|----------------------------------------|
| 2025-07-20 17:03:12   | онлайн                                 |
| 2025-07-20 17:05:44   | оффлайн (был 2025-07-20 17:04:10)      |

---

## 🤝 Контрибуция

Форкайте, дорабатывайте, присылайте PR

---

## 📄 Лицензия

MIT License
