"""
Pattern Analyzer - Clusters findings and extracts insights
Identifies dominant auth patterns, blockers, easy wins, etc.
"""

import json
from collections import defaultdict, Counter
from typing import Dict, List, Tuple

def load_findings(filepath: str = "raw_findings.json") -> list:
    """Load verified research findings"""
    with open(filepath, "r") as f:
        return json.load(f)

def analyze_auth_patterns(findings: List[Dict]) -> Dict:
    """Analyze dominant auth methods across all apps"""
    auth_counts = Counter()
    auth_by_category = defaultdict(Counter)
    
    for finding in findings:
        if 'error' in finding or 'confidence_level' == 'failed':
            continue
        
        auth = finding.get('auth_methods', 'Unknown')
        category = finding.get('category', 'Unknown')
        
        # Parse multiple auth methods
        if auth and auth != 'Unknown':
            methods = [m.strip() for m in str(auth).split(',')]
            for method in methods:
                auth_counts[method] += 1
                auth_by_category[category][method] += 1
    
    return {
        'overall': dict(auth_counts.most_common()),
        'by_category': {cat: dict(counter.most_common()) for cat, counter in auth_by_category.items()}
    }

def analyze_self_serve_patterns(findings: List[Dict]) -> Dict:
    """Analyze self-serve vs gated access patterns"""
    self_serve_counts = Counter()
    by_category = defaultdict(Counter)
    by_auth = defaultdict(Counter)
    
    for finding in findings:
        if 'error' in finding:
            continue
        
        status = finding.get('self_serve_status', 'Unknown')
        category = finding.get('category', 'Unknown')
        auth = finding.get('auth_methods', 'Unknown')
        
        # Normalize status
        if 'free' in str(status).lower() or 'self-serve' in str(status).lower():
            normalized = 'Self-Serve'
        elif 'paid' in str(status).lower() or 'gated' in str(status).lower() or 'partnership' in str(status).lower():
            normalized = 'Gated'
        else:
            normalized = 'Unknown'
        
        self_serve_counts[normalized] += 1
        by_category[category][normalized] += 1
        
        if auth and auth != 'Unknown':
            methods = [m.strip() for m in str(auth).split(',')]
            for method in methods:
                by_auth[method][normalized] += 1
    
    return {
        'overall': dict(self_serve_counts.most_common()),
        'by_category': {cat: dict(counter.most_common()) for cat, counter in by_category.items()},
        'by_auth': {auth: dict(counter.most_common()) for auth, counter in by_auth.items()}
    }

def analyze_buildability(findings: List[Dict]) -> Dict:
    """Analyze buildability verdicts and blockers"""
    buildability_counts = Counter()
    blocker_counts = Counter()
    by_category = defaultdict(Counter)
    
    for finding in findings:
        if 'error' in finding:
            continue
        
        verdict = finding.get('buildability_verdict', 'Unknown')
        blocker = finding.get('main_blocker', 'None')
        category = finding.get('category', 'Unknown')
        
        # Normalize verdict
        if 'yes' in str(verdict).lower() or 'can' in str(verdict).lower():
            normalized_verdict = 'Buildable Today'
        elif 'no' in str(verdict).lower() or 'cannot' in str(verdict).lower():
            normalized_verdict = 'Not Buildable'
        else:
            normalized_verdict = 'Partial/Unclear'
        
        buildability_counts[normalized_verdict] += 1
        by_category[category][normalized_verdict] += 1
        
        if blocker and blocker != 'None' and 'blocker' not in str(blocker).lower():
            blocker_counts[blocker[:60]] += 1  # Truncate for display
    
    return {
        'overall': dict(buildability_counts.most_common()),
        'by_category': {cat: dict(counter.most_common()) for cat, counter in by_category.items()},
        'top_blockers': dict(blocker_counts.most_common(10))
    }

def analyze_api_surface(findings: List[Dict]) -> Dict:
    """Analyze API types and breadth"""
    api_types = Counter()
    breadth_counts = Counter()
    mcp_available = 0
    
    for finding in findings:
        if 'error' in finding:
            continue
        
        api_surface = finding.get('api_surface', 'Unknown')
        
        if api_surface and api_surface != 'Unknown':
            api_str = str(api_surface).lower()
            
            # Count API types
            if 'rest' in api_str:
                api_types['REST'] += 1
            if 'graphql' in api_str:
                api_types['GraphQL'] += 1
            if 'grpc' in api_str:
                api_types['gRPC'] += 1
            
            # Count breadth
            if 'broad' in api_str:
                breadth_counts['Broad'] += 1
            elif 'moderate' in api_str:
                breadth_counts['Moderate'] += 1
            elif 'narrow' in api_str:
                breadth_counts['Narrow'] += 1
            
            # Check for MCP
            if 'mcp' in api_str:
                mcp_available += 1
    
    return {
        'api_types': dict(api_types.most_common()),
        'breadth': dict(breadth_counts.most_common()),
        'mcp_available': mcp_available
    }

