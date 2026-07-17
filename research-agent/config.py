# Research Agent Configuration

# List of 100 SaaS apps to research
# Format: {"app_id": "unique-id", "name": "App Name", "category": "Category", "website": "https://..."}

APPS_TO_RESEARCH = [
    # Communication & Collaboration
    {"app_id": "slack", "name": "Slack", "category": "Communication", "website": "https://slack.com"},
    {"app_id": "microsoft-teams", "name": "Microsoft Teams", "category": "Communication", "website": "https://teams.microsoft.com"},
    {"app_id": "discord", "name": "Discord", "category": "Communication", "website": "https://discord.com"},
    {"app_id": "telegram", "name": "Telegram", "category": "Communication", "website": "https://telegram.org"},
    {"app_id": "zoom", "name": "Zoom", "category": "Communication", "website": "https://zoom.us"},
    
    # Project Management
    {"app_id": "asana", "name": "Asana", "category": "Project Management", "website": "https://asana.com"},
    {"app_id": "monday-com", "name": "Monday.com", "category": "Project Management", "website": "https://monday.com"},
    {"app_id": "jira", "name": "Jira", "category": "Project Management", "website": "https://jira.atlassian.com"},
    {"app_id": "trello", "name": "Trello", "category": "Project Management", "website": "https://trello.com"},
    {"app_id": "notion", "name": "Notion", "category": "Project Management", "website": "https://notion.so"},
    
    # CRM & Sales
    {"app_id": "salesforce", "name": "Salesforce", "category": "CRM", "website": "https://salesforce.com"},
    {"app_id": "hubspot", "name": "HubSpot", "category": "CRM", "website": "https://hubspot.com"},
    {"app_id": "pipedrive", "name": "Pipedrive", "category": "CRM", "website": "https://pipedrive.com"},
    {"app_id": "zendesk", "name": "Zendesk", "category": "CRM", "website": "https://zendesk.com"},
    {"app_id": "freshsales", "name": "Freshsales", "category": "CRM", "website": "https://freshsales.com"},
    
    # Email & Marketing
    {"app_id": "mailchimp", "name": "Mailchimp", "category": "Email Marketing", "website": "https://mailchimp.com"},
    {"app_id": "sendgrid", "name": "SendGrid", "category": "Email Marketing", "website": "https://sendgrid.com"},
    {"app_id": "constant-contact", "name": "Constant Contact", "category": "Email Marketing", "website": "https://constantcontact.com"},
    {"app_id": "klaviyo", "name": "Klaviyo", "category": "Email Marketing", "website": "https://klaviyo.com"},
    {"app_id": "mailgun", "name": "Mailgun", "category": "Email Marketing", "website": "https://mailgun.com"},
    
    # Calendar & Scheduling
    {"app_id": "calendly", "name": "Calendly", "category": "Scheduling", "website": "https://calendly.com"},
    {"app_id": "google-calendar", "name": "Google Calendar", "category": "Calendar", "website": "https://calendar.google.com"},
    {"app_id": "microsoft-outlook", "name": "Microsoft Outlook", "category": "Calendar", "website": "https://outlook.com"},
    {"app_id": "cal-com", "name": "Cal.com", "category": "Scheduling", "website": "https://cal.com"},
    {"app_id": "doodle", "name": "Doodle", "category": "Scheduling", "website": "https://doodle.com"},
    
    # Document & File Management
    {"app_id": "google-drive", "name": "Google Drive", "category": "Cloud Storage", "website": "https://drive.google.com"},
    {"app_id": "dropbox", "name": "Dropbox", "category": "Cloud Storage", "website": "https://dropbox.com"},
    {"app_id": "microsoft-onedrive", "name": "OneDrive", "category": "Cloud Storage", "website": "https://onedrive.live.com"},
    {"app_id": "box", "name": "Box", "category": "Cloud Storage", "website": "https://box.com"},
    {"app_id": "sharepoint", "name": "SharePoint", "category": "Document Management", "website": "https://sharepoint.com"},
    
    # Accounting & Finance
    {"app_id": "quickbooks", "name": "QuickBooks", "category": "Accounting", "website": "https://quickbooks.intuit.com"},
    {"app_id": "xero", "name": "Xero", "category": "Accounting", "website": "https://xero.com"},
    {"app_id": "freshbooks", "name": "FreshBooks", "category": "Accounting", "website": "https://freshbooks.com"},
    {"app_id": "stripe", "name": "Stripe", "category": "Payment", "website": "https://stripe.com"},
    {"app_id": "square", "name": "Square", "category": "Payment", "website": "https://squareup.com"},
    
    # HR & Payroll
    {"app_id": "workday", "name": "Workday", "category": "HR", "website": "https://workday.com"},
    {"app_id": "bamboohr", "name": "BambooHR", "category": "HR", "website": "https://bamboohr.com"},
    {"app_id": "guidepoint", "name": "Guidepoint", "category": "HR", "website": "https://guidepoint.com"},
    {"app_id": "paychex", "name": "Paychex", "category": "Payroll", "website": "https://paychex.com"},
    {"app_id": "adp", "name": "ADP", "category": "Payroll", "website": "https://adp.com"},
    
    # Analytics & BI
    {"app_id": "google-analytics", "name": "Google Analytics", "category": "Analytics", "website": "https://analytics.google.com"},
    {"app_id": "tableau", "name": "Tableau", "category": "BI", "website": "https://tableau.com"},
    {"app_id": "power-bi", "name": "Power BI", "category": "BI", "website": "https://powerbi.microsoft.com"},
    {"app_id": "mixpanel", "name": "Mixpanel", "category": "Analytics", "website": "https://mixpanel.com"},
    {"app_id": "amplitude", "name": "Amplitude", "category": "Analytics", "website": "https://amplitude.com"},
    
    # Customer Support
    {"app_id": "intercom", "name": "Intercom", "category": "Support", "website": "https://intercom.com"},
    {"app_id": "freshdesk", "name": "Freshdesk", "category": "Support", "website": "https://freshdesk.com"},
    {"app_id": "helpscout", "name": "Help Scout", "category": "Support", "website": "https://helpscout.com"},
    {"app_id": "livechat", "name": "LiveChat", "category": "Support", "website": "https://livechat.com"},
    {"app_id": "drift", "name": "Drift", "category": "Support", "website": "https://drift.com"},
    
    # Social Media & Marketing
    {"app_id": "hootsuite", "name": "Hootsuite", "category": "Social Media", "website": "https://hootsuite.com"},
    {"app_id": "buffer", "name": "Buffer", "category": "Social Media", "website": "https://buffer.com"},
    {"app_id": "sprout-social", "name": "Sprout Social", "category": "Social Media", "website": "https://sproutsocial.com"},
    {"app_id": "later", "name": "Later", "category": "Social Media", "website": "https://later.com"},
    {"app_id": "instagram", "name": "Instagram", "category": "Social Media", "website": "https://instagram.com"},
    
    # Developer & DevOps
    {"app_id": "github", "name": "GitHub", "category": "Developer", "website": "https://github.com"},
    {"app_id": "gitlab", "name": "GitLab", "category": "Developer", "website": "https://gitlab.com"},
    {"app_id": "jenkins", "name": "Jenkins", "category": "DevOps", "website": "https://jenkins.io"},
    {"app_id": "docker", "name": "Docker", "category": "DevOps", "website": "https://docker.com"},
    {"app_id": "kubernetes", "name": "Kubernetes", "category": "DevOps", "website": "https://kubernetes.io"},
    
    # Monitoring & Logging
    {"app_id": "datadog", "name": "Datadog", "category": "Monitoring", "website": "https://datadog.com"},
    {"app_id": "sentry", "name": "Sentry", "category": "Monitoring", "website": "https://sentry.io"},
    {"app_id": "splunk", "name": "Splunk", "category": "Logging", "website": "https://splunk.com"},
    {"app_id": "elastic", "name": "Elastic", "category": "Logging", "website": "https://elastic.co"},
    {"app_id": "newrelic", "name": "New Relic", "category": "Monitoring", "website": "https://newrelic.com"},
    
    # E-commerce
    {"app_id": "shopify", "name": "Shopify", "category": "E-commerce", "website": "https://shopify.com"},
    {"app_id": "woocommerce", "name": "WooCommerce", "category": "E-commerce", "website": "https://woocommerce.com"},
    {"app_id": "magento", "name": "Magento", "category": "E-commerce", "website": "https://magento.com"},
    {"app_id": "bigcommerce", "name": "BigCommerce", "category": "E-commerce", "website": "https://bigcommerce.com"},
    {"app_id": "squarespace", "name": "Squarespace", "category": "E-commerce", "website": "https://squarespace.com"},
    
    # Content Management
    {"app_id": "wordpress", "name": "WordPress", "category": "CMS", "website": "https://wordpress.com"},
    {"app_id": "contentful", "name": "Contentful", "category": "Headless CMS", "website": "https://contentful.com"},
    {"app_id": "sanity", "name": "Sanity", "category": "Headless CMS", "website": "https://sanity.io"},
    {"app_id": "strapi", "name": "Strapi", "category": "Headless CMS", "website": "https://strapi.io"},
    {"app_id": "ghost", "name": "Ghost", "category": "CMS", "website": "https://ghost.org"},
    
    # Automation & Workflows
    {"app_id": "zapier", "name": "Zapier", "category": "Automation", "website": "https://zapier.com"},
    {"app_id": "make", "name": "Make", "category": "Automation", "website": "https://make.com"},
    {"app_id": "ifttt", "name": "IFTTT", "category": "Automation", "website": "https://ifttt.com"},
    {"app_id": "parabola", "name": "Parabola", "category": "Automation", "website": "https://parabola.io"},
    {"app_id": "n8n", "name": "n8n", "category": "Automation", "website": "https://n8n.io"},
    
    # Video & Media
    {"app_id": "youtube", "name": "YouTube", "category": "Video", "website": "https://youtube.com"},
    {"app_id": "vimeo", "name": "Vimeo", "category": "Video", "website": "https://vimeo.com"},
    {"app_id": "mux", "name": "Mux", "category": "Video", "website": "https://mux.com"},
    {"app_id": "cloudinary", "name": "Cloudinary", "category": "Media", "website": "https://cloudinary.com"},
    {"app_id": "figma", "name": "Figma", "category": "Design", "website": "https://figma.com"},
    
    # Others (High value/unique apps)
    {"app_id": "twilio", "name": "Twilio", "category": "Communication", "website": "https://twilio.com"},
    {"app_id": "airtable", "name": "Airtable", "category": "Database", "website": "https://airtable.com"},
    {"app_id": "linear", "name": "Linear", "category": "Project Management", "website": "https://linear.app"},
    {"app_id": "supabase", "name": "Supabase", "category": "Backend", "website": "https://supabase.com"},
    {"app_id": "firebase", "name": "Firebase", "category": "Backend", "website": "https://firebase.google.com"},
]

# Research configuration
CONCURRENT_REQUESTS = 10  # Number of concurrent API requests
REQUEST_TIMEOUT = 30  # Timeout per request in seconds
MAX_RETRIES = 3  # Maximum retries on failure

# Verification configuration
VERIFICATION_SAMPLE_SIZE = 20  # 20% of findings
VERIFICATION_TIMEOUT = 20  # Timeout for verification
MANUAL_VERIFICATION = False  # Set to True to enable manual verification prompts

# Model configuration
MODEL = "claude-3-5-sonnet-20241022"
MAX_TOKENS = 1000  # Max tokens per research request

# Output configuration
OUTPUT_DIR = "./"
RAW_FINDINGS_FILE = "raw_findings.json"
PATTERN_ANALYSIS_FILE = "pattern_analysis.json"
HTML_REPORT_FILE = "findings_report.html"
VERIFICATION_REPORT_FILE = "verification_report.csv"

# API configuration
API_RATE_LIMIT = 50  # Requests per minute
API_RETRY_DELAY = 1  # Delay between retries in seconds
