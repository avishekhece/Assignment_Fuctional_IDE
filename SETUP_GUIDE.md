# LinkedIn Agent - Setup & Usage Guide

## 🎯 Overview

Your LinkedIn agent can now **generate AND post** content directly to LinkedIn! This guide will walk you through the complete setup process.

## 📋 Prerequisites

- Python 3.7+ (with standard library - no additional packages needed!)
- LinkedIn account
- LinkedIn Developer App (we'll create this)

## 🚀 Quick Start

### Step 1: Verify Python Installation

```bash
python3 --version
# Should show Python 3.7 or higher
```

**Note**: No additional packages needed! The agent uses Python's built-in `urllib` library.

### Step 2: Create LinkedIn Developer App

1. Go to [LinkedIn Developers](https://www.linkedin.com/developers/apps)
2. Click **"Create app"**
3. Fill in the required information:
   - **App name**: LinkedIn Automation Agent
   - **LinkedIn Page**: Select your company page (or create one)
   - **App logo**: Upload any logo
   - **Legal agreement**: Check the box
4. Click **"Create app"**

### Step 3: Configure App Settings

1. In your app dashboard, go to the **"Auth"** tab
2. Under **"OAuth 2.0 settings"**:
   - Add redirect URL: `http://localhost:8000/callback`
   - Click **"Update"**
3. Under **"OAuth 2.0 scopes"**, request access to:
   - `openid`
   - `profile`
   - `email`
   - `w_member_social` (This is the key one for posting!)
4. Copy your **Client ID** and **Client Secret**

### Step 4: Configure Your Agent

1. Copy the config template:
   ```bash
   cp config.json.template config.json
   ```

2. Edit `config.json` with your credentials:
   ```json
   {
     "client_id": "YOUR_CLIENT_ID_HERE",
     "client_secret": "YOUR_CLIENT_SECRET_HERE",
     "access_token": "",
     "redirect_uri": "http://localhost:8000/callback"
   }
   ```

### Step 5: Authenticate with LinkedIn

Run the authentication script:

```bash
python3 linkedin_auth.py
```

This will:
1. Open your browser to LinkedIn's authorization page
2. Ask you to authorize the app
3. Receive the authorization code
4. Exchange it for an access token
5. Save the token to `config.json`

**Note**: The access token typically expires after 60 days. You'll need to re-authenticate when it expires.

## 📤 Publishing Posts to LinkedIn

### Option 1: Create and Publish New Post

```bash
python3 post_to_linkedin.py
```

Then select option **1** to:
1. Choose post type (Tip, Case Study, or Insight)
2. Review the generated content
3. Publish directly to LinkedIn

### Option 2: Publish Existing Draft

If you have draft posts (like the demo posts):

```bash
python3 post_to_linkedin.py
```

Then select option **2** to:
1. View all available drafts
2. Select one to publish
3. Confirm and post to LinkedIn

### Option 3: Programmatic Publishing

You can also use the agent in your own Python scripts:

```python
from linkedin_agent import LinkedInAgent

# Initialize agent
agent = LinkedInAgent()

# Generate a post
post = agent.generate_post(post_type="tip")

# Publish to LinkedIn
published_post = agent.publish_post(post)

# Check status
if published_post["status"] == "published":
    print(f"✅ Posted! ID: {published_post['linkedin_post_id']}")
else:
    print(f"❌ Failed: {published_post['error']}")
```

## 🔧 Advanced Usage

### Publishing with Custom Access Token

```python
agent = LinkedInAgent()
post = agent.generate_post(post_type="case_study")
agent.publish_post(post, access_token="YOUR_CUSTOM_TOKEN")
```

### Direct API Call

```python
agent = LinkedInAgent()
result = agent.post_to_linkedin(
    post_content="Your custom post content here...",
    access_token="YOUR_TOKEN"
)
```

## 📊 Post Status Tracking

Posts have the following statuses:

- **`draft`**: Generated but not published
- **`published`**: Successfully posted to LinkedIn
- **`failed`**: Publishing attempt failed

Published posts include:
- `linkedin_post_id`: The LinkedIn post ID
- `published_at`: Timestamp of publication

## 🔍 Troubleshooting

### Error: "No access token provided"

**Solution**: Run `python3 linkedin_auth.py` to authenticate

### Error: "Could not retrieve LinkedIn person URN"

**Solution**: Your access token may be expired. Re-authenticate with `python3 linkedin_auth.py`

### Error: "HTTP Error: 401"

**Solution**: Access token is invalid or expired. Re-authenticate.

### Error: "HTTP Error: 403"

**Solution**: Your app doesn't have the required permissions. Make sure you requested `w_member_social` scope in your LinkedIn app settings.

### Error: "HTTP Error: 429"

**Solution**: You've hit LinkedIn's rate limit. Wait a few minutes before trying again.

## 📈 Best Practices

### Posting Frequency

- **Don't spam**: LinkedIn recommends 1-2 posts per day maximum
- **Optimal times**: Tuesday-Thursday, 8-10 AM or 12-1 PM
- **Consistency**: Regular posting (3-5 times per week) is better than sporadic bursts

### Content Strategy

1. **Week 1**: Post 2 tip posts
2. **Week 2**: Post 1 case study + 1 tip
3. **Week 3**: Post 1 insight + 1 tip
4. **Week 4**: Post 1 case study + 1 insight

### Engagement

After posting:
- Respond to comments within 1-2 hours
- Engage with others' posts in your niche
- Track which post types get the most engagement
- Adjust your content strategy accordingly

## 🔐 Security Notes

1. **Never commit `config.json`** to version control (it's in `.gitignore`)
2. **Keep your access token secret** - it has full posting permissions
3. **Rotate tokens regularly** - re-authenticate every 30 days for security
4. **Use environment variables** in production:
   ```bash
   export LINKEDIN_ACCESS_TOKEN="your_token"
   ```

## 📁 File Structure

```
/vercel/sandbox/
├── linkedin_agent.py          # Main agent with posting capability
├── linkedin_auth.py           # OAuth authentication helper
├── post_to_linkedin.py        # CLI for publishing posts
├── create_post.py             # Simple post creation CLI
├── config.json                # Your credentials (DO NOT COMMIT)
├── config.json.template       # Template for credentials
├── demo_tip_post.json         # Example draft posts
├── demo_case_study_post.json
├── demo_insight_post.json
└── SETUP_GUIDE.md            # This file
```

## 🎓 Example Workflow

Here's a complete workflow from setup to posting:

```bash
# 1. Verify Python installation
python3 --version

# 2. Configure credentials
cp config.json.template config.json
# Edit config.json with your LinkedIn app credentials

# 3. Authenticate
python3 linkedin_auth.py
# Follow the browser flow

# 4. Create and publish a post
python3 post_to_linkedin.py
# Select option 1, choose post type, review, and publish

# 5. Verify on LinkedIn
# Check your LinkedIn profile to see the post!
```

## 🆘 Getting Help

If you encounter issues:

1. Check the troubleshooting section above
2. Verify your LinkedIn app has the correct permissions
3. Make sure your access token hasn't expired
4. Check LinkedIn's API status page

## 🎉 Success!

Once you see "✅ Post published successfully to LinkedIn!", your post is live! 

You can now:
- Generate unlimited posts
- Publish directly to LinkedIn
- Track your posting history
- Build your automation testing business through consistent LinkedIn presence

---

**Happy Posting! 🚀**
