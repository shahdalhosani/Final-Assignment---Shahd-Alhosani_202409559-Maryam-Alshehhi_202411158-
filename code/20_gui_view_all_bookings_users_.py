#Admin can view all bookings
def view_all_bookings(admin):
    clear_window()

    #Page title
    tk.Label(window, text="All Bookings", font=("Times New Roman", 16, "bold")).pack()

    #Text box for all booking details
    text_box = tk.Text(window, width=75, height=18)
    text_box.pack()

    #If there are no bookings, show a message
    if len(system.get_bookings()) == 0:
        text_box.insert(tk.END, "No bookings yet.")

    #Otherwise, show all bookings
    else:
        for booking in system.get_bookings():
            text_box.insert(tk.END, "Booking ID: " + str(booking.get_booking_id()) + "\n")
            text_box.insert(tk.END, "User: " + booking.get_user().get_name() + "\n")
            text_box.insert(tk.END, "Facility: " + booking.get_facility().get_name() + "\n")
            text_box.insert(tk.END, "Date: " + booking.get_date() + "\n")
            text_box.insert(tk.END, "Time: " + booking.get_time_slot() + "\n")
            text_box.insert(tk.END, "Cost: " + str(booking.get_total_cost()) + " AED\n")
            text_box.insert(tk.END, "Status: " + booking.get_status() + "\n")
            text_box.insert(tk.END, "------------------------------\n")

    #Back to admin dashboard
    def back_to_admin():
        admin_dashboard(admin)

    #Back button
    tk.Button(window, text="Back", width=25, command=back_to_admin).pack()


#Admin can view all users
#This shows all users registered in the system
def view_all_users(admin):
    clear_window()

    #Page title
    tk.Label(window, text="All Users", font=("Times New Roman", 16, "bold")).pack()

    #Text box for user details
    text_box = tk.Text(window, width=75, height=18)
    text_box.pack()

    #Loop through all users and show their details
    for user in system.get_users():
        text_box.insert(tk.END, "User ID: " + str(user.get_user_id()) + "\n")
        text_box.insert(tk.END, "Name: " + user.get_name() + "\n")
        text_box.insert(tk.END, "Email: " + user.get_email() + "\n")
        text_box.insert(tk.END, "Access Type: " + user.get_access_type() + "\n")
        text_box.insert(tk.END, "------------------------------\n")

    #Back to admin dashboard
    def back_to_admin():
        admin_dashboard(admin)

    #Back button
    tk.Button(window, text="Back", width=25, command=back_to_admin).pack()
