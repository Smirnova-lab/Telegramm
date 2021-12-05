from main import bot,dp
from aiogram.types import Message
from confing import admin_id
from search import search

async def send_to_admin(dp):
     await bot.send_message(chat_id=admin_id, text ="Бот запущен")

@dp.message_handler(commands='start')
async def echo(message):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")





@dp.message_handler()
async def echo(message: Message):
    pic = search(message.text)
    print("C:/Users/467/Documents/gsearch/"+str(message.text)+'/Image_1.jpg')
    text = f"Привет, вот изображение по твоему запросу: {message.text}"
    try:
        url = f'C:/Users/467/Documents/gsearch/{message.text}/Image_1.jpg'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        with open(url, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.chat.id, photo=photo
            )
    except:
        url = f'C:/Users/467/Documents/gsearch/{message.text}/Image_1.png'
        await bot.send_message(chat_id=message.from_user.id, text=text)
        with open(url, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.chat.id, photo=photo
            )