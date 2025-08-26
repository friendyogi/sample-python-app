from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1")
    return f"""
    <html>
        <head><title>GitOps Demo</title></head>
        <body style='text-align:center; font-family:sans-serif; margin-top:5em'>
            <h1>🚀 GitOps App - {version}</h1>
            <p>This is a pretty sample page running on EKS.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
