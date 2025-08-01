import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Standardizes currency to USD values so that we can better compare results
def format_currency(dataset):
  url = "https://api.exchangerate-api.com/v4/latest/USD"

  # Requests data from API
  response = requests.get(url)
  data = response.json()

  def convert_currency(row):
    rate = data["rates"][row["Unit Code"]]
    return row["Value"] / rate

  for index, row in dataset.iterrows():
    dataset.at[index,"Unit Code"] = "USD"
    dataset.at[index,"Value"] = convert_currency(row)
  return dataset


# ADD CODE: Pandas dataframes
wage = pd.read_csv("wage.csv", delimiter=",")
happiness = pd.read_csv("happiness.csv", delimiter=",")

wage_usd = format_currency(wage)
#print(wage_usd)
wage_and_happiness = wage.merge(happiness)
#print(wage_and_happiness)

wage_and_happiness_by_country = wage_and_happiness.groupby("Country")
#print(wage_and_happiness_by_country)


wage_average_per_country = wage_and_happiness_by_country["Value"].mean()
happiness_average_per_country = wage_and_happiness_by_country["Happiness score"].mean()

#Scatterplot

fig=sns.scatterplot(x="Value", y="Happiness score", hue="Happiness score", size="Happiness score", sizes=(20,180), data=wage_and_happiness)
plt.xlabel("Annual Salary of full-time workers in USD")
plt.ylabel("Happiness Score of Citiznes")
plt.title("Annual Salary vs Happiness Score")
fig.set_facecolor("#E5E5E5")
plt.savefig("Wage_vs_Happiness.png")




#print(f"Countries with highest average wage: {wage_average_per_country.nlargest(10)}\n\n")
#print(f"Countries with smallest average wage: {wage_average_per_country.nsmallest(10)}\n\n")

#print(f"Countries with highest happiness: {happiness_average_per_country.nlargest(10)}\n\n")
#print(f"Countries with smallest happiness: {happiness_average_per_country.nsmallest(10)}\n\n")