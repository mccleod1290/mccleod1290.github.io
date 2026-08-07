from flask import Flask, request, jsonify, render_template, redirect, session, url_for
import os
import uuid

app = Flask(__name__)
app.secret_key = 'super_secret_hack_smarter_key'

users = {
    "administrator": "SuperSecretAdminPassword123!" 
}

valid_tokens = {}

# The flag the user is trying to get
FLAG = "HSM{1mpl1c1t_trU5t_1s_b4d_mkay}"

# --- MAIN ROUTE ---

@app.route('/')
def index():
    """Serves the main login page for the vulnerable client."""
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

# --- HACK SMARTER ID (SSO PROVIDER) ROUTES ---

@app.route('/sso/login', methods=['GET', 'POST'])
def sso_login():
    """SSO Provider Login Page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and users[username] == password:
            session['sso_user'] = username
            return redirect(url_for('oauth_auth'))
        else:
            return render_template('sso_login.html', error="Invalid username or password.")
            
    return render_template('sso_login.html')

@app.route('/sso/register', methods=['GET', 'POST'])
def sso_register():
    """SSO Provider Registration Page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            return render_template('sso_register.html', error="All fields are required.")
            
        if username in users:
            return render_template('sso_register.html', error="Username already exists. Please choose another.")
            
        # Register the user and log them into the SSO provider
        users[username] = password
        session['sso_user'] = username
        return redirect(url_for('oauth_auth'))
        
    return render_template('sso_register.html')

@app.route('/oauth/auth')
def oauth_auth():
    """
    Simulates the OAuth provider's authorization endpoint.
    If the user isn't logged into the SSO provider, redirect them to login.
    """
    if 'sso_user' not in session:
        return redirect(url_for('sso_login'))
        
    return render_template('mock_consent.html', username=session['sso_user'])

@app.route('/oauth/approve', methods=['POST'])
def oauth_approve():
    """
    Simulates the user clicking "Authorize" on the consent screen.
    """
    if 'sso_user' not in session:
        return redirect(url_for('sso_login'))
        
    current_sso_user = session['sso_user']
    
    
    access_token = uuid.uuid4().hex
    valid_tokens[access_token] = current_sso_user
    
    redirect_url = f"{url_for('index')}#access_token={access_token}&username={current_sso_user}"
    return redirect(redirect_url)

# --- CLIENT APP: API & DASHBOARD ---

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Invalid request."}), 400
        
    client_token = data.get('access_token')
    client_username = data.get('username')
    
    # Fix: only trust the username bound to the token at issuance time.
    # Never accept a client-supplied username alone for session elevation.
    if client_token in valid_tokens:
        token_username = valid_tokens[client_token]
        if client_username is not None and client_username != token_username:
            return jsonify({
                "success": False,
                "message": "Token subject mismatch. Username does not match the access token."
            }), 401
        session['username'] = token_username
        return jsonify({"success": True})
        
    else:
        return jsonify({"success": False, "message": "Invalid or expired access token."}), 401

@app.route('/dashboard')
def dashboard():
    """Protected area."""
    if 'username' not in session:
        return redirect(url_for('index'))
        
    username = session['username']
    
    if username == 'administrator':
        flag = FLAG
    else:
        flag = None
        
    return render_template('dashboard.html', username=username, flag=flag)

@app.route('/logout')
def logout():
    """Clears all sessions (both Client App and SSO Provider)."""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
