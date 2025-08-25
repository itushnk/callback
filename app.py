import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def root():
    return "OK", 200

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/ae/callback")
def ae_callback():
    code = request.args.get("code")
    state = request.args.get("state")
    # Log to stdout so you'll see it in Railway logs
    print(f"[AE CALLBACK] code={code!r} state={state!r}", flush=True)
    # Keep response simple
    return "OK", 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)
