# Introduction

  Welcome to **Session 2: Introduction to Python**.

  The goal of this session is to introduce you to your first pieces of Python code and help you become comfortable enough to write your own program to solve a simple problem. You will be introduced to a series of simple Python commands and will write short pieces of code using them to achieve particular outcomes.

  By the end of this session, you will know how to use your first commands, including basic mathematical operators. You will also be able to use these commands to write a program that achieves a simple task and use comments to annotate your new code.

  Many of the topics introduced here will be revisited later in the course, where we will develop a more detailed understanding of how they work.

  Please take the time to review the learning outcomes for this session below.

    ## Learning Outcomes

    By the end of this session, you will have learned how to:

      - Use the `print` function to display information.

      - Set and use variables in Python.

      - Apply basic mathematical operators.

      - Write simple Python commands to complete a task.

      - Use comments to annotate and explain code.

      - Run, save, and review your own Python programs in Anaconda/Jupyter.

      - Recognise reserved Python keywords and avoid using them as variable names.

      - Use common Python data types, including numerical types, strings, lists and dictionaries.

  Let’s get started. The remaining topics in this session are organised below.

---

## A. The Print Statement

      In this activity, we begin to explore the use of the `print` statement. The `print` statement is a useful and important function in Python because it allows us to extract information from our code and display it on the screen.

      This is useful for creating outputs, checking whether code is working correctly, debugging errors, and providing information to a user.

## What does print do?

The `print` function sends information from a Python program to the output area. In a Jupyter Notebook, this output is displayed directly below the code cell after the cell is run.

## Why is print useful?

The `print` function is often used when learning Python because it gives immediate feedback. It can show the result of a calculation, display the value of a variable, or help identify where an error may be occurring.

## Exercise 1: Print Statement

You now have an opportunity to write and test your own code. Please use Anaconda and Jupyter Notebook to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you obtained, and any errors you encountered.

      In the next activity, we will look at how to identify and use variables in Python.

## B. Setting Variables

      In this activity, we explore variables. A key concept in any coding language is that of a variable. When data is saved in a program, it is referred to as a variable and may be referenced by one or more variable names.

      These variable names allow us to access, alter, or use the stored data in calculations. Variables are therefore central to writing useful programs because they allow information to be stored and reused.

## What is a Variable?

A variable is a named location used to store data in a program. Once a value has been assigned to a variable, the variable name can be used later in the code to refer back to that value.

## Why Variables Matter

Variables make code more flexible and easier to understand. Instead of repeating values throughout a program, you can store a value once and refer to it by name whenever it is needed.

## Exercise 2: Setting Variables

You now have an opportunity to write and test your own code. Please use Anaconda and Jupyter Notebook to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you obtained, and any errors you encountered.

      In the next activity, we look at how to identify and use mathematical operators.

## C. Mathematical Operators

      In this activity, we look at how to use some basic mathematical operators in Python. Many of these operators work in a similar way to how you would expect them to work in a mathematical equation.

      Mathematical operators allow Python to perform calculations, making them one of the most important tools for solving numerical problems in code.

## Common Operators

Python includes operators for common calculations such as addition, subtraction, multiplication, division, powers, and other mathematical operations. These operators can be used directly with numbers or with variables that store numerical values.

## Operators and Variables

Once a number has been stored in a variable, the variable name can be used inside a mathematical expression. This makes it possible to write calculations that are easier to update and reuse.

## Exercise 3: Mathematical Operators

In this exercise, you will have a chance to write and test your own code. Please use Anaconda and Jupyter Notebook to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you obtained, and any errors you encountered.

      In the next activity, we look at how comments work.

## D. Comments

      In this activity, we look at how to use comments. Comments are common to many coding languages and provide a way to write notes in a source file that will be ignored by the interpreter.

      Comments are useful because they allow you to explain what your code is doing, record your thinking, and make programs easier for other people to understand.

## What is a Comment?

A comment is text written inside a source file that is intended for human readers rather than the computer. When Python runs the program, comments are ignored and do not affect the output.

## Why Comments are Useful

Comments help explain the purpose of code, document assumptions, clarify complex sections, and make your work easier to revisit later. They are especially valuable when code is shared with other users.

## Good Practice

