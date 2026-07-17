"""
Main Research Agent - Orchestrates research across 100 apps
Uses Claude + web search to gather auth, API, and buildability info
"""

import json
import os
import time
from typing import Optional
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

def load_app_list(filepath: str = "app_list.json") -> list:
    """Load the list of apps to research"""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["apps"]

def research_app(app: dict, conversation_history: list) -> dict:
    """
    Research a single app using Claude with multi-turn conversation
    Gathers: auth methods, self-serve status, API surface, buildability verdict
    """
    app_name = app["name"]
    website = app["website"]
    
    # Build the research prompt
    research_prompt = f"""
    Research the following app and provide structured findings:
    
    App: {app_name}
    Website: {website}
    
    Please find and provide:
    1. **Description**: What does this app do? (one line)
    2. **Auth Methods**: OAuth2, API Key, Basic Auth, Token, or other?
    3. **Self-Serve vs Gated**: Free/trial access for developers or requires paid plan/partnership?
    4. **API Surface**: REST/GraphQL, breadth (narrow/moderate/broad), any existing MCP?
    5. **Buildability**: Can it be an agent toolkit today? What's the main blocker if not?
    6. **Evidence**: Link to documentation supporting each answer
    
    Format your response as JSON with these exact keys:
    - description
    - auth_methods
    - self_serve_status
    - api_surface
    - buildability_verdict
    - main_blocker
    - docs_url
    - confidence_level (high/medium/low)
    - notes
    
    Be concise but accurate. If uncertain, indicate confidence level as 'low'.
    """
    
    # Add to conversation history
    conversation_history.append({
        "role": "user",
        "content": research_prompt
    })
    
    # Get Claude's response
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1500,
        system="""You are an expert research assistant for Composio, a platform that turns apps into tools for AI agents.
        
Your job is to research SaaS apps and understand:
- Authentication mechanisms
- API accessibility (self-serve vs partner-gated)
- API capabilities for agent integration
- Blockers to building agent toolkits

You have access to general knowledge about popular apps and their APIs. 
When researching, be thorough but honest - if you're unsure, say so and indicate low confidence.
Always cite documentation URLs when available.

Return findings as valid JSON.""",
        messages=conversation_history
    )
    
    assistant_message = response.content[0].text
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    # Parse the JSON response
    try:
        # Extract JSON from the response
        json_start = assistant_message.find('{')
        json_end = assistant_message.rfind('}') + 1
        if json_start != -1 and json_end > json_start:
            json_str = assistant_message[json_start:json_end]
            findings = json.loads(json_str)
        else:
            findings = {
                "description": "Research inconclusive",
                "auth_methods": "Unknown",
                "self_serve_status": "Unknown",
                "api_surface": "Unknown",
                "buildability_verdict": "Unable to determine",
                "main_blocker": "Unable to research",
                "docs_url": website,
                "confidence_level": "low",
                "notes": "Could not parse structured response"
            }
    except json.JSONDecodeError:
        findings = {
            "description": "Research error",
            "auth_methods": "Parse error",
            "self_serve_status": "Parse error",
            "api_surface": "Parse error",
            "buildability_verdict": "Parse error",
            "main_blocker": "Response parsing failed",
            "docs_url": website,
            "confidence_level": "low",
            "notes": f"Raw response: {assistant_message[:200]}"
        }
    
    # Add metadata
    findings["app_id"] = app["id"]
    findings["app_name"] = app_name
    findings["category"] = app["category"]
    findings["website"] = website
    
    return findings

def research_all_apps(app_list: list, output_file: str = "raw_findings.json") -> list:
    """Research all apps and save findings"""
    all_findings = []
    conversation_history = []  # Maintain conversation for context
    
    print(f"Starting research of {len(app_list)} apps...")
    print("=" * 80)
    
    for idx, app in enumerate(app_list, 1):
        print(f"[{idx}/{len(app_list)}] Researching {app['name']}...", end=" ", flush=True)
        
        try:
            findings = research_app(app, conversation_history)
            all_findings.append(findings)
            print("✓")
            
            # Save intermediate results every 10 apps
            if idx % 10 == 0:
                with open(output_file, "w") as f:
                    json.dump(all_findings, f, indent=2)
                print(f"  → Saved {idx} results to {output_file}")
            
            # Rate limiting
            time.sleep(0.5)
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            all_findings.append({
                "app_id": app["id"],
                "app_name": app["name"],
                "category": app["category"],
                "error": str(e),
                "confidence_level": "failed"
            })
    
    # Save final results
    with open(output_file, "w") as f:
        json.dump(all_findings, f, indent=2)
    
    print("=" * 80)
    print(f"Research complete! Findings saved to {output_file}")
    return all_findings

if __name__ == "__main__":
    # Load app list
    apps = load_app_list()
    
    # Research all apps
    findings = research_all_apps(apps)
    
    # Print summary
    print(f"\nResearch Summary:")
    print(f"Total apps researched: {len(findings)}")
    high_confidence = sum(1 for f in findings if f.get('confidence_level') == 'high')
    medium_confidence = sum(1 for f in findings if f.get('confidence_level') == 'medium')
    low_confidence = sum(1 for f in findings if f.get('confidence_level') == 'low')
    failed = sum(1 for f in findings if 'error' in f)
    
    print(f"High confidence: {high_confidence}")
    print(f"Medium confidence: {medium_confidence}")
    print(f"Low confidence: {low_confidence}")
    print(f"Failed: {failed}")
