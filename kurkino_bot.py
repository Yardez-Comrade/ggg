import telebot
from telebot import types
from bs4 import BeautifulSoup as bs
from threading import Thread
import requests
import schedule
url = 'https://api.telegram.org/bot'
TOKEN_BOT = '5019712430:AAGkcgL1mvYgyWiU5tsIXbWL7AYEWGIjzqI'
bot = telebot.TeleBot(TOKEN_BOT)
channel_id_bye = '-1001631030723'
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0"}
print('🥳 START PROGRAMM 🥳')

def fuction_parser(name_text):
    for i in name_text:
        name_text = i.text
    return name_text.strip()

def check_choice_markup():
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да ✅', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет ❌', callback_data='no')
    keyboard.add(key_yes, key_no)
    return keyboard

def main_markup_kurkino():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    a = types.KeyboardButton(text='Новость kurkino_vmo 📰')
    b = types.KeyboardButton(text='Новость kurkino_ru 📰')
    c = types.KeyboardButton(text='Новость szao_mos_ru 📰')
    d = types.KeyboardButton(text='Новость szaopressa_ruvse-novosti 📰')
    markup.add(a)
    markup.add(b)
    markup.add(c)
    markup.add(d)
    return markup



def post_last_news_kurkino_vmo():
    url = 'https://www.kurkino-vmo.ru'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    link = soup.find('h2', class_="entry-title")
    response = requests.get(str(link).split('href="')[1].split('">')[0])
    soup = bs(response.text, 'lxml')
    title = soup.find('h1', class_="entry-title")
    main_text = soup.find('div', class_="fusion-text")
    main_text = '📰' + title.text + '\n\n' + 'ℹ️' + main_text.text
    return main_text
def post_last_news_kurkino_ru():
    url = 'https://kurkino.ru'
    response = requests.get(url)
    soup = bs(response.text, 'lxml')
    link = soup.find('div', class_="cb-grid-img")
    response = requests.get(str(link).split('href="')[1].split('">')[0])
    soup = bs(response.text, 'lxml')
    time = soup.find('time', class_="updated")
    title = soup.find('h1', class_="entry-title cb-entry-title cb-single-title")
    main_text = soup.find(class_="cb-entry-content entry-content clearfix")
    photo = soup.find(class_="cb-fi-standard wp-post-image")
    main_text = '📰' + title.text + '\n\n' + '⏰ ' + time.text + '\n\n' + f'ℹ️{main_text.text}'
    photo_link = str(photo).split('src="')[1].split('"')[0]
    return [photo_link, main_text]






def post_last_news_szao_vlast():
    url = 'https://szaopressa.ru/news/vlast/'
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    link = soup.find(class_="title-link")
    response = requests.get(str(link).split('href="')[1].split('">')[0], headers=headers)
    soup = bs(response.text, 'lxml')#
    title = soup.find('h1', class_="article-title")
    datetime_text = soup.find('div', class_="article-stamp")
    photo_link = soup.find('div', class_="photo__cover")
    main_text = soup.find('div', class_="article__body")
    main_spisok = []
    for i in main_text.text.split('\n'):
        try:
            if list(i)[0] == '«':
                pass
            else:
                main_spisok.append(i.strip())
        except:
            pass
    photo_link = str(photo_link).split('src="')[1].split('"')[0]
    m = '\n'.join(main_spisok)
    main_text = '📰' + title.text + '\n\n' + '⏰ ' + datetime_text.text.split('  ')[0] + '\n\n' + f"ℹ️{m}"
    return [photo_link, main_text]

