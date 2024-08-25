from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    json_data = request.get_json()
    try:
        # Ensure the request content type is JSON
        if not request.is_json:
            return jsonify({"is_success": False, "message": "Content type must be application/json"}), 400
        
        # Parse the JSON data
        json_data = request.get_json()

        # Check if 'data' is in the JSON payload
        if 'data' not in json_data:
            return jsonify({"is_success": False, "message": "'data' key is missing in the JSON request"}), 400

        # Extract data
        
        data = json_data['data']

        print(data)

        # Sample User Data
        user_id = "john_doe_17091999"
        email = "john@xyz.com"
        roll_number = "ABCD123"

        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find the highest lowercase alphabet
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

        # Response
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        return jsonify(response), 200

    except Exception as e:
        # Error Handling
        print("hello")
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    # Hardcoded response for GET request
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
