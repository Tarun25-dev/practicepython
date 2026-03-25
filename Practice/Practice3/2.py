"""Question 1: Task Scheduling

A system manages a list of tasks, where each task has a priority and the time required to complete it.
You are given "N" tasks.

Each task has:

"priority" (smaller value = higher priority)
"time" required to complete the task
Sort the tasks based on:
Ascending order of priority
If priorities are the same, sort by ascending time
Important: Use Selection Sort to perform the sorting.

Input Format:

First line: integer "N"
Next "N" lines: two integers "priority" and "time"

Output Format:

Print sorted tasks ("priority time")
Sample Input:

5

1 10

2 5

1 5

3 7

2 3

Sample Output:

1 5, 1 10, 2 3, 2 5, 3 7
"""

n = int(input("Enter number of tasks: "))

tasks = []

# Input
for _ in range(n):
    p, t = map(int, input().split())
    tasks.append([p, t])

# Selection Sort
for i in range(n):
    min_idx = i
    
    for j in range(i + 1, n):
        # Compare priority first
        if tasks[j][0] < tasks[min_idx][0]:
            min_idx = j
        # If priority same, compare time
        elif tasks[j][0] == tasks[min_idx][0]:
            if tasks[j][1] < tasks[min_idx][1]:
                min_idx = j
    
    # Swap
    tasks[i], tasks[min_idx] = tasks[min_idx], tasks[i]

# Output
for task in tasks:
    print(task[0], task[1], end=", ")
