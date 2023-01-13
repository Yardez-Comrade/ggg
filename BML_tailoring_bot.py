import telebot
import time
from telebot import types
import requests
main_spisok_link = []
url = 'https://api.telegram.org/bot'
TOKEN_BOT = '5933528389:AAHAgyQwfYeq2DwYGwvZpltJ2zpIf5YV0_c'
bot = telebot.TeleBot(TOKEN_BOT)
channel_id_bye = '-1001516825876'

# ~*~ coding: utf-8 ~*~
# For comrades <3
#   ___           _         ___    _____  _____
#  (  _ \ / \_/ \( )       (  _ \ (  _  )(_   _)
#  | (_) )|     || |       | (_) )| ( ) |/|| |
#  |  _ ( | (_) || |  _    |  _ ( | | | |_)| |
#  | (_) )| | | || |_( )   | (_) )| (_) |  | |
#  (____/ (_) (_)((___/    (____/ (_____)  ( )
#                (_)                       /(
#                                         (__)    by Yardez

print('🥳 START PROGRAMM 🥳')

def main_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Костюм")
    b = types.KeyboardButton("Пиджак")
    c = types.KeyboardButton("Пальто")
    d = types.KeyboardButton("Поло")
    f = types.KeyboardButton("Джинсы")
    g = types.KeyboardButton("Сорочка")
    markup.add(a,b,c)
    markup.add(d,f,g)
    return markup
def kostum_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Бизнес")
    b = types.KeyboardButton("Свадебный")
    c = types.KeyboardButton("Вечерний")
    d = types.KeyboardButton("Повседневный")
    markup.add(a,b)
    markup.add(c,d)
    return markup
def bye_markup_1():
    markup = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton("Следующий образ ⏩", callback_data='>>')
    c = types.InlineKeyboardButton("💼 Заказать", callback_data='bye')
    markup.add(b)
    markup.add(c)
    return markup
def bye_markup_2():
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("◀️ Предыдущий образ", callback_data='<')
    b = types.InlineKeyboardButton("Следующий образ ▶️", callback_data='>')
    c = types.InlineKeyboardButton("💼 Заказать", callback_data='bye')
    markup.add(a,b)
    markup.add(c)
    return markup
def bye_markup_3():
    markup = types.InlineKeyboardMarkup()
    a = types.InlineKeyboardButton("⏪ Предыдущий образ", callback_data='<<')
    c = types.InlineKeyboardButton("💼 Заказать", callback_data='bye')
    markup.add(a)
    markup.add(c)
    return markup
def markup_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("🔄 Пройти квиз снова")
    b = types.KeyboardButton("🗂 Посмотреть каталог")
    c = types.KeyboardButton("📬 Написать в ТГ")
    d = types.KeyboardButton("📞 Заказать звонок")
    markup.add(a, b)
    markup.add(c, d)
    return markup
def send_contact():
    markup_request = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    markup_request.add(a)
    return markup_request
def buy_item(message):
    global item
    try:
        username_user = message.from_user.username
        phone = str(message.contact).split(':')[1].split(',')[0]
        bot.send_message(channel_id_bye, text=f"✉️ Новый Заказ 📍\n🙎‍♂️ Пользователь: @{username_user}\n📱 Номер телефона: {phone}\n🖇 Товар:\n{item}")
        bot.send_message(message.chat.id, text="📫 Ваш заказ был успешен отправлен ✅", reply_markup=main_markup())
    except IndexError:
        bot.send_message(message.chat.id, text="❌ Вы отправили неккоректный номер телефона\nЛибо что-то пошло не так:( \nПопробуйте ещё раз ;)", reply_markup=main_markup())
