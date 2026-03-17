# Append vs Extend

- Append() adds a single element to the end of a list.
- Extend() adds each element of another iterable to the end of a list.

|Feature|append()|extend()|
|-------|--------|--------|
|purpose|Adds one element|Adds multiple elements|
|input|single item(any type)|iterable(list,tuple,etc.)|
|effect on list|Adds item as one whole element|Adds each elementindividually|
|list structure|May create nested list|Keeps list flat|
|syntax|`list.append(x)`|`list.extend(iterable)`|
|time complexity|O(1)|O(n)|

