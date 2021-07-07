Honors Project: Skip Lists
Macinze Knuth
=================

Skip Lists are particularly useful data structures for traversing a linked list 
without visting every Node. This works by building multiple layers, 
where the upper layers can be thought of as the express lane and the lowest
layer includes every node. 

I will  implementing a Skip List using a Singly Linked List design, in which a Node 
object consists of a value and a next pointer. The next pointer will be a list, and 
the list refers to the next node for each level.

The goal of this project is to learn the versatile, flexible, and practical
nature of Skip Lists, along with the operations and search algorithms which
make them so useful.


Assignment Specifications
-------------------------

### class Node: 

Represents a Node object, the building block of a Skip List.

***IMPLEMENT the following attributes/functions***

-   **Attributes**
    -   **value:**Value held by the Node
    -   **next: **A list of Nodes** which
        represents the towers or layers that each value is present in
-   **\_\_init\_\_(self, value: None, next: None) -\> None:**\
    -   Constructs a Node object
-   **\_\_repr\_\_(self) -\> str:**
    -   Represents the Node as a string for debugging
-   **\_\_str\_\_(self) -\> str:**
    -   Represents the Node as a string for debugging

### class Skip: 

Represents a Skip List object

***DO NOT MODIFY the following attributes/functions***

-   **Attributes**
    -   **head:**The left most, start Node of the Skip list
    -   **max\_height:** the height or layers of the skip list
-   **\_\_init\_\_(self) -\> None:**\
    -   Constructs an empty Skip List object

***IMPLEMENT the following functions***

-   **update(self, current, val, update=None) -\> Node:**
    -   Traverses through the skip list while keeping track of the levels to find the
        value searched for
    -   *Time Complexity: O(log n)*
    -   *Space Complexity: O(1)*
-   **search(self, val: str) -\> Node:**\
    -   Traverses through the list to find a value
    -   Returns None if no Node with value **val** exists, otherwise returns the Node
    -   *Time Complexity: O(log n)*
    -   *Space Complexity: O(1)*
-   **flip\_coin(self) -\> bool:**\
    -   Flips the coin to randomly determine if the height of the skip list should
        increase
    -   Returns bool, true if the height should increase, false otherwise
    -   *Time Complexity: O(1)*
    -   *Space Complexity: O(1)*
-   **random\_height(self) -\> int:**\
    -   Determines the height of the node by randomly flipping a coin
        Returns height, an int
    -   *Time Complexity: average O(log n)*
    -   *Space Complexity: O(1)*
-   **insert(self, val: str) -\> None:**
    -   Inserts the value into the skip list and returns None
        If the value is already in the list, do nothing
    -   *Time Complexity: O(log n)*
    -   *Space Complexity: O(n)*
-   **remove(self,val: str) -\> None:**
    -   Removes a node from the skip list and returns None
        if the value does not exist, do nothing
    -   *Time Complexity: O(log n)*
    -   *Space Complexity: O(n)*
-   **to\list(self) -\> List[int]:**
    -   Turns the bottom lane into a list for testing purposes, making sure the
        value was inserted or removed properly
    -   *Time Complexity: O(n)
    -   *Space Complexity: O(n)

Application Problem
-------------------

Even if you've never been to New York, everyone knows that the New York City 
subway system can be a challenge to navigate. It's very easy to get on the 
wrong lane, get off at the wrong stop, or head in the complete opposite 
direction. 

But, you just got hired as a software engineer at an up and coming 
tech company. Using your skills and knowledge learned from an
AMAZING undergrad class at MSU, you come up with a way to navigate the 
subway system lanes using Skip lists!

### Your Task

Given a list of stops, find the quickest path from a start location 
to a destination location.

-   **rush(self, start: str, end: str) -\> List:**
    -   Using the skip list, find the fastest route from the start
        location to the end location, switching lanes if needed.
    -   If the start or end locations are in the subway systems
        stops, return None
    -   *Time Complexity: O(log n)*
    -   *Space Complexity: O(n)*

### Example

**NYC subway system stops according to the MIT lecture**
stops = [14, 23, 34, 42, 50, 59, 66, 72, 79, 86, 96, 103, 110, 116, 125]
Here are the stops in one of the lines on the NYC subway system
However, instead of riding through each of these stops, you can
hop on different lanes to get to your destination faster.

L3:         23                                                               None

L2:         23                                      103  110        125      None

L1:         23                      72              103  110        125      None 

L0:     14  23  34  42  50  59  66  72  79  86  96  103  110  116   125      None


-   **skip.rush(12, 23)** would return
    -   None because the start location doesn't exist
-   **skip.rush(14, 331)** would return
    -   None because the end location doesn't exist
-   **skip.rush(14, 72)** would return
    -   [14, 23, 72] because that is the quickest path (using the random.seed(331))
-   **skip.rush(34, 110)** would return
    -   [34, 42, 50, 59, 66, 72, 103, 110] because that is the quickest path (using the random.seed(331))

