from edgegraph import GraphEL, VertexEL, EdgeEL
from collections import Counter

def pld_graph(g: GraphEL):
    if g is None:
        raise ValueError("Bad graph")
    
    #  set of tuples so that they will not be duplicated
    found_palindromes = set()
    
    #  return empty if no tuples
    if not found_palindromes:
        return []

    return list(found_palindromes)

#  send the sequence into the helper function
def is_palindrome(s):
    #  check there are at least 3 edeg values
    if len(s) < 3:
        return False

    #  Check if the sequence is same both ways
    return s == s[::-1]
