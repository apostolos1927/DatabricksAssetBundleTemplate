def create_schema(env,schema):
    return f"CREATE SCHEMA IF NOT EXISTS hive_metastore.{env}_{schema}"

