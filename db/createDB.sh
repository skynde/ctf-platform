#!/bin/sh

#echo "*********** Creating database ***********"
#gosu postgres postgres --single <<- EOSQL
#    CREATE DATABASE flask_app;
#EOSQL

#psql -U $POSTGRES_USER --command="CREATE DATABASE $DJANGO_DB_NAME;"
#psql -U $POSTGRES_USER --command="CREATE USER $DJANGO_DB_USER WITH PASSWORD '$DJANGO_DB_PASSWORD';"
#psql -U $POSTGRES_USER --command="ALTER ROLE $DJANGO_DB_USER SET client_encoding TO 'utf8';"
#psql -U $POSTGRES_USER --command="ALTER ROLE $DJANGO_DB_USER SET default_transaction_isolation TO 'read committed';"
#psql -U $POSTGRES_USER --command="ALTER ROLE $DJANGO_DB_USER SET timezone TO 'UTC';"
#psql -U $POSTGRES_USER --command="GRANT ALL PRIVILEGES ON DATABASE DJANGO_DB_NAME TO djangoUser;"
