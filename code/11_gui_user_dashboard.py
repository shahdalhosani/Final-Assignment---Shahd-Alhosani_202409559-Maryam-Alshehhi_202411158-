#Show user dashboard after login
def user_dashboard(user):
    clear_window()

    #Dashboard title and user details
    tk.Label(window, text="User Dashboard", font=("Times New Roman", 16, "bold")).pack()
    tk.Label(window, text="Welcome, " + user.get_name()).pack()
    tk.Label(window, text="Access Type: " + user.get_access_type()).pack()

#Functions to send the current user to the next page when a button is clicked

    #Open the facilities page
    def open_facilities():
        view_facilities(user)

    #Open the booking page
    def open_booking():
        booking_page(user)

    #Open the user's own bookings
    def open_my_bookings():
        view_my_bookings(user)

    #Open the page to modify user details
    def open_modify_details():
        modify_user_details_page(user)

    #Delete the current user account
    def open_delete_account():
        delete_user_account(user)

    #Upgrade the current user to Premium
    def open_upgrade():
        upgrade_current_user(user)

    #Open admin dashboard if user is admin
    def open_admin():
        admin_dashboard(user)

    #User buttons
    tk.Button(window, text="View Facilities", width=30, command=open_facilities).pack()
    tk.Button(window, text="Make Booking", width=30, command=open_booking).pack()
    tk.Button(window, text="View My Bookings", width=30, command=open_my_bookings).pack()
    tk.Button(window, text="Modify My Details", width=30, command=open_modify_details).pack()
    tk.Button(window, text="Delete My Account", width=30, command=open_delete_account).pack()
    tk.Button(window, text="Upgrade to Premium", width=30, command=open_upgrade).pack()

    #If the user is admin, show admin button
    if user.get_access_type() == "Admin":
        tk.Button(window, text="Admin Dashboard", width=30, command=open_admin).pack()

    #Logout returns to main menu
    tk.Button(window, text="Logout", width=30, command=main_menu).pack()
