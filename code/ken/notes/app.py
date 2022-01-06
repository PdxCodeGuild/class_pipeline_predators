from flask import Flask
app = Flask(__name__)

@app.route('/')
def show_user_name(username):
    return render_template('index.html')

app.run(debug=True)

