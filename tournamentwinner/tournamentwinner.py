def tournamentWinner(competitions, results):
    teamPoints=dict()
    #loop through the competitions array objects
    for i in range(len(competitions)):
        #check the first match in competitions, and if the winner(1-results[i]) is in the dictionary, add 3 points, if not, set 3 points as base 
        if competitions[i][1 - results[i]] in teamPoints.keys():
            teamPoints[competitions[i][1 - results[i]]] += 3
        else:
            teamPoints[competitions[i][1 - results[i]]] = 3
    return max(teamPoints, key=teamPoints.get)

