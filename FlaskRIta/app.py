from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        return f'Nome: {nome} | Email: {email}'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)

