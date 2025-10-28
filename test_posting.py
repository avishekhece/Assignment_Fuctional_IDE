#!/usr/bin/env python3
"""
Test script to demonstrate LinkedIn posting functionality
This script shows how the posting feature works without actually posting
"""

from linkedin_agent import LinkedInAgent
import json


def test_post_generation():
    """Test post generation"""
    print("\n" + "="*80)
    print("🧪 Testing LinkedIn Agent - Post Generation")
    print("="*80)
    
    agent = LinkedInAgent()
    
    # Test generating different post types
    post_types = ["tip", "case_study", "insight"]
    
    for post_type in post_types:
        print(f"\n📝 Generating {post_type} post...")
        post = agent.generate_post(post_type=post_type)
        
        print(f"✅ Generated {post_type} post")
        print(f"   - Type: {post['type']}")
        print(f"   - Topic: {post['topic']}")
        print(f"   - Status: {post['status']}")
        print(f"   - Content length: {len(post['content'])} characters")
        print(f"   - Preview: {post['content'][:100]}...")


def test_posting_methods():
    """Test that posting methods exist and are callable"""
    print("\n" + "="*80)
    print("🧪 Testing LinkedIn Agent - Posting Methods")
    print("="*80)
    
    agent = LinkedInAgent()
    
    # Check methods exist
    methods_to_check = [
        'post_to_linkedin',
        'publish_post',
        'get_linkedin_person_urn'
    ]
    
    for method_name in methods_to_check:
        if hasattr(agent, method_name) and callable(getattr(agent, method_name)):
            print(f"✅ Method '{method_name}' exists and is callable")
        else:
            print(f"❌ Method '{method_name}' not found")


def test_config_handling():
    """Test configuration handling"""
    print("\n" + "="*80)
    print("🧪 Testing LinkedIn Agent - Configuration")
    print("="*80)
    
    agent = LinkedInAgent()
    
    if agent.config:
        print(f"✅ Config loaded: {len(agent.config)} keys")
        if 'access_token' in agent.config:
            token = agent.config['access_token']
            if token and token != "YOUR_LINKEDIN_ACCESS_TOKEN":
                print(f"✅ Access token configured: {token[:20]}...")
            else:
                print("⚠️  Access token not configured (expected for demo)")
        else:
            print("⚠️  No access token in config (expected for demo)")
    else:
        print("⚠️  No config file found (expected for demo)")


def test_post_to_linkedin_without_token():
    """Test posting without token (should fail gracefully)"""
    print("\n" + "="*80)
    print("🧪 Testing LinkedIn Agent - Posting Without Token")
    print("="*80)
    
    agent = LinkedInAgent()
    
    # Try to post without token
    result = agent.post_to_linkedin("Test post content")
    
    if not result['success']:
        print(f"✅ Correctly handled missing token")
        print(f"   Error message: {result['error']}")
    else:
        print(f"❌ Should have failed without token")


def demonstrate_workflow():
    """Demonstrate the complete workflow"""
    print("\n" + "="*80)
    print("📋 Complete LinkedIn Posting Workflow")
    print("="*80)
    
    print("\n1️⃣ SETUP (One-time)")
    print("   - Create LinkedIn Developer App")
    print("   - Get Client ID & Secret")
    print("   - Run: python3 linkedin_auth.py")
    print("   - Get Access Token")
    
    print("\n2️⃣ GENERATE CONTENT")
    print("   - agent = LinkedInAgent()")
    print("   - post = agent.generate_post(post_type='tip')")
    
    print("\n3️⃣ PUBLISH TO LINKEDIN")
    print("   - agent.publish_post(post)")
    print("   - Post appears on LinkedIn profile")
    print("   - Status updated to 'published'")
    
    print("\n4️⃣ TRACK & ENGAGE")
    print("   - Monitor post performance")
    print("   - Respond to comments")
    print("   - Generate more content!")


def main():
    """Run all tests"""
    print("\n" + "="*80)
    print("🚀 LinkedIn Agent - Posting Feature Test Suite")
    print("="*80)
    
    test_post_generation()
    test_posting_methods()
    test_config_handling()
    test_post_to_linkedin_without_token()
    demonstrate_workflow()
    
    print("\n" + "="*80)
    print("✅ All Tests Complete!")
    print("="*80)
    print("\n📚 Next Steps:")
    print("   1. Read SETUP_GUIDE.md for LinkedIn API setup")
    print("   2. Run: python3 linkedin_auth.py to authenticate")
    print("   3. Run: python3 post_to_linkedin.py to start posting")
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
