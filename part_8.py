scores = [55,80,35,90,65]

scores.append(75)
print(scores)

scores[1]=85
print(scores)

print("Highest: ",max(scores))
print("Lowest: ",min(scores))

print("Average: ",sum(scores)/len(scores))

for score in scores:
    if score >= 80:
        print(score)