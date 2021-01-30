import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame, Series

#Importing CSV files into Pandas Dataframe

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

#Ranking and comparing all nations that have appeared in the final 4
winners = world_cups["Winner"]
runners_up = world_cups["Runners-Up"]
third_place = world_cups["Third"]
fourth_place = world_cups["Fourth"]

winners = winners.value_counts()
runners_up = runners_up.value_counts()
third_place = third_place.value_counts()
fourth_place = fourth_place.value_counts()

teams = pd.concat([winners, runners_up, third_place, fourth_place], axis=1)
teams = teams.fillna(0)
teams = teams.astype(int)
print(teams)

#Growth of the competition over time

gpg = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]
years= world_cups["Year"]

#Mapping average goals per game
fig, ax = plt.subplots()
ax.plot(years, gpg, linewidth=0.5, linestyle="--", marker="*")
ax.set(xlabel= "Year", ylabel = "Average Goals Per Game")
ax.set_xticks(years, minor=True)
ax.grid()
plt.xlim(1930, 2014)
#plt.show()

#Goals per tournament over time
sns.set_style("darkgrid")
sns.catplot(x="Year", y="GoalsScored", data=world_cups,
            kind="point", hue="GoalsScored", palette=sns.color_palette("flare", n_colors=17))
plt.xticks(rotation=55)
plt.show()

#Tournaments with average goals per game of 3 or higher
gpgyears = pd.concat([gpg, years], axis=1)
avg_goals_loc = gpgyears[gpgyears.iloc[:,0]>= 3]
avg_goals_loc = avg_goals_loc.round(decimals=1)
print(avg_goals_loc)

finals = matches[(matches["Stage"]=="Final")]
finals = finals.loc[:, ["Year", "Home Team Name", "Home Team Goals", "Away Team Name", "Away Team Goals"]]
finals = finals.drop_duplicates()
#print(finals)

finals_world_cups = world_cups.merge(finals, on="Year")
#print(finals_world_cups.head())
finals_goals = finals_world_cups["Home Team Goals"] + finals_world_cups["Away Team Goals"]
finals_goals = finals_goals.astype(int)
merged_years = finals_world_cups["Year"]
goals_per_final = pd.concat([merged_years, finals_goals], axis=1)

#goals_per_final = pd.concat([finals_goals, years], axis=1)
print(goals_per_final)
#gpgyears = pd.concat([gpg, years], axis=1)