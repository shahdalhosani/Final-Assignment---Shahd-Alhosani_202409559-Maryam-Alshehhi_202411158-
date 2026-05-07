#Check Standard/Premium permission
#Premium users can book different facility types
#Standard users can only book one facility type
def check_user_permission(user, facility):
    if user.get_access_type() == "Premium":
        return True

    #Check the user's old bookings
    for booking in system.get_bookings():
        if booking.get_user().get_email() == user.get_email():
            old_type = booking.get_facility().get_facility_type()
            new_type = facility.get_facility_type()

            #If the new facility type is different, do not allow it
            if old_type != new_type:
                return False
    #If there is no problem, allow the booking
    return True
