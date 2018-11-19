class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(self.name + "'s email address has been updated")

    def __repr__(self):
        return "User " + self.name + " at " + self.email + " has read " + str(len(self.books)) + " books."

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
    
    def get_average_rating(self):
        total_ratings = 0
        for book in self.books.keys():
            total_ratings += self.books[book]
        try:
            average_ratings = total_ratings / len(self.books.keys())
            return average_ratings
        except ZeroDivisionError:
            return 0
        
    
patergia = User("Patrick Wright", "patergia@yahoo.com") 
            
#records isbn's to help ensure no duplicates
all_isbn = []





class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("the ISBN of " + self.title + " has been updated.")
    
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
        
    def get_ratings(self):
        return self.ratings
    
    def get_average_rating(self):
        total_ratings = 0
        for rating in self.ratings:
            total_ratings += rating
        return total_ratings / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))

first_book = Book("How to Train Your Dragon", 112358)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return self.title + " by " + self.author

class Non_Fiction(Book):
    def __init__(self , title , subject , level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return self.title + " , a " + self.level + " manual on " + self.subject


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        
        
    def create_book(self, title, new_isbn):
        all_isbn.sort()
        for old_isbn in all_isbn:
            if old_isbn == new_isbn:
                new_isbn = all_isbn[-1] + 1
                break
        all_isbn.append(new_isbn)
        return Book(title, new_isbn)
    
    def create_novel(self, title, author, new_isbn):
        all_isbn.sort()
        for old_isbn in all_isbn:
            if old_isbn == new_isbn:
                new_isbn = all_isbn[-1] + 1
                break
        all_isbn.append(new_isbn)
        return Fiction(title, author, new_isbn)
    
    def create_non_fiction(self, title, subject, level, new_isbn):
        all_isbn.sort()
        for old_isbn in all_isbn:
            if old_isbn == new_isbn:
                new_isbn = all_isbn[-1] + 1
                break
        all_isbn.append(new_isbn)
        return Non_Fiction(title, subject, level, new_isbn)
    
    
    def add_book_to_user(self, book, email, rating=None):
        try:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if self.books.get(book) == None:
                self.books[book] = 1
            else:
                self.books[book] += 1
        except KeyError:
            print("No user with email " + email + "!")
    
    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("This user already exists!")
        else:
            new_user = User(name, email)
            if user_books != None:
                for user_book in user_books:
                    self.add_book_to_user(user_book, new_user.get_email())
            self.users[email] = new_user
    
    def print_catalog(self):
        for book in self.books.keys():
            print(book)
    
    def print_users(self):
        for address in self.users:
            print(self.users[address])
            
    def get_most_read_book(self):
        most_read_value = 0
        most_read_key = None
        for book in self.books.keys():
            if self.books[book] > most_read_value:
                most_read_value = self.books[book]
                most_read_key = book
        return most_read_key
    
    def highest_rated_book(self):
        highest_rating = 0
        highest_rated_book = None
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating = book.get_average_rating()
                highest_rated_book = book
        return highest_rated_book
    
    def most_positive_user(self):
        highest_rating = 0
        most_positive_user = None
        for email in self.users.keys():
            if self.users[email].get_average_rating() > highest_rating:
                highest_rating = self.users[email].get_average_rating()
                most_positive_user = self.users[email]
        return most_positive_user



