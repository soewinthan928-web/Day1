grades=("Excellent","Good","Pass","Fail")
students = []
for i in range(5):
    print("Student",i+1)
    name=input("Enter name: ")
    age=int(input("Enter age: "))
    study_hours=float(input("Enter study hours: "))
    score=int(input("Enter scores: "))
    while score<0 or score>100:
        print("Invalid score! Try again.")
        score= int(input("Enter scores: "))

    student={
        "name":name,
        "age":age,
        "study_hours":study_hours,
        "score":score
    }
    students.append(student)
def classify_grade(score):
    if score >= 80:
        return("Excellent")
    elif score >= 60:
        return("Good")
    elif score >= 40:
        return("Pass")
    else:
        return("Fail")

print()
print("==== STUDENT PERFORMANCE REPORT ====")
print()
for student in students:
    grade=classify_grade(student["score"])

    print("Name: ",student["name"])
    print("Age: ",student["age"])
    print("Study Hours: ",student["study_hours"])
    print("Score: ",student["score"])
    print("Grade",grade)
    print()

scores=[]

def calculate_average(scores):
    return sum(scores)/len(scores)

def count_passed(students):
    passed=0

    for student in students:
        if student["score"]>=40:
            passed+=1

    return passed

for student in students:
    scores.append(student["score"])

average=calculate_average(scores)
highest=max(scores)
lowest=min(scores)

print("====SUMMARY====")
print("Total Students: ",len(students))
print("Average Score: ",average)
print("Highest Score: ",highest)
print("Lowest Score: ",lowest)

passed=count_passed(students)
failed=len(students)-passed

print("Passed Students: ",passed)
print("Failed Students: ",failed)

top_std=students[0]

for student in students:
    if student["score"]>top_std["score"]:
        top_std=student

print("Top Student: ",top_std["name"])

