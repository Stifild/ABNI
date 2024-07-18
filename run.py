import os

def create_folders():
    os.makedirs('data', exist_ok=True)
    os.makedirs('data/temp', exist_ok=True)

def start_bot_scripts():
    import bot.bot as bot
    bot.main()


if __name__ == '__main__':
    create_folders()