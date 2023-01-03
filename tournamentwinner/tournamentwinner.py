def tournamentWinner(competitions, results):
    teamPoints=dict()
    for i in range(len(competitions)):
        if competitions[i][1 - results[i]] in teamPoints.keys():
            teamPoints[competitions[i][1 - results[i]]] += 3
        else:
            teamPoints[competitions[i][1 - results[i]]] = 3
    return max(teamPoints, key=teamPoints.get)

