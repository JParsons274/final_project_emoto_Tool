# main.py
from ebike_utils import *
import pandas as pd

bike_records = []

print("Welcome to the E-Bike Efficiency Calculator!\n")

add_another = True

while add_another:
    bike = get_bike_by_model()

    if not confirm_bike_details(bike):
        print("Please recheck your bike model or try again later.")
        continue

    bike['Avg Mileage (mi)'] = float(input("Enter your average ride distance in miles: "))
    bike['Charge Cycles'] = int(input("Enter the number of charge cycles your battery has gone through: "))

    bike['Estimated Range (mi)'] = calculate_range(bike['Battery (Wh)'], bike['Avg Mileage (mi)'])
    bike['eMPG'] = calculate_empg(bike['Battery (Wh)'], bike['Avg Mileage (mi)'])
    bike['Estimated Battery Life (cycles)'] = calculate_battery_life(bike['Charge Cycles'])
    bike['Battery Fatigue (%)'] = calculate_battery_fatigue(bike['Charge Cycles'])

    bike_records.append(bike)
    add_another = ask_to_continue()

bike_df = pd.DataFrame(bike_records)
print("\nSummary Table of Bikes:")
print(bike_df)

# Generate and save bar graphs
plot_efficiency_graph(bike_df)
plot_range_comparison_bar(bike_df)
