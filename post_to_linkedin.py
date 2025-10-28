#!/usr/bin/env python3
"""
LinkedIn Post Publisher
This script allows you to publish posts to LinkedIn using the agent.
"""

import json
import os
import sys
from linkedin_agent import LinkedInAgent


def load_draft_posts():
    """Load all draft posts from the current directory"""
    drafts = []
    for filename in os.listdir("/vercel/sandbox"):
        if filename.endswith(".json") and "post" in filename.lower():
            filepath = os.path.join("/vercel/sandbox", filename)
            try:
                with open(filepath, 'r') as f:
                    post = json.load(f)
                    if post.get("status") == "draft":
                        drafts.append({
                            "filename": filename,
                            "filepath": filepath,
                            "post": post
                        })
            except:
                pass
    return drafts


def display_menu():
    """Display the main menu"""
    print("\n" + "="*80)
    print("📤 LinkedIn Post Publisher")
    print("="*80)
    print("\nOptions:")
    print("1. Create new post and publish")
    print("2. Publish existing draft post")
    print("3. View draft posts")
    print("4. Exit")
    print("\n" + "="*80)


def create_and_publish(agent: LinkedInAgent):
    """Create a new post and publish it"""
    print("\n" + "="*80)
    print("📝 Create New Post")
    print("="*80)
    
    print("\nSelect post type:")
    print("1. Tip Post - Best practices and advice")
    print("2. Case Study - Success story with metrics")
    print("3. Insight Post - Industry trends and future")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    post_types = {
        "1": "tip",
        "2": "case_study",
        "3": "insight"
    }
    
    post_type = post_types.get(choice)
    if not post_type:
        print("❌ Invalid choice")
        return
    
    print(f"\n📝 Generating {post_type} post...")
    post = agent.generate_post(post_type=post_type)
    
    # Display the post
    agent.display_post(post)
    
    # Ask for confirmation
    confirm = input("\n📤 Do you want to publish this post to LinkedIn? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("\n📤 Publishing to LinkedIn...")
        post = agent.publish_post(post)
        
        if post.get("status") == "published":
            # Save the published post
            filename = f"published_{post_type}_{post['timestamp'].split('T')[0]}.json"
            filepath = agent.save_post(post, filename)
            print(f"\n💾 Published post saved to: {filepath}")
        else:
            print(f"\n❌ Publishing failed: {post.get('error', 'Unknown error')}")
    else:
        # Save as draft
        save = input("\n💾 Save as draft? (y/n): ").strip().lower()
        if save == 'y':
            filename = f"draft_{post_type}_{post['timestamp'].split('T')[0]}.json"
            filepath = agent.save_post(post, filename)
            print(f"\n✅ Draft saved to: {filepath}")


def publish_draft(agent: LinkedInAgent):
    """Publish an existing draft post"""
    drafts = load_draft_posts()
    
    if not drafts:
        print("\n❌ No draft posts found")
        return
    
    print("\n" + "="*80)
    print("📋 Available Draft Posts")
    print("="*80)
    
    for i, draft in enumerate(drafts, 1):
        post = draft["post"]
        print(f"\n{i}. {draft['filename']}")
        print(f"   Type: {post.get('type', 'N/A')}")
        print(f"   Topic: {post.get('topic', 'N/A')}")
        print(f"   Created: {post.get('timestamp', 'N/A')}")
    
    print("\n" + "="*80)
    
    choice = input(f"\nSelect draft to publish (1-{len(drafts)}) or 0 to cancel: ").strip()
    
    try:
        idx = int(choice) - 1
        if idx < 0 or idx >= len(drafts):
            print("❌ Invalid choice")
            return
    except ValueError:
        print("❌ Invalid input")
        return
    
    selected = drafts[idx]
    post = selected["post"]
    
    # Display the post
    agent.display_post(post)
    
    # Ask for confirmation
    confirm = input("\n📤 Do you want to publish this post to LinkedIn? (y/n): ").strip().lower()
    
    if confirm == 'y':
        print("\n📤 Publishing to LinkedIn...")
        post = agent.publish_post(post)
        
        if post.get("status") == "published":
            # Update the file
            with open(selected["filepath"], 'w') as f:
                json.dump(post, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Post status updated in: {selected['filename']}")
        else:
            print(f"\n❌ Publishing failed: {post.get('error', 'Unknown error')}")
    else:
        print("\n❌ Publishing cancelled")


def view_drafts(agent: LinkedInAgent):
    """View all draft posts"""
    drafts = load_draft_posts()
    
    if not drafts:
        print("\n❌ No draft posts found")
        return
    
    print("\n" + "="*80)
    print(f"📋 Found {len(drafts)} Draft Post(s)")
    print("="*80)
    
    for i, draft in enumerate(drafts, 1):
        post = draft["post"]
        print(f"\n{i}. {draft['filename']}")
        agent.display_post(post)


def check_authentication(agent: LinkedInAgent):
    """Check if the user is authenticated"""
    if not agent.config.get("access_token"):
        print("\n" + "="*80)
        print("⚠️  Authentication Required")
        print("="*80)
        print("\nYou need to authenticate with LinkedIn first.")
        print("\nSteps:")
        print("1. Run: python3 linkedin_auth.py")
        print("2. Follow the authentication flow")
        print("3. Come back and run this script again")
        print("\n" + "="*80)
        return False
    return True


def main():
    """Main function"""
    agent = LinkedInAgent()
    
    # Check authentication
    if not check_authentication(agent):
        sys.exit(1)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            create_and_publish(agent)
        elif choice == "2":
            publish_draft(agent)
        elif choice == "3":
            view_drafts(agent)
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Please select 1-4.")
        
        if choice in ["1", "2", "3"]:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
