# Grocery list
![](https://images.unsplash.com/photo-1509047095626-b35ae6c5bd3d?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=7b6c9a2d8e2b437681b3a6a05f682484&auto=format&fit=crop&w=1000&q=80)


## Objectives
In this module, you will learn to manipulate lists by building a program for
managing a grocery list.

## Guidelines

### 0. Data model
We will be managing a grocery list, as a list of tuple. Each tuple is a tuple
of (`quantity`, item). For example, if we've added 6 tomatoes and 4 bananas to
the list, it should be in this state:
```
[(6, 'tomatoes'), (4, 'bananas')]
```

### 1. Welcome message
When the program starts, you need to print out this message

```
"Welcome to Grocery list, "you can quit by typing 'quit' in the main menu"
```

### 2. Start prompting the user
First thing we ask the user what he want to do by prompting him with:
```
"What you wanna do (add/remove/sort/show)?\n")"
```


### 3. Quitting
When in the main menu (add/remove/sort/show), the user can quit the program by
typing `quit`.

### 4. Operations

#### `show`
Show the current list

#### `add`
This is the command to add items to the list. Prompt the user like this:
```
"Name of the item to add?\n"
```

```
"How many?\n"
```

If the item already exist in the list, you need to update its quantity. If if
does not, you'll need to add the item and its quantity as a tuple like this:
```python
# We've added 6 tomatoes to our grocery list
(6, 'tomatoes')
```

#### `remove`
If the item already exist in the list, you need to update its quantity, just
like the `add` function, but this time we remove.
If it doesn't, you need to tell the user doesn't exist in the list, for
example, if we tried to remove `bananas` while there weren't any in the list:
```
bananas is not in the list yet...
```


#### `sort`
This is the command when the user wants to see the list sorted by quantities,
in both ascending and descending order. We first prompt the user to know if he
wants it in ascending or descending with this:
```
"Descending? y/n\n"
```

if the user answer `y` (or `yes`), we print the grocery list sorted by
descending quantities.
Otherwise, we print the grocery list sorted by ascending quantities.

**[WARNING]**
When we print the sorted grocery list, the original list should stay the same.  
You can actually check this behavior by using the `show` command just before
and after the `sort` command and make sure that they're the same.


#### Invalid command
In case of invalid command, for example, if the user input `FOOBAR`, just print
out:
```
"*** Invalid command 'FOOBAR' ***\n"
```


## Going further
You can try implementing this with a `dict` instead of a list of tuples.
