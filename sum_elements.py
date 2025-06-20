#A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX = 100

def calculate_sum(arr):
    return sum(arr)

def get_integer(prompt):
    while True:
        try:
            value = input(prompt)
            if value.strip() == "":
                print("Input cannot be empty. Please enter a valid integer.")
                continue
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    try:
        n = get_integer("Enter the number of elements (1-100): ")
        if not 1 <= n <= MAX:
            print(f"Invalid input. Please provide a number from 1 to {MAX}.")
            return

        arr = []
        print(f"Enter {n} integers:")
        for i in range(n):
            arr.append(get_integer(f"Element {i+1}: "))

        total = calculate_sum(arr)
        print("Sum of the numbers:", total)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
