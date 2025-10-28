#!/usr/bin/env python3
"""
LinkedIn OAuth 2.0 Authentication Helper
This script helps you authenticate with LinkedIn and get an access token.
"""

import json
import os
import webbrowser
from urllib.parse import urlencode, parse_qs, urlparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from http.server import HTTPServer, BaseHTTPRequestHandler


class LinkedInAuthHandler(BaseHTTPRequestHandler):
    """HTTP handler for OAuth callback"""
    
    auth_code = None
    
    def do_GET(self):
        """Handle the OAuth callback"""
        query = urlparse(self.path).query
        params = parse_qs(query)
        
        if 'code' in params:
            LinkedInAuthHandler.auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <body>
                    <h1>Authentication Successful!</h1>
                    <p>You can close this window and return to the terminal.</p>
                </body>
                </html>
            """)
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
                <html>
                <body>
                    <h1>Authentication Failed</h1>
                    <p>No authorization code received.</p>
                </body>
                </html>
            """)
    
    def log_message(self, format, *args):
        """Suppress log messages"""
        pass


class LinkedInAuth:
    """LinkedIn OAuth 2.0 Authentication Manager"""
    
    def __init__(self, config_path: str = "/vercel/sandbox/config.json"):
        self.config_path = config_path
        self.config = self._load_config()
        
        self.client_id = self.config.get("client_id")
        self.client_secret = self.config.get("client_secret")
        self.redirect_uri = self.config.get("redirect_uri", "http://localhost:8000/callback")
        
        self.auth_url = "https://www.linkedin.com/oauth/v2/authorization"
        self.token_url = "https://www.linkedin.com/oauth/v2/accessToken"
    
    def _load_config(self) -> dict:
        """Load configuration from file"""
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                return json.load(f)
        return {}
    
    def _save_config(self):
        """Save configuration to file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"✅ Configuration saved to {self.config_path}")
    
    def get_authorization_url(self) -> str:
        """Generate the LinkedIn authorization URL"""
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": "openid profile email w_member_social"
        }
        return f"{self.auth_url}?{urlencode(params)}"
    
    def get_access_token(self, auth_code: str) -> dict:
        """Exchange authorization code for access token"""
        data = {
            "grant_type": "authorization_code",
            "code": auth_code,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "redirect_uri": self.redirect_uri
        }
        
        try:
            data_encoded = urlencode(data).encode('utf-8')
            req = Request(self.token_url, data=data_encoded, method='POST')
            req.add_header("Content-Type", "application/x-www-form-urlencoded")
            
            with urlopen(req) as response:
                return json.loads(response.read().decode())
        except Exception as e:
            print(f"❌ Error getting access token: {e}")
            return None
    
    def authenticate(self):
        """Run the full OAuth authentication flow"""
        print("\n" + "="*80)
        print("🔐 LinkedIn OAuth 2.0 Authentication")
        print("="*80)
        
        if not self.client_id or not self.client_secret:
            print("\n❌ Error: LinkedIn credentials not configured!")
            print("\nPlease follow these steps:")
            print("1. Go to https://www.linkedin.com/developers/apps")
            print("2. Create a new app or select an existing one")
            print("3. Add 'http://localhost:8000/callback' to Authorized Redirect URLs")
            print("4. Copy your Client ID and Client Secret")
            print("5. Update config.json with your credentials")
            return False
        
        # Generate authorization URL
        auth_url = self.get_authorization_url()
        
        print("\n📋 Step 1: Opening LinkedIn authorization page...")
        print(f"\nIf the browser doesn't open automatically, visit this URL:")
        print(f"\n{auth_url}\n")
        
        # Open browser
        webbrowser.open(auth_url)
        
        print("📋 Step 2: Waiting for authorization callback...")
        print("(Authorize the app in your browser)\n")
        
        # Start local server to receive callback
        server = HTTPServer(('localhost', 8000), LinkedInAuthHandler)
        server.handle_request()
        
        if LinkedInAuthHandler.auth_code:
            print("✅ Authorization code received!")
            print("\n📋 Step 3: Exchanging code for access token...")
            
            token_data = self.get_access_token(LinkedInAuthHandler.auth_code)
            
            if token_data and 'access_token' in token_data:
                self.config['access_token'] = token_data['access_token']
                self._save_config()
                
                print("\n" + "="*80)
                print("✅ Authentication Successful!")
                print("="*80)
                print(f"\nAccess Token: {token_data['access_token'][:20]}...")
                print(f"Expires in: {token_data.get('expires_in', 'N/A')} seconds")
                print("\n✅ You can now use the LinkedIn agent to post content!")
                print("="*80 + "\n")
                return True
            else:
                print("\n❌ Failed to get access token")
                return False
        else:
            print("\n❌ No authorization code received")
            return False


def main():
    """Main function"""
    auth = LinkedInAuth()
    
    # Check if already authenticated
    if auth.config.get('access_token'):
        print("\n" + "="*80)
        print("ℹ️  Existing Access Token Found")
        print("="*80)
        print(f"\nAccess Token: {auth.config['access_token'][:20]}...")
        
        choice = input("\nDo you want to re-authenticate? (y/n): ").strip().lower()
        if choice != 'y':
            print("\n✅ Using existing access token")
            return
    
    # Run authentication
    auth.authenticate()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Authentication cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
