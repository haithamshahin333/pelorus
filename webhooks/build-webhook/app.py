from flask import Flask, request
import os
from pymongo import MongoClient

app = Flask(__name__)

db = None

@app.route('/post/build', methods=['POST'])
def insert_build():
    request_data = request.get_json()

    build = {"app": request_data["app"],
            "commit": request_data["commit"],
            "image_sha": request_data["image_sha"],
            "git_provider": request_data["git_provider"],
            "repo": request_data["repo"],
            "branch": request_data["branch"]}

    insert_build(build)

    return "submitted"

def insert_build(build):
    print("submitting build: %s" % (build))
    build_id = db.builds.insert_one(build).inserted_id
    print("submitted build id: %s" % (build_id))

def create_mongo_client_connection(username, password, host, database):
    uri = "mongodb://%s:%s@%s:27017/%s" % (username,password,host,database)
    print(uri)
    return MongoClient(uri)[database]

if __name__=='__main__':
    print("starting app")

    mongo_username = os.environ.get('MONGODB_USER')
    mongo_password = os.environ.get('MONGODB_PASSWORD')
    mongo_servicename = os.environ.get('MONGODB_SERVICE_HOST')
    mongo_database = os.environ.get('MONGODB_DATABASE')
    db = create_mongo_client_connection(mongo_username, mongo_password, mongo_servicename, mongo_database)

    app.run(host="0.0.0.0", port=8080)