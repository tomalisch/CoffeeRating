## Dependencies
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
##

# Connect to mySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  database='dbCoffee'
)

# Create dataframe of all entries and close mySQL database connection
query = "Select * FROM CoffeeRatings;"
dataCR = pd.read_sql(query, mydb)
query = "Select * FROM CoffeeStats;"
dataCS = pd.read_sql(query, mydb)
mydb.close()

# Bargraph of ratings on coffee, rater as legend
plt.figure()
ax = sns.barplot(dataCR, x='CoffeeName', y='Rating',facecolor='gray')
sns.stripplot(dataCR, x='CoffeeName', y='Rating', hue='RaterName')
handles, labels = ax.get_legend_handles_labels()
ax.legend( title='Rater', bbox_to_anchor=(1, 1.02), loc='upper left')
plt.setp( ax.xaxis.get_majorticklabels(), rotation=45, ha='right', rotation_mode='anchor' );

# Scatter plot of mean Rating on Price (per 2lb), dots scaled by number of individual ratings
plt.figure()
ax = sns.scatterplot(dataCS, x='Price', y='mRating', s=np.array(dataCS.nRatings)*50,hue='CoffeeName',legend='brief')
handles, labels = ax.get_legend_handles_labels()
ax.legend( title='Coffee', bbox_to_anchor=(1, 1.02), loc='upper left');


