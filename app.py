from flask import Flask, request, jsonify
from simple_code_reviewer import SimpleCodeReviewer

app = Flask(__name__)
reviewer = SimpleCodeReviewer(api_key="")
standards = reviewer.load_standards("java_coding_standards.txt")

@app.route('/api/review', methods=['POST'])
def review():
    data = request.get_json()
    java_code = data.get('java_code', '')
    review = reviewer.review_code(java_code, standards)
    return jsonify({'review': review})

if __name__ == '__main__':
    app.run(port=5000)