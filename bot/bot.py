def main():
    from telebot import types, TeleBot, util
    from configs.config import TOKEN, admins_id, channel_id
    from IOP.iop import IOP
    import schedule

    io = IOP()
    bot = TeleBot(TOKEN)

    @bot.message_handler(commands=['save_channel'])
    def save_channel(message):
        if message.chat.id in admins_id:
            global channel_id  # Add this line to access the global variable
            channel_id = util.extract_arguments(message.text)
            bot.send_message(message.chat.id, "Channel saved.")
        else:
            bot.send_message(message.chat.id, "You are not an admin.")    

    def send_message_to_channel(message):
        bot.send_message(channel_id, message)

    schedule.every().day.at("12:00").do(send_message_to_channel, io.get_message())
    bot.infinity_polling()
    

if __name__ == '__main__':
    exit("Please run run.py instead of this file.")