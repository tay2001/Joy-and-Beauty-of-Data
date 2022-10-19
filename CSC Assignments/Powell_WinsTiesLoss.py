# --------------------------------------
# soccer seasons
# 
# taylor powell
# --------------------------------------

##function to process the score
def score(games, points, season):
    print("Season: " + str(season) + ", Games Played: " + str(games) +
          ", Points earned: " + str(points))
    print("Possible Win-Tie-Loss Records")
    print("-----------------------------")
    ##pass - replace it <-
    
    ##wins equation
    win = points // 3
    
    ##ties equation
    tie = points % 3
    
    ##losses are the remainder- from games minus losses and ties
    loss = games - win - tie

    ##while statement for while the wins and losses are not negative- esp. for season 4 in the orig
    while win >= 0 and loss >= 0:
        
        ##print the wins, ties, and losses with the - and as strings everytime
        print(str(win) + "-" + str(tie) + "-" + str(loss))

        ##while win or loss are greater than 0, to get other outcomes add three to ties
        ##while taking one from win and 2 from loss until they break the conditionals, not sure really how, but it works
        tie += 3
        win -= 1
        loss -= 2


##function to get the i(season basically) and sep games and points into sep lists
def get_seasons(seasons):
    
    ##cant use season, so i i guess as a counter
    i = 1
    
    ##get season 1, 2, ... i believe for loop is best? it works.
    for season in seasons:
        
        ##separate into separate lists: games played and points earned
        points = season[1]
        games = season[0]

        ##'season' counter
        i += 1
        
        ##throw them back into the score function 'i' functioning as 'season'
        score(games, points, i)
        

##main function to call everything, and to hold the list
def main():
   ##original list soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

    soccer_seasons = [[2, 3], [2, 4], [2, 6], [17, 17], [17, 24], [0, 0], [10, 2], [10, 3]]
    
    get_seasons(soccer_seasons)

# --------------------------------------

main()
