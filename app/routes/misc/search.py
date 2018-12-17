from app.routes.Classes import Teacher, Course, Room


def searchteachers(find):

    ls = []
    find = find.lower()
    find = find.split()

    for i in find:
        if len(i) == 1:
            for j in Teacher.objects:
                if i == j.name.lower()[-1]:
                    name = dict(name=j.name)
                    ls.append(name)
        else:
            for j in Teacher.objects:
                if i in j.name.lower():
                    name = dict(name=j.name)
                    ls.append(name)
    return ls


def searchcourses(find):

    ls = []
    find = find.lower()
    find = find.split()

    for i in find:
        for j in Course.objects:
            if i in j.name.lower():
                name = dict(name=j.name)
                ls.append(name)

    return ls


def searchroom(find):

    ls = []
    find.lower()

    for j in Room.objects:
        if find in j.location.lower():
            name = dict(name=j.location)
            ls.append(name)

    return ls