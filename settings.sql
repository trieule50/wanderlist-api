DROP DATABASE IF EXISTS wanderlist;
CREATE DATABASE wanderlist;
CREATE USER wanderlistuser WITH PASSWORD 'wanderlist';
GRANT ALL PRIVILEGES ON DATABASE wanderlist TO wanderlistuser;