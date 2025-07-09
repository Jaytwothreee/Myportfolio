from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/coding')
def coding():
    return render_template('coding.html')

@app.route('/pentesting')
def pentesting():
    return render_template('pentesting.html')

@app.route('/pentesting/xss')
def xss_report():
    return render_template('xss_report.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)