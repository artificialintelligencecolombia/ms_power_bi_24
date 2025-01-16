# Logical Functions
Logical Functions returns a result based on whether the condition is true or false.

### Logical operators
Logical operators determine what kind of question the formula is asking and what value it needs for its answer. These operators can be used to compare both text and numeric entries, those are:

=, >, <, >=, <=, <> (not equal to)

### IF
- =IF(test, if true, if false)

### NESTED IF
- =IF(test1, if true, IF(test2, if true, if false))

### IFS
The IFS function checks whether one or more conditions are met, and returns a value that corresponds to the first TRUE condition. IFS can take the place of multiple nested IF statements, and is much easier to read with multiple conditions.
- =IFS(test1, if true, test2, if true, TRUE, if true)

### AND/OR
With AND and OR functions, you can test for multiple conditions in Excel at once.

AND formula returns a result of TRUE because all the logical tests were met.
- =AND(A2<200,B2<200,C2<200)

OR function will generate an overall result of TRUE if just one of the logical tests is met.
- =OR(A2<200,B2<200,C2<200)

- =IF(AND(A2>200,B2>200),"On Target","Target Not Met")

### SUMIF
The SUMIF function needs the following information:

1. The range of cells that contains the criteria, 
2. What the criteria is,
3. And the range of cells holding the values must be included in the total. 

- =SUMIF(B2:B24,”seattle”,G2:G24)

In this formula, the SUMIF function examines the range B2 to B24 and identifies every row that contains the entry Seattle. The word Seattle is in double quotes to indicate to Excel that it is text. Text criteria are not case-sensitive.

### AVERAGEIF
The AVERAGEIF function works similarly to SUMIF. It works out an average of values on rows that match a specific condition.

- =AVERAGEIF(B2:B24,"seattle",G2:G24)

The AVERAGEIF scans through the cell range B2 to B24 and identifies every row that contains the entry Seattle. It then extracts the numeric values in column G for those rows and provides an average.

### COUNTIF
Just like SUMIF and AVERAGEIF, the COUNTIF function works through a range of cells and identifies all entries that match the specified condition. It then returns a count of how many occurrences it has found. 

COUNTIF only requires two arguments:

1. The range of cells to examine,
2. And the condition to search for. 

- =COUNTIF(B2:B24,”seattle”)

The result of this formula is that the word Seattle appears 3 times within this cell range. 