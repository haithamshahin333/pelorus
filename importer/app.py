from flask import Flask, request
import os
from pymongo import MongoClient

app = Flask(__name__)

mongo_client = None

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
    builds = mongo_client.build.builds
    build_id = builds.insert_one(build).inserted_id
    print("submitted build id: %s" % (build_id))

def create_mongo_client_connection(username, password, database):
    uri = "mongodb://%s:%s@mongodb:27017/%s" % (username,password,database)
    return MongoClient(uri)

if __name__=='__main__':
    print("starting app")

    mongo_username = os.environ.get('MONGODB_USER')
    mongo_password = os.environ.get('MONGODB_PASSWORD')
    mongo_client = create_mongo_client_connection(mongo_username, mongo_password, 'build')

    app.run(host="0.0.0.0", port=8080)