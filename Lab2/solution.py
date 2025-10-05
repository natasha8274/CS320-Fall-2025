def findKey(k, t):
    if t is None:
        raise ValueError("no tree")
    if k is None:
        raise ValueError("null key")
    i = 0
    while i < len(t):
        if t[i] is None:
            break
        if k == t[i]:
            return i
        try:
            if k < t[i]:
                i = (i * 2) + 1
            else:
                i = (i * 2) + 2
        except TypeError:
            raise Exception("tree error")
    raise LookupError("not in tree")


def addKey(k, t):
    if t is None:
        raise ValueError("no tree")
    if k is None:
        raise ValueError("null key")

    i = 0
    if len(t) == 0:
        return [k]

    while i < len(t):
        if t[i] is None:
            t[i] = k
            break
        elif k == t[i]:
            break
        try:
            if k < t[i]:
                i = (i * 2) + 1
            else:
                i = (i * 2) + 2
        except TypeError:
            raise Exception("tree error")
    return t


def deleteKey(k, t):
    if t is None:
        raise ValueError("no tree")
    if k is None:
        raise ValueError("null key")

    i = 0

    if len(t) == 1 and t[0] == k:
        return []
    #  when there is only k in the tree
    while i < len(t):
        if t[i] is None:
            raise LookupError("not in tree")
        if k == t[i]:
            left_child = (i * 2) + 1
            right_child = (i * 2) + 2
            l_exists = left_child < len(t) and t[left_child] is not None
            r_exists = right_child < len(t) and t[right_child] is not None
            #  for 0 children
            if not l_exists and not r_exists:
                t[i] = None
                #  for 1 child
            elif l_exists and not r_exists:
                t[i] = t[left_child]
                t[left_child] = None
            elif r_exists and not l_exists:
                t[i] = t[right_child]
                t[right_child] = None
            #  for 3 children
            elif l_exists and r_exists:
                successor_i = _iOILeft(right_child, t)
                if successor_i is None:
                    successor_i = right_child
                t[i] = t[successor_i]
                t[successor_i] = None
            return trim(t)
            #  trim the list so no none values
        elif k < t[i]:
            i = (i * 2) + 1
        elif k > t[i]:
            i = (i * 2) + 2
    raise LookupError("not in tree")


def _iOILeft(n, t):
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
        prev = i
        i = (i * 2) + 1
    return prev if (prev != n) else None


#  helper method to trim
def trim(t):
    while t and t[-1] is None:
        t.pop()
    return t
