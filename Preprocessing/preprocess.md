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
            