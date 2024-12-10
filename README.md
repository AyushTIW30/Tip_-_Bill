Tip and Bill Splitter Calculator
Welcome to the Tip and Bill Splitter Calculator! This Python program calculates how much each person needs to pay when a bill is split among multiple people, including a tip based on the user's chosen percentage.

Features
Interactive User Input:

Prompts the user for the total bill amount, tip percentage, and number of people to split the bill among.
Handles invalid input (e.g., non-numeric values or invalid tip percentages) and asks the user to re-enter data until valid input is provided.
Tip Calculation:

Calculates the tip amount based on the user's chosen tip percentage (10%, 12%, or 15%).
Adds the tip amount to the total bill and divides the resulting amount equally among the number of people.
Formatted Output:

Displays a clean, organized bill breakdown with total amounts, tip, and the amount each person needs to pay.
Requirements
Python 3.x
How to Run
Clone the repository or download the code file.

Open a terminal/command prompt in the folder where the file is located.

Run the Python script by typing:

bash
python Bill_&_Tip_Calculator.py
Follow the prompts to input the total bill, tip percentage, and the number of people splitting the bill.

Example Usage
******************************************
        Welcome to the Tip and Bill Splitter Calculator!    
******************************************

What was the total bill? $150
What percentage tip would you like to give? (Choose 10, 12, or 15): 12
How many people would you like to split the bill among? 5

******************************************
             Bill Breakdown                
******************************************
Total bill (before tip):  $150.00
Tip percentage:           12%
Total tip amount:        $18.00
Total bill with tip:     $168.00
Number of people:        5
Amount per person:       $33.60

******************************************
How It Works
User Input: The program asks the user for:

The total bill amount.
The tip percentage (choose between 10%, 12%, or 15%).
The number of people splitting the bill.
Calculations:

The program calculates the tip amount by multiplying the total bill by the chosen percentage.
It then adds the tip amount to the original bill to get the total amount to be paid.
Finally, the program divides the total bill by the number of people to determine how much each person should pay.
Formatted Output:

The breakdown of the total bill, the tip, and the amount each person owes is displayed in a neat format.
Code Explanation
The program uses input validation loops to ensure the user provides valid input for the total bill, tip percentage, and number of people.
It performs basic arithmetic to calculate the tip and the amount each person needs to pay.
The results are printed in a well-organized, user-friendly format.
Contributing
Feel free to fork the repository, make improvements, or suggest new features. If you have a bug fix or feature suggestion, please submit a pull request.
