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
            # alert the user that their entry was invalid, loop will then run again
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
        tip_percent = float(input('What percentage would you like to tip: '))
        if tip_percent >= 0:
            # quit loop if entry is valid
            break
        # code to run if number of diners is not valid
        else:
            # alert the user that their entry was invalid, loop will then run again
            print("That is an invalid input. The tip cannot be less than 0. Please try again.")
            # start the while loop over again
            continue       
    # if the input causes an error, let the user know it is inavalid and ask them to input it again
    except:
        # alert the user that their entry was invalid, loop will then run again
        print('Invalid entry. Please enter a number.')



# create a variable assigned the set 10% tax amount
tax = .1 

# FUNCTIONS:

# defines a function that calculates and returns the tax for the bill
def bill_tax(bill):
    # return the tax on the bill
    return bill * tax
    
# defines a funtion that calculates and returns the tip based on the percentage of bill
def tip (bill, tip_percent):
    # return the calculated tip
    return (bill * (tip_percent / 100))

# defines a function that calculates and returns the total bill (cost + tax + tip) rounded to two decimal places
def total_bill(bill, tip_percent):
    # return a value for the total bill after calling the bill_tax and tip functions, and rounding to two decimal places
    return round(bill + bill_tax(bill) + tip(bill, tip_percent), 2)

# defines a function that formats the total bill output to have comma seperators and always have two decimal places, even if the second is a zero, and outputs that amount in a print statement 
def format_total_bill(bill, tip_percent):
    # use the built-in format method found on https://www.kite.com/python/answers/how-to-add-commas-to-a-number-in-python
    # creates a string variable with the value formatted with comma seperators after calling the total bill function
    comma_total_bill = "{:,}".format(total_bill(bill, tip_percent))
    # create a list variable by splitting comma_total_bill into two element representing the amounts before and after the decimal point
    total_bill_list = comma_total_bill.split('.')
    # check if the length of the second element that represents the value after the decimal point is less than two
    if len(total_bill_list[1]) < 2:
        # if the length of the value after the decimal point is less than two (it should be one or two), add a zero to the end
        comma_total_bill = comma_total_bill + '0'
    # print the newly formatted total bill with commas and two values after the decimal point
    print(f'Total bill: ${comma_total_bill}')

# defines a function that calculates the the individual's total bill including tax & tip by diviing the bill by the number of diner's and returns that value rounded to two decimal places
def individual_bill(bill, tip_percent, number_in_party):
    # return a value for the individual bill after calling the total bill function dividing that returned value by the number of diners and then rounding to two decimal places
    return round((total_bill(bill, tip_percent) / number_in_party), 2)

# defines a function that formats the individual bill output to have comma seperators and always have two decimal places, even if the second is a zero, and outputs that amount in a print statement  
def format_individual_bill(bill, tip_percent, number_in_party):
    # use the built-in format method found on https://www.kite.com/python/answers/how-to-add-commas-to-a-number-in-python
    comma_individual_bill = "{:,}".format(individual_bill(bill, tip_percent, number_in_party))
    individual_bill_list = comma_individual_bill.split('.')
    if len(individual_bill_list[1]) < 2:
        comma_individual_bill = comma_individual_bill + '0'
    # print the the total bill amount (cost + tax + tip) for the individual rounded to two decimal 
    print(f'Each person should pay ${comma_individual_bill}')


# FUNCTION CALLS FOR OUTPUT:

# run the format_total_bill to print the total amount owed
format_total_bill(bill, tip_percent)

# check if there was more than one diner to calculate amount owed by each individual
if number_in_party > 1:
    # if more than one diner, run the individual_bill function to print the amount owed by each diner
    format_individual_bill(bill, tip_percent, number_in_party)




    