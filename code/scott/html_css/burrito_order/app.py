from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        tortilla= request.form.get('tortilla')
        protein= request.form.get('protein')
        beans= request.form.get('beans')
        cheese= request.form.get('cheese')
        salsa= request.form.get('salsa')
        sour_cream= request.form.get('sour_cream')
        guacamole= request.form.get('guacamole')
        return render_template('index.html', tortilla= tortilla, protein=protein, beans=beans, 
        cheese=cheese, salsa=salsa, sour_cream=sour_cream, guacamole=guacamole)
    elif request.method== 'GET':
        return 'A request was made'

@app.route('/order/', methods=['GET', 'POST'])
def order():   
    return render_template('order.html')

app.run(debug=True)