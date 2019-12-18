import tabula

def init():
    df = tabula.read_pdf(
        "https://www.mcgill.ca/exams/files/exams/december_2019_final_exam_schedule_with_room_locationsd12.pdf",
        pages="all")
    allCourses = df.values.tolist()
    return allCourses


def read(Course,allCourses):
    Course = Course.strip()
    Course = Course.upper()
    date = ""
    time = ""
    place = ""
    if len(Course) != 8:
        Course = addSpace(Course)
    for course in allCourses:
        if course[0] == Course:
            date = course[3]
            time = course[4]
            place = course[5] + " at " + course[6]
            return Course + " will be on " + date + " begin at " + time + " in " + place


def addSpace(w):
    newStr = ""
    for i in range(len(w)):
        newStr += w[i]
        if i == 3:
            newStr += " "
    return newStr


if __name__ == '__main__':
    print("fetching data......")
    allCourses = init()
    print("Please input your courses, and separate them by ','")
    courses = input()
    courselist=courses.split(",")
    for course in courselist:
        print(read(course,allCourses))