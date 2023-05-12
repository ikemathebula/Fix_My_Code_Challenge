#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Defines the User """
    
    def __init__(self, email=None):
        """ Initializes the User """
        self.__email = email

    @property
    def email(self):
        """ Returns an email address """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the email address for the user """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value

    
if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
