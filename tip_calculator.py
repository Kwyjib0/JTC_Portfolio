'''
Christopher Linton
10/10/2021
TIP CALCULATOR
'''
print()

# INPUTS and ERROR CHECKING:

# create a loop to keep asking for input until a valid numerical entry is given
# referenced code on https://stackoverflow.com/questions/36142149/python-run-try-again-after-exception-caught-and-worked-out
while True:
    # check for non-number input that will cause an error
    try:
        # have the user input the cost of the food, convert the input to a float, and assign that value to the variable bill
        bill = float(input('What did your bill come to: '))
        # quit loop if entry is valid
        break
    # if the input causes an error, let the user know it is invalid and ask them to input it again
    except:
        # alert the user that their entry was invalid, loop will then run again
        print('Invalid entry. Please enter a number.')

# create a loop to keep asking for input until a valid numerical entry is given
# referenced code on https://stackoverflow.com/questions/36142149/python-run-try-again-after-exception-caught-and-worked-out
while True:      
    # check for non-number input that will cause an error
    try:
        # have the user input the number of people splitting the bill, convert the input to an interger (could also use float but only whole numbers should be used for number of people), and assign that value to the variable number_in_party
        number_in_party = int(input('How many were in your party: '))
        # check that input for number of diners is valid 
        if number_in_party > 0:
            # quit loop if entry is valid
            break
        # code to run if number of diners is not valid
        else:
            # alert the user that their entry was an invalid number, loop will then run again
            print("That is an invalid input. The number of diners should be more than 0. Please try again.")
            # start the while loop over again
            continue
    # if the input causes an error, let the user know it is invalid and ask them to input it again
    except:
        # alert the user that their entry was invalid, loop will then run again
        print('Invalid entry. Please enter a number.')

# create a loop to keep asking for input until a valid numerical entry is given
# referenced code on https://stackoverflow.com/questions/36142149/python-run-try-again-after-exception-caught-and-worked-out
while True:    
    # check for non-number input that will cause an error
    try:
        # have the user input the tip value as a percentage of their total bill with tax that they would like to leave, convert the input to a float, and assign that value to the variable
        tip_percentage = float(input('What percentage would you like to tip: '))
        if tip_percentage >= 0:
            # quit loop if entry is valid
            break
        # code to run if number of diners is not valid
        else:
            # alert the user that their entry was an invalid amount, loop will then run again
            print("That is an invalid input. The tip cannot be less than 0. Please try again.")
            # start the while loop over again
            continue       
    # if the input causes an error, let the user know it is inavalid and ask them to input it again
    except:
        # alert the user that their entry was invalid, loop will then run again
        print('Invalid entry. Please enter a number.')



# create a variable assigned the set 10% tax amount
tax_rate = .1 

# FUNCTIONS:

# defines a function that calculates and returns the tax for the bill
def calculate_tax(bill):
    # return the tax on the bill
    return bill * tax_rate
    
# defines a function that calculates and returns the tip based on the percentage of bill
def calculate_tip (bill, tip_percentage):
    # return the calculated tip
    return (bill * (tip_percentage / 100))

# defines a function that calculates and returns the total bill (cost + tax + tip)
def calculate_total_bill(bill, tip_percentage):
    # return a value for the total bill after calling the calculate_bill_tax and tip functions
    return (bill + calculate_tax(bill) + calculate_tip(bill, tip_percentage))

# defines a function that prints & formats the total bill output to have comma seperators and two decimal places
def format_total_bill(bill, tip_percentage):
    # use the built-in format method found on https://pythonguides.com/python-format-number-with-commas/
    # calls function to calculate total bill & formats that value as a numeric string with commas & rounded to 2 decimal places
    formatted_total_bill = "{:,.2f}".format(calculate_total_bill(bill, tip_percentage))
    # print the newly formatted total bill with commas and two values after the decimal point
    print(f'Each diner should pay ${formatted_total_bill}')

# defines a function that calculates the the individual's total bill including tax & tip by dividing the bill by the number of diner's
def calculate_individual_bill(bill, tip_percent, number_in_party):
    # return a value for the individual bill after calling the total bill function dividing that returned value by the number of diners
    return (calculate_total_bill(bill, tip_percentage) / number_in_party)

# defines a function that prints & formats the individual bill output to have comma seperators and two decimal places
def format_individual_bill(bill, tip_percentage, number_in_party):
    # use the built-in format method found on https://pythonguides.com/python-format-number-with-commas/
    # calls function to calculate individual bill & formats that value as a numeric string with commas & rounded to 2 decimal places
    formatted_individual_bill = "{:,.2f}".format(calculate_individual_bill(bill, tip_percentage, number_in_party))

    # print the newly formatted individual bill with commas and two values after the decimal point
    print(f'Each person should pay ${formatted_individual_bill}')


# FUNCTION CALLS FOR OUTPUT:

# run the format_total_bill to print the total amount owed
format_total_bill(bill, tip_percentage)

# check if there was more than one diner to calculate amount owed by each individual
if number_in_party > 1:
    # if more than one diner, run the individual_bill function to print the amount owed by each diner
    format_individual_bill(bill, tip_percentage, number_in_party)




    