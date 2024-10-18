import pandas as pd
import numpy as np

# Load the dataset
data = pd.read_csv('Muni_Simple_Routes.csv')

# Convert timestamp columns to datetime format
data['data_as_of'] = pd.to_datetime(data['data_as_of'], format='%m/%d/%Y %I:%M:%S %p')
data['data_loaded_at'] = pd.to_datetime(data['data_loaded_at'], format='%m/%d/%Y %I:%M:%S %p')

# Removing duplicates
data_cleaned = data.drop_duplicates()

########### how many unique patterns for each route 

# Group data by ROUTE_NAME
grouped_data = data_cleaned.groupby('ROUTE_NAME')

# Count the number of unique patterns for each route
unique_patterns_per_route = grouped_data['PATTERN'].nunique()

# Reset the index to convert it back to a DataFrame
route_patterns_count = unique_patterns_per_route.reset_index(name='unique_patterns')

# Sort the routes by the number of unique patterns to identify routes with the most patterns 
sorted_routes_by_pattern = route_patterns_count.sort_values(by= 'unique_patterns', ascending=False)

# Analyzing the service types (SERVICE_CA) for these routes to see which service type h
# Print the unique patterns per route
print(route_patterns_count)

################## unique patterns for each service type 

# Group routes by 'SERVICE_CA' to see how many unique patterns exist for each service type
service_type_patterns = data_cleaned.groupby('SERVICE_CA')['PATTERN'].nunique() 
print(service_type_patterns)

