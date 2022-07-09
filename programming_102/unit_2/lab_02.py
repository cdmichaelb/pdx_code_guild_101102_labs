# custom_sum_user_numbers = []
# custom_sum_add_num = True

# def custom_sum(table_nums,starting_num=0): # Custom sum function.
#     custom_sum_total = 0 # Define custom_sum_total as an int starting at 0
    
#     for custom_number in table_nums: # Loop through table.
#         custom_sum_total = custom_sum_total + custom_number # Sum up table values.
#     custom_sum_total = custom_sum_total + starting_num # Add starting number if used.
#     return custom_sum_total # Return results

# def remove_all(numbers, target): # Remove all of a specific number from list.
#     for number in numbers: # Check each item on list to see if it is matching target.
#         numbers.remove(target) # Remove the number from list.
#     return numbers # Return new list.


# while custom_sum_add_num == True: # Run while user wants to add more numbers.
#     custom_sum_new_num = input(f'''
# Enter a number or "done" to quit.
# > ''') # Get users new number or quit action.
#     if custom_sum_new_num.isdigit(): # Check if entered data is a number.
#         custom_sum_user_numbers.append(int(custom_sum_new_num)) # Add new number to list of numbers.
#     elif custom_sum_new_num.lower() == 'done' or custom_sum_new_num.lower() == 'quit' or custom_sum_new_num.lower() == 'exit' or custom_sum_new_num.lower() == 'q': # Check if user wants to quit, if entered data is not number.
#         print(f'''Your numbers summed are: {custom_sum(custom_sum_user_numbers)}.''') # Print results and call function to sum tabled numbers.
#         custom_sum_add_num = False # Stop running loop.

# test_list = [1,3,4,3,1,1] # Test list for Extra Challenge

# print(f'''
# List before removing any numbers {test_list}.
# List after removing all 1s. {remove_all(test_list,1)}''') # Test use for Extra challenge.

# print("test".sort()) # Test use for Extra challenge.

# Begins my dictionary which contains the key meters and the value of 0.3048
units = {
    'meters': 0.3048,
    'miles': 1609.34,
    'mm': 1,
    'km': 1000
    }

distance_feet = input(' Please enter the distance in feet: ') # Declares the variable which prompts user for a number in feet

distance_feet = float(distance_feet) # This will convert to a float

# input_units = input('What are the units?')

# input_units = float(input_units)

total = distance_feet * units['meters'] # Were we get the total by multiplying by going into the dictionary

print(f'You entered {distance_feet} feet which is {round(total, 2)} meters')
