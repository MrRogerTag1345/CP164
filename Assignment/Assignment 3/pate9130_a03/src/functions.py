"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-10-01"
------------------------------------------------------------------------
"""

from enum import Enum

from Stack_array import Stack

# Constants
OPERATORS = "+-*/"

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    
    target1 = Stack()
    target2 = Stack()
    switch = 0
    
    while source.is_empty() != True:
        if switch == 0:
            target1.push(source.pop())
            switch = 1
        else:
            target2.push(source.pop())
            switch = 0
    
    return target1, target2


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp = Stack()
    
    while source.is_empty() != True:
        temp.push(source.pop())    
    
    source = temp
    return source


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    lst = string.split(" ")
    temp_ans = 0.0
    answer = 0.0
    temp = Stack()
    
    for i in lst:
        
        if i in OPERATORS:
            value1 = temp.pop()
            value2 = temp.pop()
            if i == OPERATORS[0]:
                temp_ans = value1 + value2
            elif i == OPERATORS[1]:
                temp_ans = value2 - value1
            elif i == OPERATORS[2]:
                temp_ans = value1 * value2
            elif i == OPERATORS[3]:
                temp_ans = value2 / value1
            
            temp.push(temp_ans)
        else:
            temp.push(int(i))
        
    answer = temp.pop()
    return answer


def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
        
    temp = Stack()
    lst = string.split()
    i = string[0]
    n = 0
    
    if m not in lst:
        return MIRRORED.NOT_MIRROR
    
    for i in lst:
        if not ((i in valid_chars) or (i == m)):
            return MIRRORED.INVALID_CHAR
        
    while i != m:
        temp.push(lst.pop())
        n += 1
        i = string[n]
    
