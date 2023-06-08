'''
Task 18 'Email Simulator' application that based on user choice,
lists all E-mails and view Unread ones.
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
# Goal: Develop a Class 'Email' with a constructor defined instance variables namely
# email_address, subject_line, email_contents, and a method 'mark_as_read' (Read/Unread).
# Define Functions to populate, list, read E-mails and give the user the options to 
# choose: view and select Emails to Read, View Unread Emails and Quit application.

# --- Email Class --- #

# Defining an Email class, with constructor and method to create a new Email objects.
class Email:
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_contents):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        # Note: 'has_been_read' is defined as instance variable rather then class variable
        self.has_been_read = False

    # Defining a method to change 'has_been_read' E-mails from False to True.
    def mark_as_read(self):
        self.has_been_read = True


# --- Lists --- #

# Initialising an empty list to store the email objects.
inbox = []


# --- Functions --- #

# Defining the required functions to program simulator using Email objects.
# Defining a function to populate 3 sample emails and adding it to the Inbox list. 
def populate_inbox(inbox):
    email_1 = Email("book.alert@whsmith.co.uk", "Your Book alert", 
              """
              AI 2041: 10 Visions for Our Future: AI 2041: Ten Visions for Our Future,
              was written by Chen Qiufan and Kai-Fu Lee. The book won numerous accolades.
              """)
    email_2 = Email("skillsbootcamps@hyperiondev.com", 
              "HyperionDev’s event is about to start!", 
              """
              Hi there, Our event "Skills Bootcamp Cohort 4
              - Career Support Series" is about to start.
              """)
    email_3 = Email("jobalerts-noreply@linkedin.com",
              "data engineer: 30+ opportunities", 
              """
              30+ new jobs in London Area, United Kingdom match your preferences.
              """)
    inbox.extend([email_1, email_2, email_3])  # Append multiple elements
    return inbox


# Defining a function to print Email’s subject_line, along with a corresponding number.
def list_emails(inbox):
    print('\n   Your E-mail list:\n')
    for index, email in enumerate(inbox):
        print(f"   {index + 1}. {email.subject_line}")


# Defining a function to display a selected email by the user. 
# Note: Email No. starts from '1' instead of inbox index '0'
def read_email(email_number):
    if email_number < 1 or email_number > len(inbox):
        print("\nInvalid E-mail number.")
        return

    email = inbox[email_number - 1]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"Contents:\n{email.email_contents}")
    # Calling the class method to set 'has_been_read' variable to True
    email.mark_as_read()


# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
inbox = populate_inbox(inbox)

# Code for the various menu operations.
try:
    while True:
        user_choice = int(input('''\n
        Would you like to:

        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:
            list_emails(inbox)
            email_number = int(input("\nEnter the E-mail number to read: "))
            read_email(email_number)
        elif user_choice == 2:
            unread_emails = [email for email in inbox if not email.has_been_read]
            if unread_emails:
                print("\nUnread E-mails:\n")
                for index, email in enumerate(unread_emails):
                    print(f"{index +1}. Subject: {email.subject_line}")
            else:
                print("\nNo Unread E-mails.")
        elif user_choice == 3:
            print("\nQuitting E-mail simulator application...\n")
            break
        else:
            print("\nInvalid selection. Please choose a valid option.")
except:
        print('\nSorry! invalid Input, Choose valid index number from the menu\n')