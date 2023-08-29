#!/usr/bin/bash

curl -X 'POST' \
  'localhost/api/v1/question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
        "question": "are google searches more popular than amazon searches??",
        "db_alias": "google_trends"
    }' && echo # | jq && echo
