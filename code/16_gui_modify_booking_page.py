#Modify booking date page
def modify_booking_page(user):
    clear_window()

    #Page title
    tk.Label(window, text="Modify Booking", font=("Times New Roman", 16, "bold")).pack()

    #Booking ID input
    tk.Label(window, text="Booking ID").pack()
    booking_id_entry = tk.Entry(window, width=35)
    booking_id_entry.pack()

    #New date input
    tk.Label(window, text="New Date").pack()
    new_date_entry = tk.Entry(window, width=35)
    new_date_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Save the new booking date
    def save_changes():
        try:
            booking_id = int(booking_id_entry.get())
            new_date = new_date_entry.get()

            #Make sure the new date is entered
            if new_date == "":
                result_label.config(text="Please enter new date.")
                return

            #Search for the booking that belongs to this user
            for booking in system.get_bookings():
                if booking.get_booking_id() == booking_id and booking.get_user().get_email() == user.get_email():

                    #Update the date
                    booking.set_date(new_date)

                    #Save the updated data
                    system.save_data()

                    #Show success message
                    result_label.config(text="Booking date updated.")
                    return

            #If booking was not found
            result_label.config(text="Booking not found.")
        #If booking ID is not a number
        except ValueError:
            result_label.config(text="Please enter a correct booking ID.")

    #Back to my bookings page
    def back_to_bookings():
        view_my_bookings(user)

    #Buttons
    tk.Button(window, text="Save Changes", width=25, command=save_changes).pack()
    tk.Button(window, text="Back", width=25, command=back_to_bookings).pack()
