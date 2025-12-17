# dataFrame - a dataframe is a 2-Dimensional, 
# Like an Excel sheet / SQL table,
# Made of rows + columns
# Each column is a Series
#--> A DataFrame is a collection of Series sharing the same index

# creating a dataframe using dict
import pandas as pd
df=pd.DataFrame({
    "name":["tharun","kumar","nani","rahul"],
    "age":[22,23,29,35],
    "marks":[100,86,66,95]
})
print(df)
"""
     name  age  marks
0  tharun   22    100
1   kumar   23     86
2    nani   29     66
3   rahul   35     95
"""
# creating dataframe from list of lists
data=[
    ["banana",5,"yellow"],
    ["apple",15,"red"],
    ["watermelon",55,"green"]
]
df1=pd.DataFrame(data,columns=["fruits","price","color"])
print(df1)
"""
       fruits  price   color
0      banana      5  yellow
1       apple     15     red
2  watermelon     55   green
"""

# creating dataframe from list of dictionaries
d=[
    {"name":"tharun","age":22,"location":"Nandyal"},
    {"name":"kumar","age":23,"location":"Hyderabad"},
    {"name":"nani","age":25,"location":"New Delhi"}
]
df2=pd.DataFrame(d)
print(df2)
"""
     name  age   location
0  tharun   22    Nandyal
1   kumar   23  Hyderabad
2    nani   25  New Delhi
"""

# dataframe properties
dfs=pd.DataFrame({
    "name":["tharun","kumar","nani"],
    "age":[22,34,23],
    "college":["srec","rgm","svr"]
})
print(dfs.shape) # (3, 3) it returns no.of rows and columns
print(dfs.columns) # Index(['name', 'age', 'college'], dtype='object') it returns all column names
print(dfs.index) # RangeIndex(start=0, stop=3, step=1)
print(dfs.dtypes)
"""
name       object
age         int64
college    object
dtype: object
"""

