
COHERE_API_KEY = "Aa3yKEwtz0wRbRRuPTZ6VvPqXrS9Nvgn9uh6cawn"

from conversant.prompts import ChatPrompt
import conversant
import cohere
import time




priv_Last_Reply = ""
booPrintElapsed = True

co = cohere.Client(COHERE_API_KEY)
bot = conversant.PromptChatbot.from_persona("therapist", client=co)
print(bot.reply("Hello!"))
while(True):
    msg = input("Me: ")
    start = time.time()
    reply = bot.reply(msg)
    if(reply != priv_Last_Reply):
        priv_Last_Reply = reply
        # print(reply[len(reply)-1])
        print("Bot: ",reply)
        end = time.time()
        elapsed = float(end-start)
        if booPrintElapsed:
            print("generation elapsed time: ",elapsed,"(seconds)")
    