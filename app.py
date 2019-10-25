@app.route("/todo", method=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

if __name__ == "__main__":
    Schema()
    app.run(debug=True)