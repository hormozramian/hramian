---
hide:
  - footer
---

<!-- **[Course Syllabus PDF](/../assets/course_syllabus_5246.pdf)**  -->

## Overview

Addressing real-world economic and financial problems via information embedded in data is an active area of academic and professional interests. This course contributes towards this goal with the following two approaches. First, the course provides a foundation to methodically structure large-dimensional datasets and summarise information into interpretable outcomes.

The second part of the course examines how the combination of large datasets accompanied by statistical learning and artificial intelligence techniques are helping practitioners to make more efficient economic and financial decisions. The cwourse is delivered based on a balanced combination of (1) descriptive contents required to formulate financial and economic problems into quantifiable objects of interest, (2) analytical derivations and statistical techniques and (3) software programming.

The course is structured based on four pillars. All pillars are equally weighted in terms of course contents and examinations but also in terms of their importance towards developing a foundation for future careers in data science and machine learning in finance within or outside academia:

 * Data
 * Methodological Frameworks
 * Software Implementations
 * Finance Theory and Applications

## Course Contents
the course may not cover all areas of ML techniques. Instead, topics are selected according to their relevance for developing a foundation in ML, to understand advanced levels, and their relevance towards common applications in the finance industry 

# Course Topics

??? note "Course Coverage (Topics in This Course)"

    | | **Non-Shrinkage** | **Shrinkage / Regularised** |
    |:---|:---|:---|
    | **Supervised Learning** | - Ordinary Least Squares (OLS)<br>- Logistic Regression<br>- k-Nearest Neighbours (k-NN) | - Constrained Least Squares (CLS)<br>- Ridge Regression<br>- LASSO (L1)<br>- Elastic Net<br>- Regularised Logistic Regression<br>- Support Vector Machines (SVM)<br>- XGBoost<br>- LightGBM<br>- Regularised Neural Networks |
    | **Unsupervised Learning** | - Principal Component Analysis (PCA) | - Sparse PCA<br>- Regularised PCA |

??? note "Extended Machine Learning Landscape - for self-study and further research"

    | | **Non-Shrinkage** | **Shrinkage / Regularised** |
    |:---|:---|:---|
    | **Supervised Learning** | - Ordinary Least Squares (OLS)<br>- Logistic Regression<br>- Decision Trees (CART)<br>- k-Nearest Neighbours (k-NN)<br>- Naïve Bayes | - Constrained Least Squares (CLS)<br>- Ridge Regression<br>- LASSO (L1)<br>- Elastic Net<br>- Regularised Logistic Regression<br>- Support Vector Machines (SVM)<br>- Random Forests<br>- Gradient Boosting<br>- XGBoost<br>- LightGBM<br>- CatBoost<br>- Regularised Neural Networks (Weight Decay, Dropout, Early Stopping) |
    | **Unsupervised Learning** | - Principal Component Analysis (PCA)<br>- Hierarchical Clustering<br>- k-Means Clustering<br>- Gaussian Mixture Models<br>- Independent Component Analysis (ICA)<br>- t-SNE<br>- UMAP | - Sparse PCA<br>- Regularised PCA<br>- Sparse Autoencoders<br>- Denoising Autoencoders<br>- Variational Autoencoders (VAE)<br>- Regularised Matrix Factorisation |

## Outline

