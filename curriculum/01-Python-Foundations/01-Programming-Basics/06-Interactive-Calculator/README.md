# Interactive calculator
![](https://images.unsplash.com/photo-1523359366921-4c14294ff5bd?ixlib=rb-0.3.5&s=934851b96243529b57ab7740e6484289&auto=format&fit=crop&w=1000&q=80)

## Objectives
* Develop a better undestanding of arithmetic operators
* Improve your control flow with `while` loops, `break` and `continue` statements

## Guidelines
In this module, we will implement an interactive calculator. It will support operations: `+`, `-`, `*`, `/`, `%`, `//` and `**`.


**This is what we're going to build, a command line interface (CLI) calculator:**
```
Welcome to Calculator, you can quit anytime by typing 'quit'
Pick an operator (+, -, *, /, //, %): /
First number: 83732
Second number: 765
The result is: 109.45359477124182
------------------------------
Pick an operator (+, -, *, /, //, %): quit
Quitting...
```

### 1. Hello message
This is the easy part: when your program launches it should alert the user that it launched by saying hello.
This is the message you need to implement.
```
Welcome to Calculator, you can quit anytime by typing 'quit'
```

### 2. Prompting
Your program should continuously prompt for 3 things.
1. The **operator** with this message:
```
`Pick an operator (+, -, \*, /, //, %): 
```
2. The **first\_number** with this message:
```
First number: 
```
3. The **second_number** with this message:
```
Second number: 
```
_**N.B.**: Do not forget the spaces after `:`_ 😉

### 3. Quitting
Users should be able to quit the program at any time by simply typing `'quit'`.
When they do, you should print out `Quitting...` and then shutdown the program.

### 4. Handling invalid operators
Only 7 operators are valid, if an invalid operator in given by the user, you should warn them it's invalid by displaying this message:
```
Sorry, 'invalid' is not a valid operator.
```

## General tips
1. Implement
2. ?
3. Profit


## Improvements
What could you do to improve your program?  
If you got the time, **implement your ideas and show us during the evening live code!**

---

Good luck and have fun!
