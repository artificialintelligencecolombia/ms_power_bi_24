# granularity
The level of detail of a dataset

### HIGH granularity: datasets that capture detailed information
Data is highly detailed, capturing specific attributes of individual records or events. It allows for in-depth analysis but increases data volume.
Example: A dataset containing each customer's purchase, including product ID, timestamp, and payment method.

- By exceeding the granularity level can lead to overload of data and slow queries

### low granularity: Data is aggregated or summarized, providing a broader view rather than individual details. It simplifies analysis but reduces specificity.
Example: A dataset showing total monthly sales per region without individual transactions.

- By misusing low granularity levels could lead to misrepresented data and incorrect insights

NOTE: Understanding the level of granularity of data is crucial to establish the correct cardinality and cross-filter direction