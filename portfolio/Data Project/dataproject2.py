'''

3.2.7 Data Project

By: Diego Santiago & Wesley Chan

How is the overall increase in car fuel efficiency correlated to the decrease in pollutants in America?

Our program shows a scatterplot depicting the amount of carbon emissions, which is the primary gas expelled from cars, 
from the past 25 years starting in 1990.  The outcome displayed a trend with the peak of the carbon emissions between 
the years 2005 and 2007 which happens to be right before the production of electric vehicles. After 2007,
the carbon emissions fell due to the integration of electric vehicles, and air efficient transmission.  

Data Retrieved From:
https://www3.epa.gov/climatechange/ghgemissions/inventoryexplorer/#transportation/all

'''

#IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import os.path


# This imports the data file from the direct location on the computer and scans it with 'readlines'
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'data1.csv')
datafile = open(filename)
data = datafile.readlines()


# The x-axis
year_list = []
# The y-axis
carbon_dioxide_list = []
#Goes through each line in data file and seperates each value by commas
for line in data[1:]:
    
    year, carbon_dioxide = line.split(',')
    year_list.append(float(year))
    carbon_dioxide_list.append(float(carbon_dioxide))

#Creates scatter plot with title and axis labels
plt.scatter(year_list, carbon_dioxide_list, s=20, c= 'b' , alpha=1)
plt.suptitle('CO2 Emissions Over the Years within the United States', fontsize = 15, )
plt.xlabel('Years')
plt.ylabel('Emissions (million metric tons of \n carbon dioxide equivalents)')
plt.xlim (1989,2016)

#Adds arrow to indicate where the rise of electric vehicles begin
plt.annotate('Rise in electric\nvehicles', xy=(2008, 1869), xytext=(2010, 1914),
            arrowprops=dict(facecolor='red', shrink=0.05))
            
plt.show()