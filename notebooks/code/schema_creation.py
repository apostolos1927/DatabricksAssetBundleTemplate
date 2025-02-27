# Databricks notebook source
dbutils.widgets.text('env_name','')
dbutils.widgets.text('schema','')

from lib.lib_code.code_example import create_schema


env_name = dbutils.widgets.get('env_name')
schema = dbutils.widgets.get('schema')
print(create_schema(env_name,schema))
spark.sql(create_schema(env_name,schema))