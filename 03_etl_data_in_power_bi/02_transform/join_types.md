### INNER JOIN
- Description: Returns only matching records from both tables. Like a strict intersection, it only includes rows where the join condition is satisfied in both tables.
- Key Characteristic: Most restrictive type of join; excludes all non-matching rows.

#### Key Insights:
1. Often used for mandatory relationships (e.g., getting all orders with their corresponding customer details)
2. Can unintentionally filter out data if your join keys contain NULL values or have data quality issues
3. Best for when you're certain all records should have matches and want to exclude incomplete data

# LEFT OUTER JOIN
- Description: Returns all records from the left table and matching records from the right table. If no match exists, NULL values are returned for right table columns.
- Key Characteristic: Preserves all rows from the left table regardless of matches.

#### Key Insights:
1. Perfect for finding missing relationships (e.g., customers who haven't placed orders)
2. Commonly used in reporting when you need to ensure no records from your primary table are lost
3. Order of tables matters significantly - switching tables changes results

# RIGHT OUTER JOIN
- Description: Returns all records from the right table and matching records from the left table. If no match exists, NULL values are returned for left table columns.
- Key Characteristic: Functionally identical to LEFT JOIN with tables swapped.

#### Key Insights:

1. Less commonly used as it's usually clearer to rewrite as a LEFT JOIN
2. Useful when maintaining existing code where table order is fixed
3. Can help identify orphaned records in the right table

### FULL OUTER JOIN
- Description: Returns all records from both tables, with NULL values in place of non-matching fields. Combines the effects of both LEFT and RIGHT joins.
- Key Characteristic: Most inclusive type of join; keeps all rows from both tables.

#### Key Insights:
1. Essential for data validation and finding inconsistencies between tables
2. Powerful for data migration projects to ensure no data is lost
3. Great for identifying referential integrity issues in your database

NOTE: join key = foreign key