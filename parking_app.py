"""
Parking App
Calculates parking charges using the client's rate of £2 per hour.
"""

from decimal import Decimal, InvalidOperation


def get_parking_hours():
    """Keep asking until the customer enters a positive number of hours."""
    while True:
        entered_hours = input("Enter the number of hours parked: ").strip()
        try:
            hours = Decimal(entered_hours)

            if not hours.is_finite() or hours <= 0:
                print("Please enter a finite number greater than zero.")
                continue

            return hours
        except InvalidOperation:
            print("Invalid input. Enter a number, such as 2 or 1.5.")


def calculate_parking_cost(hours, hourly_rate):
    """Multiply the parking time by the hourly charge."""
    return hours * hourly_rate


def display_parking_summary(hours, hourly_rate, total_cost):
    """Show the parking time, hourly rate and final amount due."""
    print("\n========== PARKING SUMMARY ==========")
    print(f"Hours parked: {hours}")
    print(f"Cost per hour: £{hourly_rate:.2f}")
    print(f"Total parking cost: £{total_cost:.2f}")
    print("=====================================")
    print("Thank you for using the Parking App!")


def main():
    """Start and control the parking application."""
    parking_rate = Decimal("2.00")

    print("=====================================")
    print("         WELCOME TO PARKING APP")
    print("=====================================")

    hours_parked = get_parking_hours()
    total_cost = calculate_parking_cost(hours_parked, parking_rate)
    display_parking_summary(hours_parked, parking_rate, total_cost)


if __name__ == "__main__":
    main()
