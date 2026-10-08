from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "minha-chave-secreta"


@app.route("/")
def index():
    tarefas = session.get("tarefas", [])
    return render_template("index.html", tarefas=tarefas)


@app.route("/add", methods=["POST"])
def add():
    tarefa = request.form.get("tarefa")

    tarefas = session.get("tarefas", [])

    if tarefa:
        tarefas.append(tarefa)

    session["tarefas"] = tarefas
    session.modified = True

    return redirect("/")


@app.route("/delete/<int:task_id>")
def delete(task_id):
    tarefas = session.get("tarefas", [])

    if 0 <= task_id < len(tarefas):
        tarefas.pop(task_id)

    session["tarefas"] = tarefas
    session.modified = True

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)