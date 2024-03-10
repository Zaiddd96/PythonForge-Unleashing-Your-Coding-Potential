#Find High Score!
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
        print(high_score)
        
print(f"The high score is {high_score}")
