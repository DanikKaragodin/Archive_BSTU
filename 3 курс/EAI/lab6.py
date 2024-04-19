import tkinter as tk
from tkinter import filedialog
import spacy
from spacy.matcher import Matcher

# Загрузить модель spaCy для русского языка
nlp = spacy.load("ru_core_news_md")

# Создать сопоставитель для поиска намерений пользователя
matcher = Matcher(nlp.vocab) 

responses = {
    "услуга": "Я могу предложить вам следующие услуги:",
    "консультация": "Я могу проконсультировать вас по следующим вопросам:",
    "консультировать": "Я могу проконсультировать вас по следующим вопросам:",
    "жалоба": "Я сожалею, что у вас возникли проблемы. Я могу помочь вам подать жалобу.",
    "жаловать": "Я сожалею, что у вас возникли проблемы. Я могу помочь вам подать жалобу.",
    "предложение": "Спасибо за ваше предложение. Я передам его соответствующему отделу.",
    "предложить": "Спасибо за ваше предложение. Я передам его соответствующему отделу.",
    "благодарность": "Я рад, что смог вам помочь!",
    "благодарить": "Я рад, что смог вам помочь!",
    "отблагодарить": "Я рад, что смог вам помочь!",
    "поблагодарить": "Я рад, что смог вам помочь!",
}

patterns= [{"LEMMA": {"IN": [*responses.keys()]}}]
matcher.add("lemmas", [patterns])

'''
"Я хочу заказать услугу"
"Мне нужна консультация по выбору ноутбука"
"У меня есть жалоба на ваш продукт"
"Я хотел бы предложить новую услугу"
"Спасибо за вашу помощь"
'''

def analyze_intent(text):
    # Проанализировать текст
    doc = nlp(text)
    print(doc)
    for token in doc:
        print(token.text,token.pos_,token.dep_,token.lemma_)
    # Найти намерение пользователя
    matches = matcher(doc)
    print(matches)
    # Получить намерение из первого совпадения (если оно есть)
    intent = ""

    if len(matches) > 0 and len(matches[0])>2:
        intent = doc[matches[0][1]].lemma_
        print(intent)
    return intent

def generate_response(intent):
    # Получить ответ из словаря ответов на основе намерения
    response = responses.get(intent, "Я не понимаю вашего запроса.")

    return response

def send_message(event):
    # Получить сообщение пользователя
    user_message = text_box.get("1.0", "end-1c")

    # Проанализировать намерение пользователя
    intent = analyze_intent(user_message)

    # Сгенерировать ответ системы
    response = generate_response(intent)

    # Очистить поле ввода
    text_box.delete("1.0", "end")

    # Отобразить ответ системы
    chat_history.insert("end", f"**Система:** {response}\n")

# Создать основное окно GUI
root = tk.Tk()
root.title("Автоматический ответчик на естественном языке")

# Создать поле ввода для сообщения пользователя
text_box = tk.Text(root)
text_box.bind("<Alt_L>", send_message)
text_box.pack()

# Создать поле вывода для чата
chat_history = tk.Text(root)
chat_history.pack()

# Запустить основное окно GUI
root.mainloop()