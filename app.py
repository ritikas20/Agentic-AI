from flask import Flask, render_template, request
from agent.utils import load_env
from agent.langgraph_agent import build_graph


load_env()
app = Flask(__name__)
graph = build_graph()

@app.route("/", methods=["GET", "POST"])
def index():
    report_path = None
    if request.method == "POST":
        product = request.form["product"]
        final_state = graph.invoke({"product": product})
        report_path = final_state.get("file")

    return render_template("index.html", file=report_path)

if __name__ == "__main__":
    app.run(debug=True)

