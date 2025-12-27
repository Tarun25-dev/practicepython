"""Reverse Words in a String
Reverse the order of words in a sentence.
Example: "hello world" → "world hello"
"""
string=str(input("Enter sentence:"))
result=""
word=""
for i in range(len(string)-1,-1,-1):
    if string[i] !=" ":
        word=string[i]+word
    else:
        if word!="": #this prevents an extra  spaces in word and takes only existing words
            result+=word+" "
            word="" # must empty the word after add to the result beacuse we also store next  word i word variable
if word!="": # this is the last word but the loop doesnt identify the word beacuse it has no spaces for last word so thats why we need to do manually
    result+=word # word has a value of last loop where the string stops but it doesnt do the add to result beacuse it has no spaces before
print(result)


# method2
words=string.split() # Important behavior of split() without arguments: Removes leading spaces, Removes trailing spaces, Treats multiple spaces as one
result=" ".join(words[::-1]) # Places exactly one space between words, Does not place space at start, Does not place space at end
# join() concatenates list elements into a single string using the specified separator between them.
print(result)

        