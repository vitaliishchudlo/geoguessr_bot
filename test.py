# @dp.message_handler(commands=['dice'])
# async def dice(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Кидаю кубика....')
#
#     result = await bot.send_dice(message.from_user.id)
#     number = result['dice']['value']
#     await sleep(3.3)
#     if number == 1 or number == 3 or number == 5:
#         await bot.send_message(message.from_user.id, f'Number is ODD - {number}.')
#         print(f'{message.from_user.username} викинув {number}')
#     else:
#         await bot.send_message(message.from_user.id, f'Number is EVEN - {number}.')
#         print(f'{message.from_user.username} викинув {number}')
#
#
# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     await bot.send_message(message.from_user.id, f'Hello.\nI am free bot GeoGuessr. Choose language....')
#     await bot.send_message(message.from_user.id, f'You are not registered. Enter your email address: ')
#
#     print(f'{message.from_user.username} registered in system.')
#     f = open('text.txt', 'a')
#     f.write(f'{message.from_user.username} registered in system in {datetime.today().now()}\n')
#     f.close()
#
#
# @dp.message_handler(commands=['help'])
# async def helper(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Available command: \"/start\", \"/dice\",')
#
#
# @dp.message_handler(content_types=["text"])
# async def repeat_all_messages(message):
#     await bot.send_message(message.chat.id, message.text)
#
#
# if __name__ == '__main__':
#     # starting bot
#     executor.start_polling(dp, skip_updates=True)
