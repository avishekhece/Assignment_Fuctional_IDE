"""
LinkedIn Automation Agent for Posting about Automation Testing
This agent generates and can post content about automation testing to attract clients.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode


class LinkedInAgent:
    """AI Agent for creating LinkedIn posts about automation testing"""
    
    def __init__(self, config_path: str = "/vercel/sandbox/config.json"):
        self.post_templates = self._load_templates()
        self.config_path = config_path
        self.config = self._load_config()
        self.topics = [
            "Test Automation Best Practices",
            "Selenium WebDriver Tips",
            "CI/CD Integration",
            "API Testing Strategies",
            "Performance Testing",
            "Mobile Test Automation",
            "Test Framework Design",
            "Quality Assurance Metrics"
        ]
    
    def _load_config(self) -> Dict:
        """Load configuration from config file"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Warning: Could not load config: {e}")
                return {}
        return {}
    
    def _load_templates(self) -> List[Dict]:
        """Load post templates for different types of content"""
        return [
            {
                "type": "tip",
                "structure": "🎯 {hook}\n\n{main_content}\n\n{call_to_action}\n\n{hashtags}"
            },
            {
                "type": "case_study",
                "structure": "📊 {hook}\n\n{problem}\n\n{solution}\n\n{results}\n\n{call_to_action}\n\n{hashtags}"
            },
            {
                "type": "insight",
                "structure": "💡 {hook}\n\n{insight_points}\n\n{conclusion}\n\n{call_to_action}\n\n{hashtags}"
            }
        ]
    
    def generate_post(self, post_type: str = "tip", topic: str = None) -> Dict:
        """Generate a LinkedIn post based on type and topic"""
        
        if topic is None:
            topic = "Test Automation Best Practices"
        
        posts = {
            "tip": self._generate_tip_post(topic),
            "case_study": self._generate_case_study_post(topic),
            "insight": self._generate_insight_post(topic)
        }
        
        post_content = posts.get(post_type, posts["tip"])
        
        return {
            "content": post_content,
            "type": post_type,
            "topic": topic,
            "timestamp": datetime.now().isoformat(),
            "status": "draft"
        }
    
    def _generate_tip_post(self, topic: str) -> str:
        """Generate a tip-style post"""
        
        tips_content = {
            "Test Automation Best Practices": {
                "hook": "5 Test Automation Mistakes That Are Costing You Time & Money",
                "main_content": """Here's what I've learned after 10+ years in QA automation:

1️⃣ Writing tests without a clear strategy
→ Start with a test automation pyramid approach

2️⃣ Testing everything through the UI
→ Use API tests for business logic validation

3️⃣ Ignoring test maintenance
→ Implement Page Object Model for better maintainability

4️⃣ Not running tests in parallel
→ Reduce execution time by 70% with parallel execution

5️⃣ Skipping test data management
→ Use data-driven testing for better coverage

The right automation strategy can reduce testing time by 60% and catch 90% of bugs before production.""",
                "call_to_action": "What's your biggest automation challenge? Let's discuss in the comments! 👇\n\nNeed help setting up your test automation framework? DM me for a free consultation.",
                "hashtags": "#TestAutomation #QualityAssurance #SoftwareTesting #QA #AutomationTesting #Selenium #CICD #DevOps"
            },
            "Selenium WebDriver Tips": {
                "hook": "Selenium WebDriver: 3 Advanced Techniques That Will Transform Your Tests",
                "main_content": """Stop writing flaky Selenium tests! Here's how:

1️⃣ Smart Waits Over Thread.Sleep()
→ Use Explicit Waits with Expected Conditions
→ Implement custom wait conditions for complex scenarios

2️⃣ Robust Element Location
→ Avoid XPath when possible
→ Use CSS selectors or data-testid attributes
→ Implement retry mechanisms for stale elements

3️⃣ Screenshot on Failure
→ Capture evidence automatically
→ Attach to test reports
→ Store in cloud storage for team access

These techniques reduced our test flakiness from 30% to less than 5%.""",
                "call_to_action": "Want to learn more advanced Selenium techniques? Follow me for weekly testing tips!\n\nLooking to improve your test automation? Let's connect!",
                "hashtags": "#Selenium #WebDriver #TestAutomation #QA #AutomationTesting #SoftwareTesting #QualityAssurance"
            }
        }
        
        content = tips_content.get(topic, tips_content["Test Automation Best Practices"])
        
        template = self.post_templates[0]["structure"]
        return template.format(**content)
    
    def _generate_case_study_post(self, topic: str) -> str:
        """Generate a case study style post"""
        
        content = {
            "hook": "How We Reduced Testing Time by 75% in 3 Months",
            "problem": """The Challenge:
• Manual testing taking 2 weeks per release
• 40% of bugs found in production
• Team working overtime before every release
• Customer satisfaction dropping""",
            "solution": """Our Approach:
✅ Implemented comprehensive test automation framework
✅ Set up CI/CD pipeline with automated testing
✅ Trained team on automation best practices
✅ Established test data management strategy
✅ Integrated API and UI testing""",
            "results": """The Results:
📈 Testing time: 2 weeks → 3 days
📈 Bug detection: 60% → 95% before production
📈 Team overtime: Reduced by 80%
📈 Customer satisfaction: Increased by 45%
📈 Release frequency: Monthly → Weekly""",
            "call_to_action": "Struggling with slow testing cycles? Let's talk about how automation can transform your QA process.\n\nDM me for a free assessment of your testing strategy.",
            "hashtags": "#TestAutomation #CaseStudy #QA #SoftwareTesting #AutomationTesting #CICD #DevOps #QualityAssurance"
        }
        
        template = self.post_templates[1]["structure"]
        return template.format(**content)
    
    def _generate_insight_post(self, topic: str) -> str:
        """Generate an insight-style post"""
        
        content = {
            "hook": "The Future of Test Automation: What's Coming in 2025",
            "insight_points": """Based on industry trends and my experience:

🤖 AI-Powered Test Generation
→ Self-healing tests that adapt to UI changes
→ Intelligent test case generation from requirements
→ Predictive analytics for test prioritization

☁️ Cloud-Based Testing Platforms
→ Scalable test execution infrastructure
→ Cross-browser testing made simple
→ Real device testing without hardware

🔄 Shift-Left Testing
→ Testing earlier in development cycle
→ Developer-driven test automation
→ Continuous testing in CI/CD pipelines

📊 Advanced Analytics
→ AI-powered test result analysis
→ Predictive defect detection
→ Real-time quality dashboards""",
            "conclusion": """The companies investing in modern test automation now will have a significant competitive advantage.

Don't wait until you're behind.""",
            "call_to_action": "What automation trends are you most excited about?\n\nReady to modernize your testing approach? Let's connect and discuss your needs.",
            "hashtags": "#TestAutomation #AI #FutureOfTesting #QA #SoftwareTesting #AutomationTesting #Innovation #TechTrends"
        }
        
        template = self.post_templates[2]["structure"]
        return template.format(**content)
    
    def save_post(self, post: Dict, filename: str = None) -> str:
        """Save post to a JSON file"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"linkedin_post_{timestamp}.json"
        
        filepath = os.path.join("/vercel/sandbox", filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(post, f, indent=2, ensure_ascii=False)
        
        return filepath
    
    def get_linkedin_person_urn(self, access_token: str) -> Optional[str]:
        """Get the LinkedIn person URN for the authenticated user"""
        url = "https://api.linkedin.com/v2/userinfo"
        
        try:
            req = Request(url)
            req.add_header("Authorization", f"Bearer {access_token}")
            req.add_header("Content-Type", "application/json")
            
            with urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data.get("sub")  # This is the person URN
        except Exception as e:
            print(f"Error getting person URN: {e}")
            return None
    
    def post_to_linkedin(self, post_content: str, access_token: str = None) -> Dict:
        """
        Post content to LinkedIn using the API
        
        Args:
            post_content: The text content to post
            access_token: LinkedIn access token (if not provided, uses config)
        
        Returns:
            Dict with status and response data
        """
        if access_token is None:
            access_token = self.config.get("access_token")
        
        if not access_token:
            return {
                "success": False,
                "error": "No access token provided. Please authenticate first."
            }
        
        # Get person URN
        person_urn = self.get_linkedin_person_urn(access_token)
        if not person_urn:
            return {
                "success": False,
                "error": "Could not retrieve LinkedIn person URN"
            }
        
        # LinkedIn UGC Post API endpoint
        url = "https://api.linkedin.com/v2/ugcPosts"
        
        payload = {
            "author": f"urn:li:person:{person_urn}",
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": post_content
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }
        
        try:
            data = json.dumps(payload).encode('utf-8')
            req = Request(url, data=data, method='POST')
            req.add_header("Authorization", f"Bearer {access_token}")
            req.add_header("Content-Type", "application/json")
            req.add_header("X-Restli-Protocol-Version", "2.0.0")
            
            with urlopen(req) as response:
                response_data = json.loads(response.read().decode())
                return {
                    "success": True,
                    "post_id": response_data.get("id"),
                    "message": "Post published successfully to LinkedIn!",
                    "response": response_data
                }
        
        except HTTPError as e:
            error_msg = f"HTTP Error: {e.code}"
            try:
                error_detail = json.loads(e.read().decode())
                error_msg += f" - {error_detail}"
            except:
                error_msg += f" - {e.reason}"
            
            return {
                "success": False,
                "error": error_msg
            }
        
        except Exception as e:
            return {
                "success": False,
                "error": f"Error posting to LinkedIn: {str(e)}"
            }
    
    def publish_post(self, post: Dict, access_token: str = None) -> Dict:
        """
        Publish a post to LinkedIn and update its status
        
        Args:
            post: Post dictionary with content
            access_token: LinkedIn access token
        
        Returns:
            Updated post dictionary with publish status
        """
        result = self.post_to_linkedin(post["content"], access_token)
        
        if result["success"]:
            post["status"] = "published"
            post["published_at"] = datetime.now().isoformat()
            post["linkedin_post_id"] = result.get("post_id")
            print(f"\n✅ {result['message']}")
        else:
            post["status"] = "failed"
            post["error"] = result["error"]
            print(f"\n❌ Failed to publish: {result['error']}")
        
        return post
    
    def display_post(self, post: Dict) -> None:
        """Display the post in a formatted way"""
        print("\n" + "="*80)
        print(f"LinkedIn Post - {post['type'].upper()}")
        print(f"Topic: {post['topic']}")
        print(f"Generated: {post['timestamp']}")
        print("="*80)
        print("\n" + post['content'])
        print("\n" + "="*80)
        print(f"Status: {post['status']}")
        print("="*80 + "\n")


def main():
    """Main function to demonstrate the LinkedIn agent"""
    
    print("🤖 LinkedIn Automation Agent - Demo")
    print("="*80)
    
    # Initialize the agent
    agent = LinkedInAgent()
    
    # Generate different types of posts
    print("\n📝 Generating demo posts...\n")
    
    # 1. Tip Post
    tip_post = agent.generate_post(post_type="tip", topic="Test Automation Best Practices")
    agent.display_post(tip_post)
    tip_file = agent.save_post(tip_post, "demo_tip_post.json")
    print(f"✅ Tip post saved to: {tip_file}")
    
    # 2. Case Study Post
    case_study_post = agent.generate_post(post_type="case_study")
    agent.display_post(case_study_post)
    case_study_file = agent.save_post(case_study_post, "demo_case_study_post.json")
    print(f"✅ Case study post saved to: {case_study_file}")
    
    # 3. Insight Post
    insight_post = agent.generate_post(post_type="insight")
    agent.display_post(insight_post)
    insight_file = agent.save_post(insight_post, "demo_insight_post.json")
    print(f"✅ Insight post saved to: {insight_file}")
    
    print("\n" + "="*80)
    print("✨ Demo completed! All posts have been generated and saved.")
    print("="*80)
    
    return {
        "tip_post": tip_post,
        "case_study_post": case_study_post,
        "insight_post": insight_post
    }


if __name__ == "__main__":
    main()
