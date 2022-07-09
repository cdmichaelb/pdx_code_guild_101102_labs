'''
programming 102
->Lab 03
10/06/21
Michael Broetje
'''

conversion_unit = ""
conversion_number = ""
origin_unit = ""

conversion_table_ver1 = {"ft":0.3048} # Version 1 dict
conversion_table_ver2 = {"mi":1609.34,"m":1,"km":1000} # Version 2 dict
conversion_table_ver3 = {"yard":0.9144,"inch":0.0254} # Version 3 dict
conversion_table_all = conversion_table_ver1 | conversion_table_ver2 | conversion_table_ver3 # All dict merged.

# Original Code
""" while conversion_unit not in conversion_table_all.keys(): # Check that entered unit is in dict.
    conversion_unit = input(f'''What unit would you convert meters to?
Your options are {conversion_table_all.keys()}.
> ''') # Ask user what unit they want to convert to.
while not conversion_number.isdigit(): # Check that entered unit is in dict.
    conversion_number = input(f'''What number would you like to conver from m to {conversion_unit}?
> ''') # Ask user for a number to convert.

converted_number = int(conversion_number)  # Convert number into an int for math.
conversion_result =  converted_number * conversion_table_all[conversion_unit] # Convert number to meters.

print(f'''You wanted to convert {converted_number} in m to {conversion_unit}.
Your result is: {conversion_result} {conversion_unit}.''') # Display results. """

# ---------------------------------------------------------------- #
# Code Converted with Extra Challenge

while origin_unit not in conversion_table_all.keys(): # Check that entered unit is in dict.
    origin_unit = input(f'''What unit would you like to convert from?
Your options are {conversion_table_all.keys()}.
> ''') # Ask user what unit they want to convert from.
while conversion_unit not in conversion_table_all.keys(): # Check that entered unit is in dict.
    conversion_unit = input(f'''\nWhat unit would you convert {origin_unit} to?
Your options are {conversion_table_all.keys()}.
> ''') # Ask user what unit they want to convert to.
while not conversion_number.isdigit():
    conversion_number = input(f'''\nWhat number would you like to convert from {origin_unit} to {conversion_unit}?
> ''') # Ask user for a number to convert.

conversion_number = int(conversion_number) # Convert number into an int for math.
origin_conversion = conversion_number * conversion_table_all[origin_unit] # Do first conversion from original unit to meters.
conversion_result =  origin_conversion * 1/conversion_table_all[conversion_unit] # Do final conversion from original number converted to meters into desired unit.

print(f'''\nYou wanted to convert {conversion_number} in {origin_unit} to {conversion_unit}.
Your result is: {round(conversion_result,7)} {conversion_unit}.''') # Display results.

# ---------------------------------------------------------------- #

""" Example Output:
What unit would you like to convert from?
Your options are dict_keys(['ft', 'mi', 'm', 'km', 'yard', 'inch']).
> ft

What unit would you convert ft to?
Your options are dict_keys(['ft', 'mi', 'm', 'km', 'yard', 'inch']).
> mi

What number would you like to convert from ft to mi?
> 100

You wanted to convert 100 in ft to mi.
Your result is: 0.0189394 mi.
"""