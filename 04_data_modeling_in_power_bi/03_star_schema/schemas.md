# Schema
- It represents the logical framework of how the data is organized and connected. 
- It defines the structure of the database, including tables, columns, relationships, and constraints. 
- There are three primary types of schemas used in data modeling: flat, star, and snowflake.

#### Benetifs of a schema
- Defines the data structure
- Enables efficient analysis
- Assists with visualizations
- Leads to meaningful insights

### Types of Schemas

#### 1. Flat Schema
- A flat schema is the simplest form of data modeling, where all data is stored in a single table.
- It is suitable for small datasets with minimal complexity.
- In a flat schema, there are no relationships between tables, and all data is stored in a single table.

##### Advantages of a flat schema
- Easy to data retrieval
- Less complex data analysis
- Simple data visualizations

##### Disadvantages of a flat schema
- Requires large datasets to store the whole structure
- Can lead to inconsistencies and redundancies
- Not suitable for complex datasets

#### 2. Star Schema
- A star schema is a more advanced form of data modeling that consists of a central fact table connected to multiple dimension tables.
- The fact table contains the primary data points or metrics (QUANTITIVE DATA), while the dimension tables provide additional context and details (DESCRIPTIVE DATA).
- In a star schema, the fact table is at the center, surrounded by dimension tables that are connected to the fact table through foreign key relationships.
- This schema is commonly used in data warehousing and business intelligence applications.

##### Advantages of a star schema
- Reduces data redundancy
- boost query performance
- Its easy to understand and navigate

##### Disadvantages of a star schema
- Less flexible (adding or modifying tables can be complex)
- Struggles to manage complex relationships

#### 3. Snowflake Schema
- A snowflake schema is an extension of the star schema that further normalizes the dimension tables (this creates a sort of hierarchy).
- In a snowflake schema, dimension tables are broken down into multiple related tables, creating a more normalized structure.
- This schema reduces data redundancy and improves data integrity by eliminating duplicate data.
- Snowflake schemas are beneficial for large datasets with complex relationships and hierarchies.

##### Advantages of a snowflake schema
- More efficient storage and retrieval
- Improved data integrity
- Reduces data redundancy
- Offers scalability

##### Disadvantages of a snowflake schema
- Difficult to analyze and understand
- Slow query performance due to complex joins

### Validating the Schema
1. Assign correct data types
2. Check the correct formatting
3. Confirm column descriptions with relevant context
4. Configure all properties