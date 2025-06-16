# final_project_emoto_Tool
# E-Bike Efficiency Calculator

**Name:** Jack Parsons  
**Class:** Python Programming Final Project  
**Date:** June 12, 2025

#Project Description

The E-Bike Efficiency Calculator is a tool that estimates performance metrics for electric dirt bikes based on rider input and manufacturer specifications. The program lets users select from a list of popular e-bike models (like Talaria, Surron, and E Ride Pro), then calculates eMPG, estimated range, remaining battery life, and battery fatigue using mileage and charge cycle data.

The program stores input and calculated results in a table using `pandas`, and visualizes efficiency and range comparisons with bar graphs using `matplotlib`.

#Testing & Inputs

To test the program, I entered different bike models including:
- MX3 with 55 average miles and 195 charge cycles
- Ultra Bee with 60 miles and 100 cycles
- E Ride Pro SR with 40 miles and 250 cycles

Each test generated accurate calculations and output a visual graph comparing the selected bikes' eMPG and range against stock range data.


## Reflection

This project helped me reinforce core Python skills like variables, user input, functions, loops, and conditional logic. I structured the code using modular functions in a separate file (`ebike_utils.py`) to keep things clean and readable.

The biggest new concept I explored was using Pandas and Matplotlib. I learned how to build and modify a DataFrame from a list of dictionaries, and how to generate bar graphs from that data. Plotting the eMPG and comparing user range to manufacturer range made the project feel practical.

One of the biggest challenges I faced was getting the plots to display and save correctly in GitHub Codespaces. With trial and error—and some help—I figured out that I needed to call `plt.savefig()` and manage figure layout using `plt.tight_layout()` to avoid cut off labels. It was frustrating at first but it felt great once it worked.

---

##  Final Output Includes:
- Command line interface for user input
- Multiple bike entries and comparisons
- Auto calculations for range, eMPG, and battery health
- Two bar graphs:
  - eMPG Comparison
  - Estimated vs Stock Range
- All data summarized in a pandas table


