# Query Parameters in Power BI
### Definition:
A query parameter is a dynamic input that allows you to change values in Power BI queries without editing the query manually. It improves flexibility and reusability of reports.

### Examples of Query Parameters
1. Dynamic Date Filter
Scenario: You want to filter sales data based on a start and end date.

Steps:
- Create a StartDate and EndDate parameter in Power Query.
- Home tab -> Manage parameters
- In manage parameters, select create a new paramenter -> Name the parameter -> Type: its for sleecting the data type
- In Suggested values, select list of values -> enter the list of categories we're interested in (reange of dates, categories, etc) -> Click OK
- Now we can modify the query to filter the data based on the parameters we've created (dynamic changes)

Result: Users can adjust date ranges without modifying the query.