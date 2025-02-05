# Best Practices

### Enhance power query workflows
1. Plan and document
Stablish the desired output -> Identify data sources -> the transformations required -> Documentation over data source and credentials

2. Selection of proper connectors to connect to data sources
To keep a secured and well organized connection to data source, consider:
- Type and location of data sources
- Volume of data 
- Connectivity options

Note: Considering the performance and optimization of the data transformation process, it is recommended to follow the principle of "do expensive operations last"

#### Resource intensive operations:
- Complex calculations
- Merge large datasets
- Multiple transformations

By executing these steps last, the performance of the data transformation process is optimized.

3. Data type selection for columns. This improves the performance and data accuracy

4. Data profiling (data quality, structure and distribution). These features will be measured by: completeness, accuracy, uniqueness, consistency


5. Error handling
- Error handling  techniques
- Conditional logic
- Error messages
- Data validation checks
- Identify data inconsistencies

6. Merge strategy
- Most effective merging strategy
- Select inner joins when applicable
- Remove unnecessary/duplicated columns/rows

7. Create groups
Groups are like folders that help organize your queries
Grouping queries makes it easier to manage your work
Groups are just for organization—they don’t affect how the data is processed.

8. Remove unnecessary steps
- Unnecessary transformations

9. Monitoring performance
- Refresh speed
- Resources consumption
- Overall efficiency