"""
Main Orchestration Script - Runs the complete research workflow
Coordinates: researcher → verifier → pattern_analyzer → html_generator
"""

import subprocess
import sys
import json
from pathlib import Path

def run_step(step_name: str, script_path: str) -> bool:
    """Run a single step and return success status"""
    print(f"\n{'='*80}")
    print(f"STEP: {step_name}")
    print(f"{'='*80}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            check=True,
            capture_output=False
        )
        print(f"✅ {step_name} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {step_name} failed with error: {e}")
        return False
    except Exception as e:
        print(f"❌ {step_name} encountered an error: {e}")
        return False

def verify_output_files(required_files: list) -> bool:
    """Verify that required output files exist"""
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n⚠️  Missing files: {missing_files}")
        return False
    
    print(f"\n✅ All output files verified:")
    for file_path in required_files:
        size = Path(file_path).stat().st_size
        print(f"   • {file_path} ({size} bytes)")
    
    return True

def print_workflow_summary():
    """Print the complete workflow"""
    print(f"""
{'='*80}
COMPOSIO RESEARCH AGENT - COMPLETE WORKFLOW
{'='*80}

This orchestration script runs a 4-step research pipeline:

1️⃣  RESEARCHER (researcher.py)
   └─ Gathers raw data on 100 SaaS apps
   └─ Uses Claude AI to research each app
   └─ Outputs: raw_findings.json

2️⃣  VERIFIER (verifier.py)
   └─ Spot-checks findings for accuracy
   └─ AI verification layer + optional manual review
   └─ Outputs: verification_report.csv, ai_verification_log.json

3️⃣  PATTERN ANALYZER (pattern_analyzer.py)
   └─ Clusters findings and extracts insights
   └─ Identifies patterns, blockers, easy wins
   └─ Outputs: pattern_analysis.json

4️⃣  HTML GENERATOR (html_generator.py)
   └─ Creates interactive dashboard
   └─ Beautiful case study report with all findings
   └─ Outputs: findings_report.html

Final Output: findings_report.html (open in browser for full report)
{'='*80}
    """)

def main():
    """Main orchestration function"""
    
    print_workflow_summary()
    
    # Define workflow steps
    steps = [
        ("RESEARCH PHASE", "researcher.py"),
        ("VERIFICATION PHASE", "verifier.py"),
        ("PATTERN ANALYSIS PHASE", "pattern_analyzer.py"),
        ("REPORT GENERATION PHASE", "html_generator.py")
    ]
    
    completed_steps = []
    
    for step_name, script_path in steps:
        if not run_step(step_name, script_path):
            print(f"\n❌ Workflow halted at {step_name}")
            print(f"\nCompleted steps: {len(completed_steps)}/{len(steps)}")
            return False
        completed_steps.append(step_name)
    
    # Verify all outputs exist
    required_files = [
        "raw_findings.json",
        "pattern_analysis.json",
        "findings_report.html"
    ]
    
    if not verify_output_files(required_files):
        print("\n⚠️  Some output files are missing")
    
    # Print final summary
    print(f"\n{'='*80}")
    print("🎉 WORKFLOW COMPLETE!")
    print(f"{'='*80}")
    print(f"\n✅ All {len(completed_steps)} phases completed successfully")
    print(f"\n📊 Final Report: findings_report.html")
    print(f"   Open in browser: file://$(pwd)/findings_report.html")
    print(f"\n📁 Output Files:")
    print(f"   • raw_findings.json - Raw research data (100 apps)")
    print(f"   • pattern_analysis.json - Pattern insights and blockers")
    print(f"   • findings_report.html - Interactive dashboard")
    print(f"   • verification_report.csv - Verification results")
    print(f"   • ai_verification_log.json - AI verification logs")
    print(f"\n{'='*80}")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
