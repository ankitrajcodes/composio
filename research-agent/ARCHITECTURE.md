# 🏗️ Architecture Reference Guide

## System Architecture

### High-Level Overview
```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPOSIO RESEARCH AGENT                      │
│                    4-Phase Pipeline System                      │
└─────────────────────────────────────────────────────────────────┘

INPUT: 100 SaaS Apps (from config.py)
  │
  ├─→ [PHASE 1: RESEARCHER]
  │      - Concurrent AI research using Claude
  │      - Gathers: auth, API, buildability
  │      - Error handling & retries
  │      └─→ raw_findings.json
  │
  ├─→ [PHASE 2: VERIFIER]
  │      - 20% sample verification
  │      - AI re-analysis for accuracy
  │      - Accuracy scoring
  │      └─→ verification_report.csv
  │
  ├─→ [PHASE 3: ANALYZER]
  │      - Pattern clustering
  │      - Insight extraction
  │      - Blocker identification
  │      └─→ pattern_analysis.json
  │
  └─→ [PHASE 4: GENERATOR]
         - HTML dashboard creation
         - Interactive visualization
         - Final report
         └─→ findings_report.html

OUTPUT: Complete research package with findings, insights, and dashboard
```

---

## Detailed Component Architecture

### Phase 1: Researcher Component

```
┌──────────────────────────────────────┐
│     RESEARCHER (researcher.py)       │
├──────────────────────────────────────┤
│                                      │
│  Input: APPS_TO_RESEARCH (100)      │
│                                      │
│  ┌────────────────────────────────┐ │
│  │ Request Queue Manager          │ │
│  │ - Concurrent: 10 at a time    │ │
│  │ - Rate limiting: 50/min       │ │
│  │ - Retry logic: 3 attempts     │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Claude AI Research Engine      │ │
│  │ - Model: claude-3.5-sonnet     │ │
│  │ - Max tokens: 1000             │ │
│  │ - Temperature: 0 (deterministic)│
│  │                                │ │
│  │ Research Prompts:              │ │
│  │ 1. What is the auth method?    │ │
│  │ 2. What's the API surface?     │ │
│  │ 3. Is it buildable?            │ │
│  │ 4. What's the main blocker?    │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ JSON Parsing & Validation      │ │
│  │ - Extract structured data      │ │
│  │ - Validate required fields     │ │
│  │ - Track confidence levels      │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  Output: raw_findings.json (100 apps)
│
└──────────────────────────────────────┘
```

### Phase 2: Verifier Component

```
┌──────────────────────────────────────┐
│     VERIFIER (verifier.py)           │
├──────────────────────────────────────┤
│                                      │
│  Input: raw_findings.json (100)     │
│                                      │
│  ┌────────────────────────────────┐ │
│  │ Sample Selection               │ │
│  │ - Random 20% sample (20 apps)  │ │
│  │ - Stratified by category       │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ AI Verification Loop           │ │
│  │ For each sampled app:          │ │
│  │ 1. Re-research the app         │ │
│  │ 2. Compare results             │ │
│  │ 3. Flag discrepancies          │ │
│  │ 4. Score accuracy (1-3)        │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Manual Review (Optional)       │ │
│  │ - Prompt for corrections       │ │
│  │ - Track manual overrides       │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Accuracy Calculation           │ │
│  │ - Overall accuracy %           │ │
│  │ - By-category accuracy         │ │
│  │ - Generate report              │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  Output: verification_report.csv
│          ai_verification_log.json
│
└──────────────────────────────────────┘
```

### Phase 3: Analyzer Component

```
┌──────────────────────────────────────┐
│    ANALYZER (pattern_analyzer.py)    │
├──────────────────────────────────────┤
│                                      │
│  Input: raw_findings.json (100)     │
│                                      │
│  ┌────────────────────────────────┐ │
│  │ Data Aggregation               │ │
│  │ - Load all findings            │ │
│  │ - Validate structure           │ │
│  │ - Track errors                 │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Pattern Analysis               │ │
│  │ - Auth patterns                │ │
│  │ - Self-serve patterns          │ │
│  │ - Buildability breakdown       │ │
│  │ - API type distribution        │ │
│  │ - Category analysis            │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Easy Wins Identification       │ │
│  │ Filter: buildable + self-serve │ │
│  │ Sort: by confidence            │ │
│  │ Result: 20-30 quick wins       │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Blocker Extraction             │ │
│  │ - Group by blocker type        │ │
│  │ - Count affected apps          │ │
│  │ - Prioritize by impact         │ │
│  │ - Top 8-10 blockers            │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Insight Generation             │ │
│  │ - Key findings                 │ │
│  │ - Recommendations              │ │
│  │ - Confidence distribution      │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  Output: pattern_analysis.json
│
└──────────────────────────────────────┘
```

### Phase 4: Generator Component

