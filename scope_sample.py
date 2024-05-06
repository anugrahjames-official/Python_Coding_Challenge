def check_scope():
    def do_local():
        test="local test"
    def do_nonlocal():
        nonlocal test
        test="nonlocal test"
    def do_global():
        global test
        test="global test"
    
    test="default test"
    do_local()
    print("test value after do_local: "+test)
    do_nonlocal()
    print("test value after do_nonlocal: "+test)
    do_global()
    print("test value after do_global: "+test)

check_scope()
print("test value after main: "+test)  