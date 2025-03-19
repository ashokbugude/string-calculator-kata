from string_calculator import StringCalculator

def main():
    calculator = StringCalculator()
    print("String Calculator")
    print("Enter numbers to add (comma separated):")
    print("Type 'exit' to quit")
    
    while True:
        try:
            numbers = input("> ")
            if numbers.lower() == 'exit':
                break
            result = calculator.add(numbers)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 