```
┌──────────────────────────────────────┐
│   GENERATOR (html_generator.py)      │
├──────────────────────────────────────┤
│                                      │
│  Input: raw_findings.json +          │
│         pattern_analysis.json        │
│                                      │
│  ┌────────────────────────────────┐ │
│  │ HTML Structure Creation        │ │
│  │ - Header with title            │ │
│  │ - Navigation sections          │ │
│  │ - Main content areas           │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ CSS Styling                    │ │
│  │ - Color scheme (purple)        │ │
│  │ - Responsive design            │ │
│  │ - Interactive elements         │ │
│  │ - Print-friendly              │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Content Generation             │ │
│  │ - Summary statistics           │ │
│  │ - Pattern visualizations       │ │
│  │ - App cards (100)              │ │
│  │ - Easy wins list               │ │
│  │ - Blocker analysis             │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  ┌────────────────────────────────┐ │
│  │ Interactive Features           │ │
│  │ - Hover effects                │ │
│  │ - Color coding                 │ │
│  │ - External links               │ │
│  │ - Responsive layout            │ │
│  └────────────────────────────────┘ │
│           ↓                          │
│  Output: findings_report.html
│
└──────────────────────────────────────┘
```

---

## Data Flow Architecture

### Data Transformation Pipeline

```
CONFIG (100 apps)
    │
    ▼
RESEARCHER
    │ processes concurrently (10 at a time)
    ▼
RAW_FINDINGS.json
    │
    ├─→ VERIFIER (20% sample) ─→ VERIFICATION_REPORT.csv
    │
    └─→ ANALYZER
            │ clusters & aggregates
            ▼
        PATTERN_ANALYSIS.json
            │
            └─→ GENERATOR
                    │ combines data
                    ▼
                FINDINGS_REPORT.html
```

### Data Structure Hierarchy

```
raw_findings.json (Array of 100)
├── app_id: string
├── app_name: string
├── category: string
├── auth_methods: string
├── self_serve_status: string
├── api_surface: string
├── buildability_verdict: string
├── main_blocker: string
├── confidence_level: enum(high|medium|low)
├── docs_url: string
└── website: string

pattern_analysis.json (Object)
├── summary: object
│   ├── total_apps: int
│   ├── easy_wins: int
│   └── major_blockers: int
├── auth_patterns: object
│   ├── overall: object (OAuth2, API Keys, etc.)
│   └── by_category: object
├── self_serve_patterns: object
├── buildability: object
├── api_analysis: object
├── easy_wins: array (20-30 items)
├── high_blockers: array (8-10 items)
├── category_analysis: object
├── key_insights: array
└── recommendations: object
```

---

## Processing Pipeline Details

### Researcher Processing

```
Per App:
1. Load app config (name, category, website)
2. Build research prompt with app details
3. Send to Claude API
4. Parse JSON response
5. Validate structure
6. Store in raw_findings.json
7. Log success/error

Concurrency:
- Queue manager maintains 10 concurrent requests
- Rate limiting: 50 requests/minute
- Retry logic: 3 attempts with exponential backoff
- Timeout: 30 seconds per request

Output Structure:
{
  "app_id": "unique-id",
  "app_name": "Full Name",
  "category": "Category",
  "auth_methods": "OAuth2, API Keys",
  "self_serve_status": "Free tier",
  "api_surface": "REST API",
  "buildability_verdict": "Yes/No",
  "main_blocker": "None or description",
  "confidence_level": "high/medium/low",
  "docs_url": "https://...",
  "website": "https://..."
}
```

### Verifier Processing

```
Per Sampled App:
1. Select random 20% of raw_findings
2. Re-research using Claude
3. Compare both sets of results
4. Check key fields for accuracy
5. Score accuracy: 1 (poor) to 3 (perfect)
6. Track corrections
7. Allow manual override if enabled

Accuracy Scoring:
- 3 points: Perfect match
- 2 points: Minor differences
- 1 point: Significant differences

Output:
verification_report.csv with:
- app_name, accuracy_score, corrections, status
- Summary stats: overall_accuracy%, by_category%
```

### Analyzer Processing

```
Step 1: Aggregation
- Load 100 app records
- Count successes/errors
- Group by category

Step 2: Pattern Clustering
- Count auth methods (OAuth2, API Keys, Custom, None)
- Count self-serve statuses
- Count buildability verdicts
- Count API types
- Track confidence levels

Step 3: Easy Wins Identification
- Filter: buildability = "Yes" AND self_serve = "Yes"
- Sort by confidence level
- Return 20-30 apps

Step 4: Blocker Extraction
- Extract main_blocker from each app
- Group by blocker type
- Count apps per blocker
- Identify top 8-10 blockers

Step 5: Category Analysis
- Analyze patterns per category
- Calculate buildability % per category
- Identify category-specific blockers

Step 6: Insight Generation
- Synthesize findings into insights
- Generate recommendations
- Calculate confidence distribution
```

### Generator Processing

```
Step 1: Load Data
- Load raw_findings.json (100 apps)
- Load pattern_analysis.json

Step 2: Generate HTML Structure
- Create header section
- Create navigation
- Create main sections for each insight

Step 3: Generate Content
For each pattern section:
  - Create summary statistics box
  - Generate tables with data
  - Create visualizations (CSS-based)
  - Add explanation text

For each app:
  - Create card with app info
  - Color code by buildability
  - Add confidence badge
  - Add quick links

Step 4: Generate CSS
- Responsive design
- Color scheme (purple gradient)
- Interactive hover effects
- Print-friendly styles

Step 5: Combine & Output
- Merge all sections into single HTML
- Validate HTML structure
- Write to findings_report.html
```

