# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [100, 80, 60]
snack_names = ["yogurt", "watermelon", "peanuts"]
colors = ["#7CFC00","#7FFFD4","#FF69B4"]

plt.pie(snack_scores, labels=snack_names, colors=colors)

# Give your pie chart a title in the quotes
plt.title("Thais' favorite snacks", fontsize=22)

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("SnackVisual.png")
