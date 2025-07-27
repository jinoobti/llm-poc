import requests

class SimpleCodeReviewer:
    def __init__(self, api_key, model=""):
        self.api_key = api_key
        self.model = model
        self.url = ""
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def load_standards(self, standards_path):
        with open(standards_path, "r", encoding="utf-8") as f:
            return f.read()

    def load_java_code(self, java_code_path):
        with open(java_code_path, "r", encoding="utf-8") as f:
            return f.read()

    def review_code(self, java_code, standards_text):
        prompt = (
            "You are a Java code reviewer. Review the following code according to these standards:\n\n"
            f"{standards_text}\n\n"
            "Java code to review:\n"
            "```java\n"
            f"{java_code}\n"
            "```\n\n"
            "Please provide a detailed review, pointing out any violations and suggesting improvements."
        )
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
    reviewer = SimpleCodeReviewer(api_key)
    standards = reviewer.load_standards("java_coding_standards.txt")
    java_code = reviewer.load_java_code("example/InvoiceCalculator.java")
    review = reviewer.review_code(java_code, standards)
    print("Code Review:\n", review) 