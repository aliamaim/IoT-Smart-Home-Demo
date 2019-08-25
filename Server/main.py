import Server.visualization as visualize
import matplotlib.pyplot as plt
import Server.power_statistics as ps

ps.PowerCalculations()
visualize.GraphCreate("a000_living_temperature", "Living Temperature")
visualize.GraphCreate("a000_office_temperature", "Office Temperature")
plt.show()
