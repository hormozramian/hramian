---
hide:
  - toc
---

# Session 1: Foundations of Python

## Overview

This session introduces programming and Python from first principles, starting with what coding actually is, moving through the practical tools used to write and run Python code, and ending with the first real building blocks of the language itself: displaying output, storing values, performing calculations, documenting code, repeating actions, and organising code into reusable functions.

The session is organised into a sequence of parts:

- **Foundations of Programming** — what a programming language is, and how Python compares along several key dimensions: interpreted versus compiled, high-level versus low-level, general-purpose versus domain-specific, dynamically versus statically typed, and multi-paradigm versus single-paradigm.
- **What is Python?** — the core properties that define Python specifically, high-level, general-purpose, interpreted, dynamically typed, and multi-paradigm, and why this combination makes it so widely used.
- **Jupyter Notebooks** — installing Anaconda, and understanding what a Jupyter Notebook is and why it's such an effective environment for learning and documenting analysis.
- **Cells and Executing Code** — how notebooks are organised into individual code and Markdown cells, and how to run, edit, and document a notebook using them.
- **The Print Statement** — using `print()` to display output and get immediate feedback from your code.
- **Setting Variables** — storing, naming, and reusing values with variables.
- **Mathematical Operators** — performing calculations using Python's arithmetic operators.
- **Comments** — writing notes in source code that explain your thinking without affecting how the program runs.
- **Python Development Environments** — stepping back to survey the wider landscape of tools Python programmers use, beyond Jupyter Notebooks, both local and cloud-based.
- **Virtual Environments** — isolating a project's Python version and packages from other projects, to avoid conflicts and improve reproducibility.
- **Python Documentation** — learning to look up how a command or function works, rather than relying on memorisation.
- **Loops** — repeating a block of code automatically, using `for` and `while` loops.
- **Functions** — grouping code into reusable, named blocks, including an introduction to recursion.

Programming is a skill built in layers, before you can write anything useful, you first need somewhere to write and run it, then a small, reliable vocabulary of core commands, and finally the tools that let you scale beyond a few lines of code into something more substantial. This session deliberately follows that order: it starts by explaining what coding and Python actually are conceptually, moves into the concrete, practical environment (Jupyter Notebooks via Anaconda) used throughout the rest of the course, introduces the first genuine Python commands, printing, variables, operators, and comments, then steps back to the wider picture of tools, environments, and documentation before returning to loops and functions, the two ideas that make it possible to write programs that do more than execute once, top to bottom, and stop.

The purpose of this session isn't just to introduce a list of commands to memorise, it's to build the practical habits of a working programmer: getting comfortable typing and running code interactively, documenting your reasoning as you go, knowing where to look things up rather than trying to remember everything, and recognising when a repeated pattern in your code is a sign that a loop or a function belongs there instead.

By the end of the session, writing a short, working Python program, one that stores values, calculates a result, explains itself with comments, and perhaps repeats a step or two, should feel like a natural and achievable task, rather than an intimidating one.

Here is a brief list of key commands frequently used throughout this session.

| Motivation | Section |
| --- | --- |
| Displays output on the screen using **`print()`**, giving immediate feedback on a calculation, a variable's value, or where an error might be occurring, the single most useful command when learning to program. | The Print Statement |
| Stores and labels a value in memory using the **assignment operator** (`=`), for example `age = 25`, so it can be reused later simply by referring to its name. | Setting Variables |
| Performs calculations using Python's **mathematical operators** (`+ - * / ** % //`), which work directly on numbers or on variables that store numerical values. | Mathematical Operators |
| Adds a note to source code using the **`#`** symbol, ignored entirely by Python but useful for explaining your reasoning to other readers, including your future self. | Comments |
| Repeats a block of code automatically using a **`for` loop** (`for x in range(n):`) or a **`while` loop** (`while condition:`), avoiding the need to copy and paste repetitive instructions. | Loops |
| Groups a set of instructions into a single, reusable, named block using **`def`**, and sends a value back to the calling code using **`return`**. | Functions |
| Looks up how an unfamiliar command or function works using **`help()`**, or the Jupyter-specific shortcut **`?`** (e.g. `print?`), the standard way programmers learn a new tool without memorising it in advance. | Python Documentation |
| Keeps a project's Python version and packages isolated from other projects using a **Conda environment**, avoiding version conflicts and making a project easier to reproduce later. | Virtual Environments |
