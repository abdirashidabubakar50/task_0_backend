from flask import Flask, jsonify
import datetime
from flask_cors import CORS


app = Flask(__name__)

CORS(app)


@app.route('/', methods=['GET'])
def info():
    email_address = 'abdirashidabubakar7@gmail.com'
    current_date_time = datetime.datetime.utcnow().isoformat() + 'Z'
    github_url = 'https://github.com/abdirashidabubakar50/task_0_backend'

    response = {
        'email': email_address,
        'current_datetime': current_date_time,
        'github_url': github_url
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run()