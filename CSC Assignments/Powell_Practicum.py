##programmer: taylor powell
##student grades(?)


##imports
import matplotlib.pyplot as plt
import numpy as np

##function to make the subplot
def subplot(plot, title, align):
    ##name the whole thing
    plt.figure("CSCI 127")
    ##make the ids 1-10
    ids = np.arange(1, 11)
    ##make the scores random 1-100
    scores = np.random.randint(0, 101, 10)

    ##use the given info to place the plot
    plt.subplot(1, 2, plot)

    ##label the x axis
    plt.xlabel("Student ID")

    ##set the axis values, then the xticks with the ids, and the yticks with the rande
    plt.axis([0.5, 10.5, 0, 100])
    plt.xticks(ids)
    plt.yticks(np.arange(0, 101, 10))

    ##set the title to the inserted title
    plt.title(title)
    ##make the graph
    plt.plot(ids, scores, align)
    ##make the 5th score me
    plt.text(5 - 0.2, scores[5-1] - 5, "me")


##call it in he
def main():
    ##plot 1
    subplot(1, "Practicum 1", "ro")
    ##only way to get the y label to work was here i guess?
    plt.ylabel("Score")
    ##plot 2
    subplot(2, "Practicum 2", "b^")
    ##show em
    plt.show()



main()
