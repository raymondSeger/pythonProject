def scope_test():
    def do_local():
        spam = "local spam"

    # the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there. spam variable in THIS function will be that value, but spam in GLOBAL scope is still not changed
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    # the global statement indicates that particular variables live in the global scope. Think of it as window in Javascript.
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

# test creating variables inside a function. we use nonlocal and global

scope_test()
print("In global scope:", spam)