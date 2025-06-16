# main.py

from ebike_utils import *
import pandas as pd

# Store all bike data 
bike_records = []

print("Welcome to the E-Bike Efficiency Calculator!\n")

add_another = True

while add_another:
    # Get user input for bike model and stats
    bike = get_bike_by_model()

    confirm = confirm_bike_details(bike)
    if not confirm:
        print("Please recheck your bike model or try again later.")
        continue

    # Continue with user-provided data
    bike['Avg Mileage (mi)'] = float(input("Enter your average ride distance in miles: "))
    bike['Charge Cycles'] = int(input("Enter the number of charge cycles your battery has gone through: "))

    # Perform calculations
    bike['Estimated Range (mi)'] = calculate_range(bike['Battery (Wh)'], bike['Avg Mileage (mi)'])
    bike['eMPG'] = calculate_empg(bike['Battery (Wh)'], bike['Avg Mileage (mi)'])
    bike['Estimated Battery Life (cycles)'] = calculate_battery_life(bike['Charge Cycles'])
    bike['Battery Fatigue (%)'] = calculate_battery_fatigue(bike['Charge Cycles'])

    # Save result
    bike_records.append(bike)

    # Ask to add another
    add_another = ask_to_continue()

# Convert to DataFrame
bike_df = pd.DataFrame(bike_records)
print("\nSummary Table of Bikes:")
print(bike_df)

# Generate and save graph
plot_efficiency_graph(bike_df)  
plt.savefig("ebike_efficiency.png")  
print("Graph saved as ebike_efficiency.png")

"""
Reference Stats:

Talaria:
- MX3: 60v 38ah 6280wh 100km range
- MX4: 60v 45ah 2700wh 120km range
- MX5: 72v 40ah 2880wh 120km range

Surron:
- Ultra Bee: 74v 55ah 4070wh 140km range
- Light Bee X: 60v 38ah 6000wh 75km range
- Light Bee S: 60v 40ah 2400wh 75km range
- Storm Bee: 104v 55ah 4320wh 110km range

E Ride Pro:
- E Ride Pro S: 72v 30ah 2160wh 65km range
- E Ride Pro SR: 72v 50ah 3600wh 62 mi @25mph / 93 mi @15mph
- E Ride Pro SS 2.0: 72v 40ah 2880wh 50+ mi @25mph / 90+ @15mph
- E Ride Pro SS 3.0: 72v 50ah 3600wh 64+ mi @25mph / 100+ @15mph

Other:
- 79 Falcon Pro: 72v 35ah 2200wh 100km range
"""



