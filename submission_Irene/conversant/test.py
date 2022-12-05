from conversant.prompts import ChatPrompt
import conversant
import cohere

co = cohere.Client("Aa3yKEwtz0wRbRRuPTZ6VvPqXrS9Nvgn9uh6cawn")
bot = conversant.PromptChatbot.from_persona("therapist", client=co)
print(bot.reply("Hello!"))
while(True):
    msg = input("Me: ")
    print("Bot: ",bot.reply(msg))