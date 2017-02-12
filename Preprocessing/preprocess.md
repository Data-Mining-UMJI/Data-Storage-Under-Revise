## Data Preprocessing:

***Data Type:*** 

* Documents
* Images
* Videos
* Audios

***Level-1:***

* Data cleaning (Noise/extreme points):
    + Eliminate extreme data points 
        - Data visualization, clustering/regression/binning (must be sequential datasets) to delete those data points OR smoothen those data points
    + Fill in missing data fields 
        - Omit missing ones/setting average values/fill in most possible value (Decision Tree..., Clustering, K-means...)
* Data integration:
    + Integrate resources from different databases
    + Problems (Redundancy):
        - Same info with different attribute names (eg: id, _id)
        - Same info with different attribute values (eg: Bill, Gates)
        - Problems resulting from the database updating
        - Non-structured mixed with structured data (data dependency missing)
    + Solutions:
        - Matching based on meta-data (data type, range, specification) to judge whether two info represent the same object
        - Redundancy (some data can be induced based on current data, eg: salary/year <= salary/month): Kai square analysis (correlation analysis) to solve the data dependency problem.

***Level-2:***

* Data Transformation (Massive Datasets, optimize feature extracting):
    + Reduce the data fields to a given range (based on special functions, z-score...)
    + Extract a higher concept layer (discrete) eg. young old ...
* Data Reduction (Massive Datasets, optimize the data mining efficiency on the data level):
    + [**Dimensional**] Figure out an efficient data representation instead of applying massive raw datasets
        - Data encoding/compression (file type)
        - Attribute Extracting (Select interesting fields)
    + [**Numerical**]
        - Mathematical transformation to represent the same data with smaller scale:
            + Parametric Model (regression, linear model)
            + Non-parametric Model (visualization, clustering, sampling)

***Workflow:***

* Data integration
* Data cleaning
* Data reduction
* Data transformation

* Motivation for Extracting Data to an external file instead of processing inside the database
    - We want to keep the raw data inside the DB to avoid losing useful features in one direction-oriented preprocessing.
    - With the external files, we can reuse them to run different algorithms.



### Data Cleaning

* Dealing with missing data:
    - Partial Deletion:
        + Listwise Deletion [Delete the problematic entries even if they contains useful info]
        + Pairwise Deletion [When dealing with the problematic entries which contains both useful and missing values, retain the useful fields while deleting the missing values]
        eg: LifeSpan (given birth dates but some don't have death dates), Height.
    - Imputaion:
        + Motivation: When the dataset is small, PARTIAL DELETION will fail since the related evaluated results are not representative.
        + Solution: Get imputed values, kind of guessing
            * [I] Get the mean of all the non-missed values: Don't change the mean, but not good when evaluating the relationship between field and field. (eg. Height v.s. Weight)
            * [II] Linear Regression:
                - Overemphasize/Amplify the trends, and all our data follows that trends.
                - Exact values suggest too much certainty. However, what's accurate is a kind of range.
            * More Robust approaches are left to be learnt...


### Data Integration

* Attributes Redundancy
    - Kai-Square Correlation Test: [Along with correlation coefficient and the covariance]
        + Restriction: Numerical, Finite range, nominal (classification) attributes [multi-variate case formulas not covered in the book.]
        + Working Pattern: Based on a contingency table <a_i, b_i>, where a_i, b_i correspond to the i-th entry of attribute A, B, we calculated a statistical result with specific formulas, then compare the result with the reference result table or 0 to decide whether A and B are positively/none/negatively dependent.
        + Reference Page: P41-42 in Springer's Book. [Check the corresponding formulas.]
    - Possible Reasons:
        + Denormalization Table (optimize the query performance in a human-readable way), and it will construct a lot of redundant entries.


* Data Encoding Problems

* Attribute Value Conflicts 


### Overall Restriction:

* Most approaches are based numerical data, and need spending more time to deal with other types.
