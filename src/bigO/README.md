# Big O notation

## Introduction - Performance or Time Complexity

An algorithm is simply an **procedure or formula for solving a problem**. But, due that into the computational world the *speed of execution* and the *memory usage* are too important, we need an efficient manner to measure this, independiently of hardware capacity and another factors.

This is where *Big O notation* comes into action.

> Big O notation describes ***how quickly runtime will grow, relative to the input as the input get arbitrarily large.***

## Runtimes of common big-O functions

So, *Big O* measures the quantity of operations and assignments done by an algotithm. Its notation is ***O***(*symbol*), where *symbol* can be:

|Symbol|Meaning|
|:--:|:--:|
|1|Constant|
|n|Linear|
|n log(n)|Log linear|
|n^2|Quadratic|
|n^3|Cubic|
|2^n|Exponential|

## Which terms Big O measures?

When it comes to Big O notation, we only care about the **most significant terms**, which are the fastest growth terms. Remember that as the input grows larger, only the fastest growing terms will matter.

This means that, if for example we have a function within which a term grows linearly, and another that has quadratic growth, we'll ignore the linear expression. So we can say the complexity of the given function is quadratic, because the **Most Significant term** have a quadratic complexity.

Let's give an example to you

``` python
def calculate_complexity(a_list):

    print( a_list[0] ) # This has constant complexity, or O(1)

    midpoint = int( len(a_list) / 2 )
    for val in a_list[ :midpoint]: # has n/2 complexity, or O(n/2)
        print(val)

    for i in range(10): # has constant 10 complexity, or O(10)
        print("constant operation!")
```

So, to measure the complete complexity, we need to add all these up

> *O( 1 + n/2 + 10 )*

But, when *n* becomes indefinitely big, ***O(1)*** and ***O(10)*** are the same thing, because they're simply constants, and we'll treat them as ***O(1)***

And at the same case, in ***O(n/2)*** or ***O(1/2 * n),*** when *n* becomes too big, *1/2* has no importance and we'll treat it as ***O(n)***

So, the complexity is the biggest between ***O(1)*** and ***O(n),*** which is ***O(n)***

## Method summary

So, the steps to get the complexity of a function are:

1. Separate the function into parts and get the complexity of each part
2. Put them all together in the same O() function
3. Simplify it as *n* grows arbitrarily large

## Introduction - Space Complexity
