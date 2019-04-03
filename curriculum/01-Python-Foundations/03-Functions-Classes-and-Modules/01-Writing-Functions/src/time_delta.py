"""
Timedelta
"""


# TODO: implement readable_timedelta
def readable_timedelta(days):
    """
    doctype de la fonction
    """
    weeks = int(days / 7)
    nb_days = int(days % 7)
    
    return str(weeks) + " week(s) and " +str(nb_days)+ " day(s)"
    