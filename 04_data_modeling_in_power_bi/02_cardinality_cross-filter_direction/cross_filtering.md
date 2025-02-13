# Cross-filtering
- Is the direction of filtering between tables. It dictates how data from one table affects data in another table. Relationships are directional by nature in Power BI, therefore its relationship with cross-filtering

### Single direction: 
changes in a primary table affect related table, but not the other way around. This is common in one-to-many relationships.

ie:
Product -> Sales <- Salesperson
The direction of the rows indicates that Sales table can be filtered by product and sales person.

### Bi-direction:  
A filter applied in both directions, meaning changes in either related table affect the other. This is useful in many-to-many relationships.