| **Topic** | **Title** | **Libraries / Platforms** | **Financial Data** | **Online AI Tools** |
|:---:|---|---|---|---|
| **1** | Foundations of Financial Data Science | Google Colab, GitHub Codespaces, Pandas, NumPy, yfinance | CRSP, Yahoo Finance | ChatGPT, GitHub Copilot |
| **2** | Statistical Learning: Linear and Regularised Models | Scikit-learn, Statsmodels, CVXPY, SciPy | CRSP–Compustat (CCM), Kenneth French Data Library | ChatGPT, Claude |
| **3** | Supervised Classification Techniques | Scikit-learn, Statsmodels, SciPy | LendingClub Loan Data, Fannie Mae Loan Performance Data | ChatGPT, GitHub Copilot |
| **4** | Unsupervised Learning and Dimensionality Reduction | Scikit-learn, UMAP, HDBSCAN | Fama–French Factor Data, CRSP Equity Returns | ChatGPT, Claude |
| **5** | Machine Learning for Asset Pricing | XGBoost, LightGBM, CatBoost, SHAP | CRSP, Compustat | ChatGPT, Perplexity AI |
| **6** | Reinforcement Learning | Gymnasium, Stable-Baselines3, FinRL, PyTorch | Yahoo Finance, Alpaca Historical Market Data | ChatGPT, GitHub Copilot |
| **7** | Neural Networks and Deep Learning | PyTorch, TensorFlow, Keras, Lightning | CRSP, Nasdaq Data Link | ChatGPT, Google AI Studio |
| **8** | Tree-Based Machine Learning | Scikit-learn, XGBoost, LightGBM, CatBoost | Compustat, CRSP–Compustat (CCM) | ChatGPT, Claude |
| **9** | AI for Financial Risk Management | XGBoost, SHAP, MLflow, PyPortfolioOpt | Moody's Default & Recovery Database, LendingClub Loan Data | ChatGPT, Microsoft Copilot |
| **10** | Explainable Artificial Intelligence (XAI) | SHAP, LIME, PDPbox, MLflow | CRSP–Compustat (CCM), LendingClub Loan Data | ChatGPT, Claude |
| **11** | Natural Language Processing *(Tentative)* | Transformers, spaCy, Sentence-Transformers, OpenAI API | SEC EDGAR Filings, Earnings Call Transcripts | ChatGPT, Perplexity AI, NotebookLM |


### Topic 1: Foundations of Financial Data Science
Financial markets and financial time series, data acquisition and management, feature engineering, firm-level characteristics, panel data from quarterly financial reports, time-series dynamics, exploratory data analysis, and correlation analysis *(Google Colab, GitHub Codespaces, Pandas, NumPy, yfinance; Datasets: CRSP, Yahoo Finance).*

### Topic 2: Statistical Learning: Linear and Regularised Models
[Linear Algebra Foundations](../../assets/Linear_Algebra_Notes.pdf), matrix rank and inverses, least squares estimation, constrained least squares (CLS), Ridge, LASSO (L1), Elastic Net, shrinkage methods, hyperparameter tuning, forecast mean squared error (FMSE), and model selection *(Scikit-learn, Statsmodels, CVXPY, SciPy; Datasets: CRSP-Compustat Merged (CCM), Kenneth French Data Library).*

### Topic 3: Supervised Classification Techniques
Logistic regression, regularised logistic regression, k-Nearest Neighbours (k-NN), and Support Vector Machines (SVM) for financial classification problems *(Scikit-learn, Statsmodels, SciPy; Datasets: LendingClub Loan Data, Fannie Mae Loan Performance Data).*

### Topic 4: Unsupervised Learning and Dimensionality Reduction
Principal Component Analysis (PCA), Sparse PCA, Regularised PCA, nonlinear dimensionality reduction, feature extraction, and latent factor discovery *(Scikit-learn, UMAP, HDBSCAN; Datasets: Fama-French Factor Data, CRSP Equity Returns).*

### Topic 5: Machine Learning for Asset Pricing
Predictive modelling for asset returns, factor discovery, feature importance, model validation, and systematic investment strategies *(XGBoost, LightGBM, CatBoost, SHAP; Datasets: CRSP, Compustat).*

### Topic 6: Reinforcement Learning
Markov Decision Processes, Q-Learning, Deep Q Networks (DQN), policy gradient methods, and financial decision-making applications *(Gymnasium, Stable-Baselines3, FinRL, PyTorch; Datasets: Yahoo Finance, Alpaca Historical Market Data).*

