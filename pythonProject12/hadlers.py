from main import bot,dp
from aiogram.types import Message
from confing import admin_id
from search import search

async def send_to_admin(dp):
     await bot.send_message(chat_id=admin_id, text ="Бот запущен")

@dp.message_handler(commands='start')
async def echo(message):
    await bot.send_message(chat_id=admin_id, text="Бот запущен")


@dp.message_handler(commands='help')
async def echo(message):
    await bot.send_message(chat_id=admin_id, text="Я не хочу вам помогать")


@dp.message_handler(lambda message: message.text not in ['1', '2', '3'])
async def echo(message: Message):
    global image_name
    image_name = message.text
    pic = search(message.text)
    print("C:/Users/467/Documents/gsearch/"+str(message.text)+'/Image_1.jpg')
    text = f"Привет, вот изображения по твоему запросу: {message.text}"
    await bot.send_message(chat_id=message.from_user.id, text=text)
    for i in range(1, 4):
        try:
            url1 = f'C:/Users/467/Documents/gsearch/{message.text}/Image_{i}.jpg'
            with open(url1, 'rb') as photo:
                await bot.send_photo(
                    chat_id=message.chat.id, photo=photo
                )
        except: #эта функция нужна для того, чтобы фото точно прислалась, ибо иногда нет фотографий в формате jpg
            url1 = f'C:/Users/467/Documents/gsearch/{message.text}/Image_{i}.png'
            with open(url1, 'rb') as photo:
                await bot.send_photo(
                    chat_id=message.chat.id, photo=photo
                )

@dp.message_handler()
async def echo(message: Message):
    if message.text in ['1', '2', '3']:
        try:
            url1 = f'C:/Users/467/Documents/gsearch/{image_name}/Image_{message.text}.jpg'
            with open(url1, 'rb') as photo:
                await bot.send_photo(
                    chat_id=message.chat.id, photo=photo
                )
        except:  # эта функция нужна для того, чтобы фото точно прислалась, ибо иногда нет фотографий в формате jpg
            url1 = f'C:/Users/467/Documents/gsearch/{image_name}/Image_{message.text}.png'
            with open(url1, 'rb') as photo:
                await bot.send_photo(
                    chat_id=message.chat.id, photo=photo
                )
    else:
        pass