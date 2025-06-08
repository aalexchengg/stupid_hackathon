from flask import Flask, render_template, redirect, url_for
import subprocess
import os

app = Flask(__name__)
scripts = []

def run_script(script_name):
    try:
        scripts.append(subprocess.Popen(['python', f'scripts/{script_name}']))
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")


@app.route('/stop_script', methods=['POST'])
def stop_script():
    while(scripts):
        curr = scripts.pop()
        curr.terminate()
    return redirect(url_for('index'))

@app.route('/')
def index():
    # subprocess.Popen(['python', 'listen.py'])
    return render_template('index.html')

@app.route('/run/<script_id>', methods=['POST'])
def run_script_by_id(script_id):
    script_map = {
        '1': 'allin.py',
        '2': 'jobapp.py',
        '3': 'chaewon.py',
        '4': 'doomscroll.py',
    }

    script_name = script_map.get(script_id)
    if script_name:
        run_script(script_name)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