### Topic 7: Neural Networks and Deep Learning
Feedforward neural networks, regularised neural networks (L1/L2 penalties), weight decay, dropout, and predictive modelling for financial data *(PyTorch, TensorFlow, Keras, Lightning; Datasets: CRSP, Nasdaq Data Link).*

### Topic 8: Tree-Based Machine Learning
Decision trees, ensemble learning, gradient boosting, XGBoost, and LightGBM for prediction and classification *(Scikit-learn, XGBoost, LightGBM, CatBoost; Datasets: Compustat, CRSP-Compustat Merged (CCM)).*

### Topic 9: AI for Financial Risk Management
Machine learning methods for credit risk, market risk, operational risk, default prediction, stress testing, and model governance *(XGBoost, SHAP, MLflow, PyPortfolioOpt; Datasets: Moody's Default & Recovery Database, LendingClub Loan Data).*

### Topic 10: Explainable Artificial Intelligence (XAI)
Model interpretability using SHAP, LIME, partial dependence plots, feature importance, and explainable machine learning for financial decision-making *(SHAP, LIME, PDPbox, MLflow; Datasets: CRSP-Compustat Merged (CCM), LendingClub Loan Data).*

### Topic 11: Natural Language Processing *(Tentative)*
Sentiment analysis, financial text mining, transformer models, and applications to earnings calls, financial news, and regulatory filings (subject to time availability) *(Transformers, spaCy, Sentence-Transformers, OpenAI API; Datasets: SEC EDGAR Filings, Earnings Call Transcripts).*




## Prerequisites
There is no formal prerequisite, however a prior background including calculus, statistics and regression  is favourable. The course assumes familiarity with the estimation and inference of the least squares framework covered earlier in the semester one courses.

## Course Timetable
The course is delivered via weekly sessions and four tutorial workshops. There are three practice problem sets with solutions to further illustrate theories and implementations, followed by three assessment assignments outlined in the semester timetable below. The timetable below is subject to change, please review this timetable on weekly basis:

[Course Schedule](/../assets/DSML Timetable.pdf)

## Office Hours

Friday 9-10 am (Gilbert Scott Building)  

## Course Tutorials and GTA Support
You are expected to have covered the material ahead of the tutorials. There are two weekly tutorial classes delivered by the following course GTAs, starting in week 3. The schedule will be posted on [MyGlasgow](https://www.gla.ac.uk/myglasgow/students/).  



### Analytical Tutorials
The classes are arranged to practice analytical problem sets. The first two weeks provide a brief summary of matrix calculus and statistical inference:  

- Hadi Movaghari  
- (i) Mondays 9-10, (ii) Thursdays 4-5, (iii) Fridays 5-6 
- TA Office Hours

### Software Tutorials
The classes are arranged to build up computational foundations to work with data and methodological frameworks:  

- Tongtong Wang  
- (i) Mondays 4-5, (ii) Mondays 5-6, (iii) Thursdays 5-6 
- TA Office Hours Fridays 1-2pm

## Computations
### Financial Datasets and Empirical Exercises

The course contents, practice problem sets and assessment components are based on real-world financial data. It is a requirement that all class participants set up their accounts with the data platforms described below:

 - Register your accounts on Financial Analysis Made Easy (FAME) via the university library and additionally Wharton Research Data Services directly on their platform using the university email address.
 - This registration is then activated by the business database administration within one week. Please initiate the registration in the first week of the course before we progress towards further course contents and assignments.
 - Key statistics and learning outcomes arising from the activities related to the data will be part of the exam.
Treat the empirical exercises as an essential part of the learning experience 
 - As a financial analyst or a research financial economist, you will work with the very same data providers repeatedly. Developing an understanding of the empirical counterparts of theories will be an important takeaway for future careers in finance.

### Software Packages and Implementations

Computational and methodological frameworks are implemented in [Matlab](https://www.gla.ac.uk/myglasgow/it/softwareandonlinetools/matlab/). An additional spreadsheet is needed for supplementary data transformation and visual inspection, e.g. Libre Office, AWK or Excel (with Analysis ToolPak and Solver Add-in packages enabled). Please make sure you have set up both packages during the first week of the course to be able to practice exercises, replicate examples and complete assignments.

### Computational Requirements
All course material and exercises are designed such that the learning outcomes are achieved based on any computer. However, you may also prefer to consider exploring the following available options to enhance computational capacity and further familiarising yourselves with professional computing systems:

- **University HPC** Access to [HPC](https://www.gla.ac.uk/myglasgow/it/hpcc/) machines are provided for research and education purposes. You will be able to access these resources depending on your computational requirements.
- **Google Cloud**: Machine template is KX8765D, you will need to set up a new machine following the template ID which provides limited free service for the purpose of the class exercises. 

## Problem Sets
- [Problem Set 1](/../assets/dsml_pset1.pdf)
- [Problem Set 2](/../assets/dsml_pset2.pdf)



## Assessments
The course summative assessment comprises the following four components:

 - **Quiz (15%)** will be made available to access on during week 4 via Moodle. The quiz will be accessible to start within a 24 hours window, and once started the allowed time to complete is 60 minutes. This is an individual assessment and only one attempt is allowed. The quiz comprises multiple-choice questions covering course contents during the first four weeks including methodological learning outcomes, key facts and statistics arising from the numerical and empirical exercises.
 - **Group Assignment (25%)** includes a problem sheet requiring methodological derivations, numerical computations followed by interpretation of results. The problem sheet will be posted during mid February..
 - **Degree exam in April/May (60%):** The final exam will be an individual assessment covering all course contents during the semester including key facts and statistics arising from empirical exercises, class reports and commentaries, methodological derivations and computations. Information regarding the final examination will be released towards the end of the semester.

### Grading
 - Grading is based on meeting the course intended learning outcomes examined in each assignment and following the University's [Schedule A](https://www.gla.ac.uk/media/Media_124293_smxx.pdf). Grades are rewarded based on both the input and output presented in each part thus demonstrating intermediate steps building up towards an overall answer are required and graded.
 - Problem set and assignments require accessing real-world financial data from the professional platforms, thus class participants are required to register and activate their accounts with data providers by following the information provided.


### Feedback
Answers to the assignments will be provided in the subsequent week after the deadline and after everyone's submissions are received. Aside from the assessed assignments indicated above, the course includes two practice problem sets with solutions. These are distributed to practice theories and implementations during the semester. Students are expected to attend the office hours and tutorial workshops for reviewing specific queries.



### Past Papers
Past exam papers are available [via the university portal](https://www.gla.ac.uk/myglasgow/students/exams/). These can serve as a basis for preparation, however, note that the exam and course contents are subject to changes on an annual basis. 


## Textbook and Reading List

-  Applied Data Science: Lessons Learned for the Data-Driven Business, By Braschler, Stadelmann, Stockinger, [Online version](https://go.exlibris.link/b55hC7yp) available via the university library
-  The elements of statistical learning: data mining, inference, and prediction, By Hastie, Tibshirani, Robert, [Online version](https://go.exlibris.link/Nn6FyPN9  ) available via the university library
-  Machine Learning in Business: An Introduction to the World of Data Science, by John Hull
 
**Software References:**

- [Software Handout](/../assets/Matlab_2022.pdf)  
- MATLAB: a practical introduction to programming and problem solving, by Stormy Attaway, [Online version]( https://go.exlibris.link/VmBv2qDr) available via the university library

Further to the textbooks, there will be journal article readings cited throughout the course. Journal articles indicated as 'required reading' should also be studied in conjunction with textbook reading and form part of the assessments: [Reading List](/../assets/dsml_reading.pdf).