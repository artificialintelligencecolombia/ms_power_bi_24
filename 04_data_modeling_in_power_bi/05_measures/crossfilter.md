# Crossfilter Function
It changes the filter direction between two tables for a specific measure, while maintaining the original settings.
- Crossfilter function can only be used within a DAX function that accepts a filter as an argument
- It changes the direction of the relationship

### Syntax
CROSSFILTER
    (
    Table1[Column1], // Many
    Table2[Column2], // 1,

    filter_direction

    )

### Crossfilter directions
- None: no crossfilter occurs within the relationship
- oneway: filters applied on one side of the relationship propagate to the other side. Can't be used for a one-to-one relationship
- oneway_rightfilersleft: filter propagation occurs from the right side to the left side of the relationship
- oneway_leftfiltersright: filter propagation occurs from the left side to the right side of the relationship

### Example
```
Product by Year =
CALCULATE (
    DISTINCTCOUNT ( Products [ProductKey] ), // Expression
    CROSSFILTER (   // Filter
        Sales[ProductKey], 
        Products[ProductKey], 
        BOTH
    )
)
```
1. Understand the relationship: Products[ProductKey] is related to Sales[ProductKey] in a ONE-TO-MANY.
    - Filters flow from Products to Sales. If I filter Products, it affects sales. But filtering Sales doesn´t affect Products

2. CROSSFILTER(Sales[ProductKey], Products[ProductKey], BOTH) changes the filter direction.
    - Changes the filter direction. Now, filtering Sales will also affect Products and vice versa.

3. CALCULATE changes the context
    - CALCULATE modifies the filter context for the calculation inside it. It applies CROSSFILTER before executing the calculation

4. DISTINCTCOUNT(Products[ProductKey]) Counts Unique Products
    - CALCULATE runs DISTINCTCOUNT(Products[ProductKey])
    - It counts the number of unique product keys from the Products table.
    - However, because of CROSSFILTER, only the Products that have matching sales in the Sales table will be counted

5. Filters from Sales Affect Products
    - Since CROSSFILTER allows Sales to filter Products, only products that appear in Sales will be counted.
    - If a product exists in Products but has no sales records, it will be excluded from the count.

6. The final result of the formula is the count of unique ProductKey values in the Products table that have corresponding sales in the Sales table.