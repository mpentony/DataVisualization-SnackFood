import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r",) as csvfile:
  tips=pd.read_csv(csvfile, delimiter=",")

tips_pivoted=tips.pivot_table(values="tip", index="size", columns="time")

fig=sns.heatmap(tips_pivoted, annot=True, cmap="Spectral")
fig.set_ylim(6,0)

plt.xlabel("Time of day")
plt.ylabel("Group size")
plt.title("Tip amount by group size and time of day")
plt.savefig("heatmap.png")

