import telebot

# ضع هنا التوكن الخاص بالبوت من @BotFather
BOT_TOKEN = "8337049334:AAHypZkvt7IJ8-xIsDHlpApOvk2qj-v0Dcs"

bot = telebot.TeleBot(BOT_TOKEN)

# أمر /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 أهلاً بك في البوت!\nاكتب /help لمعرفة الأوامر.")

# أمر /help
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "🧠 الأوامر المتاحة:\n/start - بدء المحادثة\n/help - قائمة المساعدة")

# الرد على أي رسالة نصية
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"📩 قلت: {message.text}")

print("✅ البوت يعمل الآن ...")
bot.polling(none_stop=True)