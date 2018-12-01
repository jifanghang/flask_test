from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def hello_world(postID):
    return 'Blog Number %d' % postID
# app.add_url_rule('/', 'hello', hello_world)

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run(debug = True)
