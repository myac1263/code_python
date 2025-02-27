def check(ROOMNUMS):
    try:
        X = int(input("Enter the room number to check: "))
        
        # Linear search through the ROOMNUMS list
        found = False
        for room in ROOMNUMS:
            if room == X:
                found = True
                break

        if found:
            print(f"The bill for room number {X} has been paid.")
        else:
            print(f"The bill for room number {X} has NOT been paid.")
    except ValueError:
        print("Invalid input. Please enter a valid room number.")

# Example ROOMNUMS array (from the given figure)
ROOMNUMS = [2, 216, 15, 109, 156, 120, 93, 18, 21, 56]

# Call the check function
check(ROOMNUMS)
