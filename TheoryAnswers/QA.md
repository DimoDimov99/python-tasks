# Theoritical Questions and Answers

## 1. What are the benefits of using Python language as a language,what are it's drawbacks?

Benefits - Python is dynamicly typed modern language. It reads as plain english. Easy syntax. Perfect for automation and scripting, data analysis, ML, AI, vizulization. Dynamicly typed and have collector, so no pointers and references to deal with (it handles them under the hood).
Drawbacks - Relativly slow, compared to languages where you can manage your memory processes (C, C++, Rust). Not really scalable for large corporate applications, games (large games) and hardcode GUI projects.

## 2. What is the difference between a Tuple and List in Python?

Main difference between Tuple and List data structure is that, tuple ds is imutable and list is mutable.
So we can do l = [1, 2, 3]; l[2] = 5, however we cannot do l = (1, 2, 3); l[0] = 55

## 3. Is Indentation Required in Python?

Indentation is required, as it indicates to python, where are the different blocks; according to PEP8, standart indentation in python is 4 white spaces (no tabulations) as per nesting; Indentation indicates if/else, loops and functions blocks; for example:

```
def is_able_to_vote(age):
    can_vote = False
    if age >= 18:
        can_vote = True
    return can_vote
```

## 4. Difference between for loop and while loop in Python

Main differences between the two main loops:

- We use for loops, when we know in advance how many times we want to loop or generate sequence; we use while loops mainly when we want to loop until specific condition is met (we do not know in advance how many times we would need to loop)

```
for i in range(10):
    pass
with above code we generate integer sequence from 0 to 9

while not_tired:
    code()
```

- Unlike for loops, in while loops we can easily hit infinity loop, until our machine runs out of memory. This happends, due to the reason that while loop iterate until condition is met, if condition is never met it continues (similar to recursion)

Infinity loop:

```
while True:
    pass
```

## 5. What is List Comprehension, why do we need it and is it faster than a loop for list creation? Give an Example.

List comprehension is a fancy way to create list. For example, I would like to create list with even numbers, between starting and end point:

Without list comprehension:

```
def even_numbers_between_points(start, end):
    even_numbers = []
    # 2 is the first even number
    # range func iterate until end - 1
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers
even_numbers_between_points(2, 20)
```

```
With list comprehension
start = 2
end = 21
even_numbers = [number for number in range(start, end) if number % 2 == 0]
We can archieve pretty one liners which
```

`Notes`: It's not only fancy, it is indeed faster. As when you create a list with a for loop, you append a value to the end of the list with append - this is creating overhead. A list comprehention can
be more efficient, the more elements the list needs to have. With 10-100 values - probably not noticable, but with more values (in the millions) it will be faster for sure.
Try to run the below - the more values you add to be created, the comprehension will become faster and faster.
```
from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

@timeit
def create_via_for_loop():
    l = []
    for i in range(10000000):
        l.append(i)

@timeit
def create_via_comprehension():
    l = [i for i in range(10000000)]


create_via_for_loop()
create_via_comprehension()
```

```
1000000 items:
Function create_via_for_loop took 1.1453 seconds
Function create_via_comprehension took 0.7650 seconds
Comprehension twice as fast
```


```
100000000 items:
Function create_via_for_loop took 9.8660 seconds
Function create_via_comprehension took 6.7919 seconds
Comprehension almost 3x as fast
```


## 6. What are unit tests in Python?

Unit tests are not sole Python thing, but a programming one instead. Idea of unit test is to test one functionality (unit); It is mainly used for testing separate functions. I think there is a builtin module called unittest

## 7. What is the difference between a shallow copy and a deep copy?

Main difference is how the copy is creation; In shallow copy, we literaly asing the object to point at another memory as well. In the deep copy we copy the content structure, however, we create a whole new object in the memory which will not be affected if the copy subject is mutated.
Example code:

```
test = [1, 2, 3]
test_s_copy = test
test_d_copy = test[::]
test.append(5)
print(test_s_copy)
print(test_d_copy)

In this case, if we modify the copy source (test list), the shallow destionation test_s_copy is basically the same object, as test list (point to it) so when the source is modified so is the destionation, when we have deep copy this is not the case, as it point to different memory address. I think there are several methods to do deep copy (builting method as well), I have used the slicing operator [::]. Slice operator is also pretty handy for reversing a list [::-1]

```

## 8. What are Decorators?

Honestly, I do not have many experience with decorators. I think they provide syntax sugar to a lot of functionality and can enchant functions (shortened the syntax as well). For example in OOP if we would like to have class method, we notify it with the @classmethod decorator. They are denoted with @ symbol.

## 9. When a parameter is passed to a function, is it by value (copy) or reference (pointer) ?

In python, the parameter is passed as reference (pointer) and it also needs to be managed in languages such as C, C++. This is mainly, because if we pass the parameter by value (copy), our function will not modify,mutate the object, but it will create a copy, which will be destroyed at the return point of the function. 9/10 when we pass parameter we would like to modify it current state. So the parameter is passed as memory address, not with it is actually value.

`Notes`: That's only partially true. Simple types are passed by value - i.e they are copied to a separate memory block and are different than the input variable. Structures on the other hand, are passed by reference - you can see the results in the code below. Also, usually it's not 
that common that you would like to change the original value, most of the time you want to returned a changed one. Also return does not destroy objects, it returns a reference to the returned object that can be saved in a variable. In the backend the Python garbage collector 
will in fact delete the initial variable passed if not used after the function call, so the top overview: you have a variable, you pass it to a function that returns a modified value that is saved in a variable. The initial one gets removed by Garbage Collector if it doesn't have 
any more blocks of code that need to use it.

```
x = 5
y = [1,2,3,4,5]

def test_argument_change(num:int, l:list):
    num += 1
    l.append(6)

test_argument_change(x,y)

print(x)
print(y)
```

## 10. Does Python support multiple Inheritance (OOP)

Python supports multiple Inheritance, I think it is called Polymorphism

`Notes`: The statement is correct, by it differs from Polymorphism. Polymorphism is the quality that different object can behive the similarly, for example:
You have a class `Shape` that is inherited by it's child classes `square` and `circle`. The `shape` class can have a abstract method (a method that needs to be implemented of all it's children) - `draw`. 
Then both `circle` and `square` will have this method, but in one case it will draw a circle, in the other a square.
In pseudo-code:
```
             class Shape
              def draw()
              /       \
    class Circle     class Square
    def draw()         def draw()
Draws circle            Draws Square

```
