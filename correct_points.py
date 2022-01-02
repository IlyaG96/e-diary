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

schoolkid = Schoolkid()
name = "Фролов Иван"


def chose_pupil(schoolkid, name):
    pupil = schoolkid.objects.filter(full_name__contains=name).first()

    return pupil


def correct_points(schoolkid, name):
    pupil = chose_pupil(schoolkid, name)
    marks_query = Mark.objects.filter(schoolkid=pupil, points__lte=3)
    marks_total = marks_query.count()
    for index in range(marks_total):
        mark_to_correct = marks_query[index]
        mark_to_correct.points = 5
        mark_to_correct.save()


def remove_chastisements(schoolkid, name):
    pupil = chose_pupil(schoolkid, name)

    chastisements = Chastisement.objects.filter(schoolkid=pupil)
    chastisements.delete()


# def add_commendation(schoolkid, name):
# pupil = chose_pupil(schoolkid, name)

pupil = Schoolkid.objects.filter(full_name__contains="Фролов Иван").first()

year_of_study = pupil.year_of_study
group_letter = pupil.group_letter

subject = Subject.objects.filter(year_of_study=year_of_study,
                                 title="Математика").first()
pupils_subject = Lesson.objects.filter(year_of_study=year_of_study,
                                       group_letter=group_letter,
                                       subject=subject).first()
teacher = pupils_subject.teacher
teacher_id = Teacher.objects.filter(full_name=teacher).first()
date = pupils_subject.first().date

commendation = Commendation.objects.filter(subject=subject,
                                           schoolkid=pupil,
                                           created=date)

commendation.create(text="Хвалю", created=date, schoolkid=pupil, teacher=teacher_id, subject=subject)
