# Sample dictionary 'labels'
labels = {
    'item1': 'A',
    'item2': 'B',
    'item3': 'A',
    'item4': 'C',
    'item5': 'B',
}

# Initialize an empty dictionary to store sets of keys with the same value
value_sets = {}

# Iterate through the items in the 'labels' dictionary
for key, value in labels.items():
    # Check if the value is already a key in the 'value_sets' dictionary
    if value in value_sets:
        # If it is, add the key to the existing set
        value_sets[value].add(key)
    else:
        # If it's not, create a new set with the key and store it in the 'value_sets' dictionary
        value_sets[value] = {key}

# Convert the dictionary of sets to a list of sets
list_of_sets = list(value_sets.values())

# Print the result
print(list_of_sets)
