# match cse - To handle complex conditions easily
# match-case is not just switch — it’s pattern matching.
# It can match: Values, Multiple values, Data structures, Types, Conditions.
day=int(input("enter day :"))
match day:
    case 1|7:
        print("Weekend")
    case 2|3|4|5|6:
        print("Weekday")
    case _: # DEFAULT CASE - It is executed when no other case matches.
        print("you entered wrong day")
    
# task
# split() - Removes leading spaces, Removes trailing spaces, Treats multiple spaces as ONE separator.
# split() always stores the result in a LIST.
print("Enter command: ")
command=input().split()
match command:
    case "start":
        print("System started")
    case "end":
        print("System ended")
    case "restart":
        print("System restarted")
    case ("add",a,b):
        print("addition of two numbers are :",a+b)
    case ("sub",a,b):
        print("substraction of two numbers are :",a-b)
    case ("mul",a,b):
        print("multiplication of two numbers are :",a*b)
    case ("div",a,b) if b!=0:
        print("division of two numbers are :",a/b)
    case ("div",a,0):
        print("Error: division by zero")
    case _:
        print("invalid command")