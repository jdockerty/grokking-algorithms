# Exercises

**2.1**

    Suppose you’re building an app to keep track of your finances. Every day, you write down everything you spent money on. At the end of the month, you review your expenses and sum up how much you spent. So, you have lots of inserts and a few reads. 

    Should you use an array or a list?

Using a linked list here would be wise, you have many inserts which are going to be O(1), and minimal reads of O(n).


**2.2**

    Suppose you’re building an app for restaurants to take customer orders. Your app needs to store a list of orders. 
    
    Servers keep adding orders to this list, and chefs take orders off the list and make them. 
    
    It’s an order queue: servers add orders to the back of the queue, and the chef takes the first order off the queue and cooks it. 
    
    Would you use an array or a linked list to implement this queue? 
    
    (Hint: Linked lists are good for inserts/deletes, and arrays are good for random access. Which one are you going to be doing here?)

Here, you would use a linked list. There is no requirement for random access and we have lots of insertions from the beginning and removals from the end happening with the servers adding and chefs removing. The O(1), constant time, for insertions/deletions with a linked list will be very useful here.

**2.3** 

    Let’s run a thought experiment. Suppose Facebook keeps a list of usernames. When someone tries to log in to Facebook, a search is done for their username. If their name is in the list of usernames, they can log in. 
    
    People log in to Facebook pretty often, so there are a lot of searches through this list of usernames. Suppose Facebook uses binary search to search the list. Binary search needs random access—you need to be able to get to the middle of the list of usernames instantly. 
    
    Knowing this, would you implement the list as an array or a linked list?

This would require an array. The fact binary search requires random access is also the giveaway here too. Also, considering there are lots of searches occurring, we don't want to use a linked list, since we would have to continually traverse the elements in linear time, which would not be very efficient.

**2.4 **

    People sign up for Facebook pretty often, too. 
    
    Suppose you decided to use an array to store the list of users. What are the downsides of an array for inserts? In particular, suppose you’re using binary search to search for logins. 
    
    What happens when you add new users to an array? 

Downsides of the array for inserts is that it takes O(n) time, meaning that we are likely going to need to copy all our elements into another block of memory whenever we are inserting into the array, this is not going to be efficient for huge lists, as with Facebook information for a lot of people. Adding a new user also means that the other items are going to need to be shifted, this is even more so the case as we are using a binary search, we the elements need to be sorted too, it is not like an element can just be tacked onto the end and everything is okay, it is required to be in the correct place to our sorting criteria.

**2.5**

    In reality, Facebook uses neither an array nor a linked list to store user information. Let’s consider a hybrid data structure: an array of linked lists. You have an array with 26 slots. Each slot points to a linked list. For example, the first slot in the array points to a linked list containing all the usernames starting with a. The second slot points to a linked list containing all the usernames starting with b, and so on.

    Suppose Adit B signs up for Facebook, and you want to add them to the list. You go to slot 1 in the array, go to the linked list for slot 1, and add Adit B at the end. Now, suppose you want to search for Zakhir H. You go to slot 26, which points to a linked list of all the Z names. Then you search through that list to find Zakhir H. 
    
    Compare this hybrid data structure to arrays and linked lists. Is it slower or faster than each for searching and inserting? You don’t have to give Big O run times, just whether the new data structure would be faster or slower.

For reading, I believe this would be O(n). You have constant time access to the list itself, but it still requires traversal to find the correct user, which implies the possibility of going through the entire list at this point - averaging out to O(n).

For inserting, I believe this would be O(1), possible in constant time. You have constant access to the element you need via the array, and then you can also insert an element easily into it via the linked list structure contained within the array itself.