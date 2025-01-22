# Data Sources supported by Power BI
Power BI works with data, its like its gasoline.

Power BI supports more than 100 data sources. Some examples of these data sources include:

- SQL Server databases
- Cloud-based data sources
- Microsoft Excel spreadsheets
- On-premises data sources
- Web-based data sources
- NoSQL databases

### Data sources for Power BI Desktop
Below is a list of the types of data sources available in Power BI Desktop and some common examples for each category

1. File: XML, JSON, PDF, Excel workbook (Limited to a maximum file size of 1GB)
2. Database: MySQL, SQL Server, Access, PostgreSQL, Google BigQuery
3. Power Platform: Microsoft Power Platform Power BI datasets, Datamarts, Dataverse, Dataflows
4. Azure: Azure SQL Database, Azure Synapse Analytics SQL, Azure Data Explorer
5. Online Services: GitHub, QuickBooks Online, Stripe, Dynamics 365, Salesforce
6. Other: R scripts, Python scripts and Active Directory

### Data sources for Power BI service
Below is a list of the types of data sources available in Power BI service and some common examples for each category

1. File: Excel workbooks, Power BI Desktop, or .pbix report files, and CSV
2. Database: Azure SQL Database, Azure Synapse Analytics, formerly SQL Data Warehouse, Spark on Azure HDInsight

### Flat Files
Contains a single data table.
- CSV
- Excel
- txt

### IMPORTANT: Flat Files
1. The dataset is provided as a flat file: Your workbook must not have any total rows or columns.

2. All data in each column should be of the same type: Whether it is dates, text or currency, each column must contain the same type of data.

3. The file is in an easily readable table format. It does not contain pivot tables or matrix formats

4. A space-free name: Give your table a name that is easy to remember. Just remember that the name cannot contain any spaces.