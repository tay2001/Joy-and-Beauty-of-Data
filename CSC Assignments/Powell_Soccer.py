# --------------------------------------
# Soccer seasons
# 
# taylor powell
# --------------------------------------

#string
import string

soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]


##split it
games = [i[1] for i in soccer_seasons]
points = [i[0] for i in soccer_seasons]

##make it an int to run not as list
points = [int(x) for x in points]

games = [int(x) for x in games]


##def proccess_season(season, games, points):
##    print("Season: " + str(season) + ", Games Played: " + str(games) +
##          ", Points earned: " + str(points))
##    print("Possible Win-Tie-Loss Records")
##    print("-----------------------------")
##    pass
##    print()

## --------------------------------------


def season(games,points):


    ties = 0
    wins = 0
    losses = 0

    
    points = [int(x) for x in points]

    games = [int(x) for x in games]

    x=games[0]
    y=points[0]
    print("yeet")
    i = 0
    for i in range(len(soccer_seasons)):
        for a in games:
            games[x] = games[x] - (a**3)
            ties = ties + (a**3)
        while games[x] >= 0:
            ##win if statement
            if(points[y] >= 3 and games[x] >= 0):
                points[y] = points[y] - 3
                wins = wins + 1
                games[x] = games[x] - 1
                    
                
                
                ##ties
            elif(points[y] >= 1 and games[x] >= 0):
                points[y] = points[y] - 1
                ties = ties + 1
                games[x] = games[x] - 1
                    
                
                
                ##losses  
            else:
                losses = losses + 1
                games[x] = games[x] - 1
                    

            ##add an if so it stps when there is no more games??
            if games[x] < 0 or points[y] < 0:
                print("fukin loser: " ,wins,'-',ties,'-',losses)
                break

            else:
                print(wins,'-',ties,'-',losses)
                break
                

def process():
    print("process")
    season(games,points)
    ##pass
                

# --------------------------------------

def main():
    # format of list: [[season-1-games, season-1-points], [season-2-games, season-2-points], etc.]
    soccer_seasons = [[1, 3], [1, 1], [1, 0], [20, 30]]

    ##split it to two lists so 
    games = [i[1] for i in soccer_seasons]
    points = [i[0] for i in soccer_seasons]

    ##make it an int to run not as list
    points = [int(x) for x in points]

    games = [int(x) for x in games]
    
    season(games, points)

# --------------------------------------

main()




