# Track elf number
elf = 1
printed_up_to_elf_number = 0

# Dictionary of elf numbers and their calories of food carried
elf_calories = {}

# Read input file
with open('input.txt', 'r') as f:
    # Read all lines in file
    while line := f.readline():
        # If elf number is not in dictionary
        if elf not in elf_calories:
            # Add elf number to dictionary
            elf_calories[elf] = []

        # If line is a new line, increment elf number
        # otherwise add calories to elf number
        if line == '\n':
            elf = elf + 1
        else:
            elf_calories[elf].append(int(line))

# Add all calories of food carried by each elf
elf_total_calories = { elf: sum(calories) for elf, calories in elf_calories.items() }

# Sort elf total calories by value
elf_total_calories_sorted = { elf: calories for elf, calories in sorted(elf_total_calories.items(), key=lambda item: item[1], reverse=True) }

# Print all elf numbers and their total calories of food carried
for elf, calories in elf_total_calories_sorted.items():
    print(f'Elf {elf} has a total of {calories} calories')

# Print the elf with the most calories of food carried
print('\n')
print(f'Elf {list(elf_total_calories_sorted.keys())[0]} has the most calories of food carried with {list(elf_total_calories_sorted.values())[0]} calories')