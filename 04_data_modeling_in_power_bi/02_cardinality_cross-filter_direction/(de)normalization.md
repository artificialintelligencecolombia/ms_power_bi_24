# Normalization
### normalization
Its a technique, it divides data into multiple related tables, each with a specific purpose. This approach reduces data duplication. However, it often requires creating complex relationships between the tables.

With normalization, relationships are established between tables by using primary and foreign keys. Primary keys are columns that uniquely identify each row of data.

#### advantages
Normalization offers the following advantages:
- Removal of redundant data.
- Improved data integrity.
- Easier maintenance of your data model.

### denormalization
It involves converting the normalized schema into a schema that has redundant information. Implementing denormalization helps to avoid expensive queries between the tables but at the cost of creating redundant or duplicated data.

#### Duplicated data
Duplicated data refers to records that appear multiple times within a dataset, either fully or partially identical

#### advantages
- Reduced number of tables, which could be more efficient in querying performance
- Filters are applied to that single table


### normalization vs denormalization
data integrity: maintained in normalized tables but not for denormalized tables(multiple rows may need to be updated when data changes)

redundant data: redundancy is eliminated with normalization.Denormalization increases redundant data

model size: the number of tables increase with normalization. Denormalization reduces the number of tables and relationships

memory: optimized in normalization. However, disk space is overused in denormalization

NOTE: There is no one-size-fits-all solution, and the choice depends on your project's specific business and analytical requirements.