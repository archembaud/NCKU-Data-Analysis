import pandas as pd
import matplotlib.pyplot as plt
import math
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
'''
Note: the outcome of the statistics used in this code cannot be trusted in any
real sense. There are many reasons for this:
- Earthquake strengths are not normally distrubuted,
- Future earthquakes cannot be predicted based on past earthquakes
The codes presented here form part of a data analysis course only
and are presented for education purposes.
'''

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    print("Initial Data:")
    print(data.head())
    return data

def compute_chance_greater_than(target, mean, std):
    Z = (target - mean)/std
    Pr = 1.0 - 0.5*(1 + math.erf(Z/math.sqrt(2)))
    return Pr

def create_Taiwan_figure():
    # Create a figure with PlateCarree projection
    fig = plt.figure(figsize=(8, 8))
    ax = plt.axes(projection=ccrs.PlateCarree())
    # Set extent to focus on Taiwan (lon_min, lon_max, lat_min, lat_max)
    ax.set_extent([119, 123.5, 21.5, 26.5], crs=ccrs.PlateCarree())
    # Add map features
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.OCEAN, facecolor="lightblue")
    ax.add_feature(cfeature.COASTLINE, linewidth=0.8)
    # Fancy optional features
    #ax.add_feature(cfeature.BORDERS, linestyle="--", linewidth=0.5)
    #ax.add_feature(cfeature.LAKES, facecolor="lightblue")
    #ax.add_feature(cfeature.RIVERS, linewidth=0.5)
    # Add gridlines
    gL = ax.gridlines(draw_labels=True, linewidth=0.5, color="gray", alpha=0.5)
    gL.top_labels = False
    gL.right_labels = False
    return ax, fig

# Load the unzipped data
# Your data may be located in a different location; you'll have to fix the path yourself.
df = load_data('./../../Data/CWA_Earthquakes_2023_2025/CWA_Earthquakes_2023_2025/Seismic activity_638989797821035182.csv')

# Find all the earthquakes near kaohsiung
kaohsiung_rows = df["Location Note B"].str.contains("Kaohsiung City")
kaohsiung_df = df[kaohsiung_rows]
print(f"Found {len(kaohsiung_df)} rows of data for Kaohsiung City")

# Find all the earthquakes near Tainan
tainan_rows = df["Location Note B"].str.contains("Tainan City")
tainan_df = df[tainan_rows]
print(f"Found {len(tainan_df)} rows of data for Tainan City")

# Goal is to compute the chance, based on historic data, that the next earthquake will be a magnitude 5 or higher
mag_goal = 5
# Z-score compute - Kaohsiung
Pr = compute_chance_greater_than(mag_goal, kaohsiung_df['Magnitude'].mean(), kaohsiung_df['Magnitude'].std())
print(f"The chance of a random earthquake in Kaohsiung being magnitude {mag_goal} or higher is {Pr*100} %.")
# Z-score compute - Tainan
Pr = compute_chance_greater_than(mag_goal, tainan_df['Magnitude'].mean(), tainan_df['Magnitude'].std())
print(f"The chance of a random earthquake in Tainan being magnitude {mag_goal} or higher is {Pr*100} %.")
# Perform the island-wide calculation
Pr = compute_chance_greater_than(mag_goal, df['Magnitude'].mean(), df['Magnitude'].std())
print(f"Over the entire island of Taiwan, the chance of a random earthquake being magnitude {mag_goal} or higher is {Pr*100} %.")

# Show these on a map
ax, fig = create_Taiwan_figure()
ax.scatter(kaohsiung_df['Longitude(E)'], kaohsiung_df['Latitude(N)'], c='b', marker='.')
ax.scatter(tainan_df['Longitude(E)'], tainan_df['Latitude(N)'], c='r', marker='.')

# Coordinates near a particular location
target_lat = 23.77
target_long = 120.98

# Create columns which show the DX and DY distance from this
df['DY'] = (df['Latitude(N)'] - target_lat)*111.113   # Distance in km from the target lat
df['DX'] = (df['Longitude(E)'] - target_long)*111.32*math.cos(target_lat*3.14159/180.0)
df["RADIUS"] = np.sqrt(df['DX']*df['DX'] + df['DY']*df['DY'])

# Save the data for checking later.
df.to_csv('newData.csv', index=False)

# Find quakes within 50 km of this point
rows_99 = (df['RADIUS'] < 50.0)
df_99 = df[rows_99]
print(f"Found {len(df_99)} quakes within 50km of {target_lat}, {target_long}")

# Compute the odds for this location
Pr = compute_chance_greater_than(mag_goal, df_99['Magnitude'].mean(), df_99['Magnitude'].std())
print(f"At my point of interest, the chance of a random earthquake being magnitude {mag_goal} or higher is {Pr*100} %.")

# Draw these on
ax.scatter(df_99['Longitude(E)'], df_99['Latitude(N)'], c='k', marker='.')
# Add labels
plt.legend(['Kaohsiung Earthquakes', 'Tainan Earthquakes', 'Earthquakes near point'])
plt.xlabel('Longitude (E)')
plt.ylabel('Latitude (N)')
plt.show()