Good comments should be clear, concise, and useful. They should explain why something is being done or clarify the purpose of a section of code, rather than simply repeating what is already obvious.

## E. Your Turn: My First Program

      In this activity, you will have an opportunity to test your understanding of the key concepts and skills developed in this session.

      You will bring together the main ideas covered so far by using the `print` function, setting variables, applying mathematical operators, and adding comments to your code.

## What You Will Practise

- How to use the `print` function.
- How to set variables.
- How to use mathematical operators.
- How to add comments to your code.

## Activity Guidance

Work through the task step by step. Write your code, run it, check the output, and make changes where needed. Save your file once you have completed the activity.

## Learning Tip

Your first program does not need to be complex. The important goal is to practise combining several simple ideas into one working piece of code.

      Once you have completed this activity, you will be ready to continue building more structured Python programs.

## F. Variables and Assignment

      In all coding languages, a variable is a label used in the source code to reference a piece of information stored in your computer’s memory. In this activity, you will learn more about variables in Python and how assignment statements are used to store, modify, and retrieve values.

      Choosing meaningful variable names is an important programming skill. Good variable names improve readability, make programs easier to debug, and help other programmers understand your code. Python also reserves a number of keywords for its own language syntax, meaning they cannot be used as variable names.

## Reserved Keywords in Python

The following words are reserved by Python because they have special meanings within the language. They cannot be used as variable names.

andexceptlambdawithasfinallynonlocalwhileassertFalseNoneyieldbreakfornotclassfromorcontinueglobalpassdefifraisedelimportreturnelifinTrueelseistry

## Python Code Examples

```python
# Example 1
#Keywords are highlighted
and = 1

# Example 2
#Creating a variable with assignment
a = 1 + 2

# Example 3
#Checking a variable name exists by printing its value
print(a)

# Example 4
#Printing (or otherwise accessing) a variable before it has been asigned to will result in an error
print(b)
b = 3

# Example 5
#It's valid to use a variable name in an expression that assigns to it
x = 1
x = x + x
print(x)

# Example 6
#The variable name to be assigned to must be on the left of the assignment operator
3 = x
```

      This activity reinforces the idea that variable names are labels for stored information and that assignment statements control how values are stored and updated throughout a Python program.

## G. Common Python Data Types

      This section brings together several important Python data types. You will explore how data can be represented using numerical types, strings, lists and dictionaries, and how these types can be used in simple programs.

## G.1 Overview and Glossary

          This section will help you utilise some of the common variable types in Python. By the end, you will understand the information that can be stored in numerical types, strings and lists, and how to store, manipulate and extract this information.

          You will also be able to create examples of reals, integers, booleans, lists and strings, and describe their key properties. This will allow you to use appropriate data types in appropriate situations and write more efficient and advanced code.

        ## Learning Outcomes

        By the end of this section, you will be able to:

          - Understand the information that can be stored in numerical types, strings, lists, and dictionaries.

          - Create examples of integers, floats, booleans, strings, lists, and dictionaries.

          - Manipulate and extract information from common Python data types.

          - Describe the key properties of common Python types.

          - Select appropriate data types for different coding tasks.

          Throughout this section, you will notice the use of key terms. Use the glossary below to check any definition you are unsure of.

            **Type**
            A blueprint for a specific type of data which can be stored in your computer. Also known as a class.

            **Class**
            A blueprint for a specific type of data which can be stored in your computer. Also known as a type.

            **Object**
            A specific example of a type that has been created and exists in memory. Also known as an instance.

            **Instance**
            A specific example of a type that has been created and exists in memory. Also known as an object.

            **Int**
            A Python type designed to store whole numbers or integers.

            **Float**
            A Python type designed to store numbers which may not be whole.

            **String**
            A Python type designed to store a collection of characters in a specified order, such as a word or phrase.

            **Index**
            The value used to reference a particular value in a collection such as a string or list.

            **List**
            A Python type designed to store values of any mixture of types in a specified order.

          Let’s get started. In the next activity, we learn more about types.

## G.2 Types

          In this activity, you will learn more about types. In Python, every value, expression and variable is an object. An object is an example or instance of a particular type or class of data.

          You may think of a type as a blueprint for an instance of that type. This describes how Python should store the data associated with an instance of that type and what features and behaviours the instance will have.

