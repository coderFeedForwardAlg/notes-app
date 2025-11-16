#!/bin/bash

# Test the embed endpoint
echo "Testing the embed endpoint..."

# Start the server in the background
cargo run &
SERVER_PID=$!

# Wait for server to start
sleep 5

# Test the endpoint with a sample message
curl -X POST http://localhost:8081/embed \
  -H "Content-Type: application/json" \
  -d '{"msg": "Hello, this is a test message for embedding"}' \
  | jq .

# Kill the server
kill $SERVER_PID