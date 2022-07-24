def getCount(d, n):
     
    no = n // d;
    result = no;
 
    # Consider all prime factors
    # of no. and subtract their
    # multiples from result
    for p in range(2, int(pow(no, 1 / 2)) + 1):
 
        # Check if p is a prime factor
        if (no % p == 0):
 
            # If yes, then update no
            # and result
            while (no % p == 0):
                no //= p;
                 
            result -= result // p;
 
    # If no has a prime factor greater
    # than Math.sqrt(n) then at-most one such
    # prime factor exists
    if (no > 1):
        result -= result // no;
 
    # Return the result
    return result;