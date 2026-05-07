#This class stores booking details
class Booking:
    def __init__(self, booking_id, user, facility, date, time_slot, duration, total_cost=0, status="Pending"):
        self.booking_id = booking_id
        self.user = user
        self.facility = facility
        self.date = date
        self.time_slot = time_slot
        self.duration = duration
        self.total_cost = total_cost
        self.status = status

    #Getter and setter for booking ID
    def get_booking_id(self):
        return self.booking_id

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    #Getter and setter for user
    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user

    #Getter and setter for facility
    def get_facility(self):
        return self.facility

    def set_facility(self, facility):
        self.facility = facility

    #Getter and setter for date
    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    #Getter and setter for time slot
    def get_time_slot(self):
        return self.time_slot

    def set_time_slot(self, time_slot):
        self.time_slot = time_slot

    #Getter and setter for duration
    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    #Getter and setter for total cost
    def get_total_cost(self):
        return self.total_cost

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    #Getter and setter for status
    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    #Calculate total cost
    def calculate_cost(self):
        self.total_cost = self.duration * self.facility.get_price_per_hour()
        return self.total_cost

    #Confirm booking
    def confirm_booking(self):
        self.status = "Confirmed"

    #Cancel booking
    def cancel_booking(self):
        self.status = "Cancelled"
