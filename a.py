"""
#Car rental

class Car:
    def __init__(self, model, price_per_day, km):
        self.model = model
        self.price_per_day = price_per_day
        self.km = km

    @property
    def car_info(self):
        return f"{self.model.title()}, costs ${self.price_per_day} a day, km = {self.km}"

    def calculate_rent(self, days):
        return self.price_per_day * days

    def car_is_in_good_state(self):
        if self.km < 10000:
            return True
        return False

class Sedan(Car):

    #Sedan will cost more if used for rural areas.
    
    def __init__(self, model, price_per_day, km, for_rural=False):
        super().__init__(model, price_per_day, km)
        self.for_rural = for_rural

    def calculate_rent(self, days):
        if self.for_rural:
            return (self.price_per_day+10) * days
        else:
            return self.price_per_day * days

class SUV(Car):
    #SUV costs less for each consecutive day.
    def __init__(self, model, price_per_day, km):
        super().__init__(model, price_per_day, km)

    def days_discount(self, days):
        summa = 0
        for day  in range(days):
            summa += day * 3
        return summa

    def calculate_rent(self, days):

        return self.price_per_day * days - self.days_discount(days)


class Truck(Car):
    #Trucks have a flat fee of $40 charged on the first day

    def __int__(self, model, price_per_day, km):
        super().__init__(model, price_per_day, km)

    def calculate_rent(self, days):
        return self.price_per_day * days + 40


class Rental_system:
    def __init__(self):
        self.cars = []
        self.available = []
    def add_cars(self, car):
        self.cars.append(car)
        self.available.append(car)
    def show_available_cars(self):
        return [car.model for car in self.available]



    def rent_car(self, model):
        for car in self.cars:
            if car.model == model:
                self.available.remove(car)
                print(f"You have rented {car.model}")
                return

        raise ValueError("No such cars in the list")

    def return_rented_car(self, model):
        for car in self.cars:
            if car.model == model:
                self.available.append(car)









suv = SUV("Gruzi", 50, 12000)
car1 = Car("Nexia", 40, 15000)
truck1 = Truck("Gorilla", 55, 14000)
sedan1 = Sedan("Sadnik", 35, 8000)

rental_systema = Rental_system()

cars = [suv, car1, truck1, sedan1]
for car in cars:
    rental_systema.add_cars(car)
print(rental_systema.show_available_cars())

try:
    rental_systema.rent_car("Gruzi")
except ValueError as e:
    print(f"Error: {e}")

print(rental_systema.show_available_cars())
rental_systema.return_rented_car("Gruzi")
print(rental_systema.show_available_cars())

"""


"""
#Library system
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"The book's title: {self.title}, author: {self.author}, was published in {self.year}"

class Reader:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []
        self.limit = False
    def borrow_a_book(self, book):
        self.reach_the_limit()
        if self.limit is False:
            self.borrowed_books.append(book)

    def return_the_book(self, book):
        self.borrowed_books.remove(book)

    @property
    def borrowed_count(self):
        return len(self.borrowed_books)

    def reach_the_limit(self):
        if len(self.borrowed_books) > 4:
            self.limit = True
            return f"You have reached the limit of possible book borrowings"
        return f"You haven't yet reached the limit of 4 books at a time"

class Library:

    def __init__(self):
        self.list_of_books = []

    def add_book(self, book):
        try:
            self.list_of_books.append(book)
        except Exception as e:
            print(e)

    def list_books(self):
        return [book.title  for book in self.list_of_books]

    def remove_book(self, title):
        for book in self.list_of_books:
            if book.title == title:
                self.list_of_books.remove(book)
                return print("Book added!")
        else:
            print("Error. There is no book with such a title.")

    def total_books(self):
        return f"The total number of books: {len(self.list_of_books)}"


books = [Book("The fault in our stars", "Jack Green", 2020), Book("1984", "George Orwell", 1953), Book("Soul land", "Tang Jia San Shao", 2014), Book("Battle through the heavens", "Heavenly silkworm", 2012)]

lib = Library()

for book in books:
    lib.add_book(book)

print(lib.list_books())
print(lib.total_books())
lib.remove_book("1984")
print(lib.total_books())

"""