# Defining functions

Open the `lib` file in the `src` directory and implement the `TODOs`.

## Functions

### 1. `population_density`
Write a function named `population_density`. The function should have two
arguments, `population` and `land_area` and return the population density.

```python
population_density(10, 1)
>>> 10

population_density(864816, 121.4)
>>> 7123.6902801
```

### 2. `readable_timedelta`
Write a function named `readable_timedelta`. The function should have one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:

```python
readable_timedelta(10)
>>> 1 week(s) and 3 day(s).
```

## Bonus
_This bonus is not part of the tests but **it should not take you too long** if
you understood what are scripts and imports._
Implement a script that call both of your functions within its `main()` and
print out the results when executed (just use some random values).
