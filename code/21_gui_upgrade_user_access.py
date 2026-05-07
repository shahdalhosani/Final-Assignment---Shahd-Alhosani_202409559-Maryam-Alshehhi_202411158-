#Admin upgrades user page
#Admin enters the user ID and upgrades that user to Premium
def admin_upgrade_user_page(admin):
    clear_window()

    #Page title
    tk.Label(window, text="Upgrade User", font=("Times New Roman", 16, "bold")).pack()

    #User ID input
    tk.Label(window, text="User ID").pack()
    user_id_entry = tk.Entry(window, width=35)
    user_id_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Upgrade user action
    def upgrade_user_action():
        try:
            user_id = int(user_id_entry.get())

            #Search for the user by ID
            for user in system.get_users():
                if user.get_user_id() == user_id:

                    #Admin upgrades the user
                    admin.upgrade_user(user)

                    #Save the change
                    system.save_data()

                    #Show success message
                    result_label.config(text="User upgraded to Premium.")
                    return

            #If user ID is not found
            result_label.config(text="User not found.")

        #If user ID is not a number
        except ValueError:
            result_label.config(text="Please enter a correct user ID.")

    #Back to admin dashboard
    def back_to_admin():
        admin_dashboard(admin)

    #Buttons
    tk.Button(window, text="Upgrade", width=25, command=upgrade_user_action).pack()
    tk.Button(window, text="Back", width=25, command=back_to_admin).pack()
