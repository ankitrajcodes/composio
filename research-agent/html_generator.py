"""
HTML Case Study Generator - Creates interactive dashboard and detailed report
Generates findings_report.html with all 100 apps, patterns, and insights
"""

import json
from typing import Dict, List

def load_findings(filepath: str = "raw_findings.json") -> list:
    """Load research findings"""
    with open(filepath, "r") as f:
        return json.load(f)

def load_patterns(filepath: str = "pattern_analysis.json") -> dict:
    """Load pattern analysis"""
    with open(filepath, "r") as f:
        return json.load(f)

def generate_app_card_html(app: Dict) -> str:
    """Generate HTML card for a single app"""
    
    # Determine color coding based on buildability
    verdict = app.get('buildability_verdict', 'Unknown')
    if 'yes' in str(verdict).lower() or 'can' in str(verdict).lower():
        verdict_class = 'buildable'
        verdict_text = '✓ Buildable'
    elif 'no' in str(verdict).lower() or 'cannot' in str(verdict).lower():
        verdict_class = 'not-buildable'
        verdict_text = '✗ Not Buildable'
    else:
        verdict_class = 'partial'
        verdict_text = '⚠ Partial'
    
    # Self-serve status
    self_serve = app.get('self_serve_status', 'Unknown')
    if 'free' in str(self_serve).lower() or 'self' in str(self_serve).lower():
        self_serve_text = '🟢 Self-Serve'
    elif 'paid' in str(self_serve).lower() or 'gated' in str(self_serve).lower():
        self_serve_text = '🔴 Gated'
    else:
        self_serve_text = '⚫ Unknown'
    
    # Confidence level styling
    confidence = app.get('confidence_level', 'low')
    confidence_class = f'confidence-{confidence}'
    
    html = f"""
    <div class="app-card {verdict_class}">
        <div class="app-header">
            <h3>{app.get('app_name', 'Unknown')}</h3>
            <span class="confidence {confidence_class}">{confidence.upper()}</span>
        </div>
        
        <div class="app-category">{app.get('category', 'Unknown')}</div>
        
        <div class="app-description">
            {app.get('description', 'No description available')}
        </div>
        
        <div class="app-metrics">
            <div class="metric">
                <span class="label">Auth:</span>
                <span class="value">{app.get('auth_methods', 'Unknown')}</span>
            </div>
            <div class="metric">
                <span class="label">API:</span>
                <span class="value">{app.get('api_surface', 'Unknown')}</span>
            </div>
        </div>
        
        <div class="app-status">
            <span class="status-badge {verdict_class}">{verdict_text}</span>
            <span class="status-badge self-serve">{self_serve_text}</span>
        </div>
        
        <div class="app-blocker">
            <strong>Blocker:</strong> {app.get('main_blocker', 'None')}
        </div>
        
        <div class="app-links">
            <a href="{app.get('docs_url', app.get('website', '#'))}" target="_blank">
                📖 Docs
            </a>
            <a href="{app.get('website', '#')}" target="_blank">
                🌐 Website
            </a>
        </div>
    </div>
    """
    
    return html

