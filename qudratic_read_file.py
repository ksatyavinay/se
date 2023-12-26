import time
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))
import csv

# Define file path
file_path = "weatherHistory.csv"

# Initialize empty list to store results
results = []

# Read data from file
with open(file_path, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract variables
        temperature = float(row["temperature"])
        humidity = float(row["humidity"])
        pressure = float(row["pressure"])

        # Define quadratic equation coefficients
        a = 0.01
        b = -0.5
        c = 25

        # Calculate weather parameter
        precipitation = a * temperature**2 + b * humidity + c

        # Store result
        results.append({"temperature": temperature, "humidity": humidity, "pressure": pressure, "precipitation": precipitation})

# Print results
for result in results:
    print(f"Temperature: {result['temperature']}°C, Humidity: {result['humidity']}%,"
          f" Pressure: {result['pressure']}hPa, Precipitation: {result['precipitation']}")
