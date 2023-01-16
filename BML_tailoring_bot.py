import telebot
import time
from telebot import types
import requests
main_spisok_link = []
url = 'https://api.telegram.org/bot'
TOKEN_BOT = '5933528389:AAHAgyQwfYeq2DwYGwvZpltJ2zpIf5YV0_c'
bot = telebot.TeleBot(TOKEN_BOT)
channel_id_bye = '-1001516825876'
configuration = ''
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
    #d = types.KeyboardButton("Поло")
    #f = types.KeyboardButton("Джинсы")
    g = types.KeyboardButton("Сорочка")
    markup.add(a,b)
    markup.add(c,g)
    return markup

def kostum_markup():
    global configuration
    configuration = 'kostum'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Бизнес")
    b = types.KeyboardButton("Свадебный")
    c = types.KeyboardButton("Вечерний")
    d = types.KeyboardButton("Повседневный")
    markup.add(a,b)
    markup.add(c,d)
    return markup

def pidshak_markup():
    global configuration
    configuration = 'pidshak'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Бизнес")
    b = types.KeyboardButton("Тренди")
    d = types.KeyboardButton("Повседневный")
    markup.add(a,b)
    markup.add(d)
    return markup

def palto_markup():
    global configuration
    configuration = 'palto'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Бизнес")
    b = types.KeyboardButton("Тренди")
    d = types.KeyboardButton("Повседневный")
    markup.add(a,b)
    markup.add(d)
    return markup

