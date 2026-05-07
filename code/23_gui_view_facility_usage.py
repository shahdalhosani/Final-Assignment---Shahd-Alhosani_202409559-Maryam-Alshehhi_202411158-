#Admin can view facility usage
#This shows how many bookings each facility has

def view_facility_usage(admin):
    clear_window()

    #Page title
    tk.Label(window, text="Facility Usage and Capacity", font=("Times New Roman", 16, "bold")).pack()

    #Text box for facility usage
    text_box = tk.Text(window, width=75, height=18)
    text_box.pack()

    #Loop through each facility
    for facility in system.get_facilities():
        #Count how many bookings are made for this facility
        count = 0

        #Check each booking
        for booking in system.get_bookings():
            if booking.get_facility().get_facility_id() == facility.get_facility_id():
                count = count + 1

        #Show facility usage details
        text_box.insert(tk.END, "Facility: " + facility.get_name() + "\n")
        text_box.insert(tk.END, "Capacity: " + str(facility.get_capacity()) + "\n")
        text_box.insert(tk.END, "Number of Bookings: " + str(count) + "\n")
        text_box.insert(tk.END, "Available Slots: " + str(facility.get_time_slots()) + "\n")
        text_box.insert(tk.END, "------------------------------\n")

    #Back to admin dashboard
    def back_to_admin():
        admin_dashboard(admin)

    #Back button
    tk.Button(window, text="Back", width=25, command=back_to_admin).pack()

#Save data manually
#This function is used by the Save Data button in the main menu
def save_data():
    system.save_data()
