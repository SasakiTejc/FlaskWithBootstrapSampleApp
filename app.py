from flask import Flask,render_template,request,session,redirect
app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',title='Index',message='Hello this is Bootstrap sample')

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')