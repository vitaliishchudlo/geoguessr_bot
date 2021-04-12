# import telebot
# from time import sleep
# bot = telebot.TeleBot('1718029958:AAFyyDpFHcSO-5JGiA_Oeibeck5Kt7t_UiE')
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, f'<b>Привітулі, {message.from_user.first_name} {message.from_user.last_name}.</b>\n'
#                                       f'Я - безкоштовний бот.\nМожеш використовувати мене нескінченно разів.', parse_mode='html')
#     sleep(1.33)
#     bot.send_message(message.chat.id, 'Вкажи, будь ласка, свою поштову скриньку:')
#
#     @bot.message_handler(content_types=['text'])
#     def take_mailbox(message):
#         if message.text == '@':
#             print('One more registered')
#             bot.send_message(message.chat.id, 'Okay, i got it.')
#
# @bot.message_handler(commands=['exit'])
# def goodbye(message):
#     bot.send_message(message.chat.id, 'Bye')
#     bot.send_message(message.chat.id, message.language_code)
#
#
# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     bot.send_message(message.chat.id, message.text)
#
#
# bot.polling(none_stop=True, interval=0)
#
#
#
#
#
#
#
#
#
#
#
# import telebot
# from time import sleep
# bot = telebot.TeleBot('1718029958:AAFyyDpFHcSO-5JGiA_Oeibeck5Kt7t_UiE')
#
#
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, 'privet')
#     sleep(1.33)
#     bot.send_message(message.chat.id, 'your email address? ')
#
#     @bot.message_handler(content_types=['text'])
#     def take_mailbox(message):
#         if message.text == '@':
#             bot.send_message(message.chat.id, 'Okay, i got it.')
#         else:
#             bot.send_message(message.chat.id, 'email?')
#
# @bot.message_handler(commands=['exit'])
# def goodbye(message):
#     bot.send_message(message.chat.id, 'Bye')
#     bot.send_message(message.chat.id, message.language_code)
#
#
# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     bot.send_message(message.chat.id, message.text)
#
#
# bot.polling(none_stop=True, interval=0)





# date v file & time
#
# f = open('text.txt', 'a')
# f.write(f'{message.from_user.username} registered in system in {datetime.today().now()}\n')


# print(f'{message.from_user.username} registered in system.')
# f = open('text.txt', 'a')
# f.write(f'{message.from_user.username} registered in system in {datetime.today().now()}\n')
# f.close()
