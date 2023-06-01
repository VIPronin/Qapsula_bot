# Qapsula_bot
Бот-помощник, который помогает регистрировать пилотов гоночных команд Qapsula Racing Team, Qapsula Quillers на гоночные мероприятия.  
Регистрация пилотов проводится в социальной сети ВКонтакте.  
Бот отправляет сообщение с ФИО троих пилотов в указанное время.  
Максимально можно отправить ФИО только троих пилотов.  

## Содержание
- [Технологии](#технологии)
- [Использование](#использование)
- [Зачем мы разработали этот проект?](#Зачем-мы-разработали-этот-проект)
- [To do](#to-do)
- [Команда проекта](#команда-проекта)

##
## Технологии

- [vk-api](https://vk-api.readthedocs.io/en/latest/)

##
## Использование

Клонируйте репозиторий:  
`$ git clone github.com/VIPronin/Qapsula_bot`

Создайте виртуальное окружение должен быть флажок (venv)в начале строки:  
`$ python -m venv venv`

Установите зависимости из файла requirements.txt:  
`$ pip install -r requirements.txt`

В файле ***qapsula_bot.py*** найдите следующую строчку:  
`if  now.hour == 12  and  now.minute == 42  and  now.second == 1:`  
и укажите точное время для публиакции, заменив значения.  
Сохраните файл.  

В файле ***config.ini*** заполните следующие данные:  
```
login = ВАШ ЛОГИН
password = ВАШ ПАРОЛЬ

group = ИДЕНТИФИКАТОР ГРУППЫ
topic = ИНДЕТИФИКАТОР БЕСЕДЫ

names_list = ФИО ПИЛОТА

```
Сохраните файл.

##
## Зачем мы разработали этот проект?
Проект действительн помогает регистрироваться на массовые и популярные мероприятия с высокой скоростью.  
Так же он подойдет Вам, если на момент регистрации Вас не будет рядом у компьютера.  
Вы просто запускаете бота и он отправляет сообщение точно в указанное Вами время.

##
## To do
- [ ] разработать пользовательский интерфейс

##
## Команда проекта

- [Пронин Владислав](https://github.com/VIPronin)
- [Саликов Павел](https://github.com/MatanIvanov)
##