# viewing data
#1. df.head() it returns first 5 rows
#2. df.tail() it returns last 5 rows
#3. df.info() it returns summary of that dataframe
n=pd.DataFrame({
    "singleDigit":[1,2,3,4,5,6,7,8,9],
    "doubleDigit":[10,20,30,40,50,60,70,80,90],
    "tripleDigit":[100,200,300,400,500,600,700,800,800],
    "endsWithOnes":[11,21,31,41,51,61,71,81,91],
    "endWithTwos":[12,22,32,42,52,62,72,82,92],
    "endsWithThrees":[13,23,33,43,53,63,73,83,93],
    "endsWithFours":[14,24,34,44,54,64,74,84,94],
    "endsWithFives":[15,25,35,45,55,65,75,85,95],
    "endsWithSix":[16,26,36,46,56,66,76,86,96]
})
print(n.head())
"""
   singleDigit  doubleDigit  tripleDigit  endsWithOnes  endWithTwos  endsWithThrees  endsWithFours  endsWithFives  endsWithSix
0            1           10          100            11           12              13             14             15           16
1            2           20          200            21           22              23             24             25           26
2            3           30          300            31           32              33             34             35           36
3            4           40          400            41           42              43             44             45           46
4            5           50          500            51           52              53             54             55           56
"""
print(n.tail())
"""
   singleDigit  doubleDigit  tripleDigit  endsWithOnes  endWithTwos  endsWithThrees  endsWithFours  endsWithFives  endsWithSix
4            5           50          500            51           52              53             54             55           56
5            6           60          600            61           62              63             64             65           66
6            7           70          700            71           72              73             74             75           76
7            8           80          800            81           82              83             84             85           86
8            9           90          800            91           92              93             94             95           96
"""
print(n.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 9 entries, 0 to 8
Data columns (total 9 columns):
 #   Column          Non-Null Count  Dtype
---  ------          --------------  -----
 0   singleDigit     9 non-null      int64
 1   doubleDigit     9 non-null      int64
 2   tripleDigit     9 non-null      int64
 3   endsWithOnes    9 non-null      int64
 4   endWithTwos     9 non-null      int64
 5   endsWithThrees  9 non-null      int64
 6   endsWithFours   9 non-null      int64
 7   endsWithFives   9 non-null      int64
 8   endsWithSix     9 non-null      int64
dtypes: int64(9)
memory usage: 776.0 bytes
None
"""

# Selecting Data
#1. select column
print(n["singleDigit"])
"""
0    1
1    2
2    3
3    4
4    5
5    6
6    7
7    8
8    9
Name: singleDigit, dtype: int64
"""
#2. multiple columns
print(n[["singleDigit","doubleDigit","tripleDigit"]])
"""
singleDigit  doubleDigit  tripleDigit
0            1           10          100
1            2           20          200
2            3           30          300
3            4           40          400
4            5           50          500
5            6           60          600
6            7           70          700
7            8           80          800
8            9           90          800
"""
#3. select rows
# we have two ways to select 
# labels - values inside the conatiner,index holds labels
# for example we have index range from 0 to 10 , in that the total 10 elements is known as index and each index is known as label.
# df.loc[0]     # by label if we dont have labels then index itself acts as labels
# df.iloc[0]    # by position
ns=pd.DataFrame({
    "singleDigit":[1,2,3,4,5,6,7,8,9],
    "doubleDigit":[10,20,30,40,50,60,70,80,90],
    "tripleDigit":[100,200,300,400,500,600,700,800,800],
    "endsWithOnes":[11,21,31,41,51,61,71,81,91],
    "endWithTwos":[12,22,32,42,52,62,72,82,92],
    "endsWithThrees":[13,23,33,43,53,63,73,83,93],
    "endsWithFours":[14,24,34,44,54,64,74,84,94],
    "endsWithFives":[15,25,35,45,55,65,75,85,95],
    "endsWithSix":[16,26,36,46,56,66,76,86,96]
},index=["a","b","c","d","e","f","g","h","i"])
print(ns.loc["a"])

"""
singleDigit         1
doubleDigit        10
tripleDigit       100
endsWithOnes       11
endWithTwos        12
endsWithThrees     13
endsWithFours      14
endsWithFives      15
endsWithSix        16
Name: a, dtype: int64
"""
print(ns.iloc[3]) # here 3 index value is also known as "d" index
"""
singleDigit         4
doubleDigit        40
tripleDigit       400
endsWithOnes       41
endWithTwos        42
endsWithThrees     43
endsWithFours      44
endsWithFives      45
endsWithSix        46
Name: d, dtype: int64
"""
# with multiple labels
print(ns.loc[["a","b"]])
"""
   singleDigit  doubleDigit  tripleDigit  endsWithOnes  endWithTwos  endsWithThrees  endsWithFours  endsWithFives  endsWithSix
a            1           10          100            11           12              13             14             15           16
b            2           20          200            21           22              23             24             25           26
"""
# with multiple index values
print(ns.iloc[[-1,-2]]) # it returns last two rows
"""
   singleDigit  doubleDigit  tripleDigit  endsWithOnes  endWithTwos  endsWithThrees  endsWithFours  endsWithFives  endsWithSix
i            9           90          800            91           92              93             94             95           96
h            8           80          800            81           82              83             84             85           86
"""

# select rows + specific columns
print(ns.loc[["a","b"],"singleDigit"])
"""
a    1
b    2
Name: singleDigit, dtype: int64
"""
print(ns.loc[["a","b","c"],["singleDigit","doubleDigit","tripleDigit"]])
"""
 singleDigit  doubleDigit  tripleDigit
a            1           10          100
b            2           20          200
c            3           30          300
"""
# filtering rows
marks_df = pd.DataFrame({
    "Maths":    [78, 85, 92, 66, 74, 88, 90, 69, 81, 95],
    "Physics":  [72, 80, 89, 60, 70, 85, 88, 65, 79, 91],
    "Chemistry":[75, 82, 90, 64, 73, 86, 89, 68, 80, 93]
}, index=["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10"])
print(marks_df["Maths"]>90) # condition true returns True else returns False
"""
s1     False
s2     False
s3      True
s4     False
s5     False
s6     False
s7     False
s8     False
s9     False
s10     True
Name: Maths, dtype: bool
"""
# also we can filter for multiple columns
print(marks_df[["Maths","Physics","Chemistry"]]>90)

"""
     Maths  Physics  Chemistry
s1   False    False      False
s2   False    False      False
s3    True    False      False
s4   False    False      False
s5   False    False      False
s6   False    False      False
s7   False    False      False
s8   False    False      False
s9   False    False      False
s10   True     True       True
"""
# Adding and modifying columns
marks_df["English"]=[45,78,88,67,46,90,87,56,73,99]

# add a column if any sub below 75 then they fail means it returns false other wise True

marks_df["passed"] = (
    (marks_df["Maths"] > 70) &
    (marks_df["Physics"] > 70) &
    (marks_df["Chemistry"] > 70) &
    (marks_df["English"] > 70)
)
print(marks_df)

# output:
"""
     Maths  Physics  Chemistry  English  passed
s1      78       72         75       45   False
s2      85       80         82       78    True
s3      92       89         90       88    True
s4      66       60         64       67   False
s5      74       70         73       46   False
s6      88       85         86       90    True
s7      90       88         89       87    True
s8      69       65         68       56   False
s9      81       79         80       73    True
s10     95       91         93       99    True
"""
# modify column
marks_df["English"]=marks_df["English"]+1
print(marks_df)

"""
     Maths  Physics  Chemistry  English  passed
s1      78       72         75       46   False
s2      85       80         82       79    True
s3      92       89         90       89    True
s4      66       60         64       68   False
s5      74       70         73       47   False
s6      88       85         86       91    True
s7      90       88         89       88    True
s8      69       65         68       57   False
s9      81       79         80       74    True
s10     95       91         93      100    True
"""

# dropping columns or rows
# axis 0 removes rows and whenever you remove row must place their index or label value
# axis 1 removes column and whenever you want to  remove column then must place their column name
print(marks_df.drop("passed",axis=1))
"""
 Maths  Physics  Chemistry  English  passed
s1     78       72         75       46   False
s2     85       80         82       79    True
s3     92       89         90       89    True
s4     66       60         64       68   False
s5     74       70         73       47   False
s6     88       85         86       91    True
s7     90       88         89       88    True
s8     69       65         68       57   False
s9     81       79         80       74    True
"""
print(marks_df.drop("s10",axis=0))
"""
Maths  Physics  Chemistry  English  passed
s1     78       72         75       46   False
s2     85       80         82       79    True
s3     92       89         90       89    True
s4     66       60         64       68   False
s5     74       70         73       47   False
s6     88       85         86       91    True
s7     90       88         89       88    True
s8     69       65         68       57   False
s9     81       79         80       74    True
"""

# Missing values in dataFrame
dfb = pd.DataFrame({
    "Name": ["A", "B", "C", "D"],
    "Maths": [80, None, 90, 85],
    "Science": [70, 88, None, 92]
})
print(dfb.isna()) # it returns true then thats place is empty otherwise there is a value
print(dfb.isnull()) # same funtionality for both isna() and isnull(0)

# output same for both methods
"""
 Name  Maths  Science
0  False  False    False
1  False   True    False
2  False  False     True
3  False  False    False
"""

# count missing values 
# it returns bool if true then it actual value is 1 or false its actual value is 0 by using sum() we count those values(true/false)
print(dfb.isna().sum())
"""
Name       0
Maths      1
Science    1
dtype: int64
"""
# there is also methods like notna() and notnull() it works exactly opposite to isna() and isnull()

# fill missing values by using s.fillna(0) not only zero we can give any value or character or bool to fill
# it returns float type Because NaN itself is a FLOAT in Python & NumPy

# dfb[["Maths","Science"]]=dfb[["Maths","Science"]].fillna(0).astype(int)
# print(dfb)
"""
 Name  Maths  Science
0    A     80       70
1    B      0       88
2    C     90        0
3    D     85       92
"""

# drop missing values using s.dropna() which deletes total row
# for drop purpose i do the fillna line as commented beacuse it has zeros but the dropna works only for None 
print(dfb.dropna())
"""
Name  Maths  Science
0    A   80.0     70.0
3    D   85.0     92.0
"""

# groupby groups rows based on column values and performs calculations on each group.
# groupby = split → apply → combine
# Splits data into groups
# Applies a function (sum, mean, count, etc.)
# Combines the result
db= pd.DataFrame({
    "Student": ["A","B","C","D","E","F"],
    "Class": ["10A","10A","10B","10B","10A","10B"],
    "Marks": [80, 75, 90, 85, 70, 88]
})
# Average marks per class
print(db.groupby("Class")["Marks"].mean())
"""
Class
10A    75.000000
10B    87.666667
"""
# multiple aggregations
print(db.groupby("Class")["Marks"].agg(["sum","mean","max","min","count"]))
"""
Class
10A    225  75.000000   80   70      3
10B    263  87.666667   90   85      3
"""
db["age"]=[12,13,11,10,14,13]
# Group by + multiple columns
print(db.groupby("Class")[["Marks","age"]].mean()) # this prints average age of two sections and average marks
"""
Class
10A    75.000000  13.000000
10B    87.666667  11.333333
"""
# Group by multiple keys
df2 = pd.DataFrame({
    "Class": ["10A","10A","10B","10B","10A","10A","10A","10B"],
    "Gender": ["M","F","M","F","M","M","F","F"],
    "Marks": [80, 75, 90, 85, 77, 98, 99, 78]
})
print(df2.groupby(["Class","Gender"])["Marks"].mean())

"""
Class  Gender
10A    F         87.0
       M         85.0
10B    F         81.5
       M         90.0
"""

# sort_values() → order by column values - Ascending (default)
print(df2.sort_values("Marks"))
"""
Class Gender  Marks
1   10A      F     75
4   10A      M     77
7   10B      F     78
0   10A      M     80
3   10B      F     85
2   10B      M     90
5   10A      M     98
6   10A      F     99
"""
# if we want descending order then use ascending=false
print(df2.sort_values("Marks",ascending=False))
"""
Class Gender  Marks
6   10A      F     99
5   10A      M     98
2   10B      M     90
3   10B      F     85
0   10A      M     80
7   10B      F     78
4   10A      M     77
1   10A      F     75
"""
# Order by multiple columns
print(df2.sort_values(["Gender","Marks"],ascending=[True,True])) # we dont need to write if we want ascending order with any no.of columns selected

# sorting index in ascending or descending order using sort_index()
print(df2.sort_index()) # it shows as ascending order
print(df2.sort_index(ascending=False)) # it shows in descending order
"""
Class Gender  Marks
7   10B      F     78
6   10A      F     99
5   10A      M     98
4   10A      M     77
3   10B      F     85
2   10B      M     90
1   10A      F     75
0   10A      M     80
"""

# Read CSV 
data=pd.read_csv("filename.csv")
# start the analysis on file

# read Excel
Edata=pd.read_excel("filename.xlsx")
# start the analysis on file