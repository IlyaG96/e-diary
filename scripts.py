import random
import sys
from pprint import pprint
from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from datacenter.models import Subject
from datacenter.models import Teacher

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import MultipleObjectsReturned

COMMENDATIONS = [
    "Молодец!", "Отлично!", "Хорошо!", "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!", "Великолепно!", "Прекрасно!", "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!", "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!", "Очень хороший ответ!", "Талантливо!",
    "Ты сегодня прыгнул выше головы!", "Я поражен!", "Уже существенно лучше!",
    "Потрясающе!", "Замечательно!", "Прекрасное начало!", "Так держать!",
    "Ты на верном пути!", "Здорово!", "Это как раз то, что нужно!",
    "Я тобой горжусь!", "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!", "Я вижу, как ты стараешься!",
    "Ты растешь над собой!", "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]

SUBJECTS = [
    "Краеведение", "География", "Математика", "Музыка", "Физкультура",
    "Изобразительное искусство", "Технология", "Русский язык", "Литература",
    "Обществознание", "Иностранный язык", "Биология", "История",
    "Основы безопасности жизнедеятельности (ОБЖ)"
]


def get_pupil_from_db(name):
    try:
        pupil = Schoolkid.objects.get(full_name__icontains=name.title())
        return pupil
    except ObjectDoesNotExist:
        print("Такой ученик в школе не учится. Попробуйте еще раз или уточните запрос\n"
              "Возможно, стоит поменять фамилию и имя местами")
    except MultipleObjectsReturned:
        print("Найдено несколько учеников, уточните запрос!")


def correct_points(pupil):
    marks = Mark.objects.filter(schoolkid=pupil, points__lte=3)
    for num in range(marks.count()):
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
                                           group_letter=pupil.group_letter,
                                           subject=subject)

    random_date_subject = random.choice(pupils_subject)
    teacher_id = Teacher.objects.filter(full_name=random_date_subject.teacher).first()
    commendation = Commendation.objects.filter(subject=subject,
                                               schoolkid=pupil,
                                               created=random_date_subject.date)

    commendation.create(text=random.choice(COMMENDATIONS),
                        created=random_date_subject.date,
                        schoolkid=pupil,
                        teacher=teacher_id,
                        subject=subject)


while True:
    choice, commendation_subject, pupil = "", "", None
    print("Вас приветствует система взлома электронного дневника!\n"
          "Введите, пожалуйста, свои фамилию и имя через пробел")
    while not pupil:
        name = input(":")
        pupil = get_pupil_from_db(name)
    correct_points(pupil)
    remove_chastisements(pupil)
    print("Оценки исправлены, замечания удалены")
    while choice != "нет":
        if choice not in ("да", "нет"):
            choice = input("Как насчет того, чтобы похвалить себя любимого?\n"
                           "Да/Нет?: ").lower()
        if choice == "нет":
            sys.exit("Завершаю работу. Не забудьте удалить следы своего присутствия на сайте!")
        while not commendation_subject:
            pprint(SUBJECTS)
            commendation_subject = input("Выберите название предмета из списка: ")
            if commendation_subject in SUBJECTS:
                create_commendation(commendation_subject, pupil)
            else:
                print("Где-то опечатка. Сверьтесь с названием из списка, а лучше скопируйте его")
            commendation_subject = None

