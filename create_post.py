#!/usr/bin/env python3
"""
Simple CLI to create LinkedIn posts using the agent
"""

import sys
from linkedin_agent import LinkedInAgent


def print_menu():
    """Display the menu options"""
    print("\n" + "="*80)
    print("🤖 LinkedIn Post Generator - Quick Create")
    print("="*80)
    print("\nSelect post type:")
    print("1. Tip Post - Best practices and advice")
    print("2. Case Study - Success story with metrics")
    print("3. Insight Post - Industry trends and future")
    print("4. Generate All Three")
    print("5. Exit")
    print("\n" + "="*80)


def main():
    """Main CLI function"""
    agent = LinkedInAgent()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "5":
            print("\n👋 Thanks for using LinkedIn Post Generator!")
            break
        
        if choice == "4":
            print("\n📝 Generating all three post types...\n")
            
            # Generate all posts
            posts = [
                ("tip", "Tip Post"),
                ("case_study", "Case Study"),
                ("insight", "Insight Post")
            ]
            
            for post_type, name in posts:
                post = agent.generate_post(post_type=post_type)
                agent.display_post(post)
                filename = f"linkedin_{post_type}_{post['timestamp'].split('T')[0]}.json"
                filepath = agent.save_post(post, filename)
                print(f"✅ {name} saved to: {filepath}\n")
            
            print("✨ All posts generated successfully!")
            
        elif choice in ["1", "2", "3"]:
            post_types = {
                "1": ("tip", "Tip Post"),
                "2": ("case_study", "Case Study"),
                "3": ("insight", "Insight Post")
            }
            
            post_type, name = post_types[choice]
            
            print(f"\n📝 Generating {name}...\n")
            post = agent.generate_post(post_type=post_type)
            agent.display_post(post)
            
            # Ask if user wants to save
            save = input("\nSave this post? (y/n): ").strip().lower()
            if save == 'y':
                filename = input("Enter filename (press Enter for auto-generated): ").strip()
                if not filename:
                    filename = None
                filepath = agent.save_post(post, filename)
                print(f"\n✅ Post saved to: {filepath}")
            
            # Ask if user wants to continue
            continue_choice = input("\nCreate another post? (y/n): ").strip().lower()
            if continue_choice != 'y':
                print("\n👋 Thanks for using LinkedIn Post Generator!")
                break
        
        else:
            print("\n❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted. Goodbye!")
        sys.exit(0)
