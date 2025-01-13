# Datetime Functions 
Date and time based calculations allows business to plan and calculate dates.

### Datetime calculations
Excel can be used to create formulas and calculate hours, calendar days or work days there are for deadlines. Calculations of date and time allows to identify:

- Deadlines
- Performance
- Time management
- Scheduling

### Serial numbers
Excel stores dates and times as serial numbers. The serial number is the number of days since 1/1/1900. The serial number for the date 1/1/1900 is 1, 1/2/1900 is 2, and so on.

Addtitionally, excel treats time as a decimal fraction of the unit which is a day.

Note: serial numbers can be visualized by changing the format of the cell to General.

### TODAY, NOW
- TODAY(): returns the current date.
- NOW(): returns the current date and time.

### MONTH, DAY, YEAR
- MONTH: returns the month of a date.
- DAY: returns the day of a date.
- YEAR: returns the year of a date.

- =MONTH(A2)
- =DAY(A2)
- = YEAR(A2)

### DATE
It can be used to take three arguments: year, month, and day. It returns the date in a serial number format.

1   |  A   | B     | C
2   | year | month | day
3   | 2020 | 5     | 26

- =DATE(A2, B2, C2) # returns 43900

### NETWORKDAYS
NETWORKDAYS is a function that calculates the number of working days between a start date and an end date. It does not include weekend days in the result it generates.

- =NETWORKDAYS(A2, B2) # returns the number of working days between A2 and B2
- =NETWORKDAYS(A2, B2, C2:C3) # returns the number of working days between A2 and B2 excluding the dates in C2 and C3
