from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

#pip install Flask

app = Flask(__name__)

#documents = [
#    {
#        "id": 1,
#        "name": "Bricce"
#    },
#    {
#        "id": 2,
#        "name": "Cardoso"
#    }
#]

#result = collection.insert_many(documents)
#print(f"Inserted {len(result.inserted_ids)} documents")
    #hardcoded
    #users = [{'id': 1, 'name': 'Bricce'}, {'id': 2, 'name': 'Cardoso'}]


client = MongoClient("mongodb+srv://fernandoserra:ddNSUUbo1MIhSreQ@force0.7vjgi2i.mongodb.net/?retryWrites=true&w=majority")
db = client["Force0"]
collection = db["api_example"]


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in collection.find():
        users.append({'id': str(user['_id']), 'name': user['name']})
    return jsonify(users)


@app.route('/users', methods=['POST'])
def create_user():
    # Logic to create a new user based on the request data
    data = request.get_json()
    name = data.get('name')
    # Additional validation and error handling as needed

    # Assuming you have a User model
    new_user = {'id': 3, 'name': name}  # Sample data
    return jsonify({'message': 'User created successfully'})


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Logic to update an existing user based on the request data
    data = request.get_json()
    name = data.get('name')
    # Additional validation and error handling as needed

    user = {'id': user_id, 'name': name}  # Sample data
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Logic to delete an existing user
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)