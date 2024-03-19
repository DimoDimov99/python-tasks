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

## 10. Does Python support multiple Inheritance (OOP)

Python supports multiple Inheritance, I think it is called Polymorphism
