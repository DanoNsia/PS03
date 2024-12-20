import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_inglish_words():
    url = ""
    try:
        response = requests.get(url)
        print(response)

        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id="random_words").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_inglish_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово ? ")
        if user == word:
            print("Всё верно!")
        else:
            print(f"Ответ неверный, было загадано слово - {word}")

        play_again = input("Хотите сыграть ещё раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break
