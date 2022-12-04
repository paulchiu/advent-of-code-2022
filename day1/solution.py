# Elf file reader function
def elf_reader(filename):
    # Track elf number
    elf = 1
    printed_up_to_elf_number = 0

    # Dictionary of elf numbers and their calories of food carried
    elf_calories = {}

    # Read input file
    with open(filename, 'r') as f:
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

    return elf_calories

def main():
    elf_calories = elf_reader('input.txt')
    elf_total_calories = { elf: sum(calories) for elf, calories in elf_calories.items() }
    elf_total_calories_sorted = sorted(elf_total_calories.items(), key=lambda item: item[1], reverse=True)

    # Print all elf numbers and their total calories of food carried
    for elf, calories in elf_total_calories_sorted:
        print(f'Elf {elf} carried {calories} calories of food')    

    # Print the elf with the most calories of food carried
    print('\n')
    print(f'Elf {elf_total_calories_sorted[0][0]} carried the most food with {elf_total_calories_sorted[0][1]} calories')

if __name__ == '__main__':
    main()