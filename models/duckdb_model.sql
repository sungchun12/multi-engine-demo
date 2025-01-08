MODEL (
  name sqlmesh_example.duckdb_model,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column event_date
  ),
  start '2020-01-01',
  cron '@daily',
  gateway duckdb,
  dialect duckdb,
);

-- this will read from postgres, process data in duckdb, and write it back to postgres
SELECT
  id,
  item_id,
  event_date,
FROM
  sqlmesh_example.seed_model -- let's imagine this is a large 1 billion row table
WHERE
  event_date BETWEEN @start_date AND @end_date
  
