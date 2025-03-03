# Time intelligence
- The most effective and powerful data insights a data analyst can generate are time-based.
- Time intelligence provides the ability of compare data over the time (understanding patterns and trends)
- Methods and processes that aggregate and compare data over time.
- Time-related dimensions: dates, weeks, months, quarters, years. It can also generate comparisons of time-related data on annual periods (YTD).
- It also enables real time performance monitoring (dynamic measures: YTD, MTD)

### Time-based summarization functions
Identify:
    - trends
    - patterns 
    - anomalies
in performance over a specific period.

- TOTALYTD, YTD, DATESBETWEEN

#### Time-based summarization functions syntax
Measure = function_name(arguments)

### YTD (Year To Date)
- calculates the cumulative total from the beginning of the year up to the selected date. It is commonly used for financial reporting, performance tracking, and business analytics.

```
Sales YTD Fiscal = TOTALYTD(
    SUM(Sales[Sales Amount]), // calculation
    Sales[Date], //date field used for aggregation
    "06/30") // end date(?)
```

### DATESYTD


### DATESBETWEEN

```
Summer Sales = CALCULATE(
    SUM(Sales[Sales Amount]), // calculation
    DATESBETWEEN(
        Sales[Date], // date field
        DATE(2020, 6, 1), // start date
        DATE(2020, 8, 31) // end date
    ))
```

