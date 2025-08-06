from flask import Flask, render_template, request, session, redirect, url_for
from agent.utils import load_env
from agent.chat_agent import get_response, init_memory
import uuid

load_env()

app = Flask(__name__)
app.secret_key = "y12345ghnk"  # For session tracking

@app.before_request
def setup():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
        session["chat_history"] = []

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    history = session.get("chat_history", [])

    if request.method == "POST":
        user_input = request.form["message"]
        memory = init_memory(history)

        # Get response using memory
        response = get_response(user_input, memory)
        history.append(("You", user_input))
        history.append(("Bot", response))

        session["chat_history"] = history

    return render_template("chat.html", history=session["chat_history"])



if __name__ == "__main__":
    app.run(debug=True)
