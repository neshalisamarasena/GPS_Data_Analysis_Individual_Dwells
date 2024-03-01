import pandas as pd
import numpy as np

# ----------------------------------------------------------------------
# 1. Load and prepare GPS data
# ----------------------------------------------------------------------

# Read GPS data from CSV file
df = pd.read_csv('gps.csv')

# Convert 'datetime' column to datetime format for accurate time calculations
df['datetime'] = pd.to_datetime(df['datetime'])

# Print initial data overview
print(df.head())  # Display first few rows
print(df.describe())  # Show descriptive statistics

# ----------------------------------------------------------------------
# 2. Define function for Euclidean distance calculation
# ----------------------------------------------------------------------

def euclidean_distance(lat1, lon1, lat2, lon2):
   """
   Calculates the Euclidean distance between two points on Earth
   using their latitude and longitude coordinates.
   """
   return np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

# ----------------------------------------------------------------------
# 3. Dwell identification algorithm
# ----------------------------------------------------------------------

# Initialize lists to store dwell start and end timestamps
dwell_starts = []
dwell_ends = []

current_dwell_start = None  # Keep track of potential ongoing dwell

# Define thresholds for dwell identification
min_dwell_duration = pd.Timedelta(minutes=5)
distance_threshold = 0.01  # Maximum distance between consecutive points within a dwell (in degrees)

# Iterate through GPS data points
for i in range(1, len(df)):

   # Get current and previous coordinates
   prev_lat, prev_lon = df.loc[i-1, ['lat', 'lon']]
   curr_lat, curr_lon = df.loc[i, ['lat', 'lon']]

   # Calculate distance between consecutive points
   distance = euclidean_distance(prev_lat, prev_lon, curr_lat, curr_lon)

   # Check for dwell start (if no dwell ongoing and distance is low)
   if current_dwell_start is None and distance <= distance_threshold:
       current_dwell_start = df.loc[i, 'datetime']  # Mark dwell start time

   # Check for dwell end (if dwell ongoing and distance exceeds threshold)
   elif current_dwell_start is not None and distance > distance_threshold:
       dwell_ends.append(df.loc[i-1, 'datetime'])  # Add dwell end time
       current_dwell_start = None  # Reset dwell start when movement detected

# Handle potential dwell at the end of the data
if current_dwell_start is not None:
   dwell_ends.append(df.loc[len(df)-1, 'datetime'])

# ----------------------------------------------------------------------
# 4. Filter and analyze dwells
# ----------------------------------------------------------------------

# Filter dwells based on minimum duration
dwells = [(start, end) for start, end in zip(dwell_starts, dwell_ends)
         if end - start >= min_dwell_duration]

# Print the identified dwell periods
print(dwells)

# Further analysis or visualization of dwells can be done using the 'dwells' list