def check_user(id_user):
    with open('users.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.split(' :')
            if str(id_user) == line[0]: # Надо обратить внимание на формат текста !! Str или Int !
                return True
        else:
            return False

def work_file_main(itog):
    with open('main.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.split()
            try:
                if itog == line[0]:
                    return line[1]
            except Exception:
                pass
@bot.message_handler(commands=['start', 'Start'])
def start(message):
    with open('users_bml.txt', 'a', encoding='utf-8') as write_f: # Запись Пользователей
        id_user = message.from_user.id
        name_user = message.from_user.first_name
        username_user = message.from_user.username
        result = check_user(id_user)
        if result: # Проверка пользователей есть ои в списке !
            pass # Такой полльзователь уже есть !
        else:
            write_f.write(f'\n{id_user} : {name_user} : @{username_user}')

    username_user = message.from_user.username
    bot.send_message(channel_id_bye, f'❇️ Найден новый пользователь 🥳\n🙎‍♂️ Пользователь: @{username_user}')
    bot.send_message(message.chat.id, text="""
Добро пожаловать {0.first_name}👋!
ИНДИВИДУАЛЬНЫЙ ПОШИВ С ПЕРСОНАЛЬНОЙ СКИДКОЙ -25%* 

➡️ НЕМЕЦКИЙ БРЕНД С 20-И ЛЕТНЕЙ ИСТОРИЕЙ 
➡️ ЛУЧШИЕ АНГЛИЙСКИЕ И ИТАЛЬЯНСКИЕ ТКАНИ
➡️ ВЫПОЛНЕНИЕ ЗАКАЗА ТОЧНО В СРОК
➡️ ВЫЕЗДНОЙ СЕРВИС

*при первом заказе мтм""".format(message.from_user), reply_markup=main_markup())
    bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/nDAGFXPbmfmDjQ')

@bot.message_handler(content_types=['text'])
def main(message):
    global main_spisok_link, index_in_links, len_spisok, item
    if message.text == "Костюм":
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/TD4aS00_-QQLVQ', reply_markup=kostum_markup())
    elif message.text == "Бизнес":
        main_spisok_link = ['https://disk.yandex.ru/i/Ad1gKhzuRHVAQA', 'https://disk.yandex.ru/i/aCInWWhqFfdgBQ', 'https://disk.yandex.ru/i/pjETA1SofuxHzw']
        bot.send_message(message.chat.id, text="👔 Все достпуные предложения, на основе вашего выбора:", reply_markup=markup_menu())
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        index_in_links = 0
        len_spisok = len(main_spisok_link)
        item = main_spisok_link[index_in_links]
    elif message.text == "Свадебный":
        main_spisok_link = ['https://disk.yandex.ru/i/MfCCc44DX2k9Ng', 'https://disk.yandex.ru/i/RdNQMXswh0dK5g', 'https://disk.yandex.ru/i/8Xa-Kh9zDrTJOQ']
        bot.send_message(message.chat.id, text="👔 Все достпуные предложения, на основе вашего выбора:",reply_markup=markup_menu())
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        index_in_links = 0
        len_spisok = len(main_spisok_link)
        item = main_spisok_link[index_in_links]
    elif message.text == "Вечерний":
        main_spisok_link = ['https://disk.yandex.ru/i/3SP7mC-QXaEj6Q', 'https://disk.yandex.ru/i/opj4ws0wba6knw']
        bot.send_message(message.chat.id, text="👔 Все достпуные предложения, на основе вашего выбора:", reply_markup=markup_menu())
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        index_in_links = 0
        len_spisok = len(main_spisok_link)
        item = main_spisok_link[index_in_links]
    elif message.text == "Повседневный":
        main_spisok_link = ['https://disk.yandex.ru/i/9Rp8JDMZ8ZWoJg', 'https://disk.yandex.ru/i/n5SyXDwViF9-OQ', 'https://disk.yandex.ru/i/TFHn0NAXuvBbww']
        bot.send_message(message.chat.id, text="👔 Все достпуные предложения, на основе вашего выбора:", reply_markup=markup_menu())
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        item = main_spisok_link[index_in_links]
        index_in_links = 0
        len_spisok = len(main_spisok_link)
        item = main_spisok_link[index_in_links]
    elif message.text == "🔄 Пройти квиз снова":
        bot.delete_message(message.chat.id, message.message_id-1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        index_in_links = 0
        len_spisok = len(main_spisok_link)
    elif message.text == "🗂 Посмотреть каталог":
        bot.send_message(message.chat.id, '↩️ Вы вернулись в каталог 📁', reply_markup=main_markup())
    elif message.text == "📬 Написать в ТГ":
        bot.send_message(message.chat.id, 'Телеграмм человека')
    elif message.text == "📞 Заказать звонок":
        markup = types.InlineKeyboardMarkup()
        SITE = types.InlineKeyboardButton("🌐 BML Tailoring", url='http://bmlfg.beget.tech')
        markup.add(SITE)
        bot.send_message(message.chat.id, 'Наш сайт', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global index_in_links, len_spisok, item
    if call.data == "<" or call.data == "<<":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        print('<')
        index_in_links -= 1
        if index_in_links == 0:
            bot.send_photo(call.message.chat.id, main_spisok_link[index_in_links], reply_markup=bye_markup_1())
        else:
            bot.send_photo(call.message.chat.id, main_spisok_link[index_in_links], reply_markup=bye_markup_2())
        item = main_spisok_link[index_in_links]
    elif call.data == ">" or call.data == ">>":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        index_in_links += 1
        if index_in_links+1 == len_spisok:
            bot.send_photo(call.message.chat.id, main_spisok_link[index_in_links], reply_markup=bye_markup_3())
        else:
            bot.send_photo(call.message.chat.id, main_spisok_link[index_in_links], reply_markup=bye_markup_2())
        item = main_spisok_link[index_in_links]
    elif call.data == "bye":
        bot.send_message(call.message.chat.id, text='📞 Оставьте ваш контактный номер чтобы наш менеджер смог связаться с вами.', reply_markup=send_contact())
        bot.register_next_step_handler(call.message, buy_item)
    print(item)
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        time.sleep(10)