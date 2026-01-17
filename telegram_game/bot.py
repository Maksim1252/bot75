import telebot
from telebot import types

TOKEN = '8368201207:AAGDCGUYIQDlS9Hy8_w2s8c_mGDTyAFNaH8'  # Замените на токен вашего бота
bot = telebot.TeleBot(TOKEN)

# Храним состояние пользователей
user_farm = {}

# Команда /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Играть в ферму", web_app=types.WebAppInfo(url="https://ваш_пользователь.github.io/telegram_game/"))
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку, чтобы начать игру на ферме.", reply_markup=markup)

# Обработчик нажатия на кнопки
@bot.message_handler(commands=['play'])
def play(message):
    # Начать фермерство (для демонстрации)
    bot.send_message(message.chat.id, "Твои растения на ферме: Поливай их и собирай урожай!")

# Обработчик всех текстовых сообщений
@bot.message_handler(func=lambda message: True)
def process_message(message):
    if message.chat.id not in user_farm:
        user_farm[message.chat.id] = {'watered': False, 'can_harvest': False}

    if message.text.lower() == "полить растения":
        if not user_farm[message.chat.id]['watered']:
            user_farm[message.chat.id]['watered'] = True
            user_farm[message.chat.id]['can_harvest'] = True
            bot.send_message(message.chat.id, "Растения политы! Теперь можно собрать урожай.")
        else:
            bot.send_message(message.chat.id, "Растения уже политы. Ждите, пока они не вырастут.")

    elif message.text.lower() == "собрать урожай":
        if user_farm[message.chat.id]['can_harvest']:
            user_farm[message.chat.id]['watered'] = False
            user_farm[message.chat.id]['can_harvest'] = False
            bot.send_message(message.chat.id, "Поздравляем! Урожай собран.")
        else:
            bot.send_message(message.chat.id, "Чтобы собрать урожай, сначала нужно полить растения!")

bot.polling()
