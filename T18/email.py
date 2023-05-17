
'''
Task 18 'Email Simulator' application that lists all emails and categorize as read or unread
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
inbox = []
def populate_inbox(inbox):

    for i in range(3):

        email_address = input("\nPlease enter your email address: ")
        subject_line = input("\nType in the subject: \n")
        contents = input("\nType in email content: \n")
        email = [email_address, subject_line, contents]
        inbox.append(email)

inbox = populate_inbox(inbox)
print(inbox)

# def list_emails(inbox):

#     for index, subject in enumerate(inbox, 0):
#         print(index, subject)

# list_emails(inbox)

# def read_email(i):

#     print(email_address)


# read_email(i)


# class Email:

#     has_been_read = False

#     def __init__(self, email_address, subject_line, email_contents):
#         self.email_address = email_address
#         self.subject_line = subject_line
#         self.email_contents = email_contents

#     def mark_as_read(self):
#         has_been_read = True
#         return has_been_read
#     mark_as_read()

#     def read_email(self,i):
#         print(self.email_address)
#         print(self.subject_line)
#         print(self.email_contents)

#     read_email(i)
