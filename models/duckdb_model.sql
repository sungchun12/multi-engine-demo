MODEL (
  name sqlmesh_example.duckdb_model,
  kind FULL,
  gateway duckdb,
);

SELECT
    reviewid,
    username,
    review,
    ingestion_date
FROM 
    iceberg_scan('s3://multi-engine-demo-bucket/landing_reviews/metadata/00000-19d8f4a6-f7c9-47bf-bc29-3041607f8b90.metadata.json', allow_moved_paths = true);
