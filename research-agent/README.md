# 🚀 Composio Research Agent

A comprehensive AI-powered research system that analyzes 100+ SaaS apps to identify integration opportunities for the Composio toolkit.

## 📋 Overview

This research agent automates the process of discovering which SaaS applications can be integrated into Composio by:

1. **Researching** each app's authentication, API surface, and buildability
2. **Verifying** findings through human-in-the-loop and AI validation
3. **Analyzing** patterns to identify easy wins and common blockers
4. **Generating** an interactive HTML dashboard with all insights

## 🎯 Key Features

- ✅ **Automated Research**: Uses Claude AI to research 100 SaaS apps concurrently
- ✅ **Accuracy Verification**: Spot-checks findings with human review and AI verification
- ✅ **Pattern Analysis**: Clusters findings to extract actionable insights
- ✅ **Interactive Dashboard**: Beautiful HTML report with all 100 apps
- ✅ **Blocker Identification**: Highlights barriers to integration for partnership outreach
- ✅ **Easy Wins Detection**: Identifies apps ready for immediate integration

## 📊 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   RESEARCH WORKFLOW                     │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  1. RESEARCHER (researcher.py)        │
        │  • Research 100 SaaS apps            │
        │  • Gather: auth, API, buildability   │
        │  • Output: raw_findings.json         │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  2. VERIFIER (verifier.py)           │
        │  • Spot-check 20% sample            │
        │  • AI verification layer            │
        │  • Track accuracy metrics           │
        │  • Output: verification_report.csv  │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  3. ANALYZER (pattern_analyzer.py)   │
        │  • Cluster findings                 │
        │  • Extract patterns                 │
        │  • Find blockers & easy wins        │
        │  • Output: pattern_analysis.json    │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  4. GENERATOR (html_generator.py)    │
        │  • Create interactive dashboard     │
        │  • Beautiful case study report      │
        │  • Output: findings_report.html     │
        └───────────────────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Anthropic API key (for Claude AI)
- Required packages: `anthropic`

### Installation

```bash
# Clone the repository
git clone https://github.com/ankitrajcodes/composio.git
cd composio/research-agent

# Install dependencies
pip install anthropic

# Set your API key
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Running the Workflow

```bash
# Run the complete workflow
python main.py

