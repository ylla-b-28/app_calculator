
class MathOperationsCalculator:

    def add_numbers(self, first_number, second_number):
       return first_number + second_number

    def subtract_numbers(self, first_number, second_number):
       return first_number - second_number

    def multiply_numbers(self, first_number, second_number):
       return first_number * second_number

    def divide_numbers(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("✧ Mathematical Error: Cannot divide by zero. ✧")
        return first_number / second_number

class AppCalculator(MathOperationsCalculator):
    def get_valid_number(self, prompt_text):
        while True:
            try:
                return float(input(prompt_text))
            except ValueError:
                print("₊˚ Input Error: Please enter a valid numeric value. ˚₊")

    def start_application(self):
        print("\n⋆⁺｡˚⋆˙‧₊☽ ◯ ☾₊‧˙⋆˚｡⁺⋆")
        print("")
        print("  APP CALCULATOR")
        print("\n⋆⁺｡˚⋆˙‧₊☽ ◯ ☾₊‧˙⋆˚｡⁺⋆")

        while True:
            print("\n   ₊˚ ✧ ━━━━⊱ (1) Addition")
            print("   ₊˚ ✧ ━━━━⊱ (2) Subtraction")
            print("   ₊˚ ✧ ━━━━⊱ (3) Multiplication")
            print("   ₊˚ ✧ ━━━━⊱ (4) Division")

            print("\n₊˚ ✧ ━━━━⊱⋆⊰━━━━ ✧ ₊˚")
            user_choice = input("₊˚✧ Please select an operation (1-4): ")

            if user_choice in ['1', '2', '3', '4']:
               first_value = self.get_valid_number("₊˚✧ Enter first number: ")
               second_value = self.get_valid_number("₊˚✧ Enter second number: ")

               try:
                   if user_choice == '1':
                      result = self.add_numbers(first_value, second_value)
                   elif user_choice == '2':
                      result = self.subtract_numbers(first_value, second_value)
                   elif user_choice == '3':
                      result = self.multiply_numbers(first_value, second_value)
                   elif user_choice == '4':
                      result = self.divide_numbers(first_value, second_value)

                   print(f"\n ⋆｡°✩ RESULT: {result} ✩°｡⋆ ")

               except ZeroDivisionError as error:
                   print(f"   {error}")

            else:
               print("   ✧ Error: Please select a valid option (1-4). ✧")

            print("₊˚ ✧ ━━━━⊱⋆⊰━━━━ ✧ ₊˚")

            repeat = input(".˳·˖✶ Would you like to try again? (y/n) ").lower()

            if repeat != 'y' and repeat != 'yes':
               print("\n°˖✧ Thank you for using the calculator! Have a lovely day. ✧˖°")
               print("⋆⁺｡˚⋆˙‧₊☽ ◯ ☾₊‧˙⋆˚｡⁺⋆\n")
               break

if __name__ == "__main__":
    main_app = AppCalculator()
    main_app.start_application()