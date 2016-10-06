#!/usr/bin/env python3

import sys

def euclideanGCD( a, b ):
    """Calculates the Greatest Common Denominator of two integers using
    the Euclidean algorithm.
    
    Arguments should be integers.
    Returns GCD(a,b)
    """
    return abs(a) if ( b == 0 ) else euclideanGCD( b, a%b )


def extendedEuclidean( a, b ):
    """Calculate the GCD and linear combination of two integers using
    the Extended Euclidean algorithm.
    
    Arguments should be integers.
    Returns (r,s,t) such that (r = a*s + b*t)
    """
    
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = int(b), int(a)
    
    while r:
        quotient = old_r // r #integer division
        old_r, r = r, (old_r - quotient*r)
        old_s, s = s, (old_s - quotient*s)
        old_t, t = t, (old_t - quotient*t)
    
    return (old_r, old_s, old_t)

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
    print("The GCD of a and b is:", euclideanGCD(a, b))
    print("The linear combination of GCD(a,b) is: " \
          "{2[0]} = {0}*{2[1]} + {1}*{2[2]}".format( a, b, 
                                    extendedEuclidean(a, b))
         )
