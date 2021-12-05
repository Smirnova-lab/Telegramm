
import asyncio

from aiogram import Bot, Dispatcher, executor #импортируем класс бота, доставщик, зпаускальщика бота
from confing import BOT_TOKEN

loop =asyncio.get_event_loop() #создаем поток, в котором будут обрабатываться все события, это обязательно для работы с асинхронной библиотекой
bot = Bot(BOT_TOKEN,parse_mode="HTML") #для форматирования
dp = Dispatcher(bot, loop = loop)#обработчик и доставщик
if __name__ == "__main__":
    from hadlers import dp, send_to_admin
    executor.start_polling(dp, on_startup= send_to_admin)