def identify_easy_wins(findings: List[Dict]) -> List[Dict]:
    """Identify apps that are easily buildable with self-serve access"""
    wins = []
    
    for finding in findings:
        if 'error' in finding:
            continue
        
        is_buildable = 'yes' in str(finding.get('buildability_verdict', '')).lower()
        is_self_serve = 'free' in str(finding.get('self_serve_status', '')).lower() or 'self-serve' in str(finding.get('self_serve_status', '')).lower()
        
        if is_buildable and is_self_serve:
            wins.append({
                'app_name': finding.get('app_name'),
                'category': finding.get('category'),
                'auth': finding.get('auth_methods'),
                'why': 'Buildable + Self-Serve'
            })
    
    return wins

def identify_high_blockers(findings: List[Dict]) -> List[Dict]:
    """Identify apps with common blockers that need outreach"""
    blockers = defaultdict(list)
    
    for finding in findings:
        if 'error' in finding:
            continue
        
        blocker = finding.get('main_blocker', '')
        if blocker and 'none' not in str(blocker).lower():
            blockers[blocker[:80]].append(finding.get('app_name'))
    
    # Return top blockers
    return [
        {'blocker': blocker, 'apps': apps, 'count': len(apps)}
        for blocker, apps in sorted(blockers.items(), key=lambda x: len(x[1]), reverse=True)[:10]
    ]

def generate_pattern_report(findings: List[Dict], output_file: str = "pattern_analysis.json") -> Dict:
    """Generate comprehensive pattern analysis report"""
    
    print("\n" + "="*80)
    print("PATTERN ANALYSIS - Processing 100 apps")
    print("="*80)
    
    # Run all analyses
    print("Analyzing auth patterns...", end=" ", flush=True)
    auth_patterns = analyze_auth_patterns(findings)
    print("✓")
    
    print("Analyzing self-serve patterns...", end=" ", flush=True)
    self_serve_patterns = analyze_self_serve_patterns(findings)
    print("✓")
    
    print("Analyzing buildability...", end=" ", flush=True)
    buildability = analyze_buildability(findings)
    print("✓")
    
    print("Analyzing API surfaces...", end=" ", flush=True)
    api_analysis = analyze_api_surface(findings)
    print("✓")
    
    print("Identifying easy wins...", end=" ", flush=True)
    easy_wins = identify_easy_wins(findings)
    print("✓")
    
    print("Identifying blockers...", end=" ", flush=True)
    high_blockers = identify_high_blockers(findings)
    print("✓")
    
    # Compile report
    report = {
        'summary': {
            'total_apps': len(findings),
            'successful_research': len([f for f in findings if 'error' not in f]),
            'easy_wins': len(easy_wins),
            'major_blockers': len(high_blockers)
        },
        'auth_patterns': auth_patterns,
        'self_serve_patterns': self_serve_patterns,
        'buildability': buildability,
        'api_analysis': api_analysis,
        'easy_wins': easy_wins,
        'high_blockers': high_blockers,
        'key_insights': [
            f"OAuth2 dominates ({auth_patterns['overall'].get('OAuth2', 0)} apps)",
            f"Self-serve access: {self_serve_patterns['overall'].get('Self-Serve', 0)} apps",
            f"Buildable today: {buildability['overall'].get('Buildable Today', 0)} apps",
            f"MCP available for {api_analysis['mcp_available']} apps",
            f"{len(easy_wins)} apps are easy wins (buildable + self-serve)"
        ]
    }
    
    # Save report
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "="*80)
    print("PATTERN ANALYSIS COMPLETE")
    print("="*80)
    print("\nKey Findings:")
    for insight in report['key_insights']:
        print(f"  • {insight}")
    
    print(f"\nReport saved to: {output_file}")
    return report

if __name__ == "__main__":
    findings = load_findings()
    report = generate_pattern_report(findings)
