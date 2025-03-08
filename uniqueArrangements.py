"""
This script calculates the number of unique arrangements (permutations with repetition) 
of elements distributed across multiple subsets of given sizes.

Functions:
    - fact(n): Computes the factorial of a given number `n`.
    - perm_rep(mj): Computes the number of unique permutations with repetition 
      based on subset sizes.
    - uimulti_set(): Interactively collects user input to define subset sizes 
      within specified constraints.

Usage:
    1. The user provides the number of subsets (between 3 and 8).
    2. The user defines the size of each subset (between 1 and 5).
    3. The user inputs the total number of arrangements (though this value is 
       not utilized in the calculation).
    4. The script calculates and prints the number of unique arrangements using 
       the perm_rep function.
"""

def fact(n):
    """
    Computes the factorial of a given number `n`.

    Args:
        n (int): The number for which factorial is to be computed.
    
    Returns:
        int: The factorial of `n`.
    """
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

def perm_rep(mj):
    """
    Computes the number of unique permutations with repetition, 
    given a multiset of sizes `mj`.

    Args:
        mj (list of int): A list containing the sizes of subsets.
    
    Returns:
        int: The number of distinct arrangements.
    """
    n = 0 
    divisor = 1 
    for mi in mj:
        n += mi
        divisor *= fact(mi)
    return fact(n) // (fact(n -k) * divisor)

def uimulti_set():
    """
    Collects user input to define the multiset structure.
    
    The user provides the number of subsets (between 3 and 8) and 
    the size of each subset (between 1 and 5).
    
    Returns:
        list: A list containing the sizes of subsets.
    """
    ms = []
    
    while True:
        try:
            j = int(input("Enter number of subsets that is no less that 3 or greater than 8:"))
        except: 
            print("Please enter a valid input")  
        if j not in range(3,9):
            print("Please enter a vaild number")
        else:
            break

    for i in range(0, j):
         
        while True:
            try:
                ele = int(input("Enter the size of each subset between 1 and 5: "))
            except: 
                print("Please enter a valid input")  
            if ele not in range(1,6):
                print("Please enter a vaild number")
            else:
                break
        ms.append(ele)
    return (ms)

# Collect user input for multiset sizes
mj = (uimulti_set())
# Get user input for the total number of arrangements (not used in calculation)
k = int(input("please enter the total number of arrangements: ")) 
# Calculate and display the number of unique arrangements
print("Given your inputs, the number of arrangements is" , perm_rep(mj))









