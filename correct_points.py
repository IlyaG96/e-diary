from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Chastisement

schoolkid = Schoolkid()
name = "Голубев Феофан Владленович"


def correct_points(schoolkid, name):
    pupil = schoolkid.objects.filter(full_name__contains=name)
    pupil = pupil[0]
    marks_query = Mark.objects.filter(schoolkid=pupil, points__lte=3)
    marks_total = marks_query.count()
    for index in range(marks_total):
        mark_to_correct = marks_query[index]
        mark_to_correct.points = 5
        mark_to_correct.save()


def remove_chastisements(schoolkid, name):
    pupil = Schoolkid.objects.filter(full_name__contains=name)
    pupil = pupil[0]
    chastisements = Chastisement.objects.filter(schoolkid=pupil)
    chastisements.delete()
