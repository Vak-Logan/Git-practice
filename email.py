### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    
    # Declare the class variable, with default value, for emails.
    has_been_read = False
    
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():

    # Create 3 sample emails and add it to the Inbox list. 
    email_one = Email(
        "test1@gmail.com", "Sample Email One", "This is sample email one"
    )
    email_two = Email(
        "test2@gmail.com", "Sample Email Two", "This is sample email two"
    )
    email_three = Email(
        "test3@gmail.com", "Sample Email Three", "This is sample email three"
    )
    inbox.extend([email_one, email_two, email_three]) 

def list_emails():
   
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, email in enumerate(inbox):
        print(f"{i}   {email.subject_line}")


def read_email(email_index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if 0 <= email_index < len(inbox):
        email = inbox[email_index]
        print(f"\nEmail {email_index}:")
        print(f"Email From: {email.email_address}")
        print(f"Subject Line: {email.subject_line}")
        print(f"Email Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email number. Please select a valid email number.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        print("\nYour inbox: ")
        list_emails()
        
        email_index = int(input(
            "\nPlease input which email number you would like to read: "
        ))
        read_email(email_index)

    elif user_choice == 2:
        # add logic here to view unread emails
        print("\nYour unread emails:")

        unread_email_exists = False

        for i,email in enumerate(inbox):
            if email.has_been_read == False:
                print(f"{i}   {email.subject_line}")
                unread_email_exists = True
        
        if unread_email_exists == False:
            print("\n NONE")
            
    elif user_choice == 3:
        # add logic here to quit appplication
        print("\nYou have chosen to exit. Goodbye.")
        break

    else:
        print("Oops - incorrect input.")
