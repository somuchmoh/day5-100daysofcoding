# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = student_scores[0]
#Start with the first score and keep comparing it to the others to see which is greater. Replace is greater than existing score. 

for score in student_scores:
    if max_score < score:
        max_score = score 

print(f"The highest score in the class is: {max_score}")
