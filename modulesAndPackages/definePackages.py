# Package - A package is a folder that contains Python files (modules)
# It is used to organize large programs neatly
# if there is no package for modules then Files become messy as project grows
# Why Packages
# --> Organize code
# --> Avoid confusion
# --> Reuse code
# --> Easy maintenance
# i created a package called calculator and inside i created a two modules 
import calculator.square as s
print("square of given number is:",s.squareOf(3)) #9
import calculator.cube as c
print("cube of given number is:",c.cubeOf(2)) #8

