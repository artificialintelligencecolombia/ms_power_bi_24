# Import database from postgresql into Power BI

### 1. Connection strategy
Small db: Import mode
Auto date/time: disable it
Data refresh: daily

**1.1. check the postgresql service is running:**
win + r -> service.msc -> postgresql -> start
The PostgreSQL service is the core process that runs the database server. If it's not running, no connections can be established.

**1.2. database connection test:**
```powershell/cmd
psql -h localhost -p 5432 -U postgres -d <database_name>
```

#### 2. Retrieve postgres username
**open psql -> input usr and psswd**
\l: list all databases
    - postgres: The default administrative database.
    - template0: A clean, unmodified template used for creating new databases.
    - template1: A template that can be customized and is used for creating new databases.

**check al available users:**
```
SELECT usename FROM pg_users;
```

**show the username currently used:**
```
SELECT current_user;
```

**get the server name or ip address in psql**
```
\conninfo
```
Show connection information including the host (server name or IP address), port, and other connection-related details.

### 3. Connect Power BI to postgresql
Home -> Get data -> postgresql database
Server: localhost
Database: <database_name>
Username: <username>
Password: <password>
CLICK connect

### 4. List all database objects (Those who appear in the load window when connecting to the database via power bi)

```psql
SELECT n.nspname AS schemaname,  -- Select the schema name
       c.relname AS tablename,   -- Select the table/view name
       CASE c.relkind             -- Determine the object type
           WHEN 'r' THEN 'table'  -- If relkind is 'r', it's a table
           WHEN 'v' THEN 'view'  -- If relkind is 'v', it's a view
           ELSE 'unknown'        -- Otherwise, classify it as 'unknown'
       END AS tabletype           -- Name this column 'tabletype'
FROM pg_catalog.pg_class c       -- From the pg_class catalog (all objects)
LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace  -- Join with pg_namespace to get schema names
WHERE c.relkind IN ('r', 'v')    -- Filter for tables ('r') and views ('v')
AND n.nspname NOT IN ('pg_catalog', 'information_schema')  -- Exclude system schemas
ORDER BY schemaname, tablename;  -- Order the results for readability
```