def generate_patterns_section(patterns: Dict) -> str:
    """Generate HTML for pattern analysis section"""
    
    summary = patterns.get('summary', {})
    auth_patterns = patterns.get('auth_patterns', {})
    self_serve = patterns.get('self_serve_patterns', {})
    buildability = patterns.get('buildability', {})
    api_analysis = patterns.get('api_analysis', {})
    easy_wins = patterns.get('easy_wins', [])
    blockers = patterns.get('high_blockers', [])
    
    # Build auth table
    auth_rows = ""
    for auth_type, count in list(auth_patterns.get('overall', {}).items())[:10]:
        auth_rows += f"<tr><td>{auth_type}</td><td>{count}</td></tr>"
    
    # Build blocker table
    blocker_rows = ""
    for blocker in blockers[:8]:
        blocker_rows += f"""
        <tr>
            <td>{blocker['blocker']}</td>
            <td>{blocker['count']}</td>
            <td>{', '.join(blocker['apps'][:3])}</td>
        </tr>
        """
    
    # Easy wins list
    wins_html = ""
    for win in easy_wins[:15]:
        wins_html += f"""
        <div class="easy-win">
            <strong>{win['app_name']}</strong>
            <span class="category">{win['category']}</span>
            <span class="auth">{win['auth']}</span>
        </div>
        """
    
    html = f"""
    <section class="patterns-section">
        <h2>📊 Pattern Analysis</h2>
        
        <div class="summary-stats">
            <div class="stat-box">
                <div class="stat-number">{summary.get('total_apps', 0)}</div>
                <div class="stat-label">Total Apps</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">{summary.get('successful_research', 0)}</div>
                <div class="stat-label">Researched</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">{summary.get('easy_wins', 0)}</div>
                <div class="stat-label">Easy Wins</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">{api_analysis.get('mcp_available', 0)}</div>
                <div class="stat-label">MCP Available</div>
            </div>
        </div>
        
        <div class="insights-grid">
            <div class="insight-card">
                <h3>🔐 Auth Patterns</h3>
                <table class="data-table">
                    <thead>
                        <tr><th>Auth Type</th><th>Count</th></tr>
                    </thead>
                    <tbody>
                        {auth_rows}
                    </tbody>
                </table>
            </div>
            
            <div class="insight-card">
                <h3>🏗️ Buildability</h3>
                <ul>
                    <li>Buildable Today: {buildability.get('overall', {}).get('Buildable Today', 0)}</li>
                    <li>Not Buildable: {buildability.get('overall', {}).get('Not Buildable', 0)}</li>
                    <li>Partial/Unclear: {buildability.get('overall', {}).get('Partial/Unclear', 0)}</li>
                </ul>
            </div>
            
            <div class="insight-card">
                <h3>🎯 Self-Serve Access</h3>
                <ul>
                    <li>Self-Serve: {self_serve.get('overall', {}).get('Self-Serve', 0)}</li>
                    <li>Gated: {self_serve.get('overall', {}).get('Gated', 0)}</li>
                    <li>Unknown: {self_serve.get('overall', {}).get('Unknown', 0)}</li>
                </ul>
            </div>
            
            <div class="insight-card">
                <h3>🔌 API Types</h3>
                <ul>
                    <li>REST: {api_analysis.get('api_types', {}).get('REST', 0)}</li>
                    <li>GraphQL: {api_analysis.get('api_types', {}).get('GraphQL', 0)}</li>
                    <li>gRPC: {api_analysis.get('api_types', {}).get('gRPC', 0)}</li>
                </ul>
            </div>
        </div>
        
        <div class="easy-wins-section">
            <h3>⭐ Easy Wins (Buildable + Self-Serve)</h3>
            <div class="easy-wins-list">
                {wins_html}
            </div>
        </div>
        
        <div class="blockers-section">
            <h3>⚠️ Top Blockers (for Partnerships)</h3>
            <table class="data-table">
                <thead>
                    <tr><th>Blocker</th><th>Count</th><th>Sample Apps</th></tr>
                </thead>
                <tbody>
                    {blocker_rows}
                </tbody>
            </table>
        </div>
        
        <div class="key-insights">
            <h3>🎓 Key Insights</h3>
            <ul>
    """
    
    for insight in patterns.get('key_insights', []):
        html += f"<li>{insight}</li>\n"
    
    html += """
            </ul>
        </div>
    </section>
    """
    
    return html

