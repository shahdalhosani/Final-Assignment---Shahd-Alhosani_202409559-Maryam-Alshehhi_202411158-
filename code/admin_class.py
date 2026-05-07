#Admin is a special type of User
class Admin(User):
    def __init__(self, user_id, name, email, password, access_type, admin_id):
        super().__init__(user_id, name, email, password, access_type)
        self.admin_id = admin_id

    #Getter and setter for admin ID
    def get_admin_id(self):
        return self.admin_id

    def set_admin_id(self, admin_id):
        self.admin_id = admin_id

    #Admin can view all bookings
    def view_bookings(self, bookings):
        return bookings

    #Admin can update facility time slots
    def update_facility(self, facility, time_slots):
        facility.set_time_slots(time_slots)

    #Admin can upgrade a user
    def upgrade_user(self, user):
        user.upgrade_access()
