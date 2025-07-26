# Import matplotlib library here
import matplotlib.pyplot as plt

# Let's rank some of our favorite snacks
snack_scores = [100, 80, 60]
snack_names = ["yogurt", "watermelon", "peanuts"]
               
plt.pie(snack_scores, labels=snack_names)

# Give your pie chart a title in the quotes
plt.title("Thais' favorite snacks")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("SnackVisual.png")
