from telethon import TelegramClient, sync, events
from telethon.tl.functions.messages import GetAllStickersRequest

from threading import Thread
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
import time, random
# get your api_id, api_hash, token
# from telegram as described above
import openai

openai.api_key = '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'


api_id = '24270097'
api_hash = '4347d77dd6dd870cce638adb8fb605ef'
message = "Привет !"

# your phone number
phone = '+79671386432'
#time.sleep(10)
# creating a telegram session and assigning
# it to a variable client

client = TelegramClient('session', api_id, api_hash)
client.connect()

# @client.on(events.NewMessage(chats=('Автоответчик 💭')))
# async def normal_handler(event):
#     global antipov_answer
#
#     #sticker_sets = await client(GetAllStickersRequest(0))
#     print(event.message.to_dict()['message'])
#     if event.message.to_dict()['message'].lower() == 'start':
#         pass

# sp = ['TESTTEST', 'Автоответчик 💭']
@client.on(events.NewMessage(chats=('Тютю')))
async def normal_handler(event):

    #sticker_sets = await client(GetAllStickersRequest(0))
    print(event.message.to_dict()['message'])
    if event.message.to_dict()['message'].lower() == 'привет':
        #time.sleep(random.randint(6, 10))g
        #time.sleep(1)
        await client.send_message('@asya_memka', 'Привет 👋')
        #time.sleep(1)
        sticker_sets = await client(GetAllStickersRequest(0))
        sticker_set = sticker_sets.sets[2]
        #print(sticker_set)
        stickers = await client(GetStickerSetRequest(
            stickerset=InputStickerSetID(id=sticker_set.id, access_hash=sticker_set.access_hash),hash=0))
        #print(sticker_set.id) 632063
        #await client.send_file('@dmgtelegram', stickers.documents[8])
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=event.message.to_dict()['message'].lower(),
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["You:"]
        )
        await client.send_message('@asya_memka', response['choices'][0]['text'].strip())
        # await client.send_message('@AntipovEvgeniiBot', 'Антипов, ответь другу на вопрос ' + event.message.to_dict()['message'].lower())
        #
        # @client.on(events.NewMessage(chats=('Антипов')))
        # async def antipov(event):
        #     print(event.message.to_dict()['message'])
        #     with open('answer.txt', 'w', encoding='utf-8') as f:
        #         f.write(event.message.to_dict()['message'])
        #
        # with open('answer.txt', 'r', encoding='utf-8') as f:
        #     for i in f.readlines():
        #         await client.send_message('@mismarkiza', i)


@client.on(events.NewMessage(chats=('Даня')))
async def normal_handler(event):
    #sticker_sets = await client(GetAllStickersRequest(0))
    print(event.message.to_dict()['message'])
    if event.message.to_dict()['message'].lower() == 'привет':
        #time.sleep(random.randint(6, 10))g
        #time.sleep(1)
        await client.send_message('@Danya_Polenyachenlo', 'Привет 👋')
        #time.sleep(1)
        sticker_sets = await client(GetAllStickersRequest(0))
        sticker_set = sticker_sets.sets[2]
        #print(sticker_set)
        stickers = await client(GetStickerSetRequest(
            stickerset=InputStickerSetID(id=sticker_set.id, access_hash=sticker_set.access_hash),hash=0))
        #print(sticker_set.id) 632063
        #await client.send_file('@dmgtelegram', stickers.documents[8])
    else:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=event.message.to_dict()['message'].lower(),
            temperature=0.9,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["You:"]
        )
        await client.send_message('@Danya_Polenyachenlo', response['choices'][0]['text'].strip())
        # await client.send_message('@AntipovEvgeniiBot', 'Антипов, ответь другу на вопрос ' + event.message.to_dict()['message'].lower())
        #
        # @client.on(events.NewMessage(chats=('Антипов')))
        # async def antipov(event):
        #     print(event.message.to_dict()['message'])
        #     with open('answer.txt', 'w', encoding='utf-8') as f:
        #         f.write(event.message.to_dict()['message'])
        #
        # with open('answer.txt', 'r', encoding='utf-8') as f:
        #     for i in f.readlines():
        #         await client.send_message('@mismarkiza', i)

#client.send_message('@asya_memka', message)
client.run_until_disconnected()

# import telebot
# from telethon.sync import TelegramClient
# from telethon.tl.functions.messages import GetAllStickersRequest
# from telethon.tl.types import InputPeerUser, InputPeerChannel
# from telethon.tl.functions.messages import GetStickerSetRequest
# from telethon.tl.types import InputStickerSetID
# from telethon import TelegramClient, sync, events
# from telethon.tl.functions.messages import GetAllStickersRequest
#
# from threading import Thread
# from telethon.tl.functions.messages import GetStickerSetRequest
# from telethon.tl.types import InputStickerSetID
# import time, random
#
# api_id = '181231'
# api_hash = '5a04c93c08f345a9574c8bdcfbe0de9b'
# token = 'bot token'
# message = "Я тебя люблю ❤️"
#
# # your phone number
# phone = '+79671386432'
# #time.sleep(10)
# # creating a telegram session and assigning
# # it to a variable client
#
# client = TelegramClient('session', api_id, api_hash)
# client.connect()
# client.send_message('@Yardez', 'Hello! Talking to you from Telethon')