## Python Code Examples

```python
# Example 1
# The result of an expression will be an object, which is an example of a particular type
#The "type" function returns the name of the type
print(type(1 + 3))

# Example 2
#The value associated with a variable will have a type
a = 1.1
print(type(a))

# Example 3
#We can also find the type of a value
print(type("words"))
```

          In the next activity, we look at how to identify and use numerical types.

## G.3 Numerical Types

          There are three types of numeric variables in Python: integers, floats and complex numbers. In this activity, we look at integers and reals. For those who are interested, there is also an extension section on complex numbers.

## Exercise 1: Numerical Types

In this exercise, you will have a chance to write and test your own code. Please use Anaconda to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you had and any errors.

## Python Code Examples

```python
# Example 1
# Integers are specified and printed without a decimal point and must be whole numbers
a = 1
print(a)
print(type(a))

# Example 2
# Floats are specified and printed with a decimal point
b = 3.1
print(b)
print(type(b))

# Example 3
# Floats may be whole numbers
c = -2.0
print(c)
print(type(c))

# Example 4
# Division will return a float, even if the values it operates on are both integers
print(4 / 3)

# Example 5
# Adding two ints returns an int
print(1 + 2)

# Example 6
# Adding two floats returns a float
print(3.0 + 1.0)

# Example 7
# Adding an int and a float returns a float
print(2 + 1.5)

# Example 8
#The float function returns a float version of the value in parentheses
print(float(5))

# Example 9
# The int function returns the value in parentheses rounded toward zero to the nearest integer
d = 2.6
print(int(d))

# Example 10
# Operating on a variable does not change its value
print(d)

# Example 11
# The round function rounds to the nearest whole number
print(round(d + 1))
```

## Sample Exercise Solution

```python
# Solution Cell 1
# Specify my_number. Set the value to -3.6 for the last part of the exercise
my_number = 10.8
print(my_number)

# Use  the int function to create round_down
round_down = int(my_number)
print(round_down)

# Use the round function to round to the nearest integer
round_nearest = round(my_number)
print(round_nearest)

# Use the float function to make a float from round_nearest
new_float = float(round_nearest)
print(new_float)
```

          In the next activity, we look at what a string is and use it within Jupyter Notebooks.

## G.4 Strings

          A string is a collection of characters. In this activity, we explore strings in more detail, including how they can be created, stored, manipulated and accessed in Python.

## Exercise 2: Strings

In this exercise, you will have a chance to write and test your own code. Please use Anaconda to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you had and any errors.

## Python Code Examples

```python
# Example 1
string1 = "Python"
string2 = "is my favourite language"

first_string = string1[-3]
print(first_string)

second_string = string2[1:10:3]
print(second_string)

third_string = string2[:3:] + string1
print(third_string)

print(len(third_string))
```

## Sample Exercise Solution

```python
# Solution Cell 1
string1 = "Python"
string2 = "is my favourite language"

# The third character from the end of the string is selected
first_string = string1[-3]
print(first_string)

# Every third character beginning with the second character (which has index 1) is returned
# This sampling finishes just before the character with index 10 (the "u")
second_string = string2[1:10:3]
print(second_string)

# The sampled range runs from the start of the string until just before the character with index three
# Every character in the range is sampled
third_string = string2[:3:] + string1
print(third_string)

#There are nine characters in the string (including the space)
print(len(third_string))

# Solution Cell 2
# Create the string to work with
my_string = "Python is fun"

# Solution Cell 3
#The first character has index zero
print(my_string[0])

# Solution Cell 4
# Leaving the first value in square brackets blank means we sample from the start of the string
# Selecting 3 as the stop value means the sampled range has indices 0, 1, 2
# Leaving out the step value means every value in this range is sampled
start_string = my_string[:3:]
print(start_string)

# Solution Cell 5
# Setting the first value in square brackets to -3 causes the first character of the sampled range to be three characters from the end
# Leaving the stop value blank causes the sampled range to run until the end of the string
# Leaving the step blank means every character in that range is returned
end_string = my_string[-3::]
print(end_string)

# Solution Cell 6
# We join the two strings together with the contaentation operator
joined_string = start_string + end_string
print(joined_string)

# Solution Cell 7
# Setting the first value in square brakcets to 1 causes the first character returned to be the second character of the string
# Leaving the stop value blank causes sampling to run until the end of the string
# A step of 2 samples every other value in the sampled range
alternating_string = my_string[1::2]
print(alternating_string)
```

          In the next activity, we look at how to identify and use lists.

