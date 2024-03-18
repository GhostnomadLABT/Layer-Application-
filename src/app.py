from flask import Flask, request, jsonify, render_template, redirect, url_for
from repository.grocery_main import read_csv_to_dict, append_dict_to_csv, write_dicts_to_csv
app = Flask(__name__)

data = read_csv_to_dict('sample_grocery.csv')

# http://localhost:8081/items
@app.route("/items", methods=["GET"])
def mostrar():
    return jsonify(data)

#Buscar el item por su SKU 
#http://localhost:8081/item/E234
@app.route("/item/<SKU>", methods=["GET"])
def mostrarlista(SKU):
    item = mostrarSKU(SKU)
    if item is None:
        return jsonify({})
    else:
        return jsonify({
            "SKU": item["SKU"],
            "Name": item["Name"],
            "Description": item["Description"],
            "Price": item["Price"],
            "Quantity": item["Quantity"],
            "Expiration Date": item["Expiration Date"]
        })

def mostrarSKU(SKU):
    for item in data:
        if item["SKU"] == SKU:
            return item
    return None 

# Ruta para mostrar el formulario para agregar un nuevo artículo
#http://localhost:8081/item/add
@app.route("/item/add", methods=["GET"])
def show_add_item_form():
    return render_template('nuevoitem.html')

# Ruta para manejar la solicitud POST y agregar un nuevo artículo al archivo CSV
@app.route("/item", methods=["POST"])
def add_item():
    new_item = {
        "SKU": request.form["SKU"],
        "Name": request.form["Name"],
        "Description": request.form["Description"],
        "Price": float(request.form["Price"]),
        "Quantity": int(request.form["Quantity"]),
        "Expiration Date": request.form["ExpirationDate"]
    }
    data.append(new_item)
    append_dict_to_csv('sample_grocery.csv', new_item)  # Agregar nuevo artículo al archivo CSV
    return redirect(url_for('mostrar'))  # Redirigir a la página de lista de artículos

# Mostrar formulario de eliminación de artículo
#http://localhost:8081/item/delete_form
@app.route("/item/delete_form", methods=["GET"])
def delete_form():
    return render_template('eliminar.html')

# Eliminar un artículo por SKU
@app.route("/delete_item", methods=["POST"])
def delete_item():
    SKU = request.form.get("SKU")
    if SKU:
        global data
        data = [item for item in data if item["SKU"] != SKU]
        write_dicts_to_csv('sample_grocery.csv', data)  # Actualizar archivo CSV
        return jsonify({"message": f"Item with SKU {SKU} deleted successfully"}), 200
    else:
        return jsonify({"error": "SKU is required"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8081)
