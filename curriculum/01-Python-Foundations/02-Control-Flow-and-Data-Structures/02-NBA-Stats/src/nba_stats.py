#!/usr/bin/env python3
# TODO: Write a docstring
"""
This is the 2nd exercice
"""

def main():
    players = [
        'Anthony Davis', 'LeBron James', 'James Harden', 'DeMarcus Cousins',
        'Damian Lillard', 'Stephen Curry', 'Devin Booker', 'Russell Westbrook'
    ]
    points = [28.1, 27.5, 30.4, 25.2, 26.9, 26.4, 24.9, 25.4]

    # TODO: print out the total number of points
    # Example:
    # "Total number of points: 34.3"

    total = sum(points)

    print("Total number of points: " + str(total))

    # TODO: print out the player with the biggest average points
    # Example: "Best player: Damian Lillard"

    cl = list(zip(points, players))
    cl.sort(reverse=True)
    print("Best player: " + cl[0][1])

    # TODO: print out the list of players ordered by descending points
    NewList = []
    for i in range (len(cl)):
        NewList.append(cl[i][1])
    print(NewList)

if __name__ == '__main__':
    main()
