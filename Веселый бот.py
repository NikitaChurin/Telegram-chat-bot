import telebot
import random
from telebot import types
from random import choice

 
bot = telebot.TeleBot("TOKEN")
 
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("С чего начнем? 😉")
    item2 = types.KeyboardButton("Настояние 🤪")
    item3 = types.KeyboardButton("Испытай удачу 🎲")
    item4 = types.KeyboardButton("Анекдот 🤣")
    item5 = types.KeyboardButton("Клип 🔊")
    item6 = types.KeyboardButton("Совет 😎")
 
    markup.add(item1, item2, item3, item4, item5, item6)
 
    bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы пообщаться.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
luc = ['Тебе не повезло, удача не на твоей стороне!', 'Тебе повезло, удача на твоей стороне!', 'Нифига ты невезучий, тебе на столько не повзло что лучше бы ты не тыкал на эту кнопку!', 'Ничего в следующий раз повезет!', 'Ты выйграл АААААВТОМОБИЛЬ!!!', 'Пипец... Сходи к гадалке, на тебе сглаз на невезение', 'Нифига себе, таких везучих чуваков я еще не встречал, поделишься удачей???', 'УДАЧА,УДАЧА,УДАЧА, Теперь это твое второе имя, иди играть в лотерейку!', 'Больне не тыкай никогда сюда, ты заражаешь меня свои невезением!!!', 'Сегодня не твой день...', 'В следующий раз повезет!', 'Твое счастливое число 666, как думаешь что это може значить?', 'Не везение это твое второе имя', 'Тебя сегодня поцеловала богиня удачи? Ты чертовски везучий!', 'Сходи проверся к врачу, возможно ты чем то болен.']
sup = ['Не сдавайся, однажды у тебя все получится!', 'Тебе бы что то изменить, начни с себя!', 'Если ты считаешь себя счастливым, сохрани это всеми силами.', 'Не могу выразить словами на сколько ты офигенный, тут даже моего совета не надо!', 'Займись собой.', 'Найди свою любовь там, где еще не искал!', 'Если вдруг наступила черная полоса, ожидай скоро будет белая!', 'Если что то не нравится в мире, подстройся под него или подстрой этот мир под себя.', 'Не унывай и на твой улице будет праздник!']
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'С чего начнем? 😉':
            bot.send_message(message.chat.id, 'А давай начнем с того, что я скажу какой то офигенный, что зашел ко мне в гости!')
        elif message.text == 'Настоение 🤪':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошее", callback_data='good')
            item2 = types.InlineKeyboardButton("Плохое", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'И какое же?', reply_markup=markup)
        elif message.text == 'Испытай удачу 🎲':
            bot.send_message(message.chat.id, random.choice(luc))
        elif message.text == 'Анекдот 🤣':
            bot.send_message(message.chat.id, '- Доктор, я себя чувствую, как C++. \n - Это как?\n - Меня никто не понимает, все боятся, и говорят, что я больше не нужен...')
        elif message.text == 'Клип 🔊':
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=76wzB8-GB98')
        elif message.text == 'Совет 😎':
            bot.send_message(message.chat.id, random.choice(sup))
        else:
            bot.send_message(message.chat.id, 'Извини, я не запрограммирован на чтение этих сообщений 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Отлично, продолжим общение и оно станет еще лучше!')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Ничего страшного, давай я попробую тебе его поднять!?')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Настояние 🤪",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Выбор сделан")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)