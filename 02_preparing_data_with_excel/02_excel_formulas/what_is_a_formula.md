# What is a formula
A formula is a calculation performed on values in a cell. The result of the calculation is displayed in the cell. 
Operators: (+ - * /)

### Types of formulas 
- Static: fixed numbers, always generates the same result.
- Dynamic: uses the current value in the cell.

When creating a formula, if the formula includes a cell's value from another worksheet, then we have to call it:

= Sheet!A1 + A1

### Order of precedence
1. ()
2. / *
3. + -

### Cell Reference
- Relative: If we copy a formula to another cell, excel will adjust the row numbers and column initials accordingly to the new location of the formula.
- Absolute: Excel keeps the cell references constant. If we want to keep the same cell reference in a formula, we can use the $ symbol before the row number and column initial. ($A$1)



