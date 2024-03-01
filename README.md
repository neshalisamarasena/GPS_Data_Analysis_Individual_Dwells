# GPS_Data_Analysis_Individual_Dwells
This repository contains code to analyze GPS data and identify dwells, periods where an individual or object remains relatively stationary.

# Purpose
  Identifies dwell periods from GPS coordinate data.
  Provides insights into patterns of movement or behavior by analyzing:
  The number of dwells
  Average and median dwell durations
  Any specific time-based or location-based trends
  Usage Instructions
  
# Dependencies
  - Python 3.x
  - pandas
  - NumPy

# Installation
  Bash: pip install pandas numpy

# Execution
1. Prepare your data:
  Ensure your GPS data is in a CSV file named 'gps_data.csv' and located in the data folder of this repository.
  The file must contain at least the following columns: 'datetime', 'lat', 'lon'.

2. Run the analysis script:
  Bash: python src/dwell_analyzer.py 
  Modify dwell_analyzer.py if you wish to adjust the min_dwell_duration and distance_threshold parameters.

3. Customization
  You can adjust the dwell identification criteria by modifying the following parameters in src/dwell_analyzer.py:
    min_dwell_duration: The minimum duration (in timedelta format) for a period to be considered a dwell.
    distance_threshold: The maximum distance (in degrees) allowed within a dwell period for it to be considered stationary.

4. Algorithm Explanation
  The code implements a basic algorithm to identify dwells based on distance and duration thresholds:
  It iterates through the GPS data points chronologically.
  For each pair of consecutive data points:
  It calculates the Euclidean distance between them using latitude and longitude coordinates.
  If the distance is below the distance_threshold and there is no ongoing dwell:
  It marks the current timestamp as the start of a new dwell period.
  If the distance exceeds the distance_threshold while a dwell is ongoing:
  It marks the previous timestamp as the end of the dwell period.
  Dwells shorter than the min_dwell_duration are discarded.
  This approach offers a simple yet effective way to identify dwells based on user-defined parameters, capturing periods of relative stillness based on distance and duration criteria.
