#!/usr/bin/bash

echo 'drop table google_trends;' | sqlite3 mydb.db 
cat google_trends.sql | sqlite3 mydb.db


curl -X 'POST' \
  'localhost/api/v1/database' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "db_alias": "google_trends",
  "use_ssh": false,
  "connection_uri": "sqlite:///mydb.db"
}' && echo ' - Database identified'

curl -X 'POST' \
    'localhost/api/v1/scanner' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "db_alias": "google_trends",
    "table_name": "google_trends"
}' && echo ' - Database scanned' 

curl -X 'GET' \
    'localhost/api/v1/scanned-databases?db_alias=google_trends' \
    -H 'accept: application/json' && echo 

curl -X 'PATCH' \
  'localhost/api/v1/scanned-db/google_trends/google_trends' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "description": "Google trends data on web searches for google, facebook, netflix, and amazon from 2004",
  "columns": [
    {
      "name": "date",
      "description": "The date of the web search"
    },
    {
      "name": "google",
      "description": "The aggregate number of searches that were for the term google"
    },
    {
      "name": "facebook",
      "description": "The aggregate number of searches that were for the term facebook"
    },
    {
      "name": "netflix",
      "description": "The aggregate number of searches that were for the term netflix"
    },
    {
      "name": "amazon",
      "description": "The aggregate number of searches that were for the term amazon"
    }
  ]
}' && echo ' - Provided table descriptions'

