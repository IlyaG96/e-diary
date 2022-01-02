# Скрипт для взлома онлайн-дневника

## Возможности

Скрипт предназначен для взлома онлайн-дневника и умеет исправлять все двойки и тройки на пятерки,
убирать замечания от учителей и добавлять похвалу по выбранному предмету

## Установка

Вам понадобится установленный Python 3.6-3.9 и git.
Склонируйте репозиторий или скачайте архив с кодом на компьютер:
```bash
$ git@github.com:IlyaG96/e-diary.git
```

## Использование

- Необходимо загрузить файл scripts.py на сервер в папку e-diary.

- Активируйте виртуальное окружение:
```bash
$ cd e-diary
$ source env/bin/activate
```
- После этого запустите консоль django командой:
```bash
$ python manage.py shell
```
- в консоли введите следующую команду:
```python
>>> import scripts
```
Вас поприветствует пользовательский интерфейс, который предложит ввести имя и фамилию.  
После того, как будут введены правильные данные, скрипт автоматически исправит все ваши оценки и удалит замечания.  
Для того, чтобы добавить похвалу от учителя, следуйте инструкциям пользовательского интерфейса.  

## Дополнительная информация

Это - **_учебный проект_**. Для того, чтобы пользоваться скриптом, необходимо локально развернуть сайт на свое компьютере.  
Репозитория с сайтом находится [здесь](https://github.com/devmanorg/e-diary/tree/master): 
База данных находится [здесь](https://dvmn.org/filer/canonical/1562234129/166/):  

Чтобы развернуть сайт локально, следуйте инструкции:
- Поместите все файлы, необходимые для работы сайта в папку e-diary.
- Создайте виртуальное окружение в папке e-diary, находясь в папке e-diary введите:
```bash
$ python -m venv env
```
- Активируйте виртуальное окружение и установите все зависимости из файла requirements.txt:
```bash
$ source env/bin/activate
$ cd e-diary
$ pip install -r requirements.txt
```
Запустите сайт локально командой:
```bash
$ python manage.py runserver
```
И перейдите по [этому адресу](http://127.0.0.1:8000)
