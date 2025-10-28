#!/usr/bin/env python3
"""
Example: Create a single LinkedIn post
"""

from linkedin_agent import LinkedInAgent


def create_single_post():
    """Create and display a single post example"""
    
    print("\n" + "="*80)
    print("🎯 Creating a Single LinkedIn Post Example")
    print("="*80 + "\n")
    
    # Initialize agent
    agent = LinkedInAgent()
    
    # Create a tip post about Selenium
    print("Generating a post about Selenium WebDriver tips...\n")
    
    post = agent.generate_post(
        post_type="tip",
        topic="Selenium WebDriver Tips"
    )
    
    # Display the post
    agent.display_post(post)
    
    # Save the post
    filename = "selenium_tips_post.json"
    filepath = agent.save_post(post, filename)
    
    print(f"\n✅ Post saved to: {filepath}")
    
    # Show how to use the content
    print("\n" + "="*80)
    print("📋 How to Use This Post:")
    print("="*80)
    print("""
1. Copy the content above
2. Go to LinkedIn.com
3. Click "Start a post"
4. Paste the content
5. Review and adjust if needed
6. Click "Post"

💡 Pro Tips:
- Post during business hours (9 AM - 5 PM) for better engagement
- Respond to comments within the first hour
- Use LinkedIn's native video or document features for variety
- Track which posts get the most engagement
- Follow up with people who comment or DM you
    """)
    
    print("="*80 + "\n")
    
    return post


if __name__ == "__main__":
    create_single_post()
