"""Valid Anagram
Given two strings, return true if one is an anagram of the other.
"""
str1=str(input("Enter string1:")).lower()
str2=str(input("Enter string2:")).lower()
if len(str1) != len(str2):
    print("Not an anagram")
else:
    freq1={}
    freq2={}
    for ch in str1:
         freq1[ch]=freq1.get(ch,0)+1
    for ch in str2:
        freq2[ch]=freq2.get(ch,0)+1
if freq1==freq2: # even though order is incorrect ,python checks key > hash > value to another dict of same key with same value
    print("Anagram")
else:
    print("Not an anagram")

#method 2
str3=str(input("Enter string1:")).lower()
str4=str(input("Enter string2:")).lower()
if len(str3) != len(str4):
    print("Not an anagram")
else:
    is_anagram=True
    for s in str3:
      if str3.count(s)!=str4.count(s):
          is_anagram=False
    print(is_anagram)


