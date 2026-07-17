# Getting Started Guide - Composio Research Agent

## 🎯 Quick Setup (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set API Key
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### 3. Run the Workflow
```bash
python main.py
```

## 📊 What Happens Next

The workflow will:
1. **Research** 100 SaaS apps (~2-5 minutes)
2. **Verify** findings on a sample (~1-2 minutes)
3. **Analyze** patterns to extract insights (~30 seconds)
4. **Generate** interactive HTML dashboard (~1 minute)

Total time: **5-10 minutes**

## 📁 Output Files

After running, you'll have:
- `raw_findings.json` - Raw research data
- `pattern_analysis.json` - Pattern insights
- `findings_report.html` - Interactive dashboard
- `verification_report.csv` - Verification results
- `ai_verification_log.json` - Verification logs

## 🌐 Viewing the Report

```bash
# Open the HTML report in your browser
open findings_report.html  # macOS
xdg-open findings_report.html  # Linux
start findings_report.html  # Windows
```

Or navigate to the file directly in your browser.

## 🔧 Configuration

Edit `config.py` to customize:

### Apps to Research
```python
APPS_TO_RESEARCH = [
    {"app_id": "slack", "name": "Slack", ...},
    # Add or remove apps here
]
```

### Research Settings
```python
CONCURRENT_REQUESTS = 10  # Parallel requests
VERIFICATION_SAMPLE_SIZE = 20  # 20% of findings verified
MANUAL_VERIFICATION = False  # Set True for manual review
```

### Output Files
```python
RAW_FINDINGS_FILE = "raw_findings.json"
PATTERN_ANALYSIS_FILE = "pattern_analysis.json"
HTML_REPORT_FILE = "findings_report.html"
```

## 🚀 Advanced Usage

### Run Individual Steps

```bash
# Step 1: Research only
python researcher.py

# Step 2: Verify only (requires raw_findings.json)
python verifier.py

# Step 3: Analyze only (requires raw_findings.json)
python pattern_analyzer.py

# Step 4: Generate report (requires both JSON files)
python html_generator.py
```

### Partial Run

```bash
# Research 50 apps only
# Edit config.py: APPS_TO_RESEARCH = APPS_TO_RESEARCH[:50]
python researcher.py
python verifier.py
python pattern_analyzer.py
python html_generator.py
```

### Custom App List

Edit `config.py` to include only specific apps:

```python
APPS_TO_RESEARCH = [
    {"app_id": "slack", "name": "Slack", "category": "Communication", "website": "https://slack.com"},
    {"app_id": "github", "name": "GitHub", "category": "Developer", "website": "https://github.com"},
    # Add only the apps you want to research
]
```

## 🔍 Understanding the Output

### raw_findings.json
```json
{
  "app_id": "slack",
  "app_name": "Slack",
  "category": "Communication",
  "description": "Team communication platform",
  "auth_methods": "OAuth2",
  "self_serve_status": "Free tier available",
  "api_surface": "REST API",
  "buildability_verdict": "Yes",
  "main_blocker": "None",
  "confidence_level": "high",
  "docs_url": "https://api.slack.com",
  "website": "https://slack.com"
}
```

### pattern_analysis.json
```json
{
  "summary": {
    "total_apps": 100,
    "successful_research": 98,
    "easy_wins": 20,
    "major_blockers": 8
  },
  "auth_patterns": {
    "overall": {
      "OAuth2": 45,
      "API Keys": 30,
      "Custom": 15
    }
  },
  "easy_wins": [
    {
      "app_name": "Slack",
      "category": "Communication",
      "auth": "OAuth2",
      "why": "Buildable + Self-Serve"
    }
  ]
}
```

### findings_report.html
An interactive web dashboard featuring:
- Summary statistics
- Pattern visualizations
- All 100 app cards
- Easy wins list
- Blocker analysis
- Color-coded buildability status

## 🐛 Troubleshooting

### "API Key not found"
```bash
# Make sure to set the API key
export ANTHROPIC_API_KEY="sk-ant-..."
# Verify it's set
echo $ANTHROPIC_API_KEY
```

