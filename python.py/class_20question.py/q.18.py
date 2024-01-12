import datetime

class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.reservations = []

    def check_availability(self, start_time, end_time):
        # Check if the room is available for the specified time slot
        for reservation in self.reservations:
            if (start_time < reservation.end_time and end_time > reservation.start_time):
                return False  # Room is already reserved for part of the specified time slot

        return True  # Room is available for the entire specified time slot

    def book_time_slot(self, user, start_time, end_time):
        # Book a time slot for the room
        if self.check_availability(start_time, end_time):
            reservation = Reservation(user, self, start_time, end_time)
            self.reservations.append(reservation)
            user.add_reservation(reservation)
            print(f"Room {self.room_number} booked by {user.username} from {start_time} to {end_time}.")
            self.send_notification(reservation)
        else:
            print("Room not available for the specified time slot.")

    def send_notification(self, reservation):
        print(f"Notification sent: Room {self.room_number} booked by {reservation.user.username} from {reservation.start_time} to {reservation.end_time}.")

class User:
    def __init__(self, username):
        self.username = username
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

class Reservation:
    def __init__(self, user, room, start_time, end_time):
        self.user = user
        self.room = room
        self.start_time = start_time
        self.end_time = end_time

# Example usage:
# Create rooms and users
room1 = Room(101, 20)
room2 = Room(102, 15)

user1 = User("Alice")
user2 = User("Bob")

# Book time slots
room1.book_time_slot(user1, datetime.datetime(2022, 5, 1, 10, 0), datetime.datetime(2022, 5, 1, 12, 0))
room1.book_time_slot(user2, datetime.datetime(2022, 5, 1, 14, 0), datetime.datetime(2022, 5, 1, 16, 0))
room2.book_time_slot(user1, datetime.datetime(2022, 5, 1, 15, 0), datetime.datetime(2022, 5, 1, 17, 0))

# Display reservations for users
print(f"\nReservations for {user1.username}:")
for reservation in user1.reservations:
    print(f"Room {reservation.room.room_number} from {reservation.start_time} to {reservation.end_time}")

print(f"\nReservations for {user2.username}:")
for reservation in user2.reservations:
    print(f"Room {reservation.room.room_number} from {reservation.start_time} to {reservation.end_time}")
