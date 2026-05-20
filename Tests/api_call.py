import os
import urllib.request
import json
import anthropic

class TestAPICall:
    def __init__(self):
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY environment variable is not set.")
        
    def call_with_sdk(self):
        client = anthropic.messages.client()

        response = client.chat.completions.create(
            model = "claude-sonnet-4-20250514",
            max_tokens = 256,
            messages = [ {"role": "user", "content": "What is the capital of France?"}]
        )

        return response.choices[0].message.content

    def call_with_http(self):
        url = ""
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2024-06-01",
        }

        body = json.dumps({
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 256,
            "messages": [
                {
                    "role": "user",
                    "content": "What is the capital of France?"
                }
            ],
        })

        req = urllib.request.Request(url, data=body, headers=headers, method="POST")
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            
        return result["content"][0]["text"]

if __name__ == "__main__":
    test_api = TestAPICall()
    print("callling with SDK...")
    test_api.call_with_sdk()

    print("callling with HTTP...")
    test_api.call_with_http()