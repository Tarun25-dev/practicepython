# Problem: 3 trainees run 3 rounds.
# Record oxygen level (1–100) after each round. 
# Find trainee with highest average oxygen. If tie, select all.
# If all averages < 70, print 'All trainees are unfit'.
# Invalid input if oxygen is not between 1 and 100.

trainee = []
for t in range(1,4):
    levels = []
    valid = True
    for x in range(3):
        o = int(input())
        if not (1<= o <=100):
            valid = False
        levels.append(o)
    if not valid:
        print("Invalid")
    else:
        trainee.append(round(sum(levels)//3,2)) # 2 is for after point two decimal numbers.
if max(trainee)<70:
    print("All trainees are unfit")
else:
    best = max(trainee)
    for i,v in enumerate(trainee):
        if v == best:
            print(f"Trainee {i+1}: {best}")
            