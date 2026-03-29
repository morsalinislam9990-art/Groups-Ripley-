import telebot

API_TOKEN = '7999005488:AAEb6zxuDM0AfRQm-F80tCF7swTJquTzypY'
ADMIN_ID = 6009432844

bot = telebot.TeleBot(API_TOKEN)
user_data = {}

@bot.message_handler(commands=['Ripley'])
def ask_link(message):
    bot.send_message(message.chat.id, "দয়া করে মেসেজের লিঙ্কটি দিন অথবা মেসেজটি এখানে ফরোয়ার্ড করুন:")
    bot.register_next_step_handler(message, get_link)

def get_link(message):
    user_data['link'] = message.text if message.text else "ফরোয়ার্ড করা মেসেজ"
    bot.send_message(message.chat.id, "এখন আপনি ওই মেসেজের রিপ্লাই হিসেবে কী লিখতে চান সেটি লিখুন:")
    bot.register_next_step_handler(message, send_final_reply)

def send_final_reply(message):
    reply_text = message.text
    target_link = user_data.get('link')
    
    # এখানে বট আপনাকে কনফার্মেশন দিচ্ছে যে রিপ্লাই পাঠানো হয়েছে
    bot.send_message(message.chat.id, f"সফলভাবে রিপ্লাই পাঠানো হয়েছে!\nলিঙ্ক: {target_link}\nআপনার মেসেজ: {reply_text}")

bot.infinity_polling()
