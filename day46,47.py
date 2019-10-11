class Library :
   def __init__(self,book,shelf):
       self.book=book
       self.shelf=shelf
L=Library(300,45)

class science_section (Library):
    def __init__(self,name,book,shelf):
        super().__init__(book,shelf)
        self.name=name

    def printn(self):
        print(self.name , self.book,self.shelf)


x=science_section("physics books" , 300 , 45)
x.printn()


x.book=20
x.shelf=4
x.printn()

