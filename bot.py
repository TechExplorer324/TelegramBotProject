from config import *
import telebot 
import openai


chatStr = ''

def ChatModal(prompt):
    global chatStr
    openai.api_key = OPENAI_KEY
    chatStr += f"Yours: {prompt}\nBot's reply: "
    response = openai.Completion.create(

            model="gpt-3.5-turbo-16k",
            prompt = chatStr,
            messages=[],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0  
    )
    print(response)
    chatStr += f"{response['choices'][0]['text']}"
    return response['choices'][0]['text']
    
bot = telebot.TeleBot(BOT_API)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message, "Lets start understanfdging")



@bot.message_handler()
def start(message): 
    try:
        reply = ChatModal(message.text)
        bot.reply_to(message,reply)
    except Exception as e:
        print(e)
        bot.reply_to(message,e)



print("Bot has started...")
bot.polling()