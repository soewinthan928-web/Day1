scores = [45,70,85,30,90,55]
total = 0
for score in scores:
    total+=score
average = total / len(scores)
 
fail = 0
pas = 0
for score in scores:
    if score >= 40:
        pas += 1
    elif score < 40:
        fail +=1
print ("Total: ", total)
print ("Average: ", average)
print ("Number of passing score: ",pas)
print ("Number of failing score: ",fail)