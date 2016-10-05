#!/usr/bin/env python3

import sys

def euclidean_GCD( a, b ):
    """Calculates the Greatest Common Denominator of two integers using
    the Euclidean algorithm.
    
    Arguments should be integers.
    """
    return +a if ( b == 0 ) else euclidean_GCD( b, a%b )


def extended_euclidean( a, b ):
    """
    """
    return NotImplemented

if __name__ == "__main__":
    
    a, b = 0, 0
    
    # if there are two args, use them for a and b
    # else take input
    if len(sys.argv) == 3:
        a, b = sys.argv[1:3]
        
    else:
        a = input("Enter an integer value for a: ")
        b = input("Enter an integer value for b: ")
    
    # Integer-ize a and b, watch for exceptions
    try:
        a, b = int(a), int(b)
    
    except ValueError:
        print("\nERROR: Arguments should be integers.")
        exit(1)
    
    # Output the results
    print("The GCD of a and b is:", euclidean_GCD(a, b))
    print("The linear combination of GCD(a,b) is:", extended_euclidean(a, b))
