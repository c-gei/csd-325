## Cece Geisler
## CSD 325
## M4.2 Assignment
## January 14, 2026

## START
import csv
## Change: Added sys to help with the exit process.
import sys
from datetime import datetime
from matplotlib import pyplot as plt

## Change: Defined a function to handle the data loading. Prevents repeating code for highs and lows.
def get_weather_data(filename, index):
    """Open a CSV file and return dates and temperatures from a specific column."""
    dates, temps = [], []
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                temp = int(row[index])
                temps.append(temp)
        return dates, temps
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None, None

## Change: Added a function to plot/graph the data. Prevents repeating code for highs and lows.
def plot_weather(dates, temps, title, color):
    """Create a graph with the provided data."""
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    ## Format plot.
    plt.title(title, fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    ## Agent Debug: Use a non-blocking show or save to file to avoid hanging in automated environments
    plt.savefig('weather_plot.png')
    print("Plot saved as 'weather_plot.png'")
    
    ## Agent Debug: Print the first 5 records to console
    print("\nSample Data (First 5 records):")
    for d, t in list(zip(dates, temps))[:5]:
        print(f"{d.strftime('%Y-%m-%d')}: {t} F")
    
    plt.close(fig)

## Change: Defined a main function to handle the menu loop and user input.
def run_weather_app():
    filename = "sitka_weather_2018_simple.csv"
    ## Change: Added instructions on how to use the menu.
    print("--- Welcome to the Sitka Weather Viewer ---")
    print("Instructions: Type 'Highs' to view max temps, 'Lows' for Min temps, or 'Exit' to quit.") 

    ## Change: Added a loop so the program stays open until the user chooses to exit.
    while True:
        print("\nMenu: [Highs] [Lows] [Exit]")
        user_choice = input("What would you like to view? ").strip().lower()

        if user_choice == 'highs': ## Change: Calling out the function with index 5 for TMAX.
             dates, highs = get_weather_data(filename, 5)
             if dates:
                plot_weather(dates, highs, "Daily high temperatures - 2018", 'red')
        elif user_choice == 'lows': ## Change: Calling out the function with index 6 for TMIN.
             dates, lows = get_weather_data(filename, 6)
             if dates:
                  plot_weather(dates, lows, "Daily low temperatures - 2018", 'blue')
    ## Change: Added an exit option.
        elif user_choice == 'exit':
            print("Thank you for using the Sitka Weather Viewer. Goodbye!")
            sys.exit()
            
    ## Change: Error handling for invalid input.
        else:
             print("Invalid choice. Please enter Highs, Lows, or Exit.")

## Change: This starts the program
if __name__ == "__main__":
     run_weather_app()

## END
            