def generate_full_html(findings: List[Dict], patterns: Dict) -> str:
    """Generate complete HTML report"""
    
    # Generate app cards
    app_cards = ""
    for app in findings:
        if 'error' not in app:
            app_cards += generate_app_card_html(app)
    
    # Generate patterns section
    patterns_section = generate_patterns_section(patterns)
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Composio Research: 100 SaaS Apps Analysis</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: #333;
                line-height: 1.6;
            }}
            
            .header {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 3rem 2rem;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            }}
            
            .header h1 {{
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
            }}
            
            .header p {{
                font-size: 1.1rem;
                opacity: 0.9;
            }}
            
            .container {{
                max-width: 1400px;
                margin: 2rem auto;
                padding: 0 1rem;
            }}
            
            .patterns-section {{
                background: white;
                padding: 2rem;
                border-radius: 8px;
                margin-bottom: 3rem;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            
            .patterns-section h2 {{
                font-size: 2rem;
                margin-bottom: 2rem;
                color: #667eea;
            }}
            
            .patterns-section h3 {{
                font-size: 1.3rem;
                margin: 1.5rem 0 1rem 0;
                color: #764ba2;
            }}
            
            .summary-stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 1.5rem;
                margin-bottom: 2rem;
            }}
            
            .stat-box {{
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 2rem;
                border-radius: 8px;
                text-align: center;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            
            .stat-number {{
                font-size: 2.5rem;
                font-weight: bold;
                margin-bottom: 0.5rem;
            }}
            
            .stat-label {{
                font-size: 0.9rem;
                opacity: 0.9;
            }}
            
            .insights-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 2rem;
                margin-bottom: 2rem;
            }}
            
            .insight-card {{
                background: #f8f9fa;
                padding: 1.5rem;
                border-radius: 8px;
                border-left: 4px solid #667eea;
            }}
            
            .insight-card ul {{
                list-style: none;
                padding: 0;
            }}
            
            .insight-card li {{
                padding: 0.5rem 0;
                display: flex;
                justify-content: space-between;
            }}
            
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 1rem;
            }}
            
            .data-table th {{
                background: #667eea;
                color: white;
                padding: 0.75rem;
                text-align: left;
            }}
            
            .data-table td {{
                padding: 0.75rem;
                border-bottom: 1px solid #eee;
            }}
            
            .data-table tr:hover {{
                background: #f5f5f5;
            }}
            
            .easy-wins-section, .blockers-section {{
                margin-top: 2rem;
                padding-top: 2rem;
                border-top: 2px solid #eee;
            }}
            
            .easy-wins-list {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
                gap: 1rem;
                margin-top: 1rem;
            }}
            
            .easy-win {{
                background: #e8f5e9;
                padding: 1rem;
                border-radius: 6px;
                border-left: 4px solid #4caf50;
            }}
            
            .easy-win strong {{
                display: block;
                margin-bottom: 0.5rem;
                color: #2e7d32;
            }}
            
            .category, .auth {{
                display: inline-block;
                background: rgba(0, 0, 0, 0.1);
                padding: 0.25rem 0.5rem;
                border-radius: 3px;
                font-size: 0.85rem;
                margin-right: 0.5rem;
            }}
            
            .apps-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
                gap: 1.5rem;
                margin-top: 2rem;
            }}
            
            .app-card {{
                background: white;
                border-radius: 8px;
                padding: 1.5rem;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                transition: all 0.3s ease;
                border-top: 4px solid #ddd;
            }}
            
            .app-card:hover {{
                transform: translateY(-4px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }}
            
            .app-card.buildable {{
                border-top-color: #4caf50;
            }}
            
            .app-card.not-buildable {{
                border-top-color: #f44336;
            }}
            
            .app-card.partial {{
                border-top-color: #ff9800;
            }}
            
            .app-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            
            .app-header h3 {{
                margin: 0;
                color: #333;
                font-size: 1.3rem;
            }}
            
            .confidence {{
                font-size: 0.75rem;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-weight: bold;
            }}
            
            .confidence-high {{
                background: #4caf50;
                color: white;
            }}
            
            .confidence-medium {{
                background: #ff9800;
                color: white;
            }}
            
            .confidence-low {{
                background: #f44336;
                color: white;
            }}
            
            .app-category {{
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.85rem;
                margin-bottom: 1rem;
            }}
            
            .app-description {{
                color: #666;
                margin-bottom: 1rem;
                font-size: 0.95rem;
            }}
            
            .app-metrics {{
                background: #f5f5f5;
                padding: 1rem;
                border-radius: 6px;
                margin-bottom: 1rem;
            }}
            
            .metric {{
                display: flex;
                justify-content: space-between;
                margin-bottom: 0.5rem;
                font-size: 0.9rem;
            }}
            
            .metric:last-child {{
                margin-bottom: 0;
            }}
            
            .metric .label {{
                font-weight: bold;
                color: #667eea;
            }}
            
            .metric .value {{
                color: #666;
            }}
            
            .app-status {{
                display: flex;
                gap: 0.5rem;
                margin-bottom: 1rem;
                flex-wrap: wrap;
            }}
            
            .status-badge {{
                display: inline-block;
                padding: 0.4rem 0.8rem;
                border-radius: 4px;
                font-size: 0.85rem;
                font-weight: bold;
            }}
            
            .status-badge.buildable {{
                background: #c8e6c9;
                color: #2e7d32;
            }}
            
            .status-badge.not-buildable {{
                background: #ffcdd2;
                color: #c62828;
            }}
            
            .status-badge.partial {{
                background: #ffe0b2;
                color: #e65100;
            }}
            
            .status-badge.self-serve {{
                background: #e1f5fe;
                color: #01579b;
            }}
            
            .app-blocker {{
                background: #fff3e0;
                padding: 0.75rem;
                border-radius: 4px;
                font-size: 0.9rem;
                margin-bottom: 1rem;
                color: #e65100;
            }}
            
            .app-links {{
                display: flex;
                gap: 0.5rem;
            }}
            
            .app-links a {{
                flex: 1;
                text-align: center;
                padding: 0.6rem;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 4px;
                font-size: 0.9rem;
                transition: background 0.3s ease;
            }}
            
            .app-links a:hover {{
                background: #764ba2;
            }}
            
            .key-insights {{
                background: #fff9e6;
                padding: 1.5rem;
                border-radius: 8px;
                border-left: 4px solid #fbc02d;
                margin-top: 2rem;
            }}
            
            .key-insights ul {{
                list-style-position: inside;
            }}
            
            .key-insights li {{
                margin-bottom: 0.75rem;
                color: #333;
            }}
            
            .apps-section {{
                background: white;
                padding: 2rem;
                border-radius: 8px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            
            .apps-section h2 {{
                font-size: 2rem;
                margin-bottom: 2rem;
                color: #667eea;
            }}
            
            .footer {{
                text-align: center;
                padding: 2rem;
                color: white;
                margin-top: 3rem;
            }}
            
            @media (max-width: 768px) {{
                .header h1 {{
                    font-size: 1.8rem;
                }}
                
                .apps-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .insights-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .summary-stats {{
                    grid-template-columns: repeat(2, 1fr);
                }}
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🚀 Composio Research Report</h1>
            <p>Comprehensive Analysis of 100 SaaS Apps for Agent Toolkit Integration</p>
        </div>
        
        <div class="container">
            {patterns_section}
            
            <section class="apps-section">
                <h2>📱 All 100 Apps</h2>
                <div class="apps-grid">
                    {app_cards}
                </div>
            </section>
        </div>
        
        <div class="footer">
            <p>Generated by Composio Research Agent | Analysis powered by Claude AI</p>
        </div>
    </body>
    </html>
    """
    
    return html

def generate_html_report(findings_file: str = "raw_findings.json", 
                         patterns_file: str = "pattern_analysis.json",
                         output_file: str = "findings_report.html"):
    """Main function to generate HTML report"""
    
    print("\n" + "="*80)
    print("GENERATING HTML CASE STUDY REPORT")
    print("="*80)
    
    print("Loading findings...", end=" ", flush=True)
    findings = load_findings(findings_file)
    print("✓")
    
    print("Loading pattern analysis...", end=" ", flush=True)
    patterns = load_patterns(patterns_file)
    print("✓")
    
    print("Generating HTML...", end=" ", flush=True)
    html = generate_full_html(findings, patterns)
    print("✓")
    
    print("Writing file...", end=" ", flush=True)
    with open(output_file, "w") as f:
        f.write(html)
    print("✓")
    
    print("\n" + "="*80)
    print(f"✅ HTML REPORT GENERATED: {output_file}")
    print("="*80)
    print(f"\nOpen this file in a web browser to view the interactive dashboard:")
    print(f"  file://{output_file}")
    print("\nReport includes:")
    print("  • Summary statistics")
    print("  • Auth pattern analysis")
    print("  • Buildability breakdown")
    print("  • Self-serve access patterns")
    print("  • API type distribution")
    print("  • Easy wins (buildable + self-serve)")
    print("  • Top blockers for partnerships")
    print("  • Interactive cards for all 100 apps")

if __name__ == "__main__":
    generate_html_report()
