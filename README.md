Multi-Engine Demo

This is a demo project to show how to use SQLMesh with multiple engines.

## Requirements

- Python 3.10+
- SQLMesh 0.140.1+

## Setup

1. Clone the repository
2. Install the dependencies
3. Run the project

## Tech Stack

- duckdb
- postgres
- sqlmesh
- AWS Glue Catalog

- brew install postgres

```
brew install postgresql
```

Then start it

```
brew services start postgresql
```

Connect to the database
```
psql -d postgres
```

create a user and password
```
CREATE ROLE myuser WITH LOGIN SUPERUSER PASSWORD 'mypassword';
\du --verify it was created
```

create a database
```
CREATE DATABASE demo;
CREATE DATABASE sqlmesh_state;
\l --verify it was created
```

Update the .env file with the correct values

```
POSTGRES_HOST=localhost
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
```

Export them in your shell

```
set -a        # Turn on auto-export
source .env   # Read the file, all variables are automatically exported
set +a        # Turn off auto-export
```
