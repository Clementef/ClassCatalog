from app.routes.Classes import Teacher, Course


def searchteachers(find):

    find = find.lower()

    find = find.split()

    for i in find:

        for j in Teacher.objects:

            if i in j.name.lower():

                print(j.name)


def searchcourses(find):

    find = find.lower()

    find = find.split()

    for i in find:

        for j in Course.objects:

            if i in j.name.lower():

                print(j.name)


searchcourses("ap")

