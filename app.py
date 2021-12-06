from flask import Flask, request, render_template, send_from_directory
from functions import get_posts_by_tag, read_json, get_tags, add_post


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")
def page_index():
    data = read_json(POST_PATH)
    return render_template('index.html', tags=get_tags(read_json(POST_PATH)))


@app.route("/tag")
def page_tag():
    tag_1 = request.args.get('tag')
    data = read_json(POST_PATH)
    posts = get_posts_by_tag(data, tag_1)
    return render_template('post_by_tag.html', tag_1=tag_1, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')

    content = request.form.get("content")
    picture = request.files.get("picture")

    path = f"{UPLOAD_FOLDER}/{picture.filename}"
    post = {
        'content': content,
        'pic': f'/{path}'
    }

    picture.save(path)
    add_post(POST_PATH, post)

    return render_template('post_uploaded.html', post=post)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

