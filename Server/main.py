import Server.visualization as visualize
import matplotlib.pyplot as plt

visualize.GraphVisualize("a000_office_temperature.csv", "Office Temperature")
visualize.GraphVisualize("a000_bed_temperature.csv", "Bedroom Temperature")
visualize.GraphVisualize("a000_living_temperature.csv", "Livingroom Temperature")
plt.show()

