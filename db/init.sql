CREATE DATABASE djangodb;
CREATE USER djangouser WITH PASSWORD 'djangopassword';
ALTER ROLE djangouser SET client_encoding TO 'utf8';
ALTER ROLE djangouser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangouser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE djangodb TO djangouser;
