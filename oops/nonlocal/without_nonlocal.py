def outer():
    x = 10
    def inner():
        x = x + 10
        print(x) # treats x as new local variable so we didnt give any value for that so it exits an error.
    inner()
outer()