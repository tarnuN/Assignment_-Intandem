from flask import Flask, request, render_template
import pandas as pd
from stoppage_detector import detect_stoppages
from map_generator import create_map

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['gpsfile']
        threshold = int(request.form['threshold'])

        df = pd.read_excel(file)
        stoppages = detect_stoppages(df, threshold)
        create_map(df, stoppages)
        return render_template('map.html')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
