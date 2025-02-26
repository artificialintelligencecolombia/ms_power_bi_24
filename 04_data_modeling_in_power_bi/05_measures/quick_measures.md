# Quick Measures
- Quick measures is a power bi feature to enhance the creation time of measures without writing DAX code
- Uses commonly used calculations 

### Types of Quick measures include:
aggregate per category,
filters, and
time intelligence,
totals, 
mathematical operations, and 
text. 

### Steps
Report View -> Go to Data ribbon in the right and right click in the objective table -> New Quick Measure ->
1. In the Quick Measure section, select calculation type
2. Select the base value
3. Select the category

i.e: We want to know the total quantity of each product each team member has sold, so:
calculation type: Total for Category (filters applied)
base value: Sales[Sales]
category: Product[Category]
4. Click ADD
- Now, quick measure appears in the field pane.

### Measure exemplar:
#### 1
```= SUMX(FILTER(InternetSales, InternetSales[SalesTerritoryID]=5), [Freight])```
1. FILTER: Filter
	The function scans the InternetSales table and returns only the rows where the SalesTerritoryID column equals 5.
2. SUMX(filtered_table, [Freight])
	SUMX(iterative function), function goes through each row of this filtered result and sums up the values in the [Freight] column. 	

Output: single scalar value

NOTE: equivalent SQL Logic
```
SELECT SUM(Freight)
FROM InternetSales
WHERE SalesTerritoryID = 5;
```

#### 2
```
Top 2 Products = 
VAR RankingContext =
    VALUES ( Products[Product] )

RETURN
CALCULATE (
    [Total Sales],
    TOPN ( 2, ALL ( Products[Product] ), [Total Sales] ),
    RankingContext
)
```
1. VAR RankingContext = VALUES ( Products[Product] )
	Stores a table in the variable name, it returns the distinct product names
2. RETURN CALCULATE, it will apply another filter
3. TOPN(2, ALL(Products[Product]), [Total Sales])
	Trae todos los valores de Products[Product]. [Total Sales] es la columna que usaremos para el ranking. De esta tabla organizada seleccionaremos los primeros 2 valores de product column segun total sales
4. RankingContext, se asegura que dicho filtro CALCULATE sea aplicado sobre la tabla de la variable RankingContext en lugar del modelo

#### 3
```
Sum of Total Sales running total in Year = 

```