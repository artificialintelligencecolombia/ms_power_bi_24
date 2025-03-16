# Cross-Highlight & Cross-Filtering 
1. Cross-Highlighting: When you select a data point in one visual, it highlights related data in another visuals while keeping non-related values visible but dimmed.
2. Cross-Filtering: When you select a data point in one visual, it filters out unrelated data in another visual, showing only the relevant subset.

### Steps to Enable Cross-Highlighting & Cross-Filtering
A. Enable Interaction Between Visuals
1️⃣ In Power BI Desktop, go to the Report View.
2️⃣ Select a visual (e.g., a bar chart).
3️⃣ Click on the "Format" pane (paint roller icon).
4️⃣ Expand the Edit Interactions option.
5️⃣ You’ll see three icons appear on related visuals:
    Filter (Cross-Filter)
    Highlight (Cross-Highlight)
    None (Disable Interaction)
6️⃣ Click the desired icon for each visual to choose between filtering, highlighting, or disabling interactions.

B. Using Cross-Highlighting & Cross-Filtering in Reports
1️⃣ Click on a data point in a visual (e.g., selecting "North America" in a bar chart).
2️⃣ Other visuals update dynamically based on selected interaction:
- Cross-Highlighting → Highlights related values while dimming others.
- Cross-Filtering → Completely removes unrelated data points.
3️⃣ Click outside the visual or press Esc to clear the selection.

### Tips & Tricks
✅ Use Cross-Filtering for strict filtering and deeper drill-down analysis.
✅ Use Cross-Highlighting to show comparisons between related and non-related data.
✅ Optimize user experience by adjusting interactions per visual instead of using defaults.
✅ Avoid over-filtering by testing interactions across multiple visuals.
✅ Use multi-select (Ctrl + Click) for more refined data analysis.
✅ Combine Cross-Filtering with Drillthrough for enhanced interactive reports.

### Common Use Cases
🔹 Sales Performance: Clicking a product in a bar chart highlights its contribution in total sales.
🔹 Customer Segmentation: Selecting a customer type filters detailed purchase behavior.
🔹 Regional Analysis: Clicking a country filters all visuals to display only that region’s data.
🔹 Marketing Insights: Selecting a campaign highlights its performance across multiple KPIs.
🔹 Financial Reports: Filtering an expense category updates all financial breakdowns dynamically.

### Supported Visualizations
✔ Bar & Column Charts
✔ Pie & Donut Charts
✔ Tables & Matrices
✔ Line Charts
✔ Maps
✔ Scatter Plots

#### Not Supported on:
❌ Cards
❌ Slicers
❌ KPIs