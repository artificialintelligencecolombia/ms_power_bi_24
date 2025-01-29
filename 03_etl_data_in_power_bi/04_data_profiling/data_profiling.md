# Data Profiling
Troubleshooting data:
- It consists in the evaluation of the data before being analyzed. We analyze data based on:
    - Completeness
    - Consistency
    - Accuracy
    - Alignment
    - Validity
    - Uniformity
    - Integrity
    - Timeliness

This analysis is performed especially in numerical fields.

### Evaluation of numerical fields
1. minimum or min, 
2. maximum or max, 
3. average or mean, 
4. frequently occurring values or mode and 
5. standard deviation. 

### Distribution of data
- How data points are distributed or arranged in a dataset
- Its part of the overall characteristics of the data
- Describes the shape or patttern of data when plotted on a graph.
- It helps us gain insights about the central tnendency, variability 

#### Outliers
Data point tha significantly deviates from other observations

**SOLUTION**: min/max scaling or normalization

#### Std deviation
- Statistical measure that quantifies the amount of variation or dispersion of a dataset.
- It prevents outliers from causing deviations in the analysis

### Power BI's data profiling tools
**Unique**: total number of values appearing once
**Distinct**: total number of different values regardless of how many of each the dataset has

Power Query -> View ribbon -> ...
    Column quality: (Valid, Error, Empty rows analysis -> %'s)
    Column distribution: (distinct, unique)
    Column profile: (min, max, avg, mode, std deviation, value distribution) of the column selected 