import os

def create_file(path, content):
    dirname = os.path.dirname(path)
    if dirname:
        os.makedirs(dirname, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def get_slug(text):
    return text.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace("*", "").replace("?", "")

# --- HIGH-FIDELITY APP SHELL ---
def app_shell(title, sidebar_idx, screen_content):
    return f"""<svg width="800" height="600" viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="600" fill="#f4f7f6" rx="15"/>
    <rect width="800" height="60" fill="#003366" rx="15 15 0 0"/>
    <circle cx="25" cy="30" r="6" fill="#ff5f56"/><circle cx="50" cy="30" r="6" fill="#ffbd2e"/><circle cx="75" cy="30" r="6" fill="#27c93f"/>
    <text x="400" y="38" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="16" fill="white">Fakturo Cloud - {title}</text>
    <rect x="0" y="60" width="180" height="540" fill="#ffffff" stroke="#e9ecef"/>
    {"".join([f'<rect x="15" y="{80 + i*40}" width="150" height="25" rx="6" fill="{"#e7f3ff" if i==sidebar_idx else "#f8f9fa"}"/>' for i in range(10)])}
    <rect x="200" y="80" width="580" height="500" rx="10" fill="white" stroke="#e9ecef"/>
    {screen_content}
</svg>"""

def conceptual_illustration(content, bg="#f8f9fa"):
    return f"""<svg width="800" height="500" viewBox="0 0 800 500" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="500" fill="{bg}" rx="20"/>
    <defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#0056b3"/><stop offset="100%" style="stop-color:#003366"/></linearGradient></defs>
    {content}
</svg>"""

# --- LISTS ---
feature_list = ["Invoicing Management", "Recurring Billing", "Client Database", "Product & Service Catalog", "Expense Tracking", "Estimates & Quotes", "Financial Reporting", "Multi-Currency Support", "Digital Signature Support", "Automatic Payment Reminders", "Tax Calculation & Summaries", "User Permissions & Roles", "Custom Template Designer", "Inventory Integration", "Client Portal"]
compliance_list = ["What is Verifactu", "AEAT Compliance Guide", "The Crea y Crece Law", "Electronic Signature Requirements", "QR Codes on Invoices", "Chained Hash Security", "Real-time AEAT Reporting", "VAT IVA Management in Spain", "Withholding Tax IRPF for Freelancers", "Electronic Invoicing for B2B", "Public Administration Invoicing FACe", "TicketBAI Integration", "SII Real-time Reporting", "AEAT Libro Registro"]
guide_list = ["How to Create Your First Invoice", "Setting Up Recurring Payments", "Managing Client Information", "Customizing Your Invoice Brand", "Importing Data from Excel", "Using Fakturo for Freelancers", "Fakturo for Small Retail Stores", "E-invoicing for Service Agencies", "Generating Year-End Reports", "Tracking Business Expenses on the Go", "Connecting to Stripe for Payments", "How to Handle Credit Notes", "Best Practices for Spanish Tax Compliance", "Using the Client Portal", "Exporting Data for Your Gestor"]
post_list = ["The Future of E-Invoicing in Europe", "Top 5 Mistakes in Spanish Invoicing", "How Digitalization Boosts Productivity", "Understanding the New AEAT Regulations", "Choosing the Right Software for Your SME", "The Impact of Verifactu on Small Businesses", "Preparing for the 2026 E-Invoicing Mandate"]

# --- ASSET GENERATION ---
svg_assets = {}
for i, f in enumerate(feature_list):
    slug = get_slug(f)
    svg_assets[slug] = app_shell(f, i % 10, f'<text x="490" y="310" text-anchor="middle" font-weight="bold" fill="#003366">{f.upper()} UI</text>')

for c in compliance_list:
    slug = get_slug(c)
    svg_assets[slug] = conceptual_illustration(f'<circle cx="400" cy="250" r="100" fill="none" stroke="#003366" stroke-width="10"/><text x="400" y="450" text-anchor="middle" font-weight="bold" font-size="24" fill="#003366">{c.upper()} MANDATE</text>')

for g in guide_list:
    slug = get_slug(g)
    svg_assets[slug] = app_shell(g, i % 10, f'<rect x="220" y="160" width="540" height="300" rx="8" fill="#f8f9fa"/><text x="490" y="310" text-anchor="middle" font-weight="bold" fill="#003366">{g.upper()} WALKTHROUGH</text>')

for p in post_list:
    slug = get_slug(p)
    svg_assets[slug] = conceptual_illustration(f'<rect x="200" y="150" width="400" height="200" fill="url(#g)" rx="10"/><text x="400" y="420" text-anchor="middle" font-weight="bold" font-size="24" fill="#003366">{p.upper()}</text>')

# --- MEGA CONTENT GENERATION ---
def gen_mega_content(title, category):
    return f"""
## The Definitive Guide to {title} for the Spanish Market

The **{title}** {category.lower()} within Fakturo represents a transformation of how business is conducted in Spain. As the AEAT pushes for total digital transparency, understanding {title} is critical.

### 1. Strategic Context
In the rapidly evolving landscape of Spanish business regulation, {title} is a strategic pillar of your organization's fiscal security.

### 2. Technical Workflow
Implementing {title} follows a professional, 4-stage lifecycle:
-   **Stage I: Profiling:** Adapt to your tax status (Autónomo/S.L.).
-   **Stage II: Execution:** Fakturo automates the technical heavy lifting.
-   **Stage III: Validation:** Fiscal pre-flight checks against BOE updates.
-   **Stage IV: Archiving:** Immutable 4-year data retention.

### 3. Business Advantages
-   **Risk Elimination:** Avoid heavy AEAT penalties.
-   **Operational Speed:** Reduce administrative overhead by 80%.
"""

# --- LAYOUTS ---
hugo_toml = """baseURL = "http://localhost:1313"\ntitle = "Fakturo"\ntheme = "fakturo"\n[[menu.main]]\nname = "Features"\nurl = "/features/"\nweight = 10\n[[menu.main]]\nname = "Compliance"\nurl = "/verifactu/"\nweight = 20\n[[menu.main]]\nname = "Guides"\nurl = "/guides/"\nweight = 30\n[[menu.main]]\nname = "Blog"\nurl = "/posts/"\nweight = 40"""

index_html = """{{ define "main" }}
<section class="hero bg-light"><div class="container hero-grid">
    <div class="hero-text">
        <span class="label">Expert System Architecture</span>
        <h1>Intelligent Invoice System Design for Spain.</h1>
        <p>A high-performance billing infrastructure engineered for the Spanish market. Fully compliant with Veri*factu* and AEAT standards.</p>
        <div class="btn-group"><a href="/features/" class="btn-primary">Explore Features</a></div>
    </div>
    <div class="hero-mockup"><img src="/images/mockup-hero.svg" class="float shadow"></div>
</div></section>

<section class="home-features bg-white"><div class="container">
    <div class="section-header"><h2>Professional Core Features</h2></div>
    <div class="feature-grid">
        {{ range first 6 (where .Site.RegularPages "Section" "features") }}
        <div class="feature-card shadow-sm"><img src="{{ .Params.image }}"><h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3><p>{{ .Summary }}</p></div>
        {{ end }}
    </div>
</div></section>

<section class="home-compliance bg-light"><div class="container">
    <div class="section-header"><h2>100% Spanish Compliance</h2></div>
    <div class="feature-grid">
        {{ range first 6 (where .Site.RegularPages "Section" "verifactu") }}
        <div class="feature-card shadow-sm"><img src="{{ .Params.image }}"><h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3><p>{{ .Summary }}</p></div>
        {{ end }}
    </div>
</div></section>

<section class="home-guides bg-white"><div class="container">
    <div class="section-header"><h2>Implementation Guides</h2></div>
    <div class="feature-grid">
        {{ range first 6 (where .Site.RegularPages "Section" "guides") }}
        <div class="feature-card shadow-sm"><img src="{{ .Params.image }}"><h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3><p>{{ .Summary }}</p></div>
        {{ end }}
    </div>
</div></section>

<section class="home-blog bg-light"><div class="container">
    <div class="section-header"><h2>Latest Insights</h2></div>
    <div class="feature-grid">
        {{ range first 3 (where .Site.RegularPages "Section" "posts") }}
        <div class="feature-card shadow-sm"><img src="{{ .Params.image }}"><h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3></div>
        {{ end }}
    </div>
</div></section>
{{ end }}"""

# --- EXECUTION ---
create_file('static/images/logo.svg', """<svg width="350" height="80" viewBox="0 0 350 80" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" style="stop-color:#0056b3"/><stop offset="100%" style="stop-color:#003366"/></linearGradient></defs><rect x="10" y="10" width="60" height="60" rx="15" fill="url(#g)"/><path d="M25 25 H45 V30 H32 V38 H42 V43 H32 V55 H25 Z" fill="white"/><path d="M45 45 L52 52 L65 35" stroke="#28a745" stroke-width="6" fill="none" stroke-linecap="round"/><text x="85" y="55" font-family="'Inter', sans-serif" font-weight="800" font-size="42" fill="#003366">Fakturo</text></svg>""")
create_file('hugo.toml', hugo_toml)
create_file('themes/fakturo/layouts/_default/baseof.html', """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>{{ .Title }} | Fakturo</title><link rel="stylesheet" href="/css/style.css"></head><body><header><nav class="container">
<div class="nav-left"><a href="/"><img src="/images/logo.svg" height="50"></a></div>
<div class="nav-right"><ul class="nav-links">{{ range .Site.Menus.main }}<li><a href="{{ .URL }}">{{ .Name }}</a></li>{{ end }}<li><a href="/signup/" class="btn-primary-sm">Sign Up</a></li></ul></div>
</nav></header><main>{{ block "main" . }}{{ end }}
{{ if ne .RelPermalink "/signup/" }}
<section class="global-cta bg-light"><div class="container text-center"><h2>Ready to transform your invoicing?</h2><div class="mt-30"><a href="/signup/" class="btn-primary">Start Your Free Trial</a></div></div></section>
{{ end }}
</main><footer><div class="container"><p>Built for Spain &copy; 2025.</p></div></footer></body></html>""")
create_file('themes/fakturo/layouts/index.html', index_html)
create_file('themes/fakturo/layouts/_default/list.html', """{{ define "main" }}<div class="container mt-40"><h1>{{ .Title }}</h1><div class="feature-grid">{{ range .Pages.ByTitle }}<div class="feature-card shadow-sm"><img src="{{ .Params.image }}"><h3><a href="{{ .RelPermalink }}">{{ .Title }}</a></h3></div>{{ end }}</div></div>{{ end }}""")
create_file('themes/fakturo/layouts/_default/single.html', """{{ define "main" }}<article class="container mt-40 pb-80"><h1>{{ .Title }}</h1><div class="img-wrap"><img src="{{ .Params.image }}"></div><div class="body">{{ .Content }}</div></article>{{ end }}""")
create_file('themes/fakturo/layouts/signup.html', """{{ define "main" }}<section class="signup-page bg-light"><div class="container small-container"><div class="signup-card shadow"><h1>Start with Fakturo</h1><form class="signup-form"><input type="email" placeholder="Email" required><button type="submit" class="btn-primary mt-20">Start Free Trial</button></form></div></div></section>{{ end }}""")
create_file('static/css/style.css', """body { font-family: sans-serif; margin: 0; line-height: 1.6; } .container { max-width: 1100px; margin: auto; padding: 20px; } .bg-light { background: #f8f9fa; border-top: 1px solid #eee; border-bottom: 1px solid #eee; } header { background: #fff; border-bottom: 1px solid #eee; padding: 15px 0; } nav { display: flex; justify-content: space-between; align-items: center; } .nav-links { display: flex; list-style: none; gap: 30px; margin: 0; } .nav-links a { text-decoration: none; color: #003366; font-weight: bold; } .btn-primary { background: #28a745; color: white; padding: 15px 35px; border-radius: 8px; text-decoration: none; font-weight: bold; border:none; cursor:pointer; } .btn-primary-sm { background: #003366; color: white; padding: 8px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; } .feature-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(340px, 1fr)); gap: 40px; margin-top: 40px; } .feature-card { border: 1px solid #eee; padding: 20px; border-radius: 15px; text-align: center; background: white; transition: 0.3s; } .feature-card img { width: 100%; border-bottom: 1px solid #eee; } .section-header { text-align: center; margin-top: 80px; } .hero-grid { display: grid; grid-template-columns: 1fr 1.2fr; gap: 60px; align-items: center; padding: 100px 0; } .shadow { box-shadow: 0 30px 60px rgba(0,0,0,0.1); } .shadow-sm { box-shadow: 0 5px 15px rgba(0,0,0,0.05); } .mt-40 { margin-top: 40px; } .mt-30 { margin-top: 30px; } .mt-20 { margin-top: 20px; } .pb-80 { padding-bottom: 80px; } .signup-page { padding: 100px 0; } .signup-card { background: white; padding: 50px; border-radius: 20px; } .small-container { max-width: 500px; } .img-wrap { background: #eee; padding: 40px; border-radius: 20px; margin-bottom: 40px; text-align: center; } .img-wrap img { width: 100%; border-radius: 10px; box-shadow: 0 20px 50px rgba(0,0,0,0.1); }""")

for f in feature_list:
    slug = get_slug(f)
    create_file(f'static/images/features/{slug}.svg', svg_assets[slug])
    create_file(f'content/features/{slug}.md', f'---\ntitle: "{f}"\nimage: "/images/features/{slug}.svg"\nsummary: "Automated {f.lower()} module."\n---\n{gen_mega_content(f, "Feature")}')

for c in compliance_list:
    slug = get_slug(c)
    create_file(f'static/images/verifactu/{slug}.svg', svg_assets[slug])
    create_file(f'content/verifactu/{slug}.md', f'---\ntitle: "{c}"\nimage: "/images/verifactu/{slug}.svg"\nsummary: "Official AEAT {c.lower()} documentation."\n---\n{gen_mega_content(c, "Compliance")}')

for g in guide_list:
    slug = get_slug(g)
    create_file(f'static/images/guides/{slug}.svg', svg_assets[slug])
    create_file(f'content/guides/{slug}.md', f'---\ntitle: "{g}"\nimage: "/images/guides/{slug}.svg"\nsummary: "Step-by-step for {g.lower()}."\n---\n{gen_mega_content(g, "Guide")}')

for p in post_list:
    slug = get_slug(p)
    create_file(f'static/images/posts/{slug}.svg', svg_assets[slug])
    create_file(f'content/posts/{slug}.md', f'---\ntitle: "{p}"\nimage: "/images/posts/{slug}.svg"\nsummary: "Expert analysis on {p.lower()}."\n---\n{gen_mega_content(p, "Blog Post")}')

create_file('content/signup.md', '---\ntitle: "Sign Up"\nlayout: "signup"\n---')
create_file('static/images/mockup-hero.svg', svg_assets["invoicing-management"])
print("Site generated with Features, Compliance, Guides, and Blog sections.")
