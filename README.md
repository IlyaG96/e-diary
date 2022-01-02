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


