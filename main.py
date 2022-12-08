from flask import Flask, jsonify,render_template
import os
import flask

# print(dir(flask))

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('Analisis_data.html')

@app.route('/assets/<name>')
def button_grafik(name):
    return render_template('assets/'+name)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
