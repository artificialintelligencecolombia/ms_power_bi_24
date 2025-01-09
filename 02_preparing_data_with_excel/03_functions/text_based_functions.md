# Text Based 
### Errors
- Mispelling
- Unnecesary characters
- Unncesessary spaces
- Incorrectly placed entry

- Poor layout
- Using abbreviations
- Poorly formatted data
- Duplicate information

### LEFT, MID, RIGHT

B2: Doctor Marint Garcia

- =LEFT(B2,6)
The formula in C2 will extract the six characters to the left of the entry, the title Doctor. This formula reads as follows:
Doctor

- =MID(B2,8,6)
The formula in D2 will begin with the eighth character and return the next six characters to the right, which is the first name of Martin. This formula is:
Martin

- =RIGHT(B2,6)
The formula in E2 will extract the six characters to the right of the entry, which is the last name of Garcia. Excel counts the six characters from right to left in the cell. This formula is:
Garcia

### TRIM
TRIM function is used to remove any empty spaces from text strings, except for the spaces between words. 

B2: _______Juan Magana_______

- TRIM(B2)
Juan Magana