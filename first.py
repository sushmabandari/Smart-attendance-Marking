import os
import psycopg2

# Database connection configuration for PostgreSQL
db_config_pg = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'postgres',
    'database': 'postgres',
    'port':'5394',
}

# Establish a connection to the PostgreSQL database
conn_pg = psycopg2.connect(**db_config_pg)
cursor_pg=conn_pg.cursor()
cursor_pg.execute('create extension cube')
# Commit changes and close the PostgreSQL connection
conn_pg.commit()
conn_pg.close()
