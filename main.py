from flask import Flask, request,jsonify#FLASK 

app= Flask(__name__)#create our flask app

@app.route("/get-user/<user_id>")#path
def get_user(user_id):
    user_Data={#mark some data I want to return for this user
        "user_id":user_id,
        "name":"Jonh Doe",
        "email": "john.doe@example.com"

    }#Python´s dictionary
    "/get-user/6226 "
    extra = request.args.get("extra")
    if extra:
        user_Data["extra"]= extra
    return jsonify(user_Data), 200

@app.route("/create-user",methods=["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data),201

if __name__ == "__main__":
    app.run(debug=True)