from app.routes.Classes import Teacher, Course


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



