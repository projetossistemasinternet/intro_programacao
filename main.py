from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporária de tarefas
tasks = [{"id": 1, "content": "Fazer compras"}, {"id": 2, "content": "Estudar Flask"}]
task_id_counter = 3  # contador para IDs de tarefas


# Rotas
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global task_id_counter
    content = request.form.get("content")
    task = {"id": task_id_counter, "content": content}
    tasks.append(task)
    task_id_counter += 1
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("index"))


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if request.method == "POST":
        task["content"] = request.form.get("content")
        return redirect(url_for("index"))

    return render_template("edit.html", task=task)


if __name__ == "__main__":
    app.run(debug=True)
