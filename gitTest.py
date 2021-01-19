import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame

#Importing CSV files into Pandas Dataframe
world_cups = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCups.csv")
matches = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCupMatches.csv")
players = pd.read_csv(r"C:\Users\Acer Swift 5\PycharmProjects\pythonProject\archive\WorldCupPlayers.csv")

#Data Cleaning: Dropping Null values
world_cups = world_cups.dropna()
matches = matches.dropna()
players = players.dropna()

#Data Cleaning: Amending country names
world_cups["Winner"] = world_cups["Winner"].str.replace("Germany FR","Germany")
world_cups["Runners-Up"] = world_cups["Runners-Up"].str.replace("Germany FR","Germany")
world_cups["Third"] = world_cups["Third"].str.replace("Germany FR","Germany")
world_cups["Fourth"] = world_cups["Fourth"].str.replace("Germany FR","Germany")
world_cups["Fourth"] = world_cups["Fourth"] = world_cups["Fourth"].str.replace("Soviet Union","Russia")
matches["Home Team Name"] = matches["Home Team Name"].str.replace('rn">United Arab Emirates',"United Arab Emirates")
matches["Home Team Name"] = matches["Home Team Name"].str.replace("C�te d'Ivoire","Côte d’Ivoire")
matches["Home Team Name"] = matches["Home Team Name"].str.replace('rn">Republic of Ireland',"Republic of Ireland")
matches["Home Team Name"] = matches["Home Team Name"].str.replace('rn">Bosnia and Herzegovina',"Bosnia and Herzegovina")
matches["Home Team Name"] = matches["Home Team Name"].str.replace('rn">Serbia and Montenegro',"Serbia and Montenegro")
matches["Home Team Name"] = matches["Home Team Name"].str.replace('rn">Trinidad and Tobago',"Trinidad and Tobago")
matches["Home Team Name"] = matches["Home Team Name"].str.replace("Soviet Union","Russia")
matches["Home Team Name"] = matches["Home Team Name"].str.replace("Germany FR","Germany")
matches["Away Team Name"] = matches["Away Team Name"].str.replace('rn">United Arab Emirates',"United Arab Emirates")
matches["Away Team Name"] = matches["Away Team Name"].str.replace("C�te d'Ivoire","Côte d’Ivoire")
matches["Away Team Name"] = matches["Away Team Name"].str.replace('rn">Republic of Ireland',"Republic of Ireland")
matches["Away Team Name"] = matches["Away Team Name"].str.replace('rn">Bosnia and Herzegovina',"Bosnia and Herzegovina")
matches["Away Team Name"] = matches["Away Team Name"].str.replace('rn">Serbia and Montenegro',"Serbia and Montenegro")
matches["Away Team Name"] = matches["Away Team Name"].str.replace('rn">Trinidad and Tobago',"Trinidad and Tobago")
matches["Away Team Name"] = matches["Away Team Name"].str.replace("Germany FR","Germany")
matches["Away Team Name"] = matches["Away Team Name"].str.replace("Soviet Union","Russia")

matches.dropna(subset=["Year"], inplace=True)

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
print(teams)

#Comparison of 1930 World Cup and 2014 World Cup
First_Last = world_cups.iloc[[1,-1],[0,2,6,8]]

#Growth of the competition over time
GoalsPerGame = (world_cups.loc[ :, ["Year", "QualifiedTeams", "MatchesPlayed", "GoalsScored"]])

#Goals per tournament over time
sns.set_style("darkgrid")
sns.set_palette("Blues")
sns.catplot(x="Year", y="GoalsScored", data=world_cups,
            kind="point", hue="GoalsScored")
plt.xticks(rotation=45)