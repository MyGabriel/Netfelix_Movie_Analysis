# FILE: analysis.py

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from datasets.exceptions import ManualDownloadError

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

netflix_df

# Extracting specific decade (movies between 1990 and 1999) infomation for the task
movies = netflix_df[(netflix_df["release_year"] >= 1990) & (netflix_df["release_year"] <= 1999)]
movies_1990s = movies[movies["type"] == "Movie"]

# Counting movies less 90 minutes
movies_time = movies_1990s["duration"].value_counts()
print(movies_time)                  # value_count() gave 94 as the highest

# Visualize the duration column of your filtered data to see the distribution of movie durations
# See which bar is the highest and save the duration value, this doesn't need to be exact!

plt.hist(movies_1990s["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.savefig("analysis.png" )
plt.show()

# Visualization with matplot gave 100 as the highest
duration = 100

# Isolation movies less than 90 minutes which are also "Action" genre
movies_less90 = movies_1990s[(movies_1990s["duration"] < 90) & (movies_1990s["genre"] == "Action")]
short_movie_count = len(movies_less90)
print("Using a striaght forword approach: ", short_movie_count)


# Or use a for loop and a counter to count how many short action movies there were in the 1990s
# Start the counter
short_movie_count1 = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90, if it is, add 1 to the counter, if it isn't, the counter should remain the same
for label, row in movies_less90.iterrows() :
    if row["duration"] < 90 :
        short_movie_count1 = short_movie_count1 + 1
    else:
        short_movie_count1 = short_movie_count1

print("Using the 'for' loop: ", short_movie_count1)



################# THE END ###################
# Author: Gabriel Lord Manu
# Task: DataCamp Project
# Sponsor: BHN Academy Germany