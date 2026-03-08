import re

def extract_fit_score(text):
    """Extract technical fit score from screening output."""
    match = re.search(r'(\d{1,3})\s*/\s*100', text)
    if match:
        return int(match.group(1))
    return 0


def get_hiring_recommendation(score):
    """Convert score to hiring recommendation."""
    
    if score >= 85:
        return "🔥 Strong Hire"
    elif score >= 70:
        return "✅ Hire"
    elif score >= 50:
        return "⚠️ Consider"
    else:
        return "❌ Reject"


def build_ranking_report(score):
    """Generate ranking + recommendation section."""
    
    recommendation = get_hiring_recommendation(score)

    report = f"""

----------------------------------------------------
📊 AI Hiring Decision Engine
----------------------------------------------------

Candidate Technical Score: {score}/100

Hiring Recommendation: {recommendation}

Decision Logic:
- 85+  → Strong Hire
- 70–84 → Hire
- 50–69 → Consider
- <50  → Reject

----------------------------------------------------
"""

    return report