# Create a class Movie with the following:

# Attributes:
# movie_name -> name of the movie
# total_seats -> total seats available in the theatre
# ticket_price -> price per ticket
# booked_seats -> starts at 0

# Methods:
# book_ticket(num_tickets) – books the given number of tickets. If enough seats are available,
# confirm the booking and show the total amount to pay. If not,
# show "Sorry, not enough seats available"

# show_status() – displays movie name, seats available, and seats booked so far

class Movie:

     movie_name="Dhurandhar"
     total_seats=30
     ticket_price=250
     booked_seats=0

     def book_ticket(self,num_ticket) -> None:
        
        if num_ticket <= 0:
            print("Please enter a valid number of tickets")
        elif num_ticket > Movie.total_seats:
            print("Sorry, not enough seats available")
        else:
            print(f"Tickets Booked Successfully : {num_ticket}")
            print(f"Total Amount To Pay : {Movie.ticket_price*num_ticket}")

            Movie.booked_seats = Movie.booked_seats+num_ticket
            Movie.total_seats-=num_ticket

     def show_status(self) -> None:
        print(40*"*")
        print(f"Movie Name : {Movie.movie_name}")
        print(f"Total Seats : {Movie.total_seats}")
        print(f"Booked Seats : {Movie.booked_seats}")
            


m1 = Movie()

m1.book_ticket(5)
m1.show_status()

m2 = Movie()
m2.book_ticket(10)
m2.show_status()

        