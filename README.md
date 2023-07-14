# Tutorial_1

## Task 1 - Setting up your Development Environment

Install Visual Studio Code and Python.

https://www.python.org/downloads/

https://code.visualstudio.com/

## Task 2 - Understanding Variables and Expressions

**What are expressions?**

An expression consists of one or more *operands* and zero or more *operators*. An expression returns a *value* of a certain *type* when it is *evaluated*.

**What are variables?**

A variable allows you to store a value in memory and call upon it later in your code. Variables are a named value. In programming languages a concept of type exists, which describes the handling of data types.

"Python is both a strongly typed and a dynamically typed language.

Strong typing means that variables do have a type and that the type matters when performing operations on a variable. Dynamic typing means that the type of the variable is determined only during runtime.

Due to strong typing, types need to be compatible with respect to the operand when performing operations. For example Python allows one to add an integer and a floating point number, but adding an integer to a string produces error.

Due to dynamic typing, in Python the same variable can have a different type at different times during the execution. Dynamic typing allows for flexibility in programming, but with a price in performance." From *Using static typing - Python in High Performance Computing*, FutureLearn.com

One way to debug variables throughout your code, is by drawing a trace table. Over time you will rely less and less on something like a trace table, but it's still good to know about. In the future you will learn to use debugging tools built into VS Code.



**Basic introduction to data types**

The important data types in Python that you need to know right now are:

- Integers (int)
- Floats (float)
- Strings (str)
- Booleans (bool)

        alpha = 7 # this is an integer variable
        bravo = 7.9 # this is a float variable
        charlie = "hello world" # this is a string variable
        delta = false # this is a boolean variable

**Basic operations with variables**

The important operations in Python that you need to know right now are:

- Basic arithmetic operators

        +
        -
        *
        /
- Basic assignment operators

        =
        +=
        -=
- Comparison operators

        ==
        !=
        >
        <
        >=
        <=
## Task 3 - Learning Control Structures

**Introduction to `if` statements**

One of the most common types of control structures is the if statement. It's made up of various parts. Let's work through some examples in `task_3.py`.

**Introduction to `for` and `while` loops**

See `task_3.py`.

**What's the deal with Python indentation?**

Let's discuss this. See PEP 8 for more: https://peps.python.org/pep-0008/.

## Task 4 - Using Functions

What are functions and how do they help us?

See `task_4.py`.

## More Exercises

https://orac.amt.edu.au/