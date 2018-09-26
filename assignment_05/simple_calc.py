# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:   
Copyright 2018 <Charles Walker Grimes>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will 
  - Take in two numbers from the user
  - Take in an operator from the user
  - Perform the mathematical operation and provide the number to the user
  - Repeat

Operations:
  - addition
  - subtraction
  - multiplication
  - division
  - multiplication
  - left bit shift
  - right bit shift
  - modulo

Error conditions:
  - Invalid operator --> Program should exit
  - Invalid number   --> Program should exit
  
Note on shifts:
    If either number is a float, the program will round the number to the
    nearest integer before performing either a left or right shift
    
This program is compatible with both Python 2 and Python 3

--------------------------------------------------------------------------
"""
# ------------------------------------------------------------------------
# Libraries
# ------------------------------------------------------------------------
import operator
import six
# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------


# ------------------------------4.5------------------------------------------
# Global variables
# ------------------------------------------------------------------------
operators = {
    "+"      : operator.add,
    "-"      : operator.sub,
    "*"      : operator.mul,
    "/"      : operator.truediv,
    "lshift" : operator.lshift,
    "rshift" : operator.rshift,
    "mod"    : operator.mod,
    "^"      : operator.pow
}

# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------
def get_user_input():
    try:
        number1 = float(six.moves.input("Enter the first number:  "))
        op      = six.moves.input("Enter an operator(Valid operators are +,-,*,/,^,lshift,rshift,mod): ")
        number2 = float(six.moves.input("Enter the second number: "))
        
        return(number1, op, number2)
        
    except:
        print("Invalid Input")
        return(None, None, None)
        
   

# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

if __name__ == "__main__":
    while True:
        
        (number1, op, number2) = get_user_input()
        print(number1)
        print(op)
        print(number2)
        
        func = operators.get(op, None)
    
        if(number1 is None) or (number2 is None) or (func is None):
            print("Quitting.")
            break
        elif(op == "lshift") or (op == "rshift"):
            number1 = int(round(number1))
            number2 = int(round(number2))
            print(func(number1,number2))
        else:
            print(func(number1,number2))
    
    
