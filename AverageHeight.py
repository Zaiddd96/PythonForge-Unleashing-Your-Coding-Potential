students_height = input().split()
sum = 0
count = 0
for i in range(0,len(students_height)):
  students_height[i] = int(students_height[i])
  sum += students_height[i]
  count += 1
  avg = sum/count
print(f"total height = {sum}\nnumber of students = {count}\naverage height = {round(avg)}")

