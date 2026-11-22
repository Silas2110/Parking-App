# Parking App

A Python console program based on the client requirement: charge £2 per hour and show the total parking cost.

## Features
- Requests the number of hours parked.
- Calculates the cost at £2 per hour.
- Displays a parking summary.
- Validates input and rejects zero, negative and non-numeric values.
- Uses `Decimal` for accurate currency calculations.

## Run in Visual Studio 2026
1. Open this folder in Visual Studio 2026.
2. Ensure Python support and a Python 3 interpreter are installed and selected.
3. Open `parking_app.py`.
4. Run the file, or open the integrated terminal and enter:

   `python parking_app.py`

## Example
Input: `3`
Output: `Total parking cost: £6.00`

## Test cases

| Input | Expected result |
|---|---|
| 1 | £2.00 |
| 3 | £6.00 |
| 5 | £10.00 |
| 1.5 | £3.00 |
| 0 or -2 | Validation message; ask again |
| hello | Invalid-input message; ask again |
