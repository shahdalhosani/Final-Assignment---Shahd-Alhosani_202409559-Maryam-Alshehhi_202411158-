#Show create account page
#This allows a new student/user to create an account
def create_account_page():
    clear_window()

    #Page title
    tk.Label(window, text="Create Account", font=("Times New Roman", 16, "bold")).pack()

    #Name input
    tk.Label(window, text="Name").pack()
    name_entry = tk.Entry(window, width=35)
    name_entry.pack()

    #Email input
    tk.Label(window, text="Email").pack()
    email_entry = tk.Entry(window, width=35)
    email_entry.pack()

    #Password input
    tk.Label(window, text="Password").pack()
    password_entry = tk.Entry(window, width=35, show="*")
    password_entry.pack()

    #Message label
    result_label = tk.Label(window, text="")
    result_label.pack()

    #Create a new user account
    def create_action():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        #Make sure all fields are filled
        if name == "" or email == "" or password == "":
            result_label.config(text="Please fill all fields.")
            return

        #Check if the email already exists
        for user in system.get_users():
            if user.get_email() == email:
                result_label.config(text="This email already exists.")
                return

        #Create a new user ID based on the number of users
        user_id = len(system.get_users()) + 1

        #Create a new User object
        new_user = User(user_id, name, email, password)

        #Add the new user to the system
        system.add_user(new_user)

        #Save the new user data
        system.save_data()

        #Show success message
        result_label.config(text="Account created successfully.")

    #Button to create account
    tk.Button(window, text="Create Account", width=25, command=create_action).pack()

    #Button to go back
    tk.Button(window, text="Back", width=25, command=main_menu).pack()
