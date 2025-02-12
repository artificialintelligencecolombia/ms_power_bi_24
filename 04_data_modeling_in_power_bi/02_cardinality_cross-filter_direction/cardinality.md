# cardinality
Its defined on how tables related to each other in the dataset

- one to one: one record in table a corresponds to one record in table b. Less common in data modeling
- one to many: each record in table a corresponds to multiple records in table b
- many to many: multiple records in table a correspond to multiple records in column b. This cardinality is often stablished between 2 dimension tables

In Power BI, the cardinality is display, for example as one (1) to(->) many(*)

### Creating relationships in Power BI
There are two ways relationships can be created in Microsoft Power BI: automatically, or manually. 

Autodetection: load two to more tables using Power Query, Power BI desktop autodetects the relationships between the loaded tables based on a common column. Cardinality and cross-filter direction are automatically set. 

Manual set up:  Model view in Power BI desktop. Access the Home tab, then select Manage Relationships. This action brings up the Create relationship dialog box. You can use this dialog box to create and configure relationships between the loaded tables of a dataset. 

### Editing relationships
This can be done by using the Properties pane under the Model view or the Relationship Editor dialog box. 

This dialog box can be opened in multiple ways. You can open it by selecting the relationship line between the two tables. or you can select Manage Relationships from the Model view of Power BI desktop.
