# Recursion

- [Recursion](#recursion)
  - [Base Case and Recursive Case](#base-case-and-recursive-case)
  - ['The Stack'](#the-stack)
    - [Call stack with recursion](#call-stack-with-recursion)
- [Recap](#recap)


Recursion can be used to make a solution clearer. In general, there are no performance benefits to recursion, often times loops are actually better for this.    

    Loops may achieve a performance gain for your program. Recursion may achieve a performance gain for your programmer. Choose which is more important in your situation!

**A lot of important algorithms use recursion, so understanding this concept is incredibly useful.**

## Base Case and Recursive Case

When writing a recursive function, it's quite easy to end up in an infinite loop. This is commonly caused by not having a terminating factor, this is known as the base case. The recursive case will continue until reaching the base case, done by continuing calling itself.

It is known as the base case as it cannot be broken down into any other parts. Another recursive call cannot be made, so the data or item is returned.

E.g.

```python
def countdown(i):
    print(i)

    if i <= 0:
        return # Base case
    else:
        countdown(i - 1) # Recursive case
```

## 'The Stack'

This is about the *call stack*, which is very important in programming. The stack data structure has 2 actions: *push* and *pop*.

When we think of a stack, imagine a flimsy *stack of plates*. If you take something out of the middle or bottom, it might fall over. Instead you need to remove things from the top to ensure it is stable.

Pushing will add an item from the top.

Popping will remove an item from the top.

Internally, your computer uses a *call stack*. You can see it in action using a simple function.

```python
def greet(name):
    print("Hello %s!".format(name))
    greetTwo(name)
    print("Preparing to say bye")
    bye()

def greetTwo(name):
    print("How are you %s?".format(name))

def bye():
    print("Bye!")
```

First, you computer will allocate some memory for the function call. Within that memory, the `name` variable is going to be set to something like `Jack` - imagine this with the `greet` function. Since this function contains another one, named `greetTwo`, the computer will allocate some more memory and *push* the components of this function onto the stack. Once the function has completed, it will be *popped* from the top, so that the other function, `greet`, can continue.

The idea here is that when we allocate another block of memory and push the `greetTwo` function onto the call stack, the `greet` function was paused momentarily with all of the variables stored in memory.

### Call stack with recursion

The call stack is also used in recursion. A great example of this is to calculate the factorial of a number.

E.g. `5!` (5 factorial) is calculated as `5 * 4 * 3 * 2 * 1 = 120` 

The code would look like this

```python
def calc_factorial(x):

    if x == 1:
        return 1
    else:
        x * calc_factorial(x - 1)
```

Lets assume we run `calc_factorial(3)`, we end up with the following call stack.

[3 factorial call stack](images/factorial_call_stack.png)

The function call at the top of the call stack, `calc_factorial(x=1)`, will be our call that returns, meaning it will be popped from the stack first. Subsequently, the value returns from it, meaning we would have

```python
# snippet inside calc_factorial(2)
    x * 1 
# x is 2 here and '* 1' is the returned value that was computed from calc_factorial(2 - 1)
```


**Using the stack is convenient for recursion, but the cost is that a lot of memory is used.**

# Recap

* Recursion is when a function calls itself.
* Recursive functions have 2 cases: base case and a recursive case.
* A stack structure has 2 operations: push and pop.
* All function calls go onto the call stack.
* The call stack can grow to be quite large, which will take up a lot of memory.