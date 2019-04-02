#!/usr/bin/env python3
# TODO: Write a docstring
"""
This is a docstring to add a description

"""
def main():
    # TODO: input for name: name

    name = input()

    # TODO: input for height in centimeters: height

    height = input()

    # TODO: input for weight: weight

    weight = input()

    # TODO: compute the BMI: bmi

    bmi = weight / (height/100)**2

    # TODO: print a greeting to the user followed by it's BMI
    # Example: "Hello Georges, your BMI is 26.75!"

    print("Hello %s, your BMI is %s"%(name,bmi))

if __name__ == '__main__':
    main()
