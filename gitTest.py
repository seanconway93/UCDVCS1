from typing import Union, Any

import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.core._multiarray_umath import ndarray
from pandas import DataFrame, Series

#Importing CSV files into Pandas Dataframe
from pandas.core.arrays import ExtensionArray

world_cups = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCups.csv")
matches = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCupMatches.csv")
players = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCupPlayers.csv")

#Data Cleaning: Dropping Null values
world_cups = world_cups.dropna()
matches = matches.dropna()
players = players.dropna()

#Data Cleaning: Amending relevant country names
world_cups["Winner"] = world_cups["Winner"].str.replace("Germany FR","Germany")
world_cups["Runners-Up"] = world_cups["Runners-Up"].str.replace("Germany FR","Germany")
world_cups["Third"] = world_cups["Third"].str.replace("Germany FR","Germany")
world_cups["Fourth"] = world_cups["Fourth"].str.replace("Germany FR","Germany")
world_cups["Fourth"] = world_cups["Fourth"] = world_cups["Fourth"].str.replace("Soviet Union","Russia")
matches["Home Team Name"] = matches["Home Team Name"].str.replace("Soviet Union","Russia")
matches["Home Team Name"] = matches["Home Team Name"].str.replace("Germany FR","Germany")
matches["Away Team Name"] = matches["Away Team Name"].str.replace("Germany FR","Germany")
matches["Away Team Name"] = matches["Away Team Name"].str.replace("Soviet Union","Russia")

matches.dropna(subset=["Year"], inplace=True)

#Ranking and comparing all nations that have appeared in the final 4
winners = world_cups["Winner"]
runners_up = world_cups["Runners-Up"]
third_place = world_cups["Third"]
fourth_place = world_cups["Fourth"]

winners1 = winners.value_counts()
runners_up1 = runners_up.value_counts()
third_place1 = third_place.value_counts()
fourth_place1 = fourth_place.value_counts()

teams = pd.concat([winners1, runners_up1, third_place1, fourth_place1], axis=1)
teams = teams.fillna(0)
teams = teams.astype(int)
#print(teams)

#Growth of the competition over time
goals_per_game = (world_cups.loc[ :, ["Year", "QualifiedTeams", "MatchesPlayed", "GoalsScored"]])
gpg = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]
years= world_cups["Year"]
gpgyears = pd.concat([gpg, years], axis=1)

fig, ax = plt.subplots()
ax.plot(years, gpg, linewidth=0.5)
ax.set(xlabel= "Year", ylabel = "Average Goals Per Game")
ax.set_xticks(years, minor=True)
ax.grid()
plt.xlim(1930, 2014)
#plt.show()

#Tournaments with average goals per game of 3 or higher
criteria = gpgyears[gpgyears.iloc[:,0]>= 3]
print(criteria)

#Goals per tournament over time
sns.set_style("darkgrid")
sns.set_palette("Blues")
sns.catplot(x="Year", y="GoalsScored", data=world_cups,
            kind="point", hue="GoalsScored")
plt.xticks(rotation=55)
#plt.show()

finals = matches[(matches["Stage"]=="Final")]
finals = finals.loc[:, ["Year", "Home Team Name", "Home Team Goals", "Away Team Name", "Away Team Goals"]]
finals = finals.drop_duplicates()
print(finals)

finals_world_cups = world_cups.merge(finals, on="Year")
#print(finals_world_cups.head())
finals_goals = finals_world_cups["Home Team Goals"] + finals_world_cups["Away Team Goals"]
finals_goals = finals_goals.astype(int)
merged_years = finals_world_cups["Year"]
goals_per_final = pd.concat([merged_years, finals_goals], axis=1)

#goals_per_final = pd.concat([finals_goals, years], axis=1)
print(goals_per_final)
#gpgyears = pd.concat([gpg, years], axis=1)