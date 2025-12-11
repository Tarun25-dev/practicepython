#when can call the child functions within the parent function is correct to call otherwise it rise an error
def parent():
    print("parent element")
    def child():
        print("child element")
    child() #when the parent calls it executes also child whenever child calls inside the parent otherwise py skips those lines
parent()    #first executes this function 