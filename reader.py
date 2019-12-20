import pandas

def init():
    df = pandas.read_csv('exam.csv',usecols=[1,3,4,5,6,7])
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
            date = course[2]
            time = course[3]
            place = course[4] + " at " + course[5]
            return Course + " will be on " + date + " begin at " + time + " in " + place


def addSpace(w):
    newStr = ""
    for i in range(len(w)):
        newStr += w[i]
        if i == 3:
            newStr += " "
    return newStr

def run():
    print("fetching data......")
    allCourses = init()
    print("Please input your courses, and separate them by ','")
    courses = input()
    courselist=courses.split(",")
    print("----------------------------------------------------")
    for course in courselist:
        print(read(course,allCourses))

if __name__ == '__main__':
    run()
