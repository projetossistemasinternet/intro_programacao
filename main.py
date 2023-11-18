from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporária de tarefas
tasks = [{"id": 1, "content": "Fazer compras"}, {"id": 2, "content": "Estudar Flask"}]
task_id_counter = 3

# Glossário temporário de tarefas
glossary = [
    {"id": 1, "concept": "Flask", "definition": "Um framework web leve para Python"},
    {"id": 2, "concept": "CRUD", "definition": "Create, Read, Update, Delete"},
]
glossary_id_counter = 3


# ROTAS
@app.route("/")
def index():
    return render_template("index.html")


# ROTAS TAREFAS
@app.route("/tarefas")
def tarefas():
    return render_template("tarefas.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add_task():
    global task_id_counter
    content = request.form.get("content")
    task = {"id": task_id_counter, "content": content}
    tasks.append(task)
    task_id_counter += 1
    return redirect(url_for("tarefas"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return redirect(url_for("tarefas"))


@app.route("/edit_tarefas/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)

    if request.method == "POST":
        task["content"] = request.form.get("content")
        return redirect(url_for("tarefas"))

    return render_template("edit_tarefas.html", task=task)


# ROTAS GLOSSÁRIO
@app.route("/glossario")
def glossario():
    return render_template("glossario.html", glossary=glossary)


@app.route("/add_concept", methods=["POST"])
def add_concept():
    global glossary_id_counter
    concept = request.form.get("concept")
    definition = request.form.get("definition")
    entry = {"id": glossary_id_counter, "concept": concept, "definition": definition}
    glossary.append(entry)
    glossary_id_counter += 1
    return redirect(url_for("glossario"))


@app.route("/delete_concept/<int:concept_id>")
def delete_concept(concept_id):
    global glossary
    glossary = [entry for entry in glossary if entry["id"] != concept_id]
    return redirect(url_for("glossario"))


@app.route("/edit_concept/<int:concept_id>", methods=["GET", "POST"])
def edit_concept(concept_id):
    entry = next((e for e in glossary if e["id"] == concept_id), None)

    if request.method == "POST":
        entry["concept"] = request.form.get("concept")
        entry["definition"] = request.form.get("definition")
        return redirect(url_for("glossario"))

    return render_template("edit_concept.html", entry=entry)


if __name__ == "__main__":
    app.run(debug=True)
