# ebike_utils.py
import matplotlib.pyplot as plt

def get_bike_by_model():
    bike_model_data = {
        "MX3": {"Voltage": 60, "AH": 38, "Battery (Wh)": 6280, "Stock Range": 100},
        "MX4": {"Voltage": 60, "AH": 45, "Battery (Wh)": 2700, "Stock Range": 120},
        "MX5": {"Voltage": 72, "AH": 40, "Battery (Wh)": 2880, "Stock Range": 120},
        "Ultra Bee": {"Voltage": 74, "AH": 55, "Battery (Wh)": 4070, "Stock Range": 140},
        "Light Bee X": {"Voltage": 60, "AH": 38, "Battery (Wh)": 6000, "Stock Range": 75},
        "Light Bee S": {"Voltage": 60, "AH": 40, "Battery (Wh)": 2400, "Stock Range": 75},
        "Storm Bee": {"Voltage": 104, "AH": 55, "Battery (Wh)": 4320, "Stock Range": 110},
        "E Ride Pro S": {"Voltage": 72, "AH": 30, "Battery (Wh)": 2160, "Stock Range": 65},
        "E Ride Pro SR": {"Voltage": 72, "AH": 50, "Battery (Wh)": 3600, "Stock Range": 93},
        "E Ride Pro SS 2.0": {"Voltage": 72, "AH": 40, "Battery (Wh)": 2880, "Stock Range": 90},
        "E Ride Pro SS 3.0": {"Voltage": 72, "AH": 50, "Battery (Wh)": 3600, "Stock Range": 100},
        "79 Falcon Pro": {"Voltage": 72, "AH": 35, "Battery (Wh)": 2200, "Stock Range": 100}
    }

    model = input("Enter the model of your e-bike (e.g., MX3, Ultra Bee): ")
    data = bike_model_data.get(model.strip())

    if not data:
        print("Model not found. Please try again.")
        return get_bike_by_model()

    data['Model'] = model
    return data

def confirm_bike_details(bike):
    print(f"\nYou selected: {bike['Model']}")
    print(f"Voltage: {bike['Voltage']}V")
    print(f"Amp Hours: {bike['AH']}Ah")
    print(f"Battery Capacity: {bike['Battery (Wh)']} Wh")
    return input("Is this correct? (yes/no): ").lower() == "yes"

def calculate_range(battery_wh, avg_mileage):
    return battery_wh / avg_mileage

def calculate_empg(battery_wh, avg_mileage):
    return (battery_wh / avg_mileage) / 33700 * 100

def calculate_battery_life(charge_cycles):
    expected_life = 1000
    return max(0, expected_life - charge_cycles)

def calculate_battery_fatigue(charge_cycles):
    fatigue_percent = min(100, (charge_cycles / 1000) * 100)
    return round(fatigue_percent, 2)

def ask_to_continue():
    return input("\nDo you want to add another bike? (yes/no): ").lower() == "yes"

def plot_efficiency_graph(df):
    plt.figure(figsize=(10,6))
    plt.bar(df['Model'], df['eMPG'], color='teal')
    plt.title("E-Bike Efficiency Comparison (eMPG)")
    plt.xlabel("Bike Model")
    plt.ylabel("eMPG")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("ebike_efficiency.png")
    print("Graph saved as ebike_efficiency.png")
    plt.close()

def plot_range_comparison_bar(df):
    plt.figure(figsize=(10,6))
    actual_ranges = df['Estimated Range (mi)']
    stock_ranges = df['Stock Range']

    bar_width = 0.35
    x = range(len(df))

    plt.bar([i - bar_width/2 for i in x], stock_ranges, width=bar_width, label='Stock Range', color='gray')
    plt.bar([i + bar_width/2 for i in x], actual_ranges, width=bar_width, label='Actual Range', color='green')

    plt.xticks(ticks=x, labels=df['Model'], rotation=45)
    plt.xlabel("Bike Model")
    plt.ylabel("Range (mi)")
    plt.title("Stock vs Actual Range Comparison")
    plt.legend()
    plt.tight_layout()
    plt.savefig("ebike_range_comparison.png")
    print("Graph saved as ebike_range_comparison.png")
    plt.close()



 