---

## Performance Architecture

### Concurrency Model

```
Request Queue (max 10 concurrent):

Time: 0s
├─ Request 1: Slack
├─ Request 2: GitHub
├─ Request 3: Salesforce
├─ ...
└─ Request 10: Mailchimp

Time: 2-3s (first request completes)
├─ Response 1 → stored
└─ Request 11 queued

Continues until all 100 apps processed
Typical total time: 8-12 minutes
```

### Rate Limiting Strategy

```
API Limit: 50 requests/minute
Our Rate: 10 concurrent, ~30-40 requests/minute
Headroom: 20% buffer
Retry on limit: 1 second delay, exponential backoff
```

---

## Error Handling Architecture

### Failure Recovery

```
Research Phase Errors:
├─ API timeout (30s) → Retry up to 3 times
├─ Invalid JSON → Log error, mark as failed
├─ Network error → Exponential backoff retry
└─ API rate limit → Pause, wait, resume

Verification Phase Errors:
├─ Re-research failure → Mark as unverified
├─ Comparison failure → Log anomaly
└─ Manual review skip → Continue with AI verdict

Analysis Phase Errors:
├─ Missing fields → Use defaults
├─ Invalid data → Filter out
└─ Empty results → Skip category

Generation Phase Errors:
├─ Missing JSON files → Halt with error
├─ File write error → Retry
└─ HTML validation → Log warning
```

---

## Output Architecture

### File Structure

```
research-agent/
├── .py files (scripts)
├── config.py (configuration)
├── requirements.txt (dependencies)
│
├── Output Files:
├── raw_findings.json (100 KB)
├── pattern_analysis.json (50 KB)
├── findings_report.html (500 KB)
├── verification_report.csv (20 KB)
├── ai_verification_log.json (30 KB)
│
└── Example/Template Files:
    ├── example_raw_findings.json
    └── example_pattern_analysis.json
```

### HTML Dashboard Structure

```
findings_report.html
├── Head
│   ├── Meta tags
│   ├── Title
│   └── Embedded CSS (1500+ lines)
│
└── Body
    ├── Header (title, description)
    │
    ├── Main Container
    │   ├── Patterns Section
    │   │   ├── Summary Statistics (4 cards)
    │   │   ├── Insights Grid (4 cards)
    │   │   ├── Easy Wins Section
    │   │   └── Blockers Analysis
    │   │
    │   └── Apps Grid (100 cards)
    │       ├── Card 1: Slack
    │       ├── Card 2: GitHub
    │       └── ...
    │
    └── Footer
```

---

## Technology Stack

### Languages & Libraries
- **Python 3.8+** - Core language
- **Anthropic SDK** - Claude AI integration
- **Standard Library** - json, csv, subprocess, etc.

### External Services
- **Claude 3.5 Sonnet** - AI research engine
- **Anthropic API** - Request/response handling

### Output Technologies
- **HTML5** - Dashboard markup
- **CSS3** - Styling and responsiveness
- **JavaScript** - (minimal, for future enhancements)

---

## Scalability Considerations

### Current Capacity
- **100 apps** per run
- **10 concurrent requests** per phase
- **~10 minutes** total runtime
- **~$10** API cost per run

### Scaling Options
- Increase concurrent requests (up to 50)
- Add app batching for 500+ apps
- Implement caching for repeated apps
- Parallelize analysis phase

---

## Security Considerations

### Data Handling
- No data persistence beyond output files
- API keys handled via environment variables
- Research data is non-sensitive (public app info)
- No authentication required for output files

### API Security
- Rate limiting respected
- Timeout mechanisms in place
- Error handling for failed requests
- Retry logic with exponential backoff

---

## Quality Assurance

### Validation Points
1. **Researcher** - Output validation (required fields)
2. **Verifier** - Accuracy checking (90% target)
3. **Analyzer** - Pattern consistency
4. **Generator** - HTML validity

### Testing Strategy
- Process sample of 10 apps first
- Verify output structure
- Check confidence distribution
- Review easy wins list
- Validate HTML rendering

---

## Deployment Architecture

### Prerequisites
- Python 3.8+
- pip package manager
- Anthropic API key

### Deployment Steps
1. Clone repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set API key: `export ANTHROPIC_API_KEY="..."`
4. Run: `python main.py`

### Output Access
- All outputs in same directory as scripts
- HTML viewable in any modern browser
- JSON files importable to other tools
- CSV files openable in spreadsheet software

---

This architecture is designed for:
- ✅ Efficiency (10 minutes for 100 apps)
- ✅ Reliability (error recovery, retries)
- ✅ Scalability (can handle 500+ apps)
- ✅ Quality (verification, accuracy checking)
- ✅ Usability (beautiful HTML dashboard)
