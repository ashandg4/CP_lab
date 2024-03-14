# Create a class to represent a book with attributes and methods
# Implement inheritance by creating the subclass for different types of books

class Books:
    def __init__(self,title,author,page_no):
        self.title=title
        self.author=author
        self.page_no=page_no
    
    
class Fiction(Books):
    def __init__(self,title,author,page_no):
        self.title="Marvel"
        self.author="Ashu"
        self.page_no=100
        
class Non_Fiction(Books):
    def __init__(self,title,author,page_no):
        self.title="A Brief History of Time"
        self.author="Anand"
        self.page_no=99

class Comic(Books):
    def __init__(self,title,author,page_no):
        self.title="Shinchan"
        self.author="Aditya"
        self.page_no=57

class Horror(Books):
    def __init__(self,title,author,page_no):
        self.title="The Conjuring"
        self.author="Chiku"
        self.page_no=289