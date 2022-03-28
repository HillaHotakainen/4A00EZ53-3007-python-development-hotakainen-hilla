
from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)

id = 2
posts = [{"id": 1, "title": "blahb blah", "body": "bluh bluh"}, 
         {"id": 2, "title": "liirun laarum", "body": "spurdo spärdö spörlölöö"}]

@app.route('/posts')
def get_posts():
    return jsonify(posts)

@app.route('/posts', methods=['POST'])
def add_posts():
    blog_post = json.loads(request.data)
    # https://www.programiz.com/python-programming/global-keyword
    global id
    id = id + 1
    blog_post["id"] = id
    posts.append(blog_post)
    return  make_response(jsonify(blog_post), 201)

@app.route('/posts/<int:the_id>', methods=['DELETE'])
def delete_blog_post(the_id):
    if the_id == 0:
        global id
        id = 0
        global posts
        posts.clear()
        return make_response("", 204)
    index_to_be_deleted = -1
    for i in range(0, len(posts)):
        if(posts[i]["id"] == the_id):
            index_to_be_deleted = i
    if(index_to_be_deleted != -1):
        posts.pop(index_to_be_deleted)
        return make_response("", 204)
    else:
        return make_response("", 404)
if __name__ == "__main__":
    app.run(debug=True)