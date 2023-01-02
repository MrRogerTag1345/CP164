"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-10-11"
------------------------------------------------------------------------
"""

# Import Class
from List_array import List
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue 
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
 
# Queue_array    
#----------------------------------------------------------------------


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        queue.insert(source.pop(0))
        
    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        target.append(queue.remove())

    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand
    
    print("Testing Source")
    print("-"* 60) 
    
    empty = q.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 
    
    q.insert(a[0])
    print("Testing push:")
    print("Result: {}".format(q))
    print("Testing peek:")
    print("Result: {}".format(q.peek())) 
    empty = q.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting False)".format(empty))
    print("-"* 60) 
    
    print("Testing pop")
    print("Result: {}".format(q.remove()))
    
    empty = q.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 

    return

# Priority_Queue
#-------------------------------------------------------------------------


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        pq.insert(source.pop(0))
    
    return
    

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        target.append(pq.remove())
        
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    print("Testing Source")
    print("-"* 60) 
    
    empty = pq.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 
    
    pq.insert(a[0])
    print("Testing push:")
    print("Result: {}".format(pq))
    print("Testing peek:")
    print("Result: {}".format(pq.peek())) 
    empty = pq.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting False)".format(empty))
    print("-"* 60) 
    
    print("Testing pop")
    print("Result: {}".format(pq.remove()))
    
    empty = pq.is_empty()
    print("Testing is_empty:")
    print("Result: {} (Expecting True)".format(empty))
    print("-"* 60) 
    return

# List
#--------------------------------------------------------------------------


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source != []:
        temp = source.pop(0)
        llist.append(temp)
    
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not llist.is_empty():
        temp = llist.pop(0)
        target.append(temp)
        
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    array_to_list(lst, source)
    key = lst[2]
    
    print("Testing is_empty, Expecting {}".format(lst.is_empty()))
    print()  
    print("Other Testing: ") 
    print() 
    print("Insert: {}\n".format(lst.insert(2, key)))
    print("Remove: {}\n".format(lst.remove(key)))
    print("Count: {}\n".format(lst.count(key)))
    print("Append: {}\n".format(lst.append(key)))
    print("Index: {}\n".format(lst.index(key)))
    print("Find: {}\n".format(lst.find(key)))
    print("Max: {}\n".format(lst.max()))
    print("Min: {}\n".format(lst.min()))

    return
