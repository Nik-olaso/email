from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
from dotenv import load_dotenv


def create_message():
    modules_in_process = ['Основы Python', 'Github', 'API']
    modules_done = ['Командная строка', 'Введение Python', 'Введение в JS', 'WEB-разработка']
    time = '3 месяца'
    msg = MIMEMultipart()
    msg["From"] = "Nik.Ragnar@yandex.ru"
    msg["To"] = "Nik.Ragnar@yandex.ru"
    msg["Subject"] = Header("Тестовое письмо", "utf-8") 
    if modules_done:
        text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. В процессе я выполнил модули: {', '.join(modules_done)}! Сейчас я работаю над модулями {', '.join(modules_in_process)}. Обучение мне нравится, я получил море знаний!"""
    else:
        text = f"""Привет Мама(Папа), я занимаюсь в школе третье место уже {time}. Сейчас я работаю над модулями {', '.join(modules_in_process)}. Пока что я улучшаю свои навыки и узнаю много нового!"""
    
    return msg, text


def send_message(server, EMAIL_PASSWORD):
    msg, text = create_message()
    msg.attach(MIMEText(text, "plain", "utf-8"))

    server.login(msg["From"], EMAIL_PASSWORD)

    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()


def main():
    load_dotenv()
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    send_message(server, EMAIL_PASSWORD)


if __name__ == '__main__':
    main()
