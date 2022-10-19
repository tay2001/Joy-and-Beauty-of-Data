##taylor powell
##msu enrollment assignment

##imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

##main funct
def main(file_name):
    gtitle = file_name[:-4]
    
    # read the file_name into a pandas dataframe
    dataframe = pd.read_csv(file_name)
    xaxis= dataframe.columns[0]
    yaxis = dataframe.columns[1]
    
    # plot the dataframe using arguments "title", "legend", "x", "y", "kind" and "color"
    dataframe.plot(title=gtitle, x=xaxis, y=yaxis, kind="bar", \
            color=["blue", "gold"] * dataframe.size, legend=False)

    # The only four statements that may use the matplotlib library appear next.
    # Do not modify them.
    plt.xlabel(xaxis)      # Note: x-axis should be determined above
    plt.ylabel(yaxis)      # Note: y-axis should be determined above
    interactive(True)       # This allows multiple figures to be displayed simultaneously
    plt.show()

# -------------------------------------------------

##do em
main("MSU College Enrollments.csv")
main("CS Faculty.csv")
