from flask import Flask, request
from token_service import TokenService

app = Flask(__name__)


@app.route("/validate", methods=["POST"])
def hello_world():
    token = request.headers["Authorization"]
    validation = {"status": 200, "response": ""}

    try:
        validation_results = TokenService(token).validate_token()
        print(validation_results)
        validation["status"] = validation_results[0]
        validation["response"] = validation_results[1]
    except Exception as e:
        return {
            "status": 401,
            "response": str(e)
        }

    return validation
