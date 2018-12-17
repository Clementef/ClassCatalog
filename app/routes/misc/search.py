from app.routes.Classes import Teacher, Course


def searchteachers(find):

    ls = []
    find = find.lower()
    find = find.split()

    for i in find:
        for j in Teacher.objects:
            if i in j.name.lower():
                ls.append(j.name)

    return ls


def searchcourses(find):

    ls = []
    find = find.lower()
    find = find.split()

    for i in find:
        for j in Course.objects:
            if i in j.name.lower():
                ls.append(j.name)

    return ls



