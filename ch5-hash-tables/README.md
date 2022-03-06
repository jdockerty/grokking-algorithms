# Hash Tables

- [Hash Tables](#hash-tables)
  - [Hash Functions](#hash-functions)
  - [Use Cases](#use-cases)
    - [Lookups](#lookups)
    - [Preventing duplicate entries](#preventing-duplicate-entries)
    - [As a cache](#as-a-cache)
  - [Collisions](#collisions)
  - [Performance](#performance)
    - [Load Factor](#load-factor)
    - [Good Hash Function](#good-hash-function)
  - [Recap](#recap)

## Hash Functions

A hash function is a function in which you can enter a stream of bytes (some input) and have a number returned back to you.

    "hello" --> 7
    "myString123" --> 12


        A random hash function.

This is a mapping of inputs to outputs. It seems as though there is no pattern whatsoever, but there are some requirements that must be met in order to satisfy it being a hash function:

* Consistency, if you put in "apple" and this returns 4, you should always have the value 4 returned for the string "apple".
* Different words should map to different numbers. E.g. it would be pointless if for any word you gave it, it always returns the number 1.

To get this, you can start with an empty array. Your hash function will return a number, used as an index of the array, where to place the value of the key you input into the function. For example, suppose we input "apple" and get 3, it would look like

    [nil, nil, nil, 67p, nil]

    The value (price of the item) of the key "apple", our input, has been stored in index 3.
    With syntactic sugar, we can represent this as { "apple": "67p" }

From here, we can retrieve the price of an apple in O(1), constant, time. We do not need to search for the value in the array, instead we retrieve the index of the value through supplying the key to our hash function. 

**Note: the hash function will need to know how big our array is in order to not produce values that are out of bounds**


**To create a hash table, we use an array and a hash function.**

Hash tables also have other names: hash maps, maps, dictionaries, and associative arrays.

In most modern languages, you don't have to create a hash table data structure yourself, they are typically in-built to the language itself or in the standard library. Python has hash tables known as *dictionaries*.

```python
book = dict() # we could also use {}

book["apple"] = 0.67
book["milk"] = 1.20
```

## Use Cases


### Lookups

Your phone has a phonebook built-in, each name has a phone number associated.

    Girlfriend - 01234 333333
    Parents - 01234 444444
    Friend - 01234 555555

Here, we are just mapping people's names to phone numbers. The phonebook we have needs to have the functionality of:

* Add a person's name and the phone number associated.
* Enter a name, we get the phone number back.

This is the perfect use case for a hash table.

**Hash tables are great when you want to map one thing to another or look something up.**


### Preventing duplicate entries

If we ran a voting booth, people can only vote once. How could we check that they do?

When someone comes in, we could get their full name, we check it off against a list of people who have voted. If someone's name is ticked off as already voted, we don't let them vote again. If our list of names was incredibly long, we might be searching for awhile to check their name.

We can do this a better way, by using a hash. We can keep track of people who have voted and and retrieve the name to see whether they have already.

```python
voted = {}
has_voted = voted.get("Jack Dockerty") # .get returns the value if it is present, 'None' if it doesn't exist.
```

We can use this in a larger function in order to check whether someone has voted.

```python
def check_voter(name):
    if voted.get(name):
        print("Already voted!")
    else:
        voted[name] = True
        print("Allowed to vote!")
```


### As a cache

Caching is a brilliant use case for hash tables. Caching reduces load on servers as they need to do less work for common queries of data. We can save the commonly asked queries' results and provide the data without needing to actually run the query itself (assuming the data does not mutate).

Large websites, like Facebook, will ensure that their static pages (ones which are not changing whenever you visit) are cached in order to save the user, and their servers CPU, time. The about, t&c's, and contact pages are great for this. We could map a URL to page data.

    facebook.com/about --> about page data
    facebook.com --> login page data

```python
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url] # returns cached data
    else:
        data = get_data_from_server(url)
        cache[url] = data # store our data for next time so we don't need to retrieve it again
        return data
```

## Collisions

To understand the performance of hash tables, we need to know about collisions.

In reality, it is almost impossible to write a hash function which will always map different keys to array indexes.


    E.g. if you had an array with 26 slots, our hypothetical hash function assigns a slot in this array alphabetically.

    If we have "apples", this is fine, our price goes into slot 1.

    But if we then have "avocados", we have a collision, we would override the value from "apples" to insert data here.

How can we solve it? There a numerous ways to do this.

One of the simpler solutions is to start a linked list in the slot whenever we have a collision (two keys in the same slot).

[Linked List Solution](images/linked-list-solution.png)

Here, if we need to know the price of bananas, it's quite fast. This is O(1) since we can look up the value. If we needed to look up the value of 
avocados though, its going to be slower, since we are required to traverse through the linked list to get our value. This isn't a huge deal if the linked list is small, but as it grows larger it can be a pain - this gives us the search time of O(n) in this case.

From this, we know two things:

* The hash function you use is really important. Ideally it should map keys evenly all over the hash.
* If the linked list gets long, it slows down the hash table a lot, although this can be avoided by using good hash functions.

How do we pick a good hash function in order to avoid as many collisions?

## Performance

Hash tables are blazing fast, on average. The average case for hash tables is O(1) for everything, meaning that the time taken to search/insert/delete from the hash table is going to be the same regardless of how big the hash table is, if it has 1 element or 1 billion.

For the worst case, hash tables are O(n) for everything - this is really slow.

Hash tables are the best of both worlds for searching and inserts/deletes, but only when not hitting our worst case performance. To acheive this, we need to avoid collisions, which requires:

* A low load factor
* A good hash function


### Load Factor

The load factor is easy to calculate

    Number of items in the hash table / total slots

Since hash tables use an array for storage, we can count the number of occupied slots in the array.

    [nil, 1, nil, 0, nil]

    2/5 slots are occupied, we have a load factor of 0.4

If our hash table has 100 slots and we have 100 items we need to store, this is 100/100. A load factor of 1, every item gets a slot.

If we have 50 slots, but 100 items. We have a load factor of 2, each item isn't going to get its own slot here.

**Having a load factor of greater than 1 will mean we have more items than slots available in the underlying array.**

Once your load factor increases, you need to *resize* the hash table. If we have an array which is starting to get full, we resize it. A rule of thumb is that you create an array that is twice the size.

    [2, 4, 9, nil] # load factor of 3/4 (0.75)


    [      ] # new array
    
    New array with 8 slots and reinsert items in the array using our hash function, this may give them a new index. Our new array has a load factor of 3/8, which is much better.

**A good rule of thumb is to resize when the load factor is greater than 0.7**.

Resizing is an expensive operation, so you don't want to do it a lot. Averaged out though, hash tables still take O(1) time even with resizing.

### Good Hash Function

A good hash function is going to distribute values evenly across the array. A bad one will produce a lot of collisions.

There are many tough mathematical principles behind creating a good hash function, which is rather beyond the scope of the book.

An example of a good hash function is SHA. This is a good hash function to use if you need to.

## Recap

**You almost never have to implement a hash table yourself, you can use your programming language of choice's implementation and assume you will get the average case performance: constant time.**