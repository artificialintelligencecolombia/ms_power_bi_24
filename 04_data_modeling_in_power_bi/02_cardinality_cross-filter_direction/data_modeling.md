# Data modeling
Data model is a logical and visual representation of data structure, relationships between tables and rules over these relationships
Data models are the basis for data exploration
	
### Star schema
- fact tables: Consist of measurements, metrics or facts on the business process. Hold quantifiable, measurable data. In star schema, fact table sits in center.
- dimension tables: text field, provide descriptive attributes related to the fact data. In the star schema, they're directly connected and surrounding the fact table.

NOTE: Star schema can be extended into a snowflake schema.

### Snowflake schema
This is an extension of star schema and it makes use of dimension table by normalizing them


# normalization and denormalization
One of the most important jobs of a data analyst in Microsoft Power BI is creating and managing data models. However, one of the questions you’ll often face is “to normalize or denormalize?”

### data model
 It’s a visual overview of your tables, their columns, and the relationships between the tables. 

#### data modeling advantages
- Faster data exploration
- Easier aggregate creation
- Precise reporting
- Quicker report creation
- Simpler report maintenance