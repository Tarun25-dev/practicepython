# Problem:
# Read N student scores, compute average,
# print grade: A(≥90), B(≥75), C(≥60), D(≥50), F(<50).

n = int(input())
scores = [int(input()) for _ in range(n)]
avg = sum(scores)/n
grade = ''
if avg >= 90:
    grade = 'A'
elif avg >=75:
    grade = 'B'
elif avg >=60:
    grade = 'C'
elif avg >=50:
    grade = 'D'
elif avg < 50:
    grade = 'F'

print("average:",avg)
print("grade:",grade)