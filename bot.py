import logging
from time import sleep
from config import *
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.input_file import InputFile

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_mess(message: types.Message):
    print("Clicked /start... Bot is running")
    await bot.send_message(chat_id=owner_id, text="Now bot is running!!!")
    while True:
        sleep(60)
        sticker_path = get_notify()
        if sticker_path:
            try:
                await bot.send_sticker(chat_id=REALSOFT,
                                       sticker=InputFile(path_or_bytesio=f"stickers/{sticker_path}"))
            except:
                await bot.send_message(chat_id=1456374097, text="Sticker wasn't sent! There is unknown error")

if __name__ == '__main__': executor.start_polling(dp, skip_updates=True)