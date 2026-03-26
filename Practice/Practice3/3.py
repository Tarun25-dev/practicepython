"""
Question: Dictionary + Sorting + Logic
You are given a dictionary where:
Keys are student names
Values are marks (integers)
task:
Sort the dictionary by marks in descending order
If two students have same marks, sort them alphabetically by name
Return only the names in the correct order
Example Input:
Python
Copy code
{
    "Tarun": 85,
    "Akhil": 92,
    "Ravi": 85,
    "Balu": 75
}
Expected Output:
Python
Copy code
['Akhil', 'Ravi', 'Tarun', 'Balu']
"""

d = {
    "Tarun": 85,
    "Akhil": 92,
    "Ravi": 85,
    "Balu": 75
}

# Sort by marks (descending) and name (ascending)
result = sorted(d.items(), key=lambda x: (-x[1], x[0]))

# Extract only names
names = [name for name, marks in result]

print(names)
