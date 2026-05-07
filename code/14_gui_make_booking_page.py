#Show booking page
def booking_page(user):
    clear_window()

    #Page title
    tk.Label(window, text="Make Booking", font=("Times New Roman", 16, "bold")).pack()

    #Facility ID input
    tk.Label(window, text="Facility ID").pack()
    facility_entry = tk.Entry(window, width=35)
    facility_entry.pack()

    #Date input
    tk.Label(window, text="Date").pack()
    date_entry = tk.Entry(window, width=35)
    date_entry.pack()

    #Time slot input
    tk.Label(window, text="Time Slot").pack()
    time_entry = tk.Entry(window, width=35)
    time_entry.pack()

    #Duration input
    tk.Label(window, text="Duration in hours").pack()
    duration_entry = tk.Entry(window, width=35)
    duration_entry.pack()

    #Label for messages and cost preview
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Show total cost before booking
    def preview_cost():
        try:
            facility_id = int(facility_entry.get())
            duration = int(duration_entry.get())

            #Find the selected facility
            facility = find_facility(facility_id)

            #If facility exists, calculate cost
            if facility:
                cost = duration * facility.get_price_per_hour()
                result_label.config(text="Total cost will be " + str(cost) + " AED.")

            #If the ID is wrong, show error
            else:
                result_label.config(text="Facility not found.")

        #This handles wrong number input
        except ValueError:
            result_label.config(text="Please enter numbers correctly.")

    #Confirm booking
    def confirm_booking():
        try:
            facility_id = int(facility_entry.get())
            date = date_entry.get()
            time_slot = time_entry.get()
            duration = int(duration_entry.get())

            #Make sure date and time are not empty
            if date == "" or time_slot == "":
                result_label.config(text="Please fill all fields.")
                return

            #Find the facility
            facility = find_facility(facility_id)

            #Continue only if facility exists
            if facility:
                #Check if the user is allowed to book this facility type
                if not check_user_permission(user, facility):
                    result_label.config(text="Standard users can book only one facility type.")
                    return

                #Create a new booking ID
                booking_id = len(system.get_bookings()) + 1

                #Create a booking object
                booking = Booking(booking_id, user, facility, date, time_slot, duration)

                #Try to make the booking in the system
                result = system.make_booking(booking)

                #If booking is successful, save the data
                if result:
                    system.save_data()
                    result_label.config(text="Booking confirmed. Booking ID: " + str(result.get_booking_id()))

                #If time slot is not available, show message
                else:
                    result_label.config(text="This time slot is not available.")

            #If facility is not found, show message
            else:
                result_label.config(text="Facility not found.")

        #This handles wrong number input
        except ValueError:
            result_label.config(text="Please enter correct numbers.")

    #Back to user dashboard
    def back_to_dashboard():
        user_dashboard(user)

    #Buttons for booking page
    tk.Button(window, text="Show Cost Before Confirmation", width=35, command=preview_cost).pack()
    tk.Button(window, text="Confirm Booking", width=35, command=confirm_booking).pack()
    tk.Button(window, text="Back", width=35, command=back_to_dashboard).pack()

