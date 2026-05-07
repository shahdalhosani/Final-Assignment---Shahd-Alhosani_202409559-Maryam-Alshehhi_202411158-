#Clear the window before opening a new page
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

#Show main menu
def main_menu():
    clear_window()

    #Main title of the system
    tk.Label(window, text="Smart Campus Facility Booking System - Zayed University", font=("Times New Roman", 16, "bold")).pack()

    #Buttons that take the user to different pages
    tk.Button(window, text="Login", width=30, command=login_page).pack()
    tk.Button(window, text="Create Account", width=30, command=create_account_page).pack()
    tk.Button(window, text="View Facilities", width=30, command=view_facilities_without_user).pack()
    tk.Button(window, text="Save Data", width=30, command=save_data).pack()
    tk.Button(window, text="Exit", width=30, command=window.destroy).pack()
