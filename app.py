import json
from flask import Flask
from router.Student import student_router

app = Flask(__name__)

app.register_blueprint(student_router,url_prefix="/student")

@app.route('/')
def index():
    return "Welcome to Our School"

@app.errorhandler(404)
def notFound(error):
    return {
        "error": "Page not found"
    }

if __name__ == "__main__":
    app.run(debug=True)