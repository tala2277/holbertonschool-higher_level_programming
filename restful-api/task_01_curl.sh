#!/usr/bin/env bash
# Task 1 - Consume data from an API using curl

echo "=== curl version ==="
curl --version

echo
echo "=== GET Request ==="
curl https://jsonplaceholder.typicode.com/posts

echo
echo "=== Response Headers ==="
curl -I https://jsonplaceholder.typicode.com/posts

echo
echo "=== POST Request ==="
curl -X POST \
-d "title=foo&body=bar&userId=1" \
https://jsonplaceholder.typicode.com/posts
