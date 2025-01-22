class Email():
    """ A class to represent an email."""

    has_been_read = False
    

    def __init__(self, email_address, subject_line, email_content):
        """
        Initialise an Email object with the given sender's address,
        subject, and content.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content


    def mark_as_read(self):
        """
        Mark the email as read by setting `has_been_read` to True.
        """
        self.has_been_read = True


def populate_inbox():
    """
    Populate the global `inbox` list with sample Email objects.
    """
    email_one = Email(
        "test1@gmail.com", "Sample Email One", "This is sample email one"
    )
    email_two = Email(
        "test2@gmail.com", "Sample Email Two", "This is sample email two"
    )
    email_three = Email(
        "test3@gmail.com", "Sample Email Three", "This is sample email three"
    )

    # Add the sample emails to the inbox
    inbox.extend([email_one, email_two, email_three]) 


def list_emails():
    """
    List all emails in the inbox with their index and subject line.
    """
    for i, email in enumerate(inbox):
        print(f"{i}   {email.subject_line}")


def read_email(email_index):
    """
    Display the details of the email at the specified index and mark it 
    as read.
    """
    if 0 <= email_index < len(inbox):
        email = inbox[email_index]
        print(f"\nEmail {email_index}:")
        print(f"Email From: {email.email_address}")
        print(f"Subject Line: {email.subject_line}")
        print(f"Email Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email number. Please select a valid email number.")


# --- Main Program --- #

# Global variable to store emails
inbox = []

# Populate the inbox with sample emails
populate_inbox()

# Main program loop
menu = True
while True:
    try:
        user_choice = int(input('''\nWould you like to:
        1. Read an email
        2. View unread emails
        3. Quit application
    
        Enter selection: '''))
           
        if user_choice == 1:
            print("\nYour inbox: ")
            list_emails()
            
            email_index = int(input(
                "\nPlease input which email number you would like to read: "
            ))
            read_email(email_index)
    
        elif user_choice == 2:
            print("\nYour unread emails:")
    
            unread_email_exists = False
    
            for i,email in enumerate(inbox):
                if email.has_been_read == False:
                    print(f"{i}   {email.subject_line}")
                    unread_email_exists = True
            
            if unread_email_exists == False:
                print("\n NONE")
                
        elif user_choice == 3:
            print("\nYou have chosen to exit. Goodbye.")
            break
    
        else:
            print("Oops - incorrect input.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
