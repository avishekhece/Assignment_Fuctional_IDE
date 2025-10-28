# LinkedIn Agent - Quick Reference

## 🚀 Quick Commands

### First Time Setup
```bash
# 1. Copy config template
cp config.json.template config.json

# 2. Edit config.json with your LinkedIn app credentials
# (Get from https://www.linkedin.com/developers/apps)

# 3. Authenticate
python3 linkedin_auth.py
```

### Post to LinkedIn
```bash
# Interactive posting
python3 post_to_linkedin.py

# Test the system
python3 test_posting.py
```

---

## 💻 Code Examples

### Generate and Post
```python
from linkedin_agent import LinkedInAgent

agent = LinkedInAgent()
post = agent.generate_post(post_type="tip")
agent.publish_post(post)
```

### Post Existing Draft
```python
import json
from linkedin_agent import LinkedInAgent

# Load draft
with open("demo_tip_post.json") as f:
    post = json.load(f)

# Publish
agent = LinkedInAgent()
agent.publish_post(post)
```

### Direct API Call
```python
from linkedin_agent import LinkedInAgent

agent = LinkedInAgent()
result = agent.post_to_linkedin("Your custom content here...")

if result["success"]:
    print(f"Posted! ID: {result['post_id']}")
```

---

## 📋 Post Types

| Type | Description | Use Case |
|------|-------------|----------|
| `tip` | Best practices & advice | Weekly tips, how-tos |
| `case_study` | Success stories with metrics | Showcase results |
| `insight` | Industry trends & future | Thought leadership |

---

## 🔧 Configuration

### config.json Structure
```json
{
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "access_token": "YOUR_ACCESS_TOKEN",
  "redirect_uri": "http://localhost:8000/callback"
}
```

### Get LinkedIn Credentials
1. Go to https://www.linkedin.com/developers/apps
2. Create app
3. Add redirect URL: `http://localhost:8000/callback`
4. Request scope: `w_member_social`
5. Copy Client ID & Secret

---

## 🎯 Posting Schedule

### Recommended Frequency
- **Optimal**: 3-5 posts per week
- **Maximum**: 2 posts per day
- **Best times**: Tue-Thu, 8-10 AM or 12-1 PM

### Example Schedule
```
Monday:    Tip Post
Wednesday: Case Study
Friday:    Insight Post
```

---

## 🔍 Troubleshooting

| Error | Solution |
|-------|----------|
| No access token | Run `python3 linkedin_auth.py` |
| HTTP 401 | Token expired, re-authenticate |
| HTTP 403 | Check app permissions |
| HTTP 429 | Rate limited, wait 5 minutes |

---

## 📁 File Structure

```
/vercel/sandbox/
├── linkedin_agent.py          # Main agent
├── linkedin_auth.py           # Authentication
├── post_to_linkedin.py        # Posting CLI
├── config.json                # Your credentials (gitignored)
├── config.json.template       # Template
├── demo_tip_post.json         # Example posts
├── demo_case_study_post.json
└── demo_insight_post.json
```

---

## 🎓 Common Workflows

### Daily Automation
```python
import schedule
from linkedin_agent import LinkedInAgent

agent = LinkedInAgent()

def daily_post():
    post = agent.generate_post(post_type="tip")
    agent.publish_post(post)

schedule.every().day.at("09:00").do(daily_post)

while True:
    schedule.run_pending()
    time.sleep(60)
```

### Batch Content Creation
```python
from linkedin_agent import LinkedInAgent

agent = LinkedInAgent()

# Generate week's content
for day, post_type in [("Mon", "tip"), ("Wed", "case_study"), ("Fri", "insight")]:
    post = agent.generate_post(post_type=post_type)
    filename = f"scheduled_{day.lower()}_{post_type}.json"
    agent.save_post(post, filename)
    print(f"✅ Created {filename}")
```

### Publish All Drafts
```python
import os
import json
from linkedin_agent import LinkedInAgent

agent = LinkedInAgent()

for filename in os.listdir("."):
    if filename.endswith(".json") and "draft" in filename:
        with open(filename) as f:
            post = json.load(f)
        agent.publish_post(post)
```

---

## 🔐 Security Checklist

- [ ] config.json is in .gitignore
- [ ] Never commit access tokens
- [ ] Rotate tokens every 30 days
- [ ] Use HTTPS for all API calls
- [ ] Monitor API usage

---

## 📚 Documentation

- **SETUP_GUIDE.md** - Detailed setup instructions
- **POSTING_COMPLETE.md** - Feature overview
- **IMPLEMENTATION_SUMMARY.md** - Technical details
- **QUICK_REFERENCE.md** - This document

---

## ✅ Status Check

Run this to verify everything works:
```bash
python3 test_posting.py
```

Expected output:
```
✅ LinkedInAgent imported successfully
✅ Method 'post_to_linkedin' exists and is callable
✅ Method 'publish_post' exists and is callable
✅ All Tests Complete!
```

---

## 🆘 Need Help?

1. Check **SETUP_GUIDE.md** for detailed instructions
2. Run `python3 test_posting.py` to diagnose issues
3. Verify LinkedIn app has `w_member_social` permission
4. Check access token hasn't expired (60 days)

---

**Ready to post? Run:** `python3 post_to_linkedin.py`
