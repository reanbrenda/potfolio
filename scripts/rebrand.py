#!/usr/bin/env python3
"""Rebrand static Nuxt export: text and meta only."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

META = {
    "title": "Mukindia Labs — Software Development & AI Automation",
    "description": "Custom web apps and AI-powered workflows for NGOs and SMEs. React, Python, n8n, OpenAI API. Based in Spain, working globally.",
    "keywords": "NGO software development, AI automation Spain, impact dashboard, donor reporting, SME digitalisation, Kit Digital, n8n, LangChain, OpenAI API, React developer Spain",
    "author": "Mukindia Labs",
    "og_title": "Mukindia Labs — Software Development & AI Automation",
    "og_description": "Custom web apps and AI-powered workflows for NGOs and SMEs. Based in Spain, working globally.",
    "og_url": "https://mukindia.online",
    "twitter_title": "Mukindia Labs — Software Development & AI Automation",
    "twitter_description": "Custom web apps and AI automation for NGOs and SMEs. Spain-based, working globally.",
    "nuxt_title": "Mukindia Labs — Software Development & AI Automation",
}

GLOBAL_REPLACEMENTS = [
    ("Meskith", "Mukindia Labs"),
    ("meskith.com", "mukindia.online"),
    # meskith -> mukindia.labs applied only outside /images/ paths in apply_global
    ("MESKITH.AI", "Mukindia Labs"),
    ("Meskith-Logo-Light", "Mukindia-Labs-Logo-Light"),
    ("Meskith-Logo", "Mukindia-Labs-Logo"),
    ("Branding Studio in Kenya | Strategy, Design & AI", "Software Development & AI Automation"),
    ("Branding Studio in Kenya", "Software Development & AI Automation"),
    ("Branding Studio", "Software Development & AI Automation"),
    ("branding studio", "software development & AI automation"),
    ("Kenya-based", "Spain-based"),
    ("growth@meskith.com", "mukindia67@gmail.com"),
    ("growth@mukindia.labs", "mukindia67@gmail.com"),
    ("https://meskith.com", "https://mukindia.online"),
    ("http://meskith.com", "https://mukindia.online"),
    ("meskith-logo-light.png", "meskith-logo-light.png"),  # keep path; alt text updated above
    ("welcome to meskith ai", "welcome to Mukindia Labs AI"),
    ("AI Branding Response", "AI Assistant Response"),
]

ABOUT_TEXT = (
    "Mukindia Labs is the freelance practice of Brenda Mukindia — a software engineer and AI automation "
    "specialist with 5+ years of experience. I've built data systems and dashboards at UNICEF/Giga for school "
    "connectivity monitoring across multiple countries, developed applications for MSF East Africa supporting "
    "humanitarian field operations, and delivered AI automation and custom software for clients in Spain and "
    "internationally. MSc Front-End Development, Harbour Space University, Barcelona. BSc Information Technology, "
    "Jomo Kenyatta University. Based in Spain. Working globally."
)

ABOUT_BANNER_SUB = (
    't("span",{class:"opacity-70"},"We build"),'
    't("span",{class:"text-primary opacity-100"}," custom software "),'
    't("span",{class:"opacity-70"},"and AI automation that delivers measurable impact for NGOs and SMEs.")'
)

ABOUT_COUNTERS = [
    (
        "Spain & global delivery",
        "Based in Spain and working with NGOs and SMEs worldwide — from Barcelona to East Africa and beyond.",
    ),
    (
        "5+ years engineering experience",
        "Software development and AI automation across humanitarian, education, and commercial sectors.",
    ),
    (
        "UNICEF, MSF & SME clients",
        "Trusted on data systems, dashboards, field tools, and workflow automation for mission-driven organisations.",
    ),
]

SERVICES_ARRAY = """c=[{title:"Custom Software Development",description:"Beneficiary management systems, donor & grant tracking portals, volunteer management platforms, and programme monitoring tools for NGOs.",image:C,offset:-50},{title:"AI & Workflow Automation",description:"Automated donor communications, field data collection & processing, grant report generation, and n8n / Zapier / Make workflows.",image:I,offset:80},{title:"Impact Dashboards & Data Visualisation",description:"Live KPI dashboards, donor-facing impact reports, programme performance tracking, and UNICEF/EU/USAID standard reporting.",image:U,offset:200},{title:"Custom Business Software",description:"Internal operations tools, client & project management portals, custom CRM & sales pipelines, and inventory & admin systems for SMEs.",image:$t,offset:350},{title:"AI Workflow Automation",description:"Invoice & payment automation, customer onboarding sequences, AI chatbots & internal assistants, and OpenAI API & LangChain integrations.",image:C,offset:500},{title:"Business Intelligence & Analytics",description:"Power BI & custom dashboards, sales & revenue analysis, operations performance reports, and data-driven growth recommendations.",image:I,offset:650},{title:"AI SEO",description:"SEO-optimised website content, keyword strategy for NGO & SME niches, monthly blog posts, and Google visibility for mukindia.online.",image:U,offset:800}]"""

PROJECTS_JS = json.dumps(
    [
        {
            "id": 1,
            "project_title": "UNICEF Giga",
            "project_image": "/images/projects/project1.webp",
            "tag1": "React",
            "tag2": "D3.js",
            "description": "Built a React data ingestion application and interactive D3.js KPI dashboards for real-time school connectivity monitoring across multiple countries. Used by UNICEF country teams for donor reporting.\n\nStack: React, D3.js, Python, FastAPI, PostgreSQL, Azure\nLink: https://giga.global",
            "industry": "International Development",
            "scope": "Data systems & dashboards",
        },
        {
            "id": 2,
            "project_title": "MSF East Africa",
            "project_image": "/images/projects/project2.webp",
            "tag1": "Python",
            "tag2": "Django",
            "description": "Developed application software for Médecins Sans Frontières East Africa, building digital tools to support humanitarian field operations across the region.\n\nStack: Python, Django, REST APIs",
            "industry": "Humanitarian",
            "scope": "Field operations software",
        },
        {
            "id": 3,
            "project_title": "Oceandex Labs",
            "project_image": "/images/projects/project3.webp",
            "tag1": "n8n",
            "tag2": "OpenAI API",
            "description": "AI automation and custom data systems for a Spanish technology company, delivered under a formal subcontracting agreement.\n\nStack: n8n, OpenAI API, React, Python",
            "industry": "Technology",
            "scope": "AI automation & data systems",
        },
        {
            "id": 4,
            "project_title": "Armenian Robotics Alliance",
            "project_image": "/images/projects/project4.webp",
            "tag1": "React",
            "tag2": "n8n",
            "description": "Custom web development and workflow automation tooling for an international robotics organisation.\n\nStack: React, Python, n8n",
            "industry": "Robotics",
            "scope": "Web & workflow automation",
        },
    ],
    separators=(",", ":"),
)


def apply_global(text: str) -> str:
    for old, new in GLOBAL_REPLACEMENTS:
        text = text.replace(old, new)
    # Domain-style meskith without breaking image filenames
    text = re.sub(r"(?<!/images/)meskith", "mukindia.labs", text)
    # branding phrase replacements (case-sensitive patterns)
    branding_phrases = [
        (r"\bbrand identity\b", "software development"),
        (r"\bBrand Identity\b", "Custom Software Development"),
        (r"\bbrand strategy\b", "AI automation"),
        (r"\bBrand strategy\b", "AI automation"),
        (r"\bbrand strategy\b", "AI automation"),
        (r"\blogo design\b", "software development"),
        (r"\bLogo design\b", "Software development"),
        (r"\bbrand architects\b", "software engineers"),
        (r"\bBrand architects\b", "Software engineers"),
    ]
    for pat, repl in branding_phrases:
        text = re.sub(pat, repl, text, flags=re.IGNORECASE)
    return text


def update_html_meta(path: Path, content: str) -> str:
    content = apply_global(content)
    content = re.sub(
        r"<title>[^<]*</title>",
        f"<title>{META['title']}</title>",
        content,
        count=1,
    )
    content = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{META["description"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta name="keywords" content="[^"]*"',
        f'<meta name="keywords" content="{META["keywords"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta name="author" content="[^"]*"',
        f'<meta name="author" content="{META["author"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta property="og:title" content="[^"]*"',
        f'<meta property="og:title" content="{META["og_title"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta property="og:description" content="[^"]*"',
        f'<meta property="og:description" content="{META["og_description"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta property="og:url" content="[^"]*"',
        f'<meta property="og:url" content="{META["og_url"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta name="twitter:title" content="[^"]*"',
        f'<meta name="twitter:title" content="{META["twitter_title"]}"',
        content,
        count=1,
    )
    content = re.sub(
        r'<meta name="twitter:description" content="[^"]*"',
        f'<meta name="twitter:description" content="{META["twitter_description"]}"',
        content,
        count=1,
    )
    nuxt_payload = '{"title":"' + META["nuxt_title"].replace("\\", "\\\\").replace('"', '\\"') + '"}'
    content = re.sub(
        r'\{"title":"[^"]*"\}',
        nuxt_payload,
        content,
        count=1,
    )
    return content


def patch_dthlv(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = apply_global(t)

    # Hero subheading
    t = t.replace(
        't("span",{class:"opacity-70"},"We create"),t("span",{class:"text-primary opacity-100"}," high-performing "),t("span",{class:"opacity-70"},"digital designs that elevate brands and enhance conversions.")',
        't("span",{class:"opacity-70"},"Custom web apps and AI-powered workflows for NGOs and SMEs — built by "),t("span",{class:"text-primary opacity-100"},"Mukindia Labs"),t("span",{class:"opacity-70"},".")',
    )
    t = t.replace(
        't("h1",{class:"text-white text-h1 font-weight-bold mb-0"},"MESKITH.AI",-1)',
        't("h1",{class:"text-white text-h1 font-weight-bold mb-0"},"Software that works. Automation that scales.",-1)',
    )
    t = t.replace('to:"/ai"', 'to:"/projects"', 1)
    t = t.replace("See Our Work", "See our work")

    # Stats
    t = t.replace("Presence in Global Markets  ", "NGO & SME clients worldwide  ")
    t = t.replace("In Strategic Brand Value ", "Years of engineering experience ")
    t = t.replace("Trusted Brand Collaborations", "Humanitarian & commercial delivery")
    t = t.replace(
        "High quality web design solutions you can trust.",
        "Custom software and AI automation you can trust.",
    )
    t = t.replace(
        "When selecting a design studio, it's essential to consider its reputation, experience, and the specific needs of your project.",
        "When selecting a development partner, consider technical depth, sector experience, and the specific needs of your NGO or SME.",
    )

    # Services section
    t = re.sub(
        r"c=\[\{title:\"Brand Identity\".*?\{title:\"Workshops & Training\".*?\}\]",
        SERVICES_ARRAY,
        t,
        count=1,
        flags=re.DOTALL,
    )
    t = t.replace(
        'subtitle:"We blend strategy, design, and AI to build brands people feel, remember, and become."',
        'subtitle:"Software development and AI automation for NGOs and SMEs — from dashboards to workflow automation."',
    )
    t = t.replace("Stories from clients", "Client stories")
    t = t.replace(
        "Real experiences, genuine feedback—discover how our creative solutions have transformed brands and elevated businesses.",
        "Real experiences from NGOs and SMEs — discover how custom software and AI automation delivered measurable impact.",
    )
    t = t.replace(
        "Working with Meskith felt like a true partnership. What stood out most was how available and responsive the team was. ",
        "Working with Mukindia Labs felt like a true partnership. What stood out most was the depth of technical expertise and reliability. ",
    )

    path.write_text(t, encoding="utf-8")


def patch_about(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = apply_global(t)

    t = t.replace(
        't("span",{class:"opacity-70"},"We craft"),t("span",{class:"text-primary opacity-100"}," innovative digital "),t("span",{class:"opacity-70"},"designs that amplify brand identity and drive meaningful results")',
        ABOUT_BANNER_SUB,
    )

    old_about = (
        't("p",{class:"text-subtitle-1"}," It’s a canvas for your creativity. It’s your opportunity to transform bold ideas into dynamic, interactive experiences. Your work can shape identities, tell compelling stories, or spark meaningful change. As the digital landscape grows, so do the possibilities. And whether you thrive working remotely or in a buzzing agency space, the thrill of seeing your vision come to life is unmatched. "),t("p",{class:"text-subtitle-1"},\' At Meskith, we bring ideas to life through a range of services: branding, web development, agency solutions, content creation, SaaS, and motion & 3D modeling. As a web designer, you merge artistry and technology to craft "digital experiences" that inform, captivate and inspire. Every day brings something new — one moment you’re sketching innovative concepts, the next you’re turning them into seamless, responsive designs. Web design keeps you pushing boundaries and creating at every turn! \')'
    )
    # fuzzy match - read file and replace paragraphs individually
    t = re.sub(
        r't\("p",\{class:"text-subtitle-1"\}," It[^"]*"\),t\("p",\{class:"text-subtitle-1"\},[^)]+\)',
        f't("p",{{class:"text-subtitle-1"}}," {ABOUT_TEXT} ")',
        t,
        count=1,
    )

    counters_old = [
        (
            "Presence in Global Markets",
            "Expanding our reach from Kenya to the world — Meskith proudly serves clients across 5+ countries, delivering localized creativity with global impact.",
        ),
        (
            "In Strategic Brand Value ",
            "Driving growth through impactful brand strategy, design, and creative execution — empowering clients to stand out and scale meaningfully.",
        ),
        (
            "Trusted brand collaborations",
            "Partnering with visionary brands to craft timeless identities, engaging experiences, and strong digital footprints",
        ),
    ]
    for title, desc in counters_old:
        t = t.replace(desc, ABOUT_COUNTERS[counters_old.index((title, desc))][1])
        t = t.replace(f'title:"{title}"', f'title:"{ABOUT_COUNTERS[counters_old.index((title, desc))][0]}"')

    marquee = [
        "Custom Software",
        "AI Automation",
        "Impact Dashboards",
        "n8n Workflows",
        "React Apps",
        "Python APIs",
        "OpenAI Integrations",
        "NGO Systems",
    ]
    marquee_block = ",".join(f'{{title:"{m}"}}' for m in marquee * 2)
    t = re.sub(
        r'd=\[\{title:"Branding"\}.*?\{title:"Photography"\}\]',
        f"d=[{marquee_block}]",
        t,
        count=1,
        flags=re.DOTALL,
    )

    path.write_text(t, encoding="utf-8")


def patch_footer(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = apply_global(t)
    t = t.replace(" Let's Build something together? ", " Work with Mukindia Labs ")
    t = t.replace("Victoria Plaza, 8th Floor, Westlands - Nairobi ", "Based in Spain, working globally. ")
    t = t.replace('href:"tel:+254 700 300772"', 'href:"mailto:mukindia67@gmail.com"')
    t = t.replace("+254 700 300772 ", "")
    t = re.sub(
        r'" © 2023 - "\+x\(new Date\(\)\.getFullYear\(\)\)\+" Meskith "',
        '" © 2025 Mukindia Labs. All rights reserved. "',
        t,
    )
    t = t.replace(
        '" © 2023 - "+x(new Date().getFullYear())+" Mukindia Labs "',
        '" © 2025 Mukindia Labs. All rights reserved. "',
    )
    if "mukindia.online" not in t and "mailto:mukindia67@gmail.com" in t:
        t = t.replace(
            'o[2]||(o[2]=c("Based in Spain, working globally. ",-1))',
            'o[2]||(o[2]=c("Based in Spain, working globally. ",-1)),t(n,{href:"https://mukindia.online",target:"_blank",class:"d-flex ga-3 align-center text-white text-decoration-none hover-primary-link"},{default:e(()=>[t(a(u),{icon:"material-symbols:arrow-outward",height:"24",class:"text-primary"}),c(" mukindia.online ",-1)]),_:1})',
        )
    path.write_text(t, encoding="utf-8")


def patch_contact(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = apply_global(t)
    t = t.replace('title:"Contact us"', 'title:"Work with Mukindia Labs"')
    t = t.replace(
        " Let's collaborate and create something amazing! Tell us about your project—We're all ears. ",
        " Available for NGO and SME projects. Based in Spain, working globally. ",
    )
    t = t.replace('title:"Get in touch",subtitle:""', 'title:"Work with Mukindia Labs",subtitle:"Available for NGO and SME projects. Based in Spain, working globally. Email: mukindia67@gmail.com"')
    path.write_text(t, encoding="utf-8")


def patch_contact_banner(path: Path) -> None:
    t = path.read_text(encoding="utf-8")
    t = apply_global(t)
    t = t.replace(
        't("span",{class:"opacity-70"},"Ready to"),t("span",{class:"text-primary opacity-100"}," start something "),t("span",{class:"opacity-70"},"great? Reach out we’d love to hear from you.")',
        't("span",{class:"opacity-70"},"Available for "),t("span",{class:"text-primary opacity-100"},"NGO and SME projects"),t("span",{class:"opacity-70"},". Based in Spain, working globally.")',
    )
    t = t.replace('" Contact "', '" Work with Mukindia Labs "')
    path.write_text(t, encoding="utf-8")


def patch_projects_store(path: Path) -> None:
    projects = PROJECTS_JS
    new_store = f'''import{{d as o}}from"./7cNSa_p_.js";const PROJECTS={projects};const a=o("project",{{state:()=>({{projectGrid:PROJECTS,selectedProjects:[]}}),getters:{{getPosts(t){{return t.projectGrid}}}},actions:{{async fetchPosts(){{this.projectGrid=PROJECTS}},async fetchPost(t){{const e=PROJECTS.find(p=>p.project_title.toLowerCase().replace(/ /g,"-").replace(/[^\\w-]+/g,"")===t||p.project_title.toLowerCase()===t.replace(/-/g," ").toLowerCase());this.selectedProjects=e?[e]:[]}}}}}});export{{a as u}};'''
    path.write_text(new_store, encoding="utf-8")


def patch_services_page(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    if "Services page" not in content:
        return
    new = '''import{Y as e,c as n,o,m as t,J as a,K as i,a2 as r}from"./7cNSa_p_.js";const s={};function l(c,d){return o(),n("div",{class:"bg-darkgray"},[t("div",{class:"container-lg py-lg-16 py-8"},[t("h1",{class:"text-h2 text-dark mb-6"},"Services"),t("h2",{class:"text-h4 text-dark mb-3"},"For NGOs"),t("p",{class:"text-subtitle-1 text-dark opacity-70 mb-6"},"Custom Software Development — Beneficiary management, donor & grant tracking, volunteer platforms, programme monitoring. AI & Workflow Automation — Donor communications, field data, grant reports, n8n/Zapier/Make. Impact Dashboards — Live KPIs, donor reports, UNICEF/EU/USAID reporting."),t("h2",{class:"text-h4 text-dark mb-3"},"For SMEs"),t("p",{class:"text-subtitle-1 text-dark opacity-70 mb-6"},"Custom Business Software — Operations tools, CRM, inventory. AI Workflow Automation — Invoicing, onboarding, chatbots, OpenAI & LangChain. Business Intelligence — Power BI dashboards, sales & operations analytics."),t("h2",{class:"text-h4 text-dark mb-3"},"Add-on"),t("p",{class:"text-subtitle-1 text-dark opacity-70"},"AI SEO — SEO content, keyword strategy, monthly blogs, Google visibility for mukindia.online.")])],64)}const _=e(s,[["render",l]]);export{_ as default};'''
    path.write_text(new, encoding="utf-8")


def main() -> None:
    for html in ROOT.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        html.write_text(update_html_meta(html, text), encoding="utf-8")

    for pattern in ("*.js", "*.php", "*.json", "*.webmanifest"):
        for f in ROOT.rglob(pattern):
            if "scripts" in f.parts:
                continue
            text = apply_global(f.read_text(encoding="utf-8"))
            f.write_text(text, encoding="utf-8")

    patch_dthlv(ROOT / "_nuxt" / "DThLVr5V.js")
    patch_about(ROOT / "_nuxt" / "CILV4l7I.js")
    patch_footer(ROOT / "_nuxt" / "kKI9DFHi.js")
    patch_contact(ROOT / "_nuxt" / "l2fanLi7.js")
    patch_contact_banner(ROOT / "_nuxt" / "DleifJR_.js")
    patch_projects_store(ROOT / "_nuxt" / "Lvp5gbRu.js")
    patch_services_page(ROOT / "_nuxt" / "DWDePBCL.js")

    manifest = ROOT / "site.webmanifest"
    if manifest.exists():
        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["name"] = "Mukindia Labs"
        data["short_name"] = "Mukindia"
        manifest.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    contact_php = ROOT / "contact.php"
    if contact_php.exists():
        t = contact_php.read_text(encoding="utf-8")
        t = t.replace("growth@meskith.com", "mukindia67@gmail.com").replace(
            "Meskith", "Mukindia Labs"
        )
        contact_php.write_text(t, encoding="utf-8")

    print("Rebrand complete.")


if __name__ == "__main__":
    main()
