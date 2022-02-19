from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('calculadora.html')


@app.route('/calculadora', methods=['POST'])
def result():
    v1 = request.form.get("v1", type=int)
    v2 = request.form.get("v2", type=int)
    operacao = request.form.get("operacao")
    if(operacao == 'Adição'):
        result = v1 + v2
    elif(operacao == 'Subtração'):
        result = v1 - v2
    elif(operacao == 'Multiplicação'):
        result = v1 * v2
    elif(operacao == 'Divisão'):
        result = v1 / v2
    else:
        result = 'ESCOLHA INCORRETA'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)