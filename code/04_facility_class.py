#This class stores facility details
class Facility:
    def __init__(self, facility_id, name, facility_type, capacity, time_slots, price_per_hour):
        self.facility_id = facility_id
        self.name = name
        self.facility_type = facility_type
        self.capacity = capacity
        self.time_slots = time_slots
        self.price_per_hour = price_per_hour

    #Getter and setter for facility ID
    def get_facility_id(self):
        return self.facility_id

    def set_facility_id(self, facility_id):
        self.facility_id = facility_id

    #Getter and setter for facility name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    #Getter and setter for facility type
    def get_facility_type(self):
        return self.facility_type

    def set_facility_type(self, facility_type):
        self.facility_type = facility_type

    #Getter and setter for capacity
    def get_capacity(self):
        return self.capacity

    def set_capacity(self, capacity):
        self.capacity = capacity

    #Getter and setter for time slots
    def get_time_slots(self):
        return self.time_slots

    def set_time_slots(self, time_slots):
        self.time_slots = time_slots

    #Getter and setter for price per hour
    def get_price_per_hour(self):
        return self.price_per_hour

    def set_price_per_hour(self, price_per_hour):
        self.price_per_hour = price_per_hour

    #Check if the selected time slot is available
    def check_availability(self, time_slot):
        return time_slot in self.time_slots

    #Update availability by removing the booked time slot
    def update_availability(self, time_slot):
        if time_slot in self.time_slots:
            self.time_slots.remove(time_slot)
