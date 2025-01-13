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
- =IFS(test1, if true, test2, if true, TRUE, if true)

### AND/OR
With AND and OR functions, you can test for multiple conditions in Excel at once.

 AND formula returns a result of TRUE because all the logical tests were met.
- =AND(A2<200,B2<200,C2<200)

OR function will generate an overall result of TRUE if just one of the logical tests is met.
- =OR(A2<200,B2<200,C2<200)

- =IF(AND(A2>200,B2>200),"On Target","Target Not Met")