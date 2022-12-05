from conversant.prompts import ChatPrompt
import conversant
import cohere

co = cohere.Client("api key")
bot = conversant.PromptChatbot.from_persona("therapist", client=co)
print(bot.reply("Hello!"))
while(True):
    msg = input("Me: ")
    print("Bot: ",bot.reply(msg))
