# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
heights = n + 1
#n is the length of the list but counts from 0 so you need to add 1.

#Another alternative for n:
# heights = 0 
# for students in student_heights:
  # heights =+ 1

total = 0
#Start with 0 and keep adding every element in the list
for m in student_heights:
    total = m + total 

average = round(total / heights)
print(average)
