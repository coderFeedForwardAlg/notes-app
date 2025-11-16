#!/usr/bin/env python3

import requests
import json

# Test the /vecter endpoint
def test_vector_endpoint():
    url = "http://localhost:8003/vecter"
    
    # Example request payload
    payload = {
        "msg": "Hello, this is a test message for embedding"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        # Check if the response contains a vector
        if "vector" in response.json():
            vector = response.json()["vector"]
            print(f"Vector length: {len(vector)}")
            print(f"First 5 elements: {vector[:5]}")
        else:
            print("No vector found in response")
            
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the Python service is running.")
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
    except json.JSONDecodeError:
        print(f"Response text: {response.text}")

if __name__ == "__main__":
    test_vector_endpoint()