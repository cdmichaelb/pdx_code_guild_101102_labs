list_of_strings = []
sorted_strings = []
add_another_word = True
not_anagram = False

while add_another_word:
    list_of_strings.append(input(f'''Please enter a word to check if it is an anagram with other words.
> ''').replace(" ","").lower()) # Get user input, replace " " with "" (remove white space). Change input to lowercase.

    if list_of_strings[len(list_of_strings)-1] == "!quit": # Check if user typed "!quit"
        list_of_strings.remove("!quit") # Remove "!quit" as it is not intended to be checked for anagram.
        for ana_string in list_of_strings: # Move through the list of strings.
            ana_string = list(ana_string) # Convert string to a list.
            ana_string.sort() # Sort the list by alphabetical order.
            sorted_strings.append(''.join(ana_string)) # Convert list back to string.

        for check_string in range(len(sorted_strings)): # Check each sorted string.
            if not sorted_strings[check_string] == sorted_strings[check_string-1]: # If current string being checked does not match previous string then not anagram.
                print(f'''Your words {list_of_strings} sorted as {sorted_strings} are not an anagram. Sorry.''') # Tell user result.
                not_anagram = True # Set variable for later.
                break # Break check, not anagram, no use checking the rest.
            
        if not not_anagram: # If not_anagram is flagged True, then not not anagram, is an anagram.
            print(f'''Your words {list_of_strings} sorted as {sorted_strings} are an anagram. Congrats!''') # Tell user result.
        print("goodbye") # Tell user goodbye.
        add_another_word = False # End loop.