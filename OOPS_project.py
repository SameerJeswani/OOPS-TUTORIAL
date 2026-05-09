class chatbook:
    def __init__(self):
        self.username =''
        self.password =''
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed ?
                            1. press 1 to signup
                            2. press 2 to signin
                            3. press 3 to write a post
                            4. press 4 to message a friend
                            5. press any other key to exit """)
    

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()


    def signup(self):
        email = input("Enter your email : ")
        password = input("set your password : ")
        self.username = email
        self.password = password
        print("You have signed up successfully !!")
        print("\n")
        self.menu()


    def signin(self):
        if self.username == '' and self.password == '':
            print("You need to signup first by pressing 1 in the main menu !!")
        else:
            uname = input("Enter your email : ")
            password = input("Enter your password : ")
            if self.username == uname and self.password == password:
                print("You have signed in successfully !!")
                self.loggedin = True
            else:
                print("Please input Correct credentials !!")
        print("\n")
        self.menu()


obj = chatbook()