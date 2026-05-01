class MathOperationsCalculator:

    def add_numbers(self, first_number, second_number):
       return first_number + second_number

    def subtract_numbers(self, first_number, second_number):
       return first_number - second_number

    def multiply_numbers(self, first_number, second_number):
       return first_number * second_number

    def divide_numbers(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number

class AppCalculator:
    def start_application(self):
        print("Application is starting...")

    def get_valid_number(self, prompt_text):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a numeric value.")

if __name__ == "__main__":
    main_app = AppCalculator()
    main_app.start_application()

def start_application(self):
    while True:
        print("\nSelect: 1. Add | 2. Subtract | 3. Multiply | 4. Divide")
        user_choice = input("Your choice: ")

        first_value = float(input("Enter first number: "))
        second_value = float(input("Enter second number: "))

        if user_choice == '1':
            result = self.add_numbers(first_value, second_value)
            print(f"Result: {result}")

        repeat = input("Try again? (Yes/No): ").lower()
        if repeat != 'Yes':
            print("\nThank you for using the calculator!")
            break

