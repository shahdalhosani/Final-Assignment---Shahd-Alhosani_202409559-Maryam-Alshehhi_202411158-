#View facilities when no user is logged in
#This allows visitors to see available facilities before logging in
def view_facilities_without_user():
    clear_window()

    #Page title
    tk.Label(window, text="Facilities", font=("Times New Roman", 16, "bold")).pack()

    #Text box to display all facility details
    text_box = tk.Text(window, width=75, height=18)
    text_box.pack()

    #Loop through all facilities and print their details
    for facility in system.get_facilities():
        text_box.insert(tk.END, "Facility ID: " + str(facility.get_facility_id()) + "\n")
        text_box.insert(tk.END, "Name: " + facility.get_name() + "\n")
        text_box.insert(tk.END, "Type: " + facility.get_facility_type() + "\n")
        text_box.insert(tk.END, "Capacity: " + str(facility.get_capacity()) + "\n")
        text_box.insert(tk.END, "Available Slots: " + str(facility.get_time_slots()) + "\n")
        text_box.insert(tk.END, "Fee: " + str(facility.get_price_per_hour()) + " AED/hour\n")
        text_box.insert(tk.END, "------------------------------\n")

    #Back button
    tk.Button(window, text="Back", width=25, command=main_menu).pack()

#View facilities when user is logged in
def view_facilities(user):
    clear_window()

    #Page title
    tk.Label(window, text="Facilities", font=("Times New Roman", 16, "bold")).pack()

    #Text box for facility information
    text_box = tk.Text(window, width=75, height=18)
    text_box.pack()

    #Show each facility in the text box
    for facility in system.get_facilities():
        text_box.insert(tk.END, "Facility ID: " + str(facility.get_facility_id()) + "\n")
        text_box.insert(tk.END, "Name: " + facility.get_name() + "\n")
        text_box.insert(tk.END, "Type: " + facility.get_facility_type() + "\n")
        text_box.insert(tk.END, "Capacity: " + str(facility.get_capacity()) + "\n")
        text_box.insert(tk.END, "Available Slots: " + str(facility.get_time_slots()) + "\n")
        text_box.insert(tk.END, "Fee: " + str(facility.get_price_per_hour()) + " AED/hour\n")
        text_box.insert(tk.END, "------------------------------\n")

    #Return to the same user's dashboard
    def back_to_dashboard():
        user_dashboard(user)

    #Back button
    tk.Button(window, text="Back", width=25, command=back_to_dashboard).pack()

#Find facility by ID
#This searches for a facility using the facility ID entered by the user
def find_facility(facility_id):
    for facility in system.get_facilities():
        if facility.get_facility_id() == facility_id:
            return facility
