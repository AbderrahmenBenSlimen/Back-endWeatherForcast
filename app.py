import requests
import pandas as pd
from datetime import datetime, timedelta
# Get the current date and time
current_time = datetime.utcnow()

# Calculate the start and end dates for the 7-day period
start_time = current_time - timedelta(days=7)
end_time = current_time - timedelta(days=1)
api_key = 'c2c135e363fa4eaa851105600232303'
# Convert the start and end dates to the required format
start_date = start_time.strftime("%Y-%m-%d")
end_date = end_time.strftime("%Y-%m-%d")

city = input('Enter a city/state name: ')
# Construct the API request URL
url = f"https://api.weatherapi.com/v1/history.json?key={api_key}&q={city}&dt={start_date}&end_dt={end_date}"

response = requests.get(url)

# Extract the temperature, humidity, and summary data from the response
data = response.json()
# Parse the response and extract the temperature, humidity, and summary data for each day
data = response.json()['forecast']['forecastday']
temp_data = [day['day']['avgtemp_c'] for day in data]
humidity_data = [day['day']['avghumidity'] for day in data]
summary_data = [day['day']['condition']['text'] for day in data]

# Create a DataFrame to store the data
df = pd.DataFrame({'Temperature (C)': temp_data, 'Humidity': humidity_data, 'Summary': summary_data})

# Print the first few rows of the DataFrame
print(df.head())