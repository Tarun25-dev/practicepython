def outer():
    x = 10
    def inner():
        nonlocal x # which takes x from outer function and must same variable name
        x= x + 10
        print(x)
    inner()
outer()