# Taxi Fare
![](https://images.unsplash.com/photo-1532632575048-56f6211d0d36?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=21392184a07c04e51c0fbd5653b0e060&auto=format&fit=crop&w=1000&q=80)

In this assignment, you'll compute the price of a taxi. Let's check the [price
for a taxi in
Seattle](https://www.seattle.gov/your-rights-as-a-customer/file-a-complaint/taxi-for-hire-and-tnc-complaints/taxi-fares-how-much-does-a-ride-cost).  
For convenience, we've reproduced the fare table below:

| Taxi charges                                                                                                                                        |  Fare rate        |
|-----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
|  **Drop charge:** Applied as soon as you enter the taxi and accept a ride                                                                           | $2.60             |
| **Distance charge:** Applied once the taxi is travelling to your destination                                                                        | $2.70 per mile    |
| **Time charge:** Applied when the taxi stops or travels at slow speeds during the trip (for example, at red lights or in heavy stop-and-go traffic) |  $0.50 per minute |


## Guidelines
Implement a function called `compute_fare` that takes 3 arguments:
* `distance` in miles
* `duration` in minutes
* `drop_charge` in USD ($), this should be an optional argument with a default
  value (that can be found in the table).

## General tips
The docstring for the module is already written for you. Don't forget to write
a docstring for your function.

**During the live-programming tonight, we will
vote for the most compelling docstring.**

## Going further
Why did we use a default argument for `drop_charge`, how could we have done
otherwise? What are the pros of using a positional argument (also called
"keyword argument")?

What happens if we set a negative `distance` or negative `duration`? How will
your function react? Does your docstring actually say anything about this?
