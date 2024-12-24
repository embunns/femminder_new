from flask import Flask, render_template, request, redirect, session, url_for, flash
import requests
import random
import smtplib
from email.mime.text import MIMEText
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import logging

logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "6LfPuJkqAAAAAAsLqUPqfw7dHboMkSUgDEC0LjPx"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Email configuration
EMAIL_ADDRESS = "femminder@gmail.com"  # Replace with sender's email
EMAIL_PASSWORD = "nqao nngn jubz xhqw"  # Replace with email password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Function to send OTP
def send_otp_email(recipient_email, otp):
    try:
        # Email content
        subject = "Your OTP Code"
        body = f"Your OTP code is: {otp}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email

        # Sending email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to SMTP server
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())  # Send email
        logging.info(f"OTP successfully sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send OTP email: {str(e)}")
        raise

# Routes
@app.route('/')
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        logging.debug("Form submitted in signup route")
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        gender = request.form.get('gender')
        captcha_response = request.form.get('g-recaptcha-response')

        logging.debug(f"Form data received: username={username}, email={email}, fullname={fullname}, gender={gender}, captcha_response={captcha_response}")

        if not all([username, password, email, fullname, gender, captcha_response]):
            flash("All fields are required.", "error")
            logging.error("Form submission incomplete. Missing fields.")
            return render_template('signup.html')

        # Verify captcha
        secret_key = "6LfPuJkqAAAAAAsLqUPqfw7dHboMkSUgDEC0LjPx"  # Replace with your secret key
        verify_url = "https://www.google.com/recaptcha/api/siteverify"
        data = {'secret': secret_key, 'response': captcha_response}
        verify_response = requests.post(verify_url, data=data)
        verify_result = verify_response.json()

        logging.debug(f"Captcha verification result: {verify_result}")

        if not verify_result.get("success"):
            flash("Captcha verification failed. Please try again.", "error")
            logging.error("Captcha verification failed.")
            return render_template('signup.html')

        # Check for unique username and email
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email is already taken.", "error")
            logging.warning("Username or email already taken.")
            return render_template('signup.html')

        # Save temporary data to session
        session['signup_data'] = {
            'username': username,
            'password': password,
            'email': email,
            'fullname': fullname,
            'gender': gender,
        }
        logging.debug("Signup data stored in session.")

        # Generate OTP
        otp = str(random.randint(100000, 999999))
        session['otp'] = otp

        # Send OTP to email
        try:
            send_otp_email(email, otp)
            flash("OTP has been sent to your email.", "info")
            logging.info(f"OTP sent to email {email}")
        except Exception as e:
            flash(f"Failed to send OTP: {str(e)}", "error")
            logging.error(f"Error sending OTP: {str(e)}")
            return render_template('signup.html')

        return redirect(url_for('otp'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user is None:
            flash("The username you entered is not registered.", "error")
        elif not user.check_password(password):
            flash("The password you entered is incorrect.", "error")
        else:
            session['username'] = username
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/otp', methods=['GET', 'POST'])
def otp():
    if request.method == 'POST':
        user_otp = request.form.get('otp')
        correct_otp = session.get('otp')

        if user_otp == correct_otp:
            signup_data = session.get('signup_data')
            if not signup_data:
                return "Session expired or invalid request.", 400

            # Save data to database
            try:
                new_user = User(
                    username=signup_data['username'],
                    email=signup_data['email'],
                    fullname=signup_data['fullname'],
                    gender=signup_data['gender']
                )
                new_user.set_password(signup_data['password'])
                db.session.add(new_user)
                db.session.commit()

                session.pop('signup_data', None)
                session.pop('otp', None)

                flash("Signup successful! Please login.", "success")
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                return f"Error: {str(e)}"

        else:
            flash("Invalid OTP. Please try again.", "error")

    return render_template('otp.html')

@app.route('/resend_otp', methods=['POST'])
def resend_otp():
    signup_data = session.get('signup_data')
    if not signup_data:
        return "Session expired or invalid request.", 400

    # Generate new OTP
    otp = str(random.randint(100000, 999999))
    session['otp'] = otp

    # Send OTP to email
    try:
        send_otp_email(signup_data['email'], otp)
        flash("A new OTP has been sent to your email.", "info")
    except Exception as e:
        flash(f"Failed to resend OTP: {str(e)}", "error")

    return redirect(url_for('otp'))

@app.route('/dashboard')
def dashboard():
    username = session.get('username')  # Mengambil username dari session jika ada
    return render_template("dashboard.html", username=username)


# @app.route('/dashboard')
# def dashboard():
#     if "username" in session:
#         return render_template("dashboard.html", username=session['username'])
#     return redirect(url_for('dashboard'))

@app.route('/profileUser')
def profile():
    return render_template("profileUser.html")

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash("You have been logged out.", "success")
    return redirect(url_for('home'))

@app.route('/users')
def show_users():
    # Query semua data dari tabel User
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
