string='()[]{}'
stack=[]
pairs={
    ')':'(',
    '}':'{',
    ']':'['
}
for ch in string:
    if ch in pairs: # which checks keys
        if not stack or stack[-1]!=pairs[ch]: #not stack gives true if no elements in stack also we can write len(stack)==0
            # and also if stack last element not equals current ch value in pairs then also failed
            print(False)
            exit()
        stack.pop() #if the above if statement skips then we matched the bracket in stack then we remove 
    else:
        stack.append(ch) # the ch value is not in pairs which means in pairs only key(closing brackets) are there if the ch value is opening  bracket then we add that symbol into string.
print(len(stack)==0) # we already pop the pair if there are a valid paranthesis from stack so finall stack is now empty otherwise the is extra or misvalid paranthesis so false