### "Module not found"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### "File not found: raw_findings.json"
```bash
# Run researcher first
python researcher.py
```

### "API Rate Limit Exceeded"
```bash
# Reduce concurrent requests in config.py
CONCURRENT_REQUESTS = 5  # Instead of 10
```

### "Verification failed"
```bash
# This is normal - some verifications may fail
# Check the verification_report.csv for details
# Continue with pattern analysis regardless
```

## 📈 Interpreting Results

### Confidence Levels
- 🟢 **HIGH** - Very confident in the research
- 🟡 **MEDIUM** - Reasonably confident, some assumptions made
- 🔴 **LOW** - Limited information available

### Buildability Status
- ✅ **Buildable Today** - Ready for integration
- ❌ **Not Buildable** - Significant blockers
- ⚠️ **Partial/Unclear** - Needs manual review

### Self-Serve Status
- 🟢 **Self-Serve** - Free, accessible signup
- 🔴 **Gated** - Requires approval or payment
- ⚫ **Unknown** - Status unclear

## 💡 Tips & Tricks

### Finding Easy Wins
In `findings_report.html`, look for apps that are:
1. ✅ Buildable Today (green)
2. 🟢 Self-Serve (green)

These are immediate integration candidates.

### Identifying Partnership Opportunities
Check the "Top Blockers" section for:
- Partnership required
- Special approval needed
- Account approval process

These are good candidates for vendor partnerships.

### Analyzing by Category
Use the pattern analysis to identify:
- Which categories have the most buildable apps
- Which auth methods dominate each category
- Category-specific barriers

### Monitoring Progress
Track these metrics:
- Buildable vs Not Buildable ratio
- Self-Serve vs Gated ratio
- Average confidence level

## 🔗 Integration with Composio

Once research is complete:

1. **Review Easy Wins** - Priority integration targets
2. **Contact Vendors** - For gated/partnership apps
3. **Build Integrations** - Start with high-confidence apps
4. **Update Toolkit** - Add new integrations to Composio

## 📚 File Structure

```
research-agent/
├── main.py                  # Orchestration script
├── researcher.py            # Research engine
├── verifier.py             # Verification agent
├── pattern_analyzer.py     # Pattern extraction
├── html_generator.py       # Report generation
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── README.md              # Main documentation
├── GETTING_STARTED.md     # This file
├── raw_findings.json      # Output: Raw data
├── pattern_analysis.json  # Output: Patterns
├── findings_report.html   # Output: Dashboard
├── verification_report.csv # Output: Verification
└── ai_verification_log.json # Output: Logs
```

## 🎓 Learning More

### Understanding the Research
- Each app is researched for: auth, API, buildability
- Research uses Claude AI for intelligent analysis
- Findings are stored in structured JSON

### Verification Process
- 20% of findings are randomly selected
- AI re-analyzes them for consistency
- Accuracy score is calculated
- Optional manual review available

### Pattern Analysis
- Clusters similar apps and auth methods
- Identifies common blockers
- Highlights easy wins
- Provides category-specific insights

### Report Generation
- Creates beautiful HTML dashboard
- Interactive app cards with color coding
- Summary statistics and visualizations
- Links to docs and websites

## 🚨 Important Notes

### API Costs
- Research on 100 apps: ~$5-15
- Verification adds ~$1-3
- Check your Anthropic account for pricing

### Time Estimates
- Fast run: 5-10 minutes
- With 50 apps: 3-5 minutes
- With 100 apps: 8-12 minutes

### Accuracy
- Typical accuracy: 85-90%
- Confidence levels help identify uncertain findings
- Manual review recommended for critical decisions

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the main README.md
3. Check error messages for specific guidance

## ✅ Next Steps

1. ✅ Set up the environment
2. ✅ Run `python main.py`
3. ✅ Open `findings_report.html` in browser
4. ✅ Review the 100 apps and patterns
5. ✅ Plan integration roadmap
6. ✅ Start with easy wins

---

**Happy researching! 🚀**
