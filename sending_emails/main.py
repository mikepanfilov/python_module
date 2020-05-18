import os
import smtplib

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

email_from = 'timur.savji@yandex.ru'
email_to = 'mikepaf@gmail.com'
message = '''From: timur.savji@yandex.ru
To: mikepaf@gmail.com
Subject: Приглашение
Content-Type: text/plain; charset="UTF-8";

Привет, {%friend_name%}! {%my_name%} приглашает тебя на сайт {%website%}!

{%website%} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {%website%}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {%website%}  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

variables = {'%website%': 'dvmn.org', 
'%friend_name%': 'Алина',
'%my_name%': 'Михаил'}
message = message.format(**variables)
message = message.encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()