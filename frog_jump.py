def frog_jump(length):
    """
    Given a given length of a river, find all posible ways a frog can jump from his position to the end of the river
    where the frog is able to jump either 1 foot or 2 feet

    We know there is only two ways the frog can jump from its current position that is either taking 1 foot or two feet
    This forms our base case.

    We also know from any position the frog reach there by either jumping 1 foot form the previous or 2 feet 
    from the position before that.
    
    """

    if length <= 2:
        return length
    else:
        return frog_jump(length-1) + frog_jump(length-2)