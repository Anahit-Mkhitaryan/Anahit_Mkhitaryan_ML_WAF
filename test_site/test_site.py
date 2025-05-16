from flask import Flask, request, jsonify, abort, redirect, url_for
import requests

app = Flask(__name__)

# URL of the WAF API
WAF_API_URL = 'http://127.0.0.1:5000/predict'


@app.before_request
def waf_filter():
    # Ignore form submission and root index so they can be used manually
    if request.endpoint in ['index', 'submit_request']:
        return

    # Create a simplified string representing the incoming request
    req_text = f"{request.method} {request.path}?{request.query_string.decode()}"

    try:
        response = requests.post(WAF_API_URL, json={'request': req_text})
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'blocked':
                return f"<h3>🚫 Blocked by WAF: {data['message']}</h3>", 403
    except Exception as e:
        return f"<h3>⚠️ WAF check failed: {str(e)}</h3>", 500


@app.route('/')
def index():
    return """
    <html>
        <body>
            <h1>Welcome to the Test Website!</h1>
            <form action="/submit" method="post">
                <label for="request">Enter request text:</label><br>
                <textarea id="request" name="request" rows="4" cols="50"></textarea><br>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """


@app.route('/submit', methods=['POST'])
def submit_request():
    request_text = request.form['request']

    try:
        response = requests.post(WAF_API_URL, json={'request': request_text})
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": "WAF prediction failed"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/admin/delete')
def admin_delete():
    return "<h3>Admin delete page accessed!</h3>"


@app.route('/user/profile')
def user_profile():
    return "<h3>User profile page</h3>"


if __name__ == '__main__':
    app.run(port=8000)

