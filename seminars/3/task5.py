# Write a function unpack that unpacks a list of elements that can contain objects (int, str, list, tuple, dict, set) within each other without any predefined depth, meaning that there can be many levels of elements contained in one another.
# Example:
# unpack([None, [1, ({2, 3}, {'foo': 'bar'})]]) == [None, 1, 2, 3, 'foo', 'bar']
# Note: you don't have to bother about the order of the elements, espesially when unpacking a dict or a set. Just unpack all the elements.

def unpack(lst):
    unpacked = []
    for i in lst:
        if isinstance(i, (list, set, tuple)):
            element = unpack(i)
        elif isinstance(i, dict):
            element =unpack(i.items())
        else:
            element = [i]
        unpacked += element
    return unpacked

lst = [None, [1, ({2, 3}, {'foo': 'bar'})]]
print(unpack(lst))