def post_last_news_szao_vse_novosti():
    url = 'https://szaopressa.ru/vse-novosti/'
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    link = soup.find(class_="title-link")
    response = requests.get(str(link).split('href="')[1].split('">')[0], headers=headers)
    soup = bs(response.text, 'lxml')#
    title = soup.find('h1', class_="article-title")
    datetime_text = soup.find('div', class_="article-stamp")
    photo_link = soup.find('div', class_="photo__cover")
    main_text = soup.find('div', class_="article__body")
    main_spisok = []
    for i in main_text.text.split('\n'):
        try:
            if list(i)[0] == '«':
                pass
            else:
                main_spisok.append(i.strip())
        except:
            pass
    photo_link = str(photo_link).split('src="')[1].split('"')[0]
    m = '\n'.join(main_spisok)
    main_text = '📰' + title.text + '\n\n' + '⏰ ' + datetime_text.text.split('  ')[0] + '\n\n' + f"ℹ️{m}"
    return [photo_link, main_text]


def post_last_news_szao_construction():
    url = 'https://szaopressa.ru/news/construction/'
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    link = soup.find(class_="title-link")
    response = requests.get(str(link).split('href="')[1].split('">')[0], headers=headers)
    soup = bs(response.text, 'lxml')#
    title = soup.find('h1', class_="article-title")
    datetime_text = soup.find('div', class_="article-stamp")
    photo_link = soup.find('div', class_="photo__cover")
    main_text = soup.find('div', class_="article__body")
    main_spisok = []
    for i in main_text.text.split('\n'):
        try:
            if list(i)[0] == '«':
                pass
            else:
                main_spisok.append(i.strip())
        except:
            pass
    photo_link = str(photo_link).split('src="')[1].split('"')[0]
    m = '\n'.join(main_spisok)
    main_text = '📰' + title.text + '\n\n' + '⏰ ' + datetime_text.text.split('  ')[0] + '\n\n' + f"ℹ️{m}"
    return [photo_link, main_text]


def post_last_news_szao_sport():
    url = 'https://szaopressa.ru/news/sport/'
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    link = soup.find(class_="title-link")
    response = requests.get(str(link).split('href="')[1].split('">')[0], headers=headers)
    soup = bs(response.text, 'lxml')#
    title = soup.find('h1', class_="article-title")
    datetime_text = soup.find('div', class_="article-stamp")
    photo_link = soup.find('div', class_="photo__cover")
    main_text = soup.find('div', class_="article__body")
    main_spisok = []
    for i in main_text.text.split('\n'):
        try:
            if list(i)[0] == '«':
                pass
            else:
                main_spisok.append(i.strip())
        except:
            pass
    photo_link = str(photo_link).split('src="')[1].split('"')[0]
    m = '\n'.join(main_spisok)
    main_text = '📰' + title.text + '\n\n' + '⏰ ' + datetime_text.text.split('  ')[0] + '\n\n' + f"ℹ️{m}"
    return [photo_link, main_text]


def save_link_post(link):
    with open('post.txt', 'w', encoding='utf-8') as f:
        f.write(link)

def check_link_post(link_check):
    with open('post.txt', 'r', encoding='utf-8') as f:
        link = f.readline()
        if link == link_check:
            return False
        else:
            return True

