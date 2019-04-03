"""
Taxi Fare

A module that implements a function to compute the fare of a taxi trip.
"""


# TODO: implement the compute_fare function.
# NOTE: Don't forget to write a nice docsring

def compute_fare(distance, duration, drop_charge=2.60):
    """
    Docstring for the function to calculate the price of a complet taxi run
    """
    distance_price = distance*2.70
    duration_price = duration*0.50
    final_price = distance_price + duration_price + drop_charge
    return float(final_price)