# Phone-comparison (Compare a phone)-
in this project we crafted a tool which  helps to compare between mobile phones, it has all the mainstream  specifications related to phones and thats how it helps to determine which one is better 


It allows you to input specifications for multiple devices side-by-side, calculates a "Raw Performance Score", and determines which device offers the best "Value for Money" (VFM) based on current Indian market trends.

--GUI Interface: Clean, scrollable interface built with Tkinter.

--Dynamic Comparison: Add as many devices as you need to compare at once.

---Smart Scoring Engine:

    CPU Database: Includes scores for Snapdragon, MediaTek, Apple, and Google chips.

    Screen Analysis: Awards bonus points for LTPO and AMOLED technology.

    RAM & Size Weighting: Factors in memory and display size.

    The Verdict System: Automatically identifies:

    performance King: The most powerful device regardless of price.

    Value Winner: The device that gives the most performance per Rupee (₹).

## ##############################################
The file (Python.py) is ready to use , feel free to use it as you please

use it in vs code for easy execution of the code make sur eto install and import "TKINTER"
Here is a short, simple, and human-friendly README for your project.

## Features
Visual Comparison: Add as many devices as you want side-by-side.

Smart Scoring: It uses a built-in database of processors (Snapdragon, Apple, MediaTek, Google) to grade performance.

Screen Quality: It knows that an LTPO AMOLED is better than an IPS LCD and awards points accordingly.

The Verdict: Instantly tells you if you should pay up for performance or save money for the best deal.

## What You Need
Just Python! There are no external libraries to install. (This app uses tkinter, which comes pre-installed with Python).

## How to Run
Save the code as compare_app.py.

Open your terminal or command prompt.

Run the command:

python Python.py


## How the "Brain" Works
The app calculates a Raw Score based on:

Processor Power (0-100 points based on the chip model).

RAM (More GB = More points).

Screen Type (Bonus points for OLED/AMOLED tech).

It then calculates a VFM Score (Value For Money) by dividing the performance score by the price.

## Note
I've included popular chips (Snapdragon 8 Gen 3, A17 Pro, etc.). If a processor is missing, you can easily add it to the CPU_DB list in the code!

Happy Shopping! 🛒


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
changes -- 
1. we have added new sliders for battery capacity and its charger wattage
2. added a new budget slot to get recomendations in between the given budgert or else it suggests if we shoukd save up for the other expensive device if the phone in budget isnt good enough for the given price
3. the output now occurs in another window making it visible and easy to read
4. changes in theme and ui - made it look a bit more clean and proffesional 
