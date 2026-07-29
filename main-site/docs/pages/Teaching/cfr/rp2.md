---
hide:
  - title
  #- footer
  #- toc
---



To use the software for data exploration, visualization, and statistical analysis, two main installations are required:

1. **Software Core Engine**: The software core platform is developed by the R-Project and can be downloaded from the [Installation Page](https://cran.r-project.org). While the core platform provides a basis including the main abilities, it is considered less user-friendly thus an additional user-interface is needed to utilise the software to a fuller extent. 

2. **R-Studio**: A graphical user-interface "[R-Studio](https://posit.co/download/rstudio-desktop/#download)" provides the suitable tools to apply the core engine to data and statistical analyses, e.g. separately developing and executing code, provide a visual interface to inspect and manage existing variables, etc. This additional platform serves as an *Integrated Development Environment* (IDE) which acts in between the basis core engine and the user and enables accessing and managing resources. R-Studio is not the only user-interface and alternatives can be used. [Cloud-Based Environments](https://posit.cloud) are also available to enable web-based computations. While both the core engine (1) and R-Studio are freeware packages, other desktop- or cloud-based solutions may be subject to fees.  

After installations, the software environment is ready for launch. As a third step, additional [*libraries*](rp5.md) are required to be installed. Each library provides specialised toolboxes intended for further productivity such as visualisation, obtaining statistical properties and similar context-dependent features (explained in the page sections). 

=== "R-Studio"
    !!! note "R Engine and R-Studio"
        ![Image title](/../assets/rstudio.png){ align=right }
            The R Programming Language has been ranked between numbers 8 and 73 by the TIOBE Index during 2007-2023 with the current standing at 19th position. The ranking captures an overall popularity amongst a wide range of object-oriented, database and computational languages. Note while all packages share capabilities to carry out numerical and dataset computations, several of the higher rating languages are often considered less focused on statistical analysis. Integrating the consensus within our contexts together with the TIOBE index ranks R after Python, Matlab, and Fortran.

=== "R Engine"
    !!! note "R Engine and R-Studio"
        ![Image title](/../assets/rmain.png){ align=left }
            The R Programming Language has been ranked between numbers 8 and 73 by the TIOBE Index during 2007-2023 with the current standing at 19th position. The ranking captures an overall popularity amongst a wide range of object oriented, database and computational languages. Note while all packages share capabilities to carry out numerical and dataset computations, several of the higher rating languages are often considered less focused on statistical analysis. Integrating the consensus within our contexts together with the TIOBE index ranks R after Python, Matlab, and Fortran.



The course refers to the R-Studio henceforth as the primary interface. R-Studio provide four main panels:

- Top left (as illustrated above) is the *Editor* where operation are coded line by line without executing. This panel is used to developing sections of code and editing code in preparation for executing. Each line is numbered and later executed in the same order.
- Top right panel is the *workspace* providing a visual illustration of the existing objects already created and stored in the software. These objects (variables, numbers, vectors, etc.) are accessible by the developer and can be called into operations, deleted or replaced.
- Bottom left panel is the *RConsole* where a user can interact with the software via entering separate lines of code which are instantly executed. 
- Bottom right panel provides additional interfaces such as the *working directory* where the software assumes as the default filing location to input and output information. It is essential to match the location of the working directory correctly to the intended location where data files are stored otherwise the software is unable to access and operate on the data.

## Interacting with R-Studio
The editor window is a coding space to develop the code and prepare for execution. The software then executes each line by applying the functions or commands to the software space, variables, etc. note that the editor window disregards code or lines of code when '#' is entered which instructs the software to skip over the contents after '#' within the same line. 

- *Commenting*: Using '#' is considered a good practice to add comments to the same coding environment for the purpose of informing readers (or for future references). This commonly is considered a requirement when working as a part of a teamwork where the code is partially developed and passed to other contributors for further implementations where comments provide further context for others to better follow the logic behind the coded sections, variable naming practices, external references, etc.

- *Executing Code*: Pressing ctrl+enter runs the entire code contents in the editor window. Highlighting a subsection of the code followed by pressing ctrl + enter amounts to the selection of the code to be executed. As a counterpart, once a section of the code is selected for execution, the operation can be cancelled by repeating ctrl+enter. Note that for short sections of code, the execution takes place very fast and there is limited scope to attempt cancellation. Nevertheless, longer segments of code with several iterations may take longer to run and cancellation is important to abort and amend.

!!! info 
    It is essential to ensure the working directory is correctly set up. This involves instructing R to assume a default filing position on the computer via `setwd("location")` command displayed below, where the location indicates a local address. Once a working directory is set up, it subsequently can be checked via `getwd()` where the parentheses is left blank. Executing `getwd()` leads to the original location address to be printed out on the output window:
    

=== "Code"
    ``` SLexer title="Setting Working Directory" linenums="1"
    setwd("C:/r/class1")   # Set up the working directory
    getwd()                # print out assumed location
    ```

=== "Results (Console)"
    ![Image title](/../assets/res1.png){ align=left }

Interaction with the software leads to storing new information in the memory or changing the default setting. When starting a new session in R-Studio, the software begins with a clean workspace. However, after interacting with the software through only a few commands, the memory tracks inputted commands and changes according to the interactions. Suppose instead of directly entering the directory address into the `setwd("C:/r/class1")`, the code is set up to first store the directory address as a text value into a variable `x = "C:/r/class1"` which then carries its value to the next line for setting the address as the default working directory:

=== "Code"
    ``` SLexer title="Clearing Memory" linenums="1" 
    x = "C:/r/class1"    # New text variable
    setwd(x)             # Set up the working directory
    getwd()              # print out assumed location
    rm(list=ls())        # Clear working space (variables, memory)
    cat("\f")            # Clear console
    ```
    ![Image title](/../assets/res0.png){ align=left }


=== "Results (Workspace Variable Created)"
    ``` SLexer title="Clearing Memory" linenums="1" hl_lines="1 2 3"
    x = "C:/r/class1"    # New text variable
    setwd(x)             # Set up the working directory
    getwd()              # print out assumed location
    rm(list=ls())        # Clear working space (variables, memory)
    cat("\f")            # Clear console
    ```
    ![Image title](/../assets/res2.png){ align=left }

=== "Results (Workspace Variable Cleared)"
    ``` SLexer title="Clearing Memory" linenums="1" hl_lines="4 5"
    x = "C:/r/class1"    # New text variable
    setwd(x)             # Set up the working directory
    getwd()              # print out assumed location
    rm(list=ls())        # Clear working space (variables, memory)
    cat("\f")            # Clear console
    ```
    ![Image title](/../assets/res3.png){ align=left }

In the example above the value `x` is stored in the software workspace and remains as an accessible information for future use. When needed, this added value can be erased via the command in line 4: `rm(list=ls())`. Note that the entire workspace is cleared including the value for `x`. Deleting individual variables is possible via ...

The coded section above can be copied into the editor window and saved as a `.Rmd` file as the default saving format.


## Basic Objects 

- Operators
- Commands
- Variables
- Functions


## Accessing Built-in Help Documentations

=== "Code"
    ``` SLexer title="Accessing Help Files" linenums="1" 
    ?setwd()
    ?getwd()
    ```

=== "Results (Bottom-right Panel)"
    ![Image title](/../assets/res5.png){ align=left }