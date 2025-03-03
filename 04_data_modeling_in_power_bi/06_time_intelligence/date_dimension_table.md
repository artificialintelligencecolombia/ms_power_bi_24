# Date Common Table
Its possible for a dataset to not have a Date dimension table, and Date dimension table is a prerequisite to perform time intelligence calculations.

### Date dimension table
- One record per day
- No missing or BLANK dates
- Must start with the min date and end with the max date in the dataset

Date dimension can be created using Power Query or DAX (CALENDAR, CALENDARAUTO)

### CALENDAR
```
Date =
CALENDAR ( 
    DATE ( 2019, 1, 1 ), 
    DATE ( 2020, 12, 31 ) )
```

### CALENDARAUTO
Returns a table with a single column named "Date" that contains a contiguous set of dates. The range of dates is calculated automatically based on data in the model.