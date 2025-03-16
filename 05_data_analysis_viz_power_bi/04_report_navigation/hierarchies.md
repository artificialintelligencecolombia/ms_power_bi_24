# Hierarchies
- Is a way to structure organized data at various levels of details
- Group related data by hierarchical relationship

ej:
Year
    Quarter
        Month
            Day
                Hour
                    Minute
                        Second

Category
    Subcategory
        Product

### Steps:
1. Open Power BI Desktop and go to the Modeling or Data view.
2. Locate the table containing the hierarchical fields (e.g., Date → Year, Quarter, Month, Day).
3. Right-click on the parent field (e.g., Year).
4. Select Create Hierarchy – A new hierarchy appears under the field.
5. Drag and drop additional fields (e.g., Quarter, Month, Day) into the hierarchy.
6. Rename the hierarchy if needed by double-clicking on its title.
7. Use the hierarchy in visuals by dragging it to a chart or table.
8. Enable drill down in the visual by clicking the drill-down arrow in the report view.