## G.5 Lists

          In this activity, you will learn more about lists. Lists are another common type in Python. Like a string, a list is a sequence, meaning it is an ordered collection of values.

## Exercise 3: Lists

In this exercise, you will have a chance to write and test your own code. Please use Anaconda to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you had and any errors.

## Python Code Examples

```python
# Example 1
# Create a list using square brackets
new_list = []
print(new_list)

# Example 2
# We can give a list values when we create it
shopping_list = ["apples", "bananas", "bread", "mushrooms"]
print(shopping_list)

# Example 3
# We can access items in a list in the same way as we did for strings
print(shopping_list[0])

# Example 4
print(shopping_list[-1])

# Example 5
print(shopping_list[1::2])

# Example 6
# This syntax changes the value stored in the list with a specified index to a new value
shopping_list[0] = "tomatoes"
print(shopping_list)

# Example 7
# This syntax appends a new value to the end of the list, extending it
shopping_list.append("grapes")
print(shopping_list)

# Example 8
# This syntax inserts a new value into a list at a specified location
# Displaced values will be shifted to the right (i.e. their index will be increased by one)
shopping_list.insert(1, "lettuce")
print(shopping_list)

# Example 9
# The "len" function tells us the number of entries in the list
print(len(shopping_list))

# Example 10
# The plus sign will concatenate two lists to form a new list
print(shopping_list + ["turnips", "beetroot"])
```

## Sample Exercise Solution

```python
# Solution Cell 1
# Create the list with its initial values
cuddly_animals = ["rabbit", "hamster"]
print(cuddly_animals)

# Solution Cell 2
# USe the append method to add the string "rat" to the end of the list
cuddly_animals.append("rat")
print(cuddly_animals)

# Solution Cell 3
# Use the insert method to insert "chinchilla" at the start of the list
# Subsequent items in the list are shifted to the right
cuddly_animals.insert(0, "chinchilla")
print(cuddly_animals)

# Solution Cell 4
# Change the value of the second item in the list to "ferret"
cuddly_animals[1] = "ferret"
print(cuddly_animals)

# Solution Cell 5
# When we try to print the item from the list with index 99 we get an error
# This is because the list is not large enough for any item to have an index of 99
print(cuddly_animals[99])

# Solution Cell 6
# When we try to assign to the item in the list with an index of 99 we get an error
# This is because the list is not large enough for any item to have an index of 99
cuddly_animals[99] = "gerbil"
```

          In the next extension activity, we look at how to recognise complex numbers.

## G.6 Extension: Dictionaries

          By the end of this activity, you will know how to create dictionaries and how to use their basic functions. Dictionaries are useful when information is naturally organised as key-value pairs.

## Exercise 4: Dictionaries

In this exercise, you will have a chance to write and test your own code. Please use Anaconda to complete the exercise.

Run your code and save the file. You may also want to make note of the steps you followed, the results you had and any errors.

## Python Code Examples

```python
# Example 1
# Create a dictionary and give it some initial values
# Create a dictionary with curly brackets
# Key-value pairs and specified and separated by commas
# Each key value-pair contains a colon which separates the key and the value
atomic_numbers = {"H":1, "He":2}
print(atomic_numbers)

# Example 2
#We can add a new value by inserted the key in square brackets and using item assignment
atomic_numbers["Li"] = 3
print(atomic_numbers)

# Example 3
# We can also use item assignment to change an existing value
atomic_numbers["H"] = 0
print(atomic_numbers)

# Example 4
# We can access inidividual items from a dictionary by placing the key in square brackets after the name of the dictionary variable
print(atomic_numbers["He"])
```

          In the next activity, you have the chance to test your learning with a quiz.

