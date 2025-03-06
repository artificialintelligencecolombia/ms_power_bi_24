# Aggregations
- Aggregations in Power BI improve query performance by summarizing large datasets into smaller, pre-aggregated tables stored in memory. 
- This technique enhances interactivity, particularly in DirectQuery mode, which can be slow due to frequent queries sent to the data source.
- Aggregations refers to consolidation of large volumes of data into more manageable summary tables by condensing detailed information into more simpler high level values.
- Aggregated tables are always smaller than the fact table.
- To define the level of granularity is crucial for the aggregated table creation through PowerQuery Editor

### Power BI Storage Modes & Their Relation to Aggregations
**Import Mode**
- Data is fully loaded into Power BI’s in-memory storage.
- Provides the fastest query performance since no external queries are needed.
- Limited by Power BI file size restrictions.
**Note:** Aggregations are not critical in this mode, as all data is already optimized in memory.

**DirectQuery Mode**
- Data is not stored in Power BI; queries are sent to the data source live.
- Suitable for very large datasets that can't fit in memory.
- Performance depends on the database speed and network latency.
**Note:** Aggregations are crucial here because they reduce the number of queries sent to the data source, improving speed.

**Composite Mode (Hybrid of Import & DirectQuery)**
- Allows a mix of Import Mode (for smaller tables like dimensions) and DirectQuery Mode (for large fact tables).
- Improves performance while keeping real-time access to large datasets.
**Note:** Aggregations play a key role by pre-calculating summary data and storing it in memory, reducing queries to DirectQuery sources.

### How Aggregations Help
- In DirectQuery Mode, every interaction triggers a query to the database, slowing performance. Aggregations store summarized data in memory, reducing query load.
- In Composite Mode, aggregations optimize DirectQuery tables by providing pre-aggregated results in memory while keeping detailed data accessible when needed.
- Aggregations balance speed and data freshness, making large datasets more manageable in Power BI.