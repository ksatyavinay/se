import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
import matplotlib.pyplot as plt 
# Input variables from keyboard
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
pressure = float(input("Enter pressure (hPa): "))
# Define quadratic equation coefficients
a = 0.01
b = -0.5
c = 25
# Calculate weather parameter
precipitation = a * temperature**2 + b * humidity + c
# Print result
print(f"Precipitation: {precipitation}")
temperature_range = range(0, 31)
# Calculate precipitation for each temperature value
precipitation_values = [a * temp**2 + b * humidity + c for temp in temperature_
# Create plot
plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='o', linestyle='-'
, co
plt.xlabel('Temperature (°C)')
plt.ylabel('Precipitation (mm)')
plt.title('Relationship between Temperature and Precipitation')
plt.grid(True)
plt.legend()
# Show plot
plt.show()
