#!/bin/bash

# Test the Python FastAPI embed endpoint
echo "Testing the Python FastAPI embed endpoint..."

# Navigate to the fastapi-template directory
cd fastapi-template

# Start the server in the background
python main.py &
SERVER_PID=$!

# Wait for server to start
sleep 5

# Test the endpoint with a sample message
echo "Sending request to embed endpoint..."
curl -X POST http://localhost:8003/vecter \
  -H "Content-Type: application/json" \
  -d '{"msg": "Hello, this is a test message for embedding"}' \
  | jq .

# Kill the server
kill $SERVER_PID

# Go back to the parent directory
cd ..