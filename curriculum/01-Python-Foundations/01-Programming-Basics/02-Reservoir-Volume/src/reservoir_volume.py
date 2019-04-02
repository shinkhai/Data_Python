#!/usr/bin/env python3
"""
A simple program to compute reservoir volume

"""


def main():
    # The current volume of a water reservoir (in cubic metres)
    reservoir_volume = 4.445e8
    # The amount of rainfall from a storm (in cubic metres)
    rainfall = 5e6

    # TODO: decrease the rainfall variable by 10% to account for runoff

    rainfall = rainfall * 0.9

    # TODO: add the rainfall variable to the reservoir_volume variable

    reservoir_volume = reservoir_volume + rainfall

    # TODO: increase reservoir_volume by 5% to account for stormwater that
    # flows into the reservoir in the days following the storm

    reservoir_volume = reservoir_volume * 1.05

    # TODO: decrease reservoir_volume by 5% to account for evaporation

    reservoir_volume = reservoir_volume*0.95

    # TODO: subtract 2.5e5 cubic metres from reservoir_volume to account for
    # water that's piped to arid regions.

    reservoir_volume = reservoir_volume - 2.5e5

    # TODO: print the new value of the reservoir_volume variable

    print(reservoir_volume)

if __name__ == '__main__':
    main()