@bot.message_handler(commands=['start', 'Start'])
def start(message):
    global main_send_spisok
    def send():
        try:
            main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_vlast()]
            if check_link_post(main_send_spisok[2][0]):
                bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],caption=f'{main_send_spisok[2][1]}')
                save_link_post(main_send_spisok[2][0])
            else:
                raise 'POST ALREADY !'
        except:
            try:
                main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_vse_novosti()]
                bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0], caption=f'{main_send_spisok[2][1]}')
                save_link_post(main_send_spisok[2][0])

            except:
                try:
                    main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_construction()]
                    if check_link_post(main_send_spisok[2][0]):
                        bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],
                                       caption=f'{main_send_spisok[2][1]}')
                        save_link_post(main_send_spisok[2][0])
                    else:
                        raise 'POST ALREADY !'
                except:
                    try:
                        main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_sport()]
                        if check_link_post(main_send_spisok[2][0]):
                            bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],
                                           caption=f'{main_send_spisok[2][1]}')
                            save_link_post(main_send_spisok[2][0])
                        else:
                            raise 'POST ALREADY !'
                    except:
                        try:
                            main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_mos_ru()]
                            if check_link_post(main_send_spisok[2][0]):
                                bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],
                                               caption=f'{main_send_spisok[2][1]}')
                                save_link_post(main_send_spisok[2][0])
                            else:
                                raise 'POST ALREADY !'
                        except:
                            try:
                                main_send_spisok = ["Photo and Message", channel_id_bye, post_last_news_kurkino_ru()]
                                if check_link_post(main_send_spisok[2][0]):
                                    bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],
                                                   caption=f'{main_send_spisok[2][1]}')
                                    save_link_post(main_send_spisok[2][0])
                                else:
                                    raise 'POST ALREADY !'
                            except:
                                try:
                                    main_send_spisok = ["Message", channel_id_bye, post_last_news_kurkino_vmo()]
                                    if check_link_post(main_send_spisok[2][0]):
                                        bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0],
                                                       caption=f'{main_send_spisok[2][1]}')
                                        save_link_post(main_send_spisok[2][0])
                                    else:
                                        raise 'POST ALREADY !'
                                except:
                                    bot.send_message('1157878010', 'Что-то пошло не так :(')

    schedule1 = schedule.Scheduler()
    schedule1.every().day.at("11:00").do(send)
    schedule2 = schedule.Scheduler()
    schedule2.every().day.at("17:00").do(send)
    schedule3 = schedule.Scheduler()
    schedule3.every().day.at("20:00").do(send)

    def Timer():
        while True:
            schedule1.run_pending()
            schedule2.run_pending()
            schedule3.run_pending()

    Thread(target=Timer).start()
    bot.send_message(message.chat.id, text="🚀 Добро пожаловать {0.first_name} 👋!".format(message.from_user), reply_markup=main_markup_kurkino())


@bot.message_handler(content_types=['text'])
def main(message):
    global main_send_spisok
    if message.text == "Новость kurkino_ru 📰" :
        try:
            main_send_spisok = ["Photo", channel_id_bye, post_last_news_kurkino_ru()]
            bot.send_photo(message.chat.id, photo=main_send_spisok[2][0],caption=f'{main_send_spisok[2][1]}\n\n🤔 Вы хотите опубликовать этот пост ?', reply_markup=check_choice_markup())
        except:
            main_send_spisok = ["Photo and Message", channel_id_bye, post_last_news_kurkino_ru()]
            bot.send_message(message.chat.id, text=f'{main_send_spisok[2][1]}\n\n🤔 Вы хотите опубликовать этот пост ?', reply_markup=check_choice_markup())
    elif message.text == "Новость kurkino_vmo 📰" :
        main_send_spisok = ["Message", channel_id_bye, post_last_news_kurkino_vmo()]
        bot.send_message(message.chat.id, text=f'{main_send_spisok[2]}', reply_markup=check_choice_markup())
    elif message.text == "Новость szao_mos_ru 📰" :
        print(post_last_news_szao_construction())
        main_send_spisok = ["Photo", channel_id_bye, post_last_news_szao_construction()]

        bot.send_photo(message.chat.id, photo=main_send_spisok[2][0],caption=f'{main_send_spisok[2][1]}\n\n🤔 Вы хотите опубликовать этот пост ?',reply_markup=check_choice_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global main_send_spisok
    if call.data == "yes":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        if main_send_spisok[0] == "Photo":
            bot.send_photo(main_send_spisok[1], photo=main_send_spisok[2][0], caption=main_send_spisok[2][1])
        elif main_send_spisok[0] == "Message":
            bot.send_message(main_send_spisok[1], text=main_send_spisok[2])
        elif main_send_spisok[0] == "Photo and Message":
            bot.send_message(main_send_spisok[1], text=main_send_spisok[2][1])
    elif call.data == "no":
        bot.delete_message(call.message.chat.id, call.message.message_id)



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        pass