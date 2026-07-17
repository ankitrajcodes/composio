"""
Verification Agent - Spot-checks research findings and tracks accuracy
Performs human-in-the-loop verification on a sample of apps
"""

import json
import csv
from typing import Dict, List, Tuple
from anthropic import Anthropic

client = Anthropic()

def load_findings(filepath: str = "raw_findings.json") -> list:
    """Load raw research findings"""
    with open(filepath, "r") as f:
        return json.load(f)

def manual_verification_prompt(app: Dict) -> Dict:
    """
    Present a verification prompt for human review
    Returns human feedback on accuracy
    """
    print("\n" + "="*80)
    print(f"VERIFICATION CHECK: {app['app_name']} (ID: {app['app_id']})")
    print("="*80)
    print(f"Category: {app['category']}")
    print(f"Website: {app['website']}")
    print(f"\nAgent Findings:")
    print(f"  Description: {app.get('description', 'N/A')}")
    print(f"  Auth Methods: {app.get('auth_methods', 'N/A')}")
    print(f"  Self-Serve: {app.get('self_serve_status', 'N/A')}")
    print(f"  API Surface: {app.get('api_surface', 'N/A')}")
    print(f"  Buildability: {app.get('buildability_verdict', 'N/A')}")
    print(f"  Main Blocker: {app.get('main_blocker', 'N/A')}")
    print(f"  Confidence: {app.get('confidence_level', 'N/A')}")
    print(f"  Docs URL: {app.get('docs_url', 'N/A')}")
    
    print("\nVERIFICATION:")
    accuracy = input("Is the research accurate? (1=incorrect, 2=partially correct, 3=correct): ").strip()
    corrections = input("Any corrections needed? (press Enter to skip): ").strip()
    
    return {
        "app_id": app["app_id"],
        "app_name": app["app_name"],
        "accuracy": int(accuracy) if accuracy in ["1", "2", "3"] else 2,
        "corrections": corrections,
        "verified": True
    }

def verify_sample(findings: List[Dict], sample_size: int = 20) -> Tuple[List[Dict], float]:
    """
    Verify a sample of findings through human review
    Returns verified results and accuracy percentage
    """
    print(f"\n{'='*80}")
    print(f"VERIFICATION LOOP: Spot-checking {sample_size} apps (20% sample)")
    print(f"{'='*80}")
    
    # Select sample (spread across categories)
    sample_indices = []
    categories = {}
    
    for idx, finding in enumerate(findings):
        cat = finding.get('category', 'Unknown')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(idx)
    
    # Sample proportionally from each category
    for cat, indices in categories.items():
        sample_count = max(1, int(len(indices) * sample_size / len(findings)))
        sample_indices.extend(indices[:sample_count])
    
    sample_indices = sample_indices[:sample_size]
    
    verification_results = []
    correct_count = 0
    
    for idx, sample_idx in enumerate(sample_indices, 1):
        finding = findings[sample_idx]
        
        print(f"\n[{idx}/{len(sample_indices)}]", end=" ")
        
        try:
            result = manual_verification_prompt(finding)
            verification_results.append(result)
            
            if result["accuracy"] == 3:
                correct_count += 1
            
            # Save corrections if provided
            if result["corrections"]:
                finding["human_correction"] = result["corrections"]
                finding["accuracy_feedback"] = result["accuracy"]
        
        except ValueError:
            print("Invalid input, skipping...")
            continue
    
    accuracy_percentage = (correct_count / len(verification_results) * 100) if verification_results else 0
    
    return verification_results, accuracy_percentage

def ai_verify_findings(findings: List[Dict]) -> List[Dict]:
    """
    Use Claude to verify findings against known facts about popular apps
    This is a secondary verification layer
    """
    print("\n" + "="*80)
    print("RUNNING AI VERIFICATION LAYER")
    print("="*80)
    
    verification_log = []
    
    for finding in findings[:20]:  # Verify first 20 as sample
        app_name = finding.get('app_name', 'Unknown')
        
        prompt = f"""
        I researched the following app and got these findings. 
        Please verify if they seem accurate based on your knowledge:
        
        App: {app_name}
        - Auth Methods: {finding.get('auth_methods', 'Unknown')}
        - Self-Serve: {finding.get('self_serve_status', 'Unknown')}
        - API Surface: {finding.get('api_surface', 'Unknown')}
        
        Are these findings likely correct? If not, what's incorrect?
        Reply with: CORRECT / PARTIALLY_CORRECT / INCORRECT and brief explanation.
        """
        
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        
        verdict = response.content[0].text
        
        verification_log.append({
            "app_name": app_name,
            "ai_verdict": verdict,
            "original_findings": {
                "auth": finding.get('auth_methods'),
                "self_serve": finding.get('self_serve_status'),
                "api": finding.get('api_surface')
            }
        })
    
    return verification_log

def generate_verification_report(verification_results: List[Dict], accuracy_pct: float, 
                                  ai_verification: List[Dict], output_file: str = "verification_report.csv"):
    """
    Generate CSV verification report
    """
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['App Name', 'Accuracy (1-3)', 'Corrections', 'Status'])
        
        for result in verification_results:
            writer.writerow([
                result['app_name'],
                result['accuracy'],
                result['corrections'] if result['corrections'] else 'None',
                'Verified'
            ])
    
    print(f"\nVerification Report Summary:")
    print(f"  Accuracy: {accuracy_pct:.1f}%")
    print(f"  Verified: {len(verification_results)} apps")
    print(f"  Report saved to: {output_file}")

def run_verification(findings_file: str = "raw_findings.json"):
    """
    Main verification workflow
    """
    print("Loading raw findings...")
    findings = load_findings(findings_file)
    
    print(f"Loaded {len(findings)} findings")
    
    # Run AI verification layer
    print("\nRunning AI verification on sample...")
    ai_verification = ai_verify_findings(findings)
    
    # Optional: Run manual verification (comment out for automated testing)
    print("\nWould you like to perform manual spot-checks? (y/n): ", end="")
    manual_check = input().strip().lower() == 'y'
    
    if manual_check:
        verification_results, accuracy_pct = verify_sample(findings, sample_size=20)
        generate_verification_report(verification_results, accuracy_pct, ai_verification)
    else:
        print("Skipping manual verification")
        # Save AI verification results
        with open("ai_verification_log.json", "w") as f:
            json.dump(ai_verification, f, indent=2)
        print("AI verification saved to ai_verification_log.json")
    
    return findings

if __name__ == "__main__":
    run_verification()
