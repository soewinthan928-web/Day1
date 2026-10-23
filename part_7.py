scores = [10,20,40,50,60]

def calculate_total(scores):
    return sum(scores)
def calculate_average(scores):
    return sum(scores)/len(scores)
def calssify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"

def count_passed(scores):
    passed = 0
    for score in scores:
        if score >= 40:
            passed+=1

print(calculate_total(scores))
print(calculate_average(scores))
print(count_passed(scores))
for score in scores:
    print(calssify_grade(score))