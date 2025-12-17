# series - A Series is: 1-Dimensional, Like a single column in Excel and Has index + values
# creating a series:
# Series stores data as a NumPy array
# series with mixed datatypes are considered as an object
import pandas as pd
s=pd.Series([10,20,30,40,50])
print(s)

# output:
"""
0    10
1    20
2    30
3    40
4    50
dtype: int64

"""
# if we give strings it automatically treats as an object
ss=pd.Series(["t","u"])
print(ss)

# output:
"""
0    t
1    u
dtype: object

"""

sss=pd.Series([1.2,3.4,5.4,1.2])
print(sss)
"""
0    1.2
1    3.4
2    5.4
3    1.2
dtype: float64

"""
"""
| Feature          | NumPy Array | Pandas Series  |
| ---------------- | ----------- | -------------- |
| Internal storage | NumPy array | NumPy array    |
| Index            | no          | yes            |
| Missing values   | Limited     | Strong support |
| Data alignment   | no          | yes            |
"""

# custom index
ps=pd.Series([10,2,30,44], index=["a","b","c","d"])
print(ps)

# output:
"""
a    10
b     2
c    30
d    44
dtype: int64

"""
# from a dictionary:
sp=pd.Series({"name":"tharun","age":22,"college":"srec"})
print(sp)

# output:
"""
name     tharun 
age          22
college    srec
dtype: object
"""

# accessing elements from dictionary
#1. by index label
print(sp["name"]) #tharun
#2. by position
print(sp[1]) #22
#3. by multiple values
print(sp[["age","college"]])


# output:
"""
age          22
college    srec
"""

# series properties
#1. x.index
x=pd.Series([1,2,3,4,5])
print(x.index)
# RangeIndex(start=0, stop=5, step=1)
# start-inclusive, stop-exclusive,step-takes every first element
#2. y.values - shows all values
y=pd.Series([1,2,3,4,5,6])
yy=pd.Series({1:"a",2:"b",3:"c",4:"d"})
print(y.values) # [1 2 3 4 5 6]
print(yy.values) # ['a' 'b' 'c' 'd']
#3.dtype it shows which datatype
print(y.dtype) #int64
print(yy.dtype) #object

# vectorized operations - no loops needed like s+5,s>20
marks=pd.Series([10,45,21,34,12,54])
print(marks+10)

# output:
"""
0    20
1    55
2    31
3    44
4    22
5    64
dtype: int64
"""
print(marks>35) # it returns true or false
"""
0    False
1     True
2    False
3    False
4    False
5     True
dtype: bool
"""
# series methods
series=pd.Series([1,2,3,4,5,6,7,8,9])
print(series.sum()) #45
print(series.min()) #1
print(series.max()) #9
print(series.mean()) #5.0
print(series.median()) #5.0
 
# handling missing values:
numbers=pd.Series([10,20,None,40,50])
# when we place any None in series/dataframe it is automatically becomes Nan then thats why it converted into float
print(numbers)
"""
0    10.0
1    20.0
2     NaN
3    40.0
4    50.0
dtype: float64
"""
# to find missing values
print(numbers.isna()) # it returns true if there is no value otherwise it returns false
print(numbers.isnull()) # both methods are valid to find missing values

"""
0    False
1    False
2     True
3    False
4    False
dtype: bool
"""
# we also use notna(), notnull() for existing values if the value is there it retruns true else it returns false
print(numbers.notna())
print(numbers.notnull())

"""
0     True
1     True
2    False
3     True
4     True
dtype: bool
"""
# count missing values 
# it returns bool if true then it actual value is 1 or false its actual value is 0 by using sum() we count those values(true/false)
print(numbers.isna().sum()) #1 there is one missing values

# fill missing values by using s.fillna(0) not only zero we can give any value or character or bool to fill
# it returns float type Because NaN itself is a FLOAT in Python & NumPy
print (numbers.fillna(0).astype(int)) # we converted float to int

"""
0    10
1    20
2     0
3    40
4    50
dtype: int64
"""

# drop ,missing values using s.dropna()
print(numbers.dropna())
"""
0    10.0
1    20.0
3    40.0
4    50.0
"""
# nan != nan (true)
# nan == nan (false)
# NaN means “unknown / missing”
# If two values are unknown, you cannot say they are equal.
# if there is no value it remains constant as nan 

print(numbers.ffill()) # in the pov from previous element of missing element is always forward element
print(numbers.bfill()) # in the pov from next element of missing element is always backward element

"""
dtype: float64
0    10.0
1    20.0
2    20.0
3    40.0
4    50.0
dtype: float64
"""
"""
0    10.0
1    20.0
2    40.0
3    40.0
4    50.0
dtype: float64
"""