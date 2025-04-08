from flask import Flask, request, jsonify
from app.call_handler import process_call

app = Flask(__name__)

@app.route('/trigger_call', methods=['POST'])
def trigger_call():
    data = request.json
    mobile_number = data.get('mobile_number')
    if not mobile_number:
        return jsonify({"error": "mobile_number is required"}), 400
    
    try:
        result = process_call(mobile_number)
        return jsonify({"status": "success", "data": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
