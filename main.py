from flask import Flask, jsonify,render_template
import os
import flask

# print(dir(flask))

app = Flask(__name__)



@app.route('/')
def home():
    # return "<h1>Rizal Mujahiddan Ganteng</h1>"
    # return '<h1>'+app.root_path+'</h1>'
    return render_template('Analisis_data.html')

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
