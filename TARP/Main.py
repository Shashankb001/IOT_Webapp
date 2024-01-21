from flask import Flask, render_template, Response, request, redirect, jsonify, session
from flask_session import Session
from Data import generate_data

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#redirects
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

#data
@app.route('/login_response', methods=['POST'])
def login_response():
    data = request.get_json()
    username = data['username']
    password = data['password']
    if username == 'admin' and password == 'admin':
        session['username'] = username
        return jsonify({"result": "success"})
    else:
        return jsonify({"result": "failure"})
    
@app.route('/graph_data')
def graph_data():
    graph1, graph2, graph3, graph4, graph5, graph6, target = generate_data()
    data = {
        "graph1": graph1,
        "graph2": graph2,
        "graph3": graph3,
        "graph4": graph4,
        "graph5": graph5,
        "graph6": graph6,
        "target": target
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)