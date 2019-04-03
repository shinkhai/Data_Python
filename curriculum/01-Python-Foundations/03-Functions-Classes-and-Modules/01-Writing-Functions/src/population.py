"""
lib.py
"""

def population_density(population, land_area):
    """ Return the population density from population and land_area.
    
    Args
    ----
    days: integer

    Returns
    -------
    a string
    """
    density = population / land_area

    if(density!=0):
        return density
    else:
        return False
