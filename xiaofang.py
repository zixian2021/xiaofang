from urllib import response
import speech_recognition as sr
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def speech_recognition():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print('我在听')
            voice = listener.listen(source)
            #语音识别
            command = listener.recognize_google(voice, language="zh-CN")
            print(command)
            return command
    except:
        print('我不理解')
        return('我不理解')
#语音合成
def text_to_speech(response):
    engine =pyttsx3.init()
    engine.say(str(response))
    engine.runAndWait()


def chatter(command):
    if ('小张' in command):
        text_to_speech('没错，小张就是笨蛋')

    return chatbot.get_response(command)



def xiaofang():
    #语音识别
    command = speech_recognition()
    #聊天
    response = chatter(command)
    #语音合成
    text_to_speech(response)
    
    

chatbot = ChatBot('xiaofang')

#train
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.courpus.chinese.ai")

while True:
    xiaofang()
