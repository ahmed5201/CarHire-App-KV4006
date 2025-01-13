from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')

# Route for the car rentals page
@app.route('/car_rentals')
def car_rentals():
    return render_template('car_rentals.html')

# Route for the search page
@app.route('/search')
def search():
    return render_template('search.html')

# Route for the signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route for the suggestions page
@app.route('/suggestions')
def suggestions():
    return render_template('suggestions.html')

# Route for the vehicle details page
@app.route('/vehicledetails')
def vehicledetails():
    return render_template('vehicledetails.html')

if __name__ == '__main__':
    app.run(debug=True)
