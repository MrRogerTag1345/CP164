"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-24"
------------------------------------------------------------------------
"""

# Import Class
from Stack_array import Stack


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        temp = source.pop()
        stack.push(temp)
    
    return

        
def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not stack.is_empty():
        temp = stack.pop()
        target.insert(0, temp)
        
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    stack = Stack()
    
    print("Testing Source")
    print("-"* 60) 
    
    empty = stack.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 
    
    stack.push(source[0])
    print("Testing push:")
    print("Result: {}".format(stack))
    print("Testing peek:")
    print("Result: {}".format(stack.peek())) 
    empty = stack.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting False)".format(empty))
    print("-"* 60) 
    
    print("Testing pop")
    print("Result: {}".format(stack.pop()))
    
    empty = stack.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 
    
    return
    
