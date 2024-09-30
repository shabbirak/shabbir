from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to calculate force
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        mass = float(request.form['mass'])
        acceleration = float(request.form['acceleration'])
        force = mass * acceleration
        return render_template('index.html', force=force, mass=mass, acceleration=acceleration)
    except ValueError:
        return render_template('index.html', error="Please enter valid numbers.")

if __name__ == '__main__':
    app.run(debug=True)
