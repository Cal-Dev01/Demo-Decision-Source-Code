from flask import Flask, request, render_template, redirect, url_for, session, send_from_directory
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Create upload folder if not exist
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            session['uploaded_filepath'] = filepath

            # Identify rows with issues
            missing_values = df.isnull().sum().sum()
            duplicates = df.duplicated().sum()
            columns = df.columns.tolist()

            return render_template('review.html', filename=file.filename, missing_values=missing_values,
                                   duplicates=duplicates,
                                   data=df.to_html(classes='table table-striped', table_id='data-table'))

    return render_template('index.html')


@app.route('/clean', methods=['POST'])
def clean():
    filepath = session.get('uploaded_filepath')
    df = pd.read_csv(filepath)

    if request.form.get('remove_duplicates') == 'on':
        df.drop_duplicates(inplace=True)

    interpolate_numeric = request.form.get('interpolate_numeric')
    nan_numeric = request.form.get('nan_numeric')
    nan_string = request.form.get('nan_string')

    if nan_numeric and not interpolate_numeric:
        try:
            nan_numeric = float(nan_numeric)  # Ensure it is a numeric value
        except ValueError:
            nan_numeric = None  # If conversion fails, set to None

    if interpolate_numeric:
        df.interpolate(method='linear', inplace=True)

    for column in df.select_dtypes(include=[np.number]).columns:
        if nan_numeric is not None and not interpolate_numeric:
            df[column].fillna(nan_numeric, inplace=True)

    for column in df.select_dtypes(include=[object]).columns:
        if nan_string:
            df[column].fillna(nan_string, inplace=True)

    cleaned_filename = 'cleaned_' + os.path.basename(filepath)
    cleaned_filepath = os.path.join(app.config['UPLOAD_FOLDER'], cleaned_filename)
    df.to_csv(cleaned_filepath, index=False)

    return render_template('data.html',
                           original_df=pd.read_csv(filepath).to_html(classes='table table-striped',
                                                                     table_id='data-table'),
                           cleaned_df=df.to_html(classes='table table-striped', table_id='data-table'),
                           cleaned_filename=cleaned_filename)


@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)
