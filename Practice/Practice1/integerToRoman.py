num=1568
values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
#  why we taakes only these values beacuse we know that 1000 before value must substract with bigger vvalues so changes occurs only in these values only 
symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
result=""
for i in range(len(values)):
    while num >= values[i]:
        result+=symbols[i]
        num-=values[i]
print(result)
