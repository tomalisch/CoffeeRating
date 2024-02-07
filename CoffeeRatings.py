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
mydb.close()

# Bargraph of data
ax = sns.barplot(dataCR, x='CoffeeName', y='Rating',facecolor='gray')
sns.stripplot(dataCR, x='CoffeeName', y='Rating', hue='RaterName')
handles, labels = ax.get_legend_handles_labels()
ax.legend( title='Rater', bbox_to_anchor=(1, 1.02), loc='upper left')
plt.setp( ax.xaxis.get_majorticklabels(), rotation=45, ha='right', rotation_mode='anchor' );

