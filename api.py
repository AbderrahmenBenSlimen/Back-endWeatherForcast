import requests

# Set the API endpoint and parameters
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
params = {'datasetid': 'GHCND', 'locationid': 'CITY:US060013', 'startdate': '2018-01-01', 'enddate': '2022-01-31'}

# Set the API token
token = 'YhSJEnpdjgFPeodfxjwZxjwlSmwCsAuB'

# Set the headers to include the token
headers = {'token': token}

# Make the API request
response = requests.get(url, params=params, headers=headers)

# Print the response content
print(response.content)
