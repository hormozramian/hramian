---
hide:
  - title
  #- footer
  #- toc
---

## Operators



=== "Logical"
    ``` SLexer title="Clearing Memory" linenums="1"
    &   # and
    |   # or
    !   # not (negation)
    ```

=== "Assignment"
    ``` SLexer title="Clearing Memory" linenums="1"
    <−  # Left Assignment
    =
    <<−
    ->  # Right Assignment
    ->>
    ```

=== "Relational"
    ``` SLexer title="Clearing Memory" linenums="1"
    <   Less than
    >   Greater than
    <=  Less than or equal to
    >=  Greater than or equal to
    ==  Equal to
    !=  Not equal to
    ```

=== "Arithmetics"
    ``` SLexer title="Clearing Memory" linenums="1" 
    +   Addition
    -   Subtraction
    *   Multiplication
    /   Division
    ^   Exponent
    %%  Modulus(Remainder from division)
    %/% Integer Division
    ```


!!! question "Exercise: $0^0$"
    === "Exercise"
        Clear the workspace, program $0^0$ and verify your results:
        ``` SLexer title="Code" linenums="1" 
        rm(list=ls())        # Clear working space
        cat("\f")            # Clear console
        x = 0^0
        ```
    
    === "Answer"
        While in mathematical analysis, the expression $0^0$ is sometimes left undefined, in algebra and combinatorics, one typically defines $0^0 = 1$. In computer sciences, the standard answer is $0^0 = 1$.


!!! question "Exercise: $x!$"
    === "Exercise"
        Clear the workspace, program the factorial value $100!$:
        ``` SLexer title="Code" linenums="1" 
        rm(list=ls())        # Clear working space
        cat("\f")            # Clear console
        factorial(100)
        ```
    
    === "Answer"
        Note that the mathematical symbol for factorial is given by $x!$ whereas within the R language, `!` operates as *logical negation*. The factorial is computed using the function `factorial(100)` and equal to `9.332622e+157`.


!!! question "Exercise: $\pi$"
    === "Exercise"
        Clear the workspace, program the mathematical constant value $\pi$:
        ``` SLexer title="Code"  linenums="1" 
        rm(list=ls())        # Clear working space
        cat("\f")            # Clear console
        pi
        ```
    
    === "Answer"
        Note that the mathematical symbol for factorial is given by $x!$ whereas within the R language, `!` operates as *logical negation*. The factorial is computed using the function `factorial(100)` and equal to `9.332622e+157`.


!!! question "Exercise: Exponential $e^x$, and logarithmic function $\log(x)$, $\ln(x)$"
    === "Exercise"
        Clear the workspace, program the following:
            
        - mathematical constant value $e^1$,
        - compute $\log(e)$.

        ``` SLexer title="Code"   linenums="1" 
        rm(list=ls())        # Clear working space
        cat("\f")            # Clear console
        exp(1)
        log(exp(1))
        ```
    
    === "Answer"
        R language provides a default logarithmic fuction `log()` operating as the natural logarithm. While there exists a short hand function `log10(x)` to carry out the base-10 as a special case, more general cases can be defined via inputting an extended argument: `log(x, base = 10)`.



!!! question "Exercise: Price of a three-year bond"
    === "Exercise"
        Clear the workspace, program the following which reflect the present value of a three-year 3% annual coupon bearing bond with the face value of $100 and a 5% market discount rate: 

        $\frac{5}{1+5\%} + \frac{5}{(1+5\%)^2} + \frac{5}{(1+5\%)^3} + \frac{100}{(1+5\%)^3}$

        ``` SLexer title="Code"   linenums="1" 
        rm(list=ls())        # Clear working space
        cat("\f")            # Clear console
        exp(1)
        3/(1+0.05) + 3/(1+0.05)^2 + 3/(1+0.05)^3 + 100/(1+0.05)^3    
        ```
    
    === "Answer"
        R language provides a default logarithmic fuction `log()` operating as the natural logarithm. While there exists a short hand function `log10(x)` to carry out the base-10 as a special case, more general cases can be defined via inputting an extended argument: `log(x, base = 10)`. 