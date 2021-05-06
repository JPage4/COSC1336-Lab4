# Jesse Page
# Lab 4 assignment
# This program reads the contactsLab4.txt file and will print
# out every contact's name, age, the season they were born,
# and whether not they were born in a leap year. Finally,
# this program will print out the average age of all the contacts

def main():
    # opens contactsLab4 file to read
    try:
        contacts = open("contactsLab4.txt", "r")
        names_list = []
        birthdates_list = []

        # begins reading the first line of the file
        name = contacts.readline()

        # reads each line of the file til it reaches the end
        while name != "":
            # removes trailing whitespace from name 
            # and adds name to list
            name = name.rstrip("\n")
            names_list.append(name)
            birthday = contacts.readline()
            # removes trailing whitespace from birthday 
            # and adds birthday to list
            birthday = birthday.rstrip("\n")
            birthdates_list.append(birthday)
            name = contacts.readline()
        contacts.close()

        # call function to display contact info
        display_contacts(names_list, birthdates_list)
    
    # exception for if
    except IOError:
        print('An error occurred trying to read')
        print('the file', contacts)


################################################
# Function name: find_season                   #
# Input: birthdate as a string                 #
# Output: season as an string                  #
# Purpose: This function gets the season the   #
#          month is in                         #
################################################
def find_season(birthdates_str):
    # separates the string into month, 
    # date and year elements in a list
    date = birthdates_str.split("/")

    # identifies the month element
    month = int(date[0])

    #if-else condition to check month and 
    # assign correct season
    if month <= 2:
        season = "winter"
    elif month <= 5:
        season = "spring"
    elif month <= 8:
        season = "summer"
    elif month <= 11:
        season = "fall"
    elif month == 12:
        season = "winter"
    return season
    
################################################
# Function name: is_leap_year                  #
# Input: birthdate as a string                 #
# Output: True if year is a leap year          #
#         False if it is not                   #
# Purpose: This function determines if a year  #
#          is a leap year or not               #
################################################
def is_leap_year(birthdates_str):
    # separates the string into month, 
    # date and year elements in a list
    date = birthdates_str.split("/")

    # identifies the year element
    year = int(date[2])

    #if-else condition to check if year is a leap year
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    else:
        return False

################################################
# Function name: get_age                       #
# Input: user input for the current date and   #
# contact's birthdate as a string              #
# Output: contact's age as an int              #
# Purpose: This function calculate's the age   #
#  of the contact based on the current date    #
################################################    
def get_age(current_date, birthdate):
    # separates the current_date string into month, 
    # date and year elements in a list
    date = current_date.split("/")
    current_month = int(date[0])
    current_day = int(date[1])
    current_year = int(date[2])

    # separates the birthdate string into month, 
    # date and year elements in a list
    birthday = birthdate.split("/")
    birthday_month = int(birthday[0])
    birthday_day = int(birthday[1])
    birthday_year = int(birthday[2])

    # calculates the contact's age
    if (current_month, current_day) < (birthday_month, birthday_day):
        age = current_year - birthday_year - 1
    else:
        age = current_year - birthday_year

    return age

################################################
# Function name: display_contacts              #
# Input: list of names, list of birthdates and #
# the current date input from the user         #
# Output: displays all the contacts' names,    #
# ages, season they were born, if they were    #
# born in a leap year, followed by the average #
# age of all the contacts                      #
# Purpose: This function will display all the  #
# information calculated and call find_season()#
# is_leap_year() and get_age() functions       #
################################################   
def display_contacts(names_list, birthdates_list):
    yes_no = ""
    age_total = 0

    # reads date input from user
    current_date = input("Enter the current date in the format m/d/yyyy: ")

    # displays headings for columns
    print(
        format("Names", '25'), 
        format("Age", '5'), 
        format("Season Born", '12'), 
        "Leap Year?")
    
    print(
        format("-----", '25'), 
        format("----", '5'), 
        format("---------", '12'), 
        "---------")

    # iterates through the length of birthdates_list 
    for i in range(len(birthdates_list)):
        # gets contact's name
        name = names_list[i]

        # gets contact's age, exception for invalid date input
        try:
            age = get_age(current_date, birthdates_list[i])
            age_total = (age_total + age)
        except Exception(ValueError):
            print(ValueError)

        # gets season contact was born in
        season = find_season(birthdates_list[i])

        # Call function to determine if the year was a leap year or not
        leap_year = is_leap_year(birthdates_list[i])
        if leap_year:
            yes_no = "Yes"
        else:
            yes_no = "No"
        # displays message to the user
        print(
            format(name, '25'), 
            format(str(age), '5'), 
            format(season, '12'), 
            yes_no)
    
    print("")
    # displays average age of all contacts
    print("Average age of contact is", int(age_total / len(birthdates_list)))
    
main()