def sorocka_markup():
    global configuration
    configuration = 'sorocka'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton("Бизнес")
    b = types.KeyboardButton("С принтом")
    d = types.KeyboardButton("Повседневный")
    markup.add(a,b)
    markup.add(d)
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
    a = types.KeyboardButton("🔄 Вернуться в начало")
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
        bot.send_message(message.chat.id, text="📫 Ваш заказ был успешен отправлен ✅", reply_markup=markup_menu())
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
    # with open('users_bml.txt', 'a', encoding='utf-8') as write_f: # Запись Пользователей
    #     id_user = message.from_user.id
    #     name_user = message.from_user.first_name
    #     username_user = message.from_user.username
    #     result = check_user(id_user)
    #     if result: # Проверка пользователей есть ои в списке !
    #         pass # Такой полльзователь уже есть !
    #     else:
    #         write_f.write(f'\n{id_user} : {name_user} : @{username_user}')
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
    global main_spisok_link, index_in_links, len_spisok, item, configuration, flag, main_spisok_link
    if message.text == "Костюм":
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/NJQ3n8axfAB-xA', reply_markup=kostum_markup())
        flag = False
    elif message.text == "Бизнес" and configuration == 'kostum':
        main_spisok_link = ['https://disk.yandex.ru/i/Ad1gKhzuRHVAQA', 'https://disk.yandex.ru/i/aCInWWhqFfdgBQ', 'https://disk.yandex.ru/i/pjETA1SofuxHzw']
        flag = True
    elif message.text == "Свадебный" and configuration == 'kostum':
        main_spisok_link = ['https://disk.yandex.ru/i/MfCCc44DX2k9Ng', 'https://disk.yandex.ru/i/RdNQMXswh0dK5g', 'https://disk.yandex.ru/i/8Xa-Kh9zDrTJOQ']
        flag = True
    elif message.text == "Вечерний" and configuration == 'kostum':
        main_spisok_link = ['https://disk.yandex.ru/i/3SP7mC-QXaEj6Q', 'https://disk.yandex.ru/i/opj4ws0wba6knw']
        flag = True
    elif message.text == "Повседневный" and configuration == 'kostum':
        main_spisok_link = ['https://disk.yandex.ru/i/9Rp8JDMZ8ZWoJg', 'https://disk.yandex.ru/i/n5SyXDwViF9-OQ', 'https://disk.yandex.ru/i/TFHn0NAXuvBbww']
        flag = True


    elif message.text == "Пиджак":
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/PQOV-A_Q1Q6siw', reply_markup=pidshak_markup())
        flag = False
    elif message.text == "Бизнес" and configuration == 'pidshak':
        main_spisok_link = ['https://disk.yandex.ru/i/gE8xEUTbaJLRrw', 'https://disk.yandex.ru/i/uesSWZfSKL6l4A', 'https://disk.yandex.ru/i/zwG2F8N-WukiEQ']
        flag = True
    elif message.text == "Тренди" and configuration == 'pidshak':
        main_spisok_link = ['https://disk.yandex.ru/i/QTf03fkjarCXXA', 'https://disk.yandex.ru/i/qC2Ev-fON4DdiQ', 'https://disk.yandex.ru/i/0S0mcV0fNJqj9Q']
        flag = True
    elif message.text == "Повседневный" and configuration == 'pidshak':
        main_spisok_link = ['https://disk.yandex.ru/i/kkRbW_ArrLqgag', 'https://disk.yandex.ru/i/z6OTl0D0xvGang', 'https://disk.yandex.ru/i/x7RQupp-gITBHQ']
        flag = True


    elif message.text == "Пальто":
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/rVVV1OUio-Uy5g', reply_markup=palto_markup())
        flag = False
    elif message.text == "Бизнес" and configuration == 'palto':
        main_spisok_link = ['https://disk.yandex.ru/i/OuiDuW_d0jD8sA', 'https://disk.yandex.ru/i/s8pms5zLnExUBA', 'https://disk.yandex.ru/i/xhyoPahj-qcNtg']
        flag = True
    elif message.text == "Тренди" and configuration == 'palto':
        main_spisok_link = ['https://disk.yandex.ru/i/RZwaMNOez-ghxw', 'https://disk.yandex.ru/i/G5fo421RtgBsag', 'https://disk.yandex.ru/i/-OmergFuV7Yn4Q']
        flag = True
    elif message.text == "Повседневный" and configuration == 'palto':
        main_spisok_link = ['https://disk.yandex.ru/i/_-Dx1u1kakm24A', 'https://disk.yandex.ru/i/-t_I8dBvkH-VJA', 'https://disk.yandex.ru/i/TkXLVG85eNinDg']
        flag = True

    elif message.text == "Сорочка":
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/a2JExk6tHTPG8g', reply_markup=sorocka_markup())
        flag = False
    elif message.text == "Бизнес" and configuration == 'sorocka':
        main_spisok_link = ['https://disk.yandex.ru/i/Ow-xmE0I53RKUw', 'https://disk.yandex.ru/i/sViiANwTDiF_3A', 'https://disk.yandex.ru/i/KroGpwJAiNIzXw']
        flag = True
    elif message.text == "С принтом" and configuration == 'sorocka':
        main_spisok_link = ['https://disk.yandex.ru/i/qnHConaVyhpndA', 'https://disk.yandex.ru/i/KnQMdJI698QYpw', 'https://disk.yandex.ru/i/_Cy6Vw6ZfKpkNw']
        flag = True
    elif message.text == "Повседневный" and configuration == 'sorocka':
        main_spisok_link = ['https://disk.yandex.ru/i/Mq0XL4FKU9XeOg', 'https://disk.yandex.ru/i/Hnl5Lc9qfqjXBg', 'https://disk.yandex.ru/i/_SsmcpdSwzyVgA']
        flag = True

    elif message.text == "🔄 Вернуться в начало":
        # bot.delete_message(message.chat.id, message.message_id-1)
        # time.sleep(1)
        # bot.delete_message(message.chat.id, message.message_id)
        # bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        # index_in_links = 0
        # len_spisok = len(main_spisok_link)
        bot.send_message(message.chat.id, '↩️ Вы вернулись в каталог 📁', reply_markup=main_markup())
        bot.send_photo(message.chat.id, 'https://disk.yandex.ru/i/nDAGFXPbmfmDjQ')
        flag = False
    elif message.text == "🗂 Посмотреть каталог":
        try:
            doc = open('bml__ зентация_MTM_v2_c.pdf', 'rb')
            bot.send_document(message.chat.id, doc)
            bot.send_document(message.chat.id, "FILEID")
        except:
            pass
        flag = False
    elif message.text == "📬 Написать в ТГ":
        flag = False
    elif message.text == "📞 Заказать звонок":
        markup = types.InlineKeyboardMarkup()
        SITE = types.InlineKeyboardButton("🌐 BML Tailoring", url='http://bmlfg.beget.tech')
        markup.add(SITE)
        bot.send_message(message.chat.id, 'Наш сайт', reply_markup=markup)
        flag = False

    if flag:
        index_in_links = 0
        bot.send_message(message.chat.id, text="👔 Все достпуные предложения, на основе вашего выбора:", reply_markup=markup_menu())
        bot.send_photo(message.chat.id, main_spisok_link[0], reply_markup=bye_markup_1())
        item = main_spisok_link[index_in_links]

        len_spisok = len(main_spisok_link)
        item = main_spisok_link[index_in_links]

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global index_in_links, len_spisok, item, main_spisok_link
    if call.data == "<" or call.data == "<<":
        bot.delete_message(call.message.chat.id, call.message.message_id)
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
        # bot.answer_callback_query(call.id, text="👨‍💼 Наш менеджер сколько с вами свяжется ⏰")
    username_user = call.message.chat.username
    print(f'@{username_user} ===> {item}')
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass