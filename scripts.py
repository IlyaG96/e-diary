import random

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from datacenter.models import Subject
from datacenter.models import Teacher

commendations = [
    "Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!", "Очень хороший ответ!", "Талантливо!",
    "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!",
    "Потрясающе!", "Замечательно!",  "Прекрасное начало!", "Так держать!",
    "Ты на верном пути!", "Здорово!", "Это как раз то, что нужно!",
    "Я тобой горжусь!", "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!", "Я вижу, как ты стараешься!",
    "Ты растешь над собой!", "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]

subjects = [
    "Краеведение", "География", "Математика", "Музыка", "Физкультура",
    "Изобразительное искусство", "Технология", "Русский язык", "Литература",
    "Обществознание", "Иностранный язык", "Биология", "История",
    "Основы безопасности жизнедеятельности (ОБЖ)"
]


def chose_pupil():
    pupil = None
    while not pupil:
        name = input("Вас приветствует система взлома электронного дневника!\n"
                     "Введите, пожалуйста, свои фамилию и имя через пробел\n"
                     ":")
        pupil = Schoolkid.objects.filter(full_name__contains=name)
        if not pupil:
            print("Такой ученик в школе не учится. Попробуйте еще раз или уточните запрос\n"
                  " (возможно, стоит поменять фамилию и имя местами)")
        elif len(pupil) > 1:
            print("Найдено несколько учеников, уточните запрос!")
            pupil = None
        else:
            pupil = pupil.first()
            return pupil


def correct_points(pupil):
    marks = Mark.objects.filter(schoolkid=pupil, points__lte=3)
    for num, mark in marks.count():
        mark_to_correct = marks[num]
        mark_to_correct.points = 5
        mark_to_correct.save()


def remove_chastisements(pupil):
    chastisements = Chastisement.objects.filter(schoolkid=pupil)
    chastisements.delete()


def create_commendation(commendation_subject, pupil):

    subject = Subject.objects.filter(year_of_study=pupil.year_of_study,
                                     title=commendation_subject).first()
    pupils_subject = Lesson.objects.filter(year_of_study=pupil.year_of_study,
                                           group_letter=pupil.group_lette,
                                           subject=subject).first()
    teacher_id = Teacher.objects.filter(full_name=pupils_subject.teacher).first()
    commendation = Commendation.objects.filter(subject=subject,
                                               schoolkid=pupil,
                                               created=pupils_subject.date)
    commendation.create(text=random.choice(commendations),
                        created=pupils_subject.date,
                        schoolkid=pupil,
                        teacher=teacher_id,
                        subject=subject)


while True:
    pupil = chose_pupil()
    action = int(input("Введите желаемое действие: \n"
                       "1 - Исправить оценки\n"
                       "2 - Удалить замечания\n"
                       "3 - Создать похвалу\n"
                       ":"))
    if action not in range(1, 4):
        commendation_subject = input("Напишите название предмета, на котором вас надо похвалить")

