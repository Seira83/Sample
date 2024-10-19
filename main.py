from weather import get_weather
from news import get_news
from jokes import get_joke
from greetings import get_greeting
from faq import get_faq
from emotion import get_emotion_response
from reminder import set_reminder

#
def chatbot_response(user_input):
    if "天気" in user_input:
        return get_weather()
    elif "ニュース" in user_input:
        return get_news()
    elif "ジョーク" in user_input:
        return get_joke()
    elif "こんにちは" in user_input or "おはよう" in user_input:
        return get_greeting()
    elif "質問" in user_input:
        return get_faq()
    elif "リマインド" in user_input:
        try:
            parts = user_input.split(" ")
            minutes = int(parts[2])
            task = " ".join(parts[2:])
            return set_reminder(minutes, task)
        except ValueError:
            return "リマインドの形式が間違っています。'5分後に〇〇をリマインドして'と入力してください。"
    else:
        return get_emotion_response(user_input)