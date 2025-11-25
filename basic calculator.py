def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Calculator Class
class Calculator:

    # Arithmetic Methods
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return a / b

    # Menu Method – shows options
    def menu(self):
        print("\n" + "=" * 45)
        print("              BASIC CALCULATOR")
        print("=" * 45)
        print("1. Add Two Numbers")
        print("2. Subtract Two Numbers")
        print("3. Multiply Two Numbers")
        print("4. Divide Two Numbers")
        print("5. Exit")
        print("=" * 45)

    # Main Controller / Runner
    def run(self):
        while True:
            self.menu()
            choice = input("Enter your choice (1-5): ")

            # Exit handling
            if choice == '5':
                print("\nThank you for using my calculator!")
                break

            # Invalid choice handling
            if choice not in ['1', '2', '3', '4']:
                print("Invalid choice! Please select 1–5 only.")
                continue

            # Taking valid numbers
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            print("\n----------------------")
            # Choice operation
            if choice == '1':
                result = self.add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")

            elif choice == '2':
                result = self.subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")

            elif choice == '3':
                result = self.multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")

            elif choice == '4':
                result = self.divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")

            print("----------------------\n")

calc = Calculator()
calc.run()
