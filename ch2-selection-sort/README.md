# Selection Sort

- [Selection Sort](#selection-sort)
  - [How memory works](#how-memory-works)
  - [Arrays and Linked Lists](#arrays-and-linked-lists)
    - [Array](#array)
    - [Linked Lists](#linked-lists)
    - [Operation run times](#operation-run-times)
    - [Inserting into the middle of a list](#inserting-into-the-middle-of-a-list)
    - [Deletion](#deletion)
  - [Selection Sort](#selection-sort-1)
  - [Recap](#recap)

## How memory works

This can be done with an analogy of a set of drawers where you wish to store some of your own items. Each drawer can hold a single element, if you want to store 3 things, you need to ask to use 3 drawers.

A computer can be a giant set of drawers, each drawer has an address, this address is a slot of memory. Each time you want to store an item, you are asking the computer for some space and it provides you an address where an item can be stored. When you are storing multiple items, there are 2 basic ways to do this: an array or a linked list.

## Arrays and Linked Lists

Sometimes you need to store a list of elements in memory, such as with a `to-do` application, all of the items, the *todo's*, will be stored as a list in memory.

*How do you choose to do this with an array or a linked list?*

### Array

Using an array will mean that each task is stored contiguously, i.e. next to each other, in memory.

This means we could store them nicely together, but suppose that the next one along in your drawers is taken by somebody else. This causes a dilemma, as if you wish to store everything together, you are required to move all of the items into another contiguous memory block where all of the items now sit together. In the case of a computer, assuming you have 3 items and want to add another, you would need to find a block of memory with 4 spaces available and then move every item there - consider what happens if this occurs again. Everytime you are out of space, you need to move to another block in memory, making adding new items rather slow.

An easy fix to this could be to hold blocks of memory, even if you only have 3 tasks at the moment, you could ask the computer for 10 slots, just in case. This is a fine workaround, but you must consider the following:

* You may not need those extra slots which you have asked for, meaning that memory is being wasted which could otherwise be used.
* If more than 10 items are added to the list, you are going to need to move them all again anyway.

Linked lists solve the issue of adding items.

### Linked Lists

When using linked lists, an item can be anywhere in memory, this is because each item stores the address of the next one in the list. This means that a bunch of random memory addresses are linked together.

Adding an item to a linked list is relatively simple, you can add it anywhere and then store the address of where you put it in the previous item. They are not required to be stored together, you also do not have to move your items.

However, they have their own drawbacks. You cannot simply check any element at random, you do not know its address. This means you must traverse the list to find it, you start at the first item and move through in sequence. Meaning that if you are wanting to read the items all at once each time, this is great, but if you want to jump around and access them in different ways, linked lists are not so good - this is where arrays are better, you have direct access to any element via its index.

### Operation run times

Arrays:
* Reading - `O(1)`
* Insertion - `O(n)`
* Deletion - `O(n)`

Linked lists:
* Reading - `O(n)`
* Insertion - `O(1)`
* Deletion - `O(1)`

`O(1)` is constant time.
`O(n)` is linear time.

Questions:

    Why does it take O(n) time to insert an element into an array? 
    
    Suppose you wanted to insert an element at the beginning of an array. 
    
    How would you do it? 

    How long would it take?

My answer:

    It takes O(n) time to insert into an array as you need to move the elements in order to have contiguous spaces in memory. If it cannot fit into the array, all elements must be moved into a space which allows for it to be inserted.

    Inserting an element at the beginning of the array, index 0, would require shifting all of the elements to the right. This could be done by moving to a new memory block of n + 1 size and placing the new element at the start, making it the first item in the array. This is going to take O(n) time, since you are having to move every element in the list to a new memory location.


### Inserting into the middle of a list

What if we want our todo list to work more like a calendar. Before, we were always inserting items to the end, now we want to add them in the order that they should be done, such as via priority.

What would be better if you want to insert elements in the middle? With a linked list, you can easily change what the previous elements are pointing to, with an array you are required to then shift all of the rightmost elements by 1 to the right, this makes it more annoying if there is no space since we then have to move everything too!

### Deletion

Deletions are best served here with linked lists again, similar to insertions, you can easily change what the previous element is pointing to. With an array, everything is going to need to be moved up.

Unlike insertion, a deletion can always work. An insertion may fail because there is no room left in memory, but you can always remove an element.

Do note that an insertion and deletion will only be O(1) when you have instant access to the element which is to be deleted. It is common practice to keep track of the first/last items in a linked list, so it is trivial to remove these.

There are 2 types of access: random and sequential. 

Sequential means reading the elements one by one, starting at the first element. Linked lists are seqeuential access, you start at the beginning and traverse through the pointers to the next memory address, stopping if you find your required element.

Random access means you can jump to any block of memory, as long as you have its address to hand. With arrays, this is possible by referring to an index position of an element, lots of use cases require random access, so this means that arrays are used for a lot of things.

**Arrays and linked lists are the building blocks of more complex data structures.**

## Selection Sort

Putting everything together now, lets assume you want to rank your favourite artists, from most to least played.

Algorithm demonstrated in the [exercises.](Exercises.md), taken from the book.

## Recap

* You can think of your computer's memory like a giant set of drawers.
* When you want to store multiple elements you can choose between an array or a linked list.
* Using an array means that all of the elements will be stored next to each other.
* Using a linked list means that the elements are not together, but are linked by each element pointing to the next one's memory location.
* Arrays allow fast reads
* Linked lists allow fast insertions/deletions
* All elements within an array should be of the same type (integer, string etc.)