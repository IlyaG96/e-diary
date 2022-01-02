import random

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
from datacenter.models import Subject
from datacenter.models import Teacher

commendations = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!"
]

subjects = [
    "Краеведение",
    "География",
    "Математика",
    "Музыка",
    "Физкультура",
    "Изобразительное искусство",
    "Технология",
    "Русский язык",
    "Литература",
    "Обществознание",
    "Иностранный язык",
    "Биология",
    "История",
    "Основы безопасности жизнедеятельности (ОБЖ)",
]


def chose_pupil(input_name):
    while True:
        pupil = Schoolkid.objects.filter(full_name__contains=input_name).first()
        return pupil


def correct_points(name):
    pupil = chose_pupil(name)
    marks_query = Mark.objects.filter(schoolkid=pupil, points__lte=3)
    marks_total = marks_query.count()
    for index in range(marks_total):
        mark_to_correct = marks_query[index]
        mark_to_correct.points = 5
        mark_to_correct.save()


def remove_chastisements(name):
    pupil = chose_pupil(name)
    chastisements = Chastisement.objects.filter(schoolkid=pupil)
    chastisements.delete()


def create_commendation(commendation_subject, name):
    pupil = chose_pupil(name)
    year_of_study = pupil.year_of_study
    group_letter = pupil.group_letter
    subject = Subject.objects.filter(year_of_study=year_of_study, title=commendation_subject).first()
    pupils_subject = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter,
                                           subject=subject).first()
    teacher = pupils_subject.teacher
    teacher_id = Teacher.objects.filter(full_name=teacher).first()
    date = pupils_subject.date
    commendation = Commendation.objects.filter(subject=subject, schoolkid=pupil, created=date)
    commendation_text = random.choice(commendations)
    commendation.create(text=commendation_text, created=date, schoolkid=pupil, teacher=teacher_id, subject=subject)


def main():
    input_name = input("Вас приветствует система взлома электронного дневника!\n "
                       "Введите, пожалуйста, свои фамилию и имя через пробел")
    name = chose_pupil(input_name)
    if not name:
        print("Такой ученик в школе не учится. Попробуйте еще раз")
    action = int(input("выберите желаемое действие\n"
                        "1 - исправить оценки\n"
                        "2 - удалить замечания\n"
                        "3 - создать похвалу\n"))
    if action not in range(1, 4):
        commendation_subject = input("Напишите название предмета, на котором вас надо похвалить")



input_name = input("Вас приветствует система взлома электронного дневника!\n "
                   "Введите, пожалуйста, свои фамилию и имя через пробел")
chose_pupil(input_name)