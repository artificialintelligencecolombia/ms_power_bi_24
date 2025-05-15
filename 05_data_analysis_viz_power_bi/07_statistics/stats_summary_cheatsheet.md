# Statistical Summary

## Average and Median

1. AVERAGE(<column>): The average value in the given column is calculated by summing all values and dividing it by the number of data points. 
2. AVERAGEA(<column>): The average value in the given column is calculated, handling non-numeric data types
based on specific rules.

The rules are as follows: 
-  Values that evaluate to TRUE count as 1.
-  Values that evaluate to FALSE count as 0 (zero).
-  Values that contain non-numeric text count as 0 (zero).
-  Empty text ("") counts as 0 (zero).

3. AVERAGEX(<table>, <expression>): The average of the expression in the specified table is calculated. It evaluates the expression for each row in the table and uses the average of the results.
Example: AVERAGEX(Sales, [ItemPrice] * [QuantitySold])

4. MEDIAN(<column>): Returns the median value of a numeric column. 
Example: MEDIAN(Sales[ItemPrice]) 

## Variance and Standard Deviation

Variance and standard deviation are both measures of how spread out or dispersed a set of data points is, playing a critical role when data variability needs to be measured. In the context of financial portfolio management, computing variance and standard deviation of stock returns assists in gauging the riskiness of investments. 

The calculation of these two functions differs slightly depending on whether the dataset represents the entire population of data points or just a sample from it. In DAX, this differentiation is denoted by a P for population and an S, for a sample in their formulas. 

### Variance and standard deviation using a sample population
Assuming the column on which the variance/deviation will be calculated refers to a sample population:

1. VAR.S(<column>): Returns the variance of a column containing a sample population.
Example: VAR.S(Sales[ItemPrice]) = 1.629

2. STDEV.S(<column>): Returns the standard deviation of a column containing a sample population.
Example: STDEV.S(Sales[ItemPrice])= 40

### Variance and standard deviation using the entire population
Assuming the column on which the variance/deviation will be calculated contains the entire population of data points:

1. VAR.P(<column>): Returns the variance of a column, assuming that the column refers to the entire population.
Example: VAR.P(Sales[ItemPrice]) = 1.425

2. STDEV.P(<column>): Returns the standard deviation of a column containing an entire population. 
Example: STDEV.P(Sales[ItemPrice]) = 38

## Count functions
1. COUNT(<column>): Counts the total number of rows, containing any or no value.
Example: COUNT([ItemPrice_withText]) = 8

2. COUNTBLANK(<column>): Counts the number of blank or empty rows in a column.
Example: COUNTBLANK([ItemPrice_withText])= 1

3. DISTINCTCOUNT(<column>): Counts the number of distinct values in the column.
Example: DISTINCTCOUNT([ItemPrice_withText]) = 8

### Max function
      1.     MAX(<column>):Returns the largest numeric value or largest string in a column. Ignores logical values.

                Example MAX([ItemPrice_withText]) = “TRUE”

                Note: As the MAX function ignores logical values, TRUE and FALSE in the table are interpreted as texts. Texts  
                are considered “larger” than numbers in DAX alphabetically, so the largest value in the column is TRUE, as it’s 
                the last text in alphabetical order.

### Min function
1. MIN(<column): Returns the smallest numeric value or shortest string in a column. Ignores logical values.
Example MIN([ItemPrice_withText]) = “”

Note: As the MIN function also ignores logical values, same as the MAX function, the sequence of blank values, 
numbers and texts is followed in ascending order. A blank value in the sample column is considered as the 
minimum value. 

## Combination and permutation functions
Combination and permutation functions in statistics calculate the number of combinations for a given number of items. The difference between the two functions is that in a combination function, the output order of items is not important, while in a permutation function, the output order of the items is significant. For an easy example, let’s calculate the odds of winning a lottery ticket, where you have to guess 6 numbers out of 49, using these two functions in Power BI.

### Combination function
1. COMBIN(n,k): Returns the number of ways k items can be selected from n, where the order does not matter.
Example: COMBIN(49,6) = 13.983.816

### Permutation function
1. PERMUT(n,k): Returns the number of ways k items can be selected from n, where the order does matter.
Example: PERMUT(49,6) = 10.068.347.520