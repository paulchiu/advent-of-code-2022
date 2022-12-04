# Track elf number
elf = 1
printed_up_to_elf_number = 0

# Read input file
with open('input.txt', 'r') as f:
    # Read all lines in file
    while line := f.readline():
        # If elf number is not printed yet
        if elf > printed_up_to_elf_number:
            # Print elf number
            print(f"Elf number: {elf}")
            printed_up_to_elf_number += 1

        print(line)

        if line == '\n':
            elf = elf + 1

        # Stop script after elf 3
        if elf == 3:
            break