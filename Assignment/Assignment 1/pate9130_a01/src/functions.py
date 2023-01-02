"""
------------------------------------------------------------------------
This is the function testing file.
------------------------------------------------------------------------
Author: Chetas Patel
ID:     200679130
Email:  pate9130@mylaurier.ca
__updated__ = "2021-09-16"
------------------------------------------------------------------------
"""


# t02.py
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    # Calculate if year is leap.
    if (year % 400 == 0):
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
        
    # Return
    return leap_year


# t02.py    
def list_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of the values
    in 2D list a.
    Use: small, large, total, average = list_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (list of lists of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    # Defining Variables.
    i = 0
    small = a[0]
    large = a[0]
    total = 0

    # Statement that determines small, large, total, and average.
    for i in range(len(a)):
        if a[i] <= small:
            small = a[i]
        if a[i] >= large:
            large = a[i]
        
        # Total the values in the list. 
        total = total + a[i]
    
    # Averages at the end of a for statement.
    average = total / len(a)   

    # Return Statement.
    return small, large, total, average


# t03.py
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0
    
    # 1st loop is for going thought all the values in list.
    while i < len(values):
        k = i + 1
        
        # 2nd loop is for comparing the k value to the i values in fist loop.
        while k < len(values):
            if values[k] == values[i]:
                values.pop(k)
            else:
                k += 1
        i += 1
    # Return Statement.         
    return


# t04.py
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    
    mb = 0
    
    for i in range(len(a) - 1):
        k = i + 1
        temp = a[i] - a[k]
        if temp < 0:
            temp = temp * -1
        if temp > mb:
            mb = temp
    
    return mb


# t05.py
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """

    b = []
    # Cols = range(len(a[0]))
    # Rows = range(len(a))

    # For loop to run through the matrix.
    for i in range(len(a[0])):
        temp = []
        # This loop checks all the values and places them in a temp list.
        for k in range(len(a)):
            temp.append(a[k][i])
        # Appends list to variable b.
        b.append(temp)

    # Return Statement.
    return b


# t06.py
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    # Declaring Variables.
    small = a[0][0]
    large = a[0][0]
    total = 0
    count = 0
    
    for i in range(len(a)):
        for k in range(len(a[i])):
            if a[i][k] <= small:
                small = a[i][k]
            if a[i][k] >= large:
                large = a[i][k]
            total += a[i][k]
            count += 1
            
    average = total / count
    
    # Return Statement.
    return small, large, total, average


# t07.py
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    # Declared Variables.
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0
    
    # Loop goes through each line in the file.
    for line in fv:
        test = line.strip()
        
        # Loop goes through all element in line.
        for i in range(len(test)):
            if test[i].isupper():
                u += 1
            elif test[i].islower():
                l += 1
            if test[i].isdigit():
                d += 1
            if test[i].isspace():
                w += 1
            r += 1
    
    # Return Statement.
    return u, l, d, w, r   

    
# t08.py
def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    # Declaring Variables.
    ns = ""
    rs = ""
 
    # Loops adds all alphabets in string.
    for i in s:
        if i.isalpha():
            ns += i
            
    # Lowers the string of characters.    
    ns = ns.lower()  
    
    # Reverses the loop and adds reversed values to string
    for k in range(len(ns) - 1, -1, -1):
        rs += ns[k]  
    
    # Return Statement.
    return rs == ns
    
