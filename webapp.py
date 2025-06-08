from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

@app.route('/run-after-countdown', methods=['POST'])
def run_after_countdown():
    print("Countdown finished — running backend Python code.")
    # You can put any logic here (e.g., saving data, triggering a task, etc.)
    return jsonify({"redirect_url": url_for('index')})

if __name__ == '__main__':
    app.run(debug=True)