## H. Pandas

      This section introduces **pandas**, one of the main Python libraries for working with structured datasets. Pandas is especially useful when data are organised in tables, such as CSV files, spreadsheets, financial datasets, or survey data.

      The material is organised into a short sequence: first, we introduce DataFrames using toy data; then we load and inspect a real dataset; after that, we access, modify and filter data; finally, we practise these skills and introduce more advanced DataFrame operations.

        ## Learning Focus

        By the end of this section, you should be able to:

          - Explain the purpose of pandas in Python data analysis.

          - Create and inspect basic DataFrames.

          - Load a CSV file into pandas.

          - Access rows, columns and summary information.

          - Modify, filter and transform tabular data.

          - Recognise how pandas supports more advanced empirical analysis.

## H.1 Pandas and DataFrames

          Pandas provides data analysis and statistical functionality in Python. It is designed for working with structured data, especially data arranged in rows and columns.

          The central object introduced here is the **DataFrame**. A DataFrame can be thought of as a spreadsheet-like table: it has rows, columns, column names, and values that can be inspected, summarised and transformed.

          This part begins with toy data so that the main ideas are clear before moving on to a real dataset.

## Python Code Examples: Creating and Inspecting DataFrames

```python
# Example 1
import pandas as pd

# Example 2
# # Here we generate some toy data. We will explore the numpy package later
# # but for now, just know we are use it to generate some random data.
import numpy as np

# # We fix the seed so that the results are reproducible.
# # Please do not change this code.
np.random.seed(seed=9)
# # Generate some toy data (sampled from a Gaussian distribution)
values = np.random.randn(100, 1)

# Example 3
# # Let's use the data that we created above to create a DataFrame.
dataframe = pd.DataFrame(data=values)

# Example 4
# # Let's inspect our dataframe.
# # For instance, you can get the shape of the dataframe, to see its dimensions.
print(dataframe.shape)

# # Some pandas methods have the same names as in standard Python, such as
# # max, min, and sum. Other common methods are the median, mean, and std
# # (standard deviation) methods.
print(dataframe.max())

# # The max value should be 2.45. But notice the result is not a simple value
# # but a pandas data "series"
print('Result type:', type(dataframe.max()))

# # To get only the max value without the additional information, you
# # could do:
print(dataframe.max()[0])

# Example 5
# Change the next line so that min_elem_df contains the min
# element of dataframe.
# The expected result is ONLY the min value.
min_elem_df = ...

# Change the next line so that mean_elem_df contains the mean
# element of dataframe.
# The expected result is ONLY the mean value.
mean_elem_df = ...

# Example 6
# Please do not modify the line below (allows us to replicate the results).
np.random.seed(seed=9)

# The lines below concern part C of Question 1.
# Modify the line below so that it creates the dataframe of 10k elements
# as mentioned in the description (part C above).
dataframe_10k = ...

# Change the next line so that mean_10k contains the mean
# element of dataframe_10k.
mean_10k = ...

# Example 7
# Test cell; please do not change!
_ = ok.grade('q1')

# Example 8
d1 = {}
d1['countries'] = ['UK', 'France', 'Spain', 'Netherlands']
d1['codes'] = ['uk', 'fr', 'es', 'nl']
# # the population is measured in millions
d1['population'] = [65.6, 66.9, 46.6, 17.0]
# # the gdp is measured in billions
d1['gdp'] = [2619, 2465, 1232, 770]

# Example 9
# # Let's create a dataframe now with that data.
# # DataFrame includes a convenience constructor that
# # just accepts the dictionary data and creates
# # the same structure as in the previous example.
countries_data = pd.DataFrame(d1)

print(countries_data['gdp'])
countries_data # Notebook gives a nice HTML table of the dataframe

# Example 10
# # Additionally, we can call the aggregation methods as above, but now we get
# # a result per column (which makes sense, we do not want to average
# # gdps together with populations). Set numeric_only to True to avoid errors.
countries_data.mean(numeric_only=True)

# Example 11
# Change the next line so that sum_pop_countries_data computes the sum of
# the populations from countries_data, rounded to one decimal.
sum_pop_countries_data = ...

# Change the next line so that std_gdp_countries_data computes the standard deviation of
# the gdp from countries_data, rounded to one decimal.
std_gdp_countries_data = ...

# Example 12
# Test cell; please do not change!
_ = ok.grade('q2')
```

