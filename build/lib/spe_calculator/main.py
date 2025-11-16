"""Command-line interface for the scientific calculator."""

from __future__ import annotations

from typing import Callable

from . import calculator


def prompt_number(prompt: str, caster: Callable[[str], float]) -> float:
    """Prompt the user for a number until a valid one is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return caster(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def to_float(value: str) -> float:
    return float(value)


def to_int(value: str) -> float:
    integer_value = int(value)
    return float(integer_value)


def display_menu() -> None:
    print("\nScientific Calculator")
    print("---------------------")
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln x)")
    print("4. Power (x^b)")
    print("5. Exit")


def main() -> None:
    """Run the calculator CLI."""
    while True:
        display_menu()
        choice = input("Select an option (1-5): ").strip()

        try:
            if choice == "1":
                value = prompt_number("Enter a non-negative number: ", to_float)
                result = calculator.square_root(value)
                print(f"√{value} = {result}")
            elif choice == "2":
                value = prompt_number("Enter a non-negative integer: ", to_int)
                result = calculator.factorial(value)
                print(f"{int(value)}! = {result}")
            elif choice == "3":
                value = prompt_number("Enter a positive number: ", to_float)
                result = calculator.natural_log(value)
                print(f"ln({value}) = {result}")
            elif choice == "4":
                base = prompt_number("Enter the base (x): ", to_float)
                exponent = prompt_number("Enter the exponent (b): ", to_float)
                result = calculator.power(base, exponent)
                print(f"{base}^{exponent} = {result}")
            elif choice == "5":
        # Jenkins webhook test comment
                print("Goodbye!")
                break
            else:
                print("Invalid selection. Please choose a number between 1 and 5.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
