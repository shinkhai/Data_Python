"""
Warmup for the first exercice
"""


def main():

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # TODO: print out the length of days_in_month

    print(len(days_in_month))

    # TODO: print out the max value of days_in_month

    print(max(days_in_month))
    
    # TODO: print out the min value of days_in_month

    print(min(days_in_month))

    # TODO: use list indexing to determine the number of days in the 9th month
    #       and print it out

    print(days_in_month[8])

    # Here is a new list, a list of names
    names = ["Carol", "Albert", "Ben", "Donna"]

    # TODO: add Eugenia to the list of names

    names.append("Eugenia")
    print(names)

    # TODO: print out the names separated by "&" and spaces between each name
    # NOTE: You need to pass previous test for this to work
    
    print(" & ".join(names))

if __name__ == '__main__':
    main()
