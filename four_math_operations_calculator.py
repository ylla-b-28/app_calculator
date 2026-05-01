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

class AppCalculator(MathOperationsCalculator):
    def get_valid_number(self, prompt_text):
        while True:
            try:
                return float(input(prompt_text))
            except ValueError:
                print("Error: Please enter a numeric value.")

    def start_application(self):
        print("Application is starting...")
        while True:
            print("\nSelect: 1. Add | 2. Subtract | 3. Multiply | 4. Divide")
            user_choice = input("Your choice: ")

            if user_choice in ['1', '2', '3', '4']:
               first_value = self.get_valid_number("Enter first number: ")
               second_value = self.get_valid_number("Enter second number: ")

               try:
                  if user_choice == '1':
                     result = self.add_numbers(first_value, second_value)
                  elif user_choice == '2':
                     result = self.subtract_numbers(first_value, second_value)
                  elif user_choice == '3':
                     result = self.multiply_numbers(first_value, second_value)
                  elif user_choice == '4':
                     result = self.divide_numbers(first_value, second_value)

                  print(f"Result: {result}")
            except ZeroDivisionError as error:
                  print(error)

        else:
            print("Invalid choice, please select 1-4.")

        repeat = input("Try again? (Yes/No): ").lower()
        if repeat != 'Yes':
           print("\nThank you for using the calculator!")
           break

if __name__ == "__main__":
    main_app = AppCalculator()
    main_app.start_application()