class AboutMeClass:
    year=2024
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    
    def add_age(self):
        self.age=self.age+1
        
    def relocate(self,place):
        self.place=place   
    
    def display(self):
        print("Year: "+str(AboutMeClass.year))
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("Place: "+self.place)
    
    @classmethod
    def add_year(cls):
        cls.year=cls.year+1  
    @staticmethod
    def display_welcome():
        print("Welcome")

x=AboutMeClass("Anugrah",18,"Kannur")
y=AboutMeClass("Athul",17,"Kannur")

AboutMeClass.display_welcome()

x.display()
y.display()

print("--------------------------------------------------------------")


x.add_age()
y.add_age()
AboutMeClass.add_year()

x.display()
y.display()