## H.2 Loading and Inspecting Data

          Once you understand the basic DataFrame structure, the next step is to load data from an external file. In practice, much of data analysis begins by importing a dataset and checking its structure.

          This part introduces loading a CSV file, inspecting rows and columns, viewing summary statistics, and producing a simple plot directly from pandas.

## Python Code Examples: Loading and Inspecting Data

```python
# Example 1
# # Let's load the first csv file.
data = pd.read_csv('data/titanic.csv')

# # Printing the shape of the dataset we have just loaded.
print(data.shape)

# # The first step in data analysis is the exploration step.
# # We want to verify that a) our dataset is appropriately loaded,
# # b) get a sense of what values it has.
# # Let's display the 5 first rows:
data.head(5)
# # (When we run this in the Notebook, we will get a nice
# #  HTML representation of the table.)

# Example 2
data.describe()

# Example 3
# # Pandas also allow us to plot values directly.
# # Let's plot a histogram of the age of the passengers
# # pandas can create plots using a package called matplotlib
# # (matplotlib must be installed in your environment)
data.hist(column='Age')

# Example 4
# Change the next line so that age_passenger_10 computes the age of
# the 10th passenger.
age_passenger_10 = ...

# Change the next line so that cabin_194_passenger computes the
# cabin number of the 194th passenger.
cabin_194_passenger = ...

# Example 5
# Test cell; please do not change!
_ = ok.grade('q3')

# Example 6
# Change the next line so that it computes ticket number/id of
# the 100th passenger
ticket_i_th_passenger = ...

# We've put this line in this cell so that it will print
# the value you've given to ticket_i_th_passenger when you
# run it.  You don't need to change this.
ticket_i_th_passenger

# Example 7
# Test cell; please do not change!
_ = ok.grade('q4')
```

## H.3 Accessing, Modifying and Filtering Data

          After loading a dataset, you often need to access specific rows, extract columns, remove unnecessary data, replace values, or create new variables. These operations are central to preparing data for analysis.

          This part focuses on indexing, column selection, dropping rows or columns, replacing values, inserting new fields, and filtering observations that meet specific conditions.

## Python Code Examples: Accessing and Modifying Data

```python
# Example 1
data.head(5)

# Example 2
# # Let's delete the first and the third
# # passengers (remember the indexing in
# # python starts from 0).
data.drop([0, 2], axis=0).head(5)

# Example 3
# # Apart from that, you can also delete whole columns or rows.
# # For instance, for your problem, the Cabin column might be
# # irrelevant, let's delete it.
data.drop(['Cabin'], axis=1).head(5)

# Example 4
data.head(5)

# Example 5
# # Let's check that the data type is the same.
print(type(data))
# # What about the return type from a drop operation?
print(type(data.drop(['Cabin'], axis=1)))

# Example 6
# Change the next line so that it computes the reduced data matrix.
reduced_data = ...

# We've put this line in this cell so that it will print
# the value you've given to reduced_data when you
# run it.  You don't need to change this.
reduced_data.head()

# Example 7
# Test cell; please do not change!
_ = ok.grade('q5')

# Example 8
data.replace('male', 1).head(5)

# Example 9
# # An alternative way to replace the data is the following:
data['Sex'] = data['Sex'].map({'female': 1, 'male': 0})

# Example 10
data.head(5)

# Example 11
# # Right after the Sex, we want to include a new field named 'Nationality'.
# # Since most of the passengers are Irish, we will by default assign
# # the label 'Irish' to them and refine for those that are not.
data.insert(5, 'Nationality', 'Irish')

data.head(5)

# Example 12
# # Let's assume for a moment that the nationality of
# # those with Age NaN is Other European (hence why there
# # are no records of their age).
# # We want to replace the default nationality with
# # their known nationality.

# # Don't worry about how this works for now, it will be clear when we cover numpy.
import numpy as np
for index, row in data.iterrows():
    if np.isnan(data.loc[index, "Age"]):
        data.loc[index, "Nationality"] = "European"

# Example 13
data.head(10)

# Example 14
# # What we've done above is to replace some of the nationalities with 'European'.
# # One property of pandas that we've utilised for that is the '.loc'.
# # Let's explore that a bit more:
print(data.loc[3])

# Example 15
# # As typically done in higher level libraries in python, '.loc' offers a great deal of functionality.
# # You can find furthr information by executing data.loc??
help(data.loc)

# Example 16
european_bool = data['Nationality'] == 'European' # creates Booleans for each entry
print(european_bool.head(10))
# We could then pick only these records with
europeans = data[european_bool]
# If we want to count different values, we can do
data['Nationality'].value_counts()
# Counting how many non null values exist would be data['Nationality'].count()
```

