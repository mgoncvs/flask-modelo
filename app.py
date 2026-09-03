from flask import Flask, render_template, request, redirect , session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave-super-secreta'

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/painel")
def painel():
    if 'usuario_nome' in session:
        return render_template("painel.html",usuario_nome=session['usuario_nome'],usuario_cpf=session['usuario_cpf'])
    return redirect('/')

@app.route("/verificar", methods=['POST'])
def verificar():
    cpf = request.form.get('cpf')
    senha = request.form.get('senha')

    print('tentando login com: ', cpf,'/senha: ',senha)
    
    if cpf == "07771232159" and senha == "4295":
        session['usuario_nome'] = "maria"
        session['usuario_cpf'] = cpf
        return redirect('/painel')
    
    if cpf=="044223345608" and senha == "123454":
        session['usuario_nome'] = "taylor"
        session['usuario_cpf'] = cpf
        return redirect('/painel')

    return redirect('/')

@app.route('/Sair')
def Sair():
    session.pop('usuario_nome',None)
    session.pop('usuario_cpf',None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)