from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Database initialization
def init_db():
    conn = sqlite3.connect('portfolio.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  email TEXT NOT NULL,
                  subject TEXT NOT NULL,
                  message TEXT NOT NULL,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('simple.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # Store in database
        conn = sqlite3.connect('portfolio.db')
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name, email, subject, message) VALUES (?, ?, ?, ?)",
                  (name, email, subject, message))
        conn.commit()
        conn.close()
        
        # Send email (configure with your email settings)
        try:
            send_email(name, email, subject, message)
            flash('Message sent successfully!', 'success')
        except:
            flash('Message saved! I will get back to you soon.', 'info')
        
        return redirect(url_for('index') + '#contact')

def send_email(name, email, subject, message):
    # Configure your email settings here
    sender_email = os.environ.get('SENDER_EMAIL', 'your-email@gmail.com')
    sender_password = os.environ.get('SENDER_PASSWORD', 'your-app-password')
    receiver_email = os.environ.get('RECEIVER_EMAIL', 'janinidhi191@gmail.com')
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f"Portfolio Contact: {subject}"
    
    body = f"""
    New contact form submission:
    
    Name: {name}
    Email: {email}
    Subject: {subject}
    Message: {message}
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

@app.route('/download-resume')
def download_resume():
    try:
        return send_file('static/files/Nidhi_Jani_Resume.pdf', as_attachment=True)
    except:
        flash('Resume not found. Please contact me directly.', 'error')
        return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 9000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)