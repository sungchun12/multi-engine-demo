from pyiceberg.catalog import load_catalog
import pyarrow.parquet as pq
import pyarrow as pa
from typing import Dict


def create_and_load_iceberg_demo_table(
    catalog_name: str,
    s3_bucket_path: str, 
    s3_region: str,
    table_name: str
) -> None:
    """Creates and loads an Iceberg demo table in AWS Glue catalog.
    
    Args:
        catalog_name: Name of the catalog namespace
        s3_bucket_path: S3 bucket path for table location
        s3_region: AWS region for S3
        table_name: Name of the table to create
    """
    # Create catalog
    catalog_config: Dict[str, str] = {
        "type": "glue",
        "s3.region": s3_region
    }
    catalog = load_catalog("glue", **catalog_config)

    # Create schema if it doesn't exist
    namespaces = catalog.list_namespaces()
    if catalog_name not in [ns[0] for ns in namespaces]:
        print(f"Creating namespace: {catalog_name}")
        catalog.create_namespace(catalog_name)

    # Create sample review data
    reviews_data = [
        {
            "reviewid": "r1", 
            "username": "user1",
            "review": "Great product!",
            "ingestion_date": 20241218
        },
        {
            "reviewid": "r2",
            "username": "user2", 
            "review": "Could be better",
            "ingestion_date": 20241218
        },
        {
            "reviewid": "r3",
            "username": "user3",
            "review": "Hate it",
            "ingestion_date": 20241218
        }
    ]

    # Convert to Arrow table and write to parquet
    reviews_table = pa.Table.from_pylist(reviews_data)
    pq.write_table(reviews_table, f"s3://{s3_bucket_path}/{table_name}/reviews_data.parquet")

    # Define and create iceberg table if it doesn't exist
    tables = catalog.list_tables(catalog_name)
    if (catalog_name, table_name) not in tables:
        print(f"Creating table: {table_name}")
        schema = pa.schema([
            pa.field("reviewid", pa.string(), nullable=False),
            pa.field("username", pa.string(), nullable=False),
            pa.field("review", pa.string(), nullable=True),
            pa.field("ingestion_date", pa.int64(), nullable=False),
        ])

        catalog.create_table(
            identifier=f"{catalog_name}.{table_name}",
            schema=schema,
            location=f"s3://{s3_bucket_path}/{table_name}",
        )


if __name__ == "__main__":
    create_and_load_iceberg_demo_table(
        catalog_name="multi-engine-demo",
        s3_bucket_path="multi-engine-demo-bucket", 
        s3_region="us-west-2",
        table_name="landing_reviews"
    )
