#Create the system object
system = BookingSystem()

#Load old saved data if it exists
system.load_data()

#Add sample facilities only if there is no saved data
#This avoids adding the same facilities many times
if len(system.get_facilities()) == 0:
    system.add_facility(Facility(1, "Study Room C", "Study Room", 4, ["9-11 AM", "2-4 PM"], 0))
    system.add_facility(Facility(2, "Tennis Court", "Sports Court", 4, ["3-5 PM", "5-7 PM"], 15))
    system.add_facility(Facility(3, "Conference Hall", "Event Hall", 60, ["10-12 PM", "1-3 PM"], 40))

#Add sample users only if there is no saved data
if len(system.get_users()) == 0:
    system.add_user(User(1, "Student One", "student1@zu.ac.ae", "1111"))
    system.add_user(Admin(2, "Admin", "admin@zu.ac.ae", "admin", "Admin", 200))

#Save the data
#This saves the starting data into the pickle file
system.save_data()