## H.4 Practice and Titanic Extension

          This part provides additional practice using the Titanic dataset. The aim is to reinforce core pandas skills by asking you to compute values, subset data, and apply the earlier tools to a more realistic dataset.

          Treat these examples as an opportunity to experiment. Run the code, inspect each output, and adjust small parts of the commands to test your understanding.

## Python Code Examples: Optional Practice

```python
# Example 1
# Change the next line so that it computes the number of
# people with European nationality.
n_european = ...

# Change the next line so that it computes the number of
# people for which we have cabin information.
n_passengers_cabin = ...

# Example 2
# Test cell; please do not change!
_ = ok.grade('q6')

# Example 3
# Change the next line so that it computes a new dataframe
# that includes only the people with Pclass = 2.
# One way to use conditions in pandas is directly with data[CONDITION]
only_pclass2 = ...

# We've put this line in this cell so that it will print
# the value you've given to only_pclass2 when you
# run it.  You don't need to change this.
only_pclass2.head()

# Example 4
# Test cell; please do not change!
_ = ok.grade('q7')

# Example 5
import pandas as pd

# Example 6
# Reads the file titanic.csv
data_org = pd.read_csv('data/titanic.csv')

# Reads the file nationalities.csv
data_nat = pd.read_csv('data/nationalities.csv')
```

## H.5 Advanced DataFrame Processing

          The final part introduces more advanced DataFrame workflows. These include combining datasets, selecting data conditionally, applying transformations, and carrying out grouped calculations.

          These techniques are widely used in empirical finance, economics, and data science because real datasets often need to be merged, cleaned and transformed before analysis.

## Python Code Examples: Advanced DataFrame Processing

```python
# Example 1
# # First, let's ensure that the two datasets have the same number of elements (passenger data).
assert data_org.shape[0] == data_nat.shape[0]

# Example 2
# # Let's print the heads of the two datasets to figure out if there are any common elements.
data_org.head(5)

# Example 3
data_nat.head(5)

# Example 4
# # We are ready to perform the merging. Observe that the datasets share a common column in
# # the PassengerId, so we will use it to combine the data.
data_new = data_org.merge(data_nat, on='PassengerId')

# # Let's see what we've created now.
data_new.head(5)

# Example 5
# # Pandas offers several convenient methods for conditional selection and actions on them.
# # For instance, above we worked on getting useful aggregate statistics
# # over the whole dataset (do you remember the commands?).
# # However, often we'd like to select only a subset of the data based on some condition.
# # For instance, let's say we would like to print the average age per class.
# # One way to do that would be to iterate over all the elements, create a list, sum them
# # and then compute the average.
# # But pandas conveniently allows us to do it with a single command.
# # It works as follows:
# # First we group the data by the class, then we ask pandas to compute the mean of the age.
print(data_new.groupby(['Pclass'])['Age'].mean())

# Example 6
# # In the command above, we've averaged both men and women based only on the Pclass.
# # However, we could separate the two sexes and compute the mean for each sex.
print(data_new.groupby(['Pclass', 'Sex'])['Age'].mean())

# Example 7
# # We will now drop few columns that contain strings to mention few methods for statistical processing.
data = data_new.drop(['Cabin', 'Name', 'Ticket', 'Embarked', 'Nationality', 'Sex'], axis=1)

# Example 8
# # We can for example "clip" the values, i.e. restrict them in a chosen interval.
# # Notice that some values were greater than our upper bound, but are now
# # restricted to the maximum upper bound we set.
data.clip(lower=0, upper=40).head(5)

# Example 9
# # If the method we would like to apply to the data does not exist, we can use the
# # '.apply' method that allows us to choose any function to be applied to each record.
# # One way to do this is through an "anonymous" lambda function.
# # This works as defining a function without an explicit name to apply to each record
data["SurvivedPlusOne"] = data["Survived"].apply(lambda x: x + 1)
data.head(5)
```
