import Server.visualization as visualize
import matplotlib.pyplot as plt
import Server.power_statistics as ps

ps.PowerCalculations()
visualize.GraphVisualize("a000_living_temperature.csv", "Living Temperature")
visualize.GraphVisualize("a000_office_temperature.csv", "Office Temperature")
plt.show()


