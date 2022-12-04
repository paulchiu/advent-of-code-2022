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

        # Stop script after elf 3
        if elf == 3:
            break

# Add all calories of food carried by each elf
elf_total_calories = { elf: sum(calories) for elf, calories in elf_calories.items() }

# Print all elf numbers and their total calories of food carried
for elf, calories in elf_total_calories.items():
    print(f'Elf {elf} has a total of {calories} calories')