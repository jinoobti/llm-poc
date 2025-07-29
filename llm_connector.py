import requests

class LLMConnector:
    def __init__(self, api_key, model=""):
        self.api_key = api_key
        self.model = model
        self.url = ""
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def ask(self, prompt):
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post(self.url, headers=self.headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]

# Example usage:
if __name__ == "__main__":
    api_key = ""  # Replace with your actual API key
    llm = LLMConnector(api_key)
    answer = llm.ask("What is the capital of France?")
    print("LLM Response:", answer)