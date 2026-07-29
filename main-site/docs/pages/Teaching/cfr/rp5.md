---
hide:
  - title
  - footer
---

Libraries are pre-defined collections of operations intended for specific purposes. The libraries are customizable to several extents and created by contributors to carry out multiple programming without re-programming all steps.

To view the list of available libraries in a current sessions use either of the following commands:
=== "Code"
    ``` SLexer title="Installing R Libraries" linenums="1"
    search()        # Show the list of loaded libraries
    sessionInfo()   # Loaded libraries in addition to R system information
    ```
=== "Results (Console)"
    ![Image title](/../assets/res6.png){ align=left }

When the software is freshly started, the list of available libraries appear to around ten items. Installing and calling further libraries lead to the list above to be updated for further monitroing. 

## Installation

While ordinary operations can be programmed by a developer at each instance, it is often considered more time-efficient to rely on a pre-existing packages to achieve the same end results. Libraries are required to be installed via `install.packages("name")` as illustrated in the example below, prior to calling the tools they offer. As a general practice, libraries are stacked and called at the beginning of a large section of code to ensure they are processed before executing the subsequent computations. 

=== "Code"
    ``` SLexer title="Installing R Libraries" linenums="1"
    search()        # Show the list of loaded libraries
    sessionInfo()   # Loaded libraries in addition to R system information
    ```
=== "Results (Console)"
    ![Image title](/../assets/res6.png){ align=left }

=== "Results (Newly installed software)"
    ![Image title](/../assets/res7.png){ align=left }
    [Rtools42](https://cran.rstudio.com/bin/windows/Rtools/rtools42/rtools.html)


Once the R program reaches a line including the command `library()`, it automatically searches (i) the local working directory and subsequently (ii) accesses [CRAN](https://cran.r-project.org/web/packages/available_packages_by_name.html) online repository to download and install them. As a practice, developers rely on the online repositories - this has to be downloaded only once for installation, however, each R program session or separate editor code requires the intended libraries to be called in order for the subsequent components to access and apply their tools. 

=== "Code"
    ``` SLexer title="Installing R Libraries" linenums="1"
    library(ggplot2)    # Visualization
    library(tidyverse)  # Data manipulation, exploration and visualization
    ```


# Libraries

!!! info "Library Repositories"
    [Library Repository](https://cran.r-project.org/web/packages/available_packages_by_name.html)