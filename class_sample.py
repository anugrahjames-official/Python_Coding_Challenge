class   MySampleClass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print("Hello "+self.name)   

x=MySampleClass()
y=MySampleClass()
name=input("Enter your name: ")
x.hello(name)
x.print_name()

y.hello("Anugrah")
y.print_name()