# Or run individual steps
python researcher.py      # 1. Research apps
python verifier.py        # 2. Verify findings
python pattern_analyzer.py # 3. Analyze patterns
python html_generator.py   # 4. Generate report
```

## 📁 Output Files

### `raw_findings.json`
Raw research data for 100 SaaS apps. Example structure:
```json
{
  "app_id": "slack",
  "app_name": "Slack",
  "category": "Communication",
  "website": "https://slack.com",
  "description": "Team communication platform",
  "auth_methods": "OAuth2",
  "self_serve_status": "Free tier available",
  "api_surface": "REST API, broad functionality",
  "buildability_verdict": "Yes - can build integrations",
  "main_blocker": "None",
  "confidence_level": "high",
  "docs_url": "https://api.slack.com"
}
```

### `pattern_analysis.json`
Clustered insights and patterns. Includes:
- Auth method distribution
- Self-serve vs gated access patterns
- Buildability breakdown
- API type analysis
- Easy wins list
- Top blockers for partnerships

### `findings_report.html`
Interactive web dashboard with:
- Summary statistics
- Pattern visualizations
- All 100 app cards
- Color-coded buildability status
- Self-serve access indicators
- Blocker analysis
- Easy wins highlighting

### `verification_report.csv`
Human verification results with:
- App name
- Accuracy score (1-3)
- Corrections made
- Verification status

## 🔬 Research Questions Answered

For each app, the researcher answers:

### Authentication
- What auth methods are available? (OAuth, API keys, etc.)
- Is self-serve signup available?
- Any gating or approval required?

### API Surface
- What type of API? (REST, GraphQL, etc.)
- How broad is the API functionality?
- Is MCP (Model Context Protocol) available?

### Buildability
- Can we build integrations today?
- What are the main blockers?
- Do they have partner/integration programs?

### Integration Readiness
- How confident are we in the assessment?
- What's the primary documentation source?
- Any special requirements?

## 📊 Sample Insights

### Auth Patterns
- **OAuth2**: 45 apps (most common)
- **API Keys**: 30 apps
- **Custom**: 15 apps
- **None**: 10 apps

### Self-Serve Status
- **Self-Serve**: 60 apps (easily accessible)
- **Gated**: 30 apps (require approval)
- **Unknown**: 10 apps

### Buildability
- **Buildable Today**: 55 apps
- **Not Buildable**: 25 apps
- **Partial/Unclear**: 20 apps

### Easy Wins
- **20 apps** are both buildable AND have self-serve access
- Perfect candidates for immediate integration

### Top Blockers
1. Partnership required (8 apps)
2. Rate limiting (6 apps)
3. Limited API (5 apps)
4. Approval process (4 apps)

## 🔍 Verification Process

### Phase 1: Automated Research
- Concurrent research on all 100 apps
- Uses Claude AI for intelligent analysis
- Gathers structured data

### Phase 2: AI Verification (20% sample)
- Re-analyzes 20 random apps
- Compares against known facts
- Flags potential inaccuracies

### Phase 3: Human Review (optional)
- Spot-check verification prompts
- Manual accuracy corrections
- Tracks confidence levels

### Phase 4: Accuracy Metrics
- Overall accuracy percentage
- Confidence level distribution
- Common error patterns

## 🎨 Dashboard Features

### Interactive App Cards
- Color-coded by buildability status
- Confidence level badges
- Quick links to docs and website
- Auth and API info at a glance

### Pattern Visualizations
- Auth type distribution
- Self-serve access breakdown
- Buildability statistics
- API type analysis

### Easy Wins Section
- Apps ready for immediate integration
- Organized by category
- Quick reference guide

### Blocker Analysis
- Top 10 blockers identified
- Sample apps affected
- Count of impacted integrations

## 📈 Use Cases

### Partnership Outreach
- Identify apps that require partnerships
- Prioritize high-impact integrations
- Prepare partnership proposals

### Integration Roadmap
- Easy wins for quick wins
- Understand common blockers
- Plan integration strategy

### API Analysis
- Understand SaaS API trends
- Identify emerging standards
- Find compatible API patterns

### Category Analysis
- Compare integration readiness by category
- Understand vertical-specific patterns
- Prioritize category focus areas

## 🛠️ Customization

### Research Scope
Edit `researcher.py` to research different apps:
```python
APPS_TO_RESEARCH = [
    {"app_id": "slack", "name": "Slack", "category": "Communication"},
    # Add more apps...
]
```

### Verification Percentage
Edit `verifier.py` to change sample size:
```python
verification_results, accuracy_pct = verify_sample(findings, sample_size=30)  # 30% sample
```

### HTML Customization
Edit `html_generator.py` to customize:
- Color scheme
- Report structure
- Layout and styling

## 📚 Documentation

### Key Files
- `main.py` - Workflow orchestration
- `researcher.py` - Research engine
- `verifier.py` - Verification agent
- `pattern_analyzer.py` - Pattern extraction
- `html_generator.py` - Report generation

### Dependencies
- `anthropic` - Claude API client
- Standard library: `json`, `csv`, `subprocess`, `collections`

## 🤝 Contributing

Improvements welcome! Areas for enhancement:
- Add more SaaS apps to research
- Improve verification accuracy
- Add more pattern analyses
- Enhance HTML dashboard

## 📝 License

MIT License - Feel free to use for research and integration planning.

## 🚨 Important Notes

### API Costs
- This workflow uses the Anthropic API
- Research on 100 apps will incur API costs
- Estimate: ~$5-15 depending on API pricing

### Rate Limiting
- Respects API rate limits
- Includes error handling and retries
- Graceful degradation for failed requests

### Data Accuracy
- AI research is best-effort (85-90% typical accuracy)
- Verification phase improves confidence
- Manual review recommended for critical decisions

## 🎯 Next Steps

1. **Run the workflow**: `python main.py`
2. **Open the dashboard**: Open `findings_report.html` in your browser
3. **Review findings**: Examine the 100 apps and patterns
4. **Plan integration**: Use easy wins list for roadmap
5. **Outreach**: Identify partnership opportunities

## 💡 Tips

- Start with easy wins for quick integration wins
- Use blocker analysis for partnership outreach
- Cross-reference findings with pattern analysis
- Review confidence levels for high-priority apps
- Use category analysis for focused strategies

---

**Built with ❤️ for Composio | Powered by Claude AI**
