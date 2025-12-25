import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='wikipedia-client/1.0', language='en')

def get_page(title, section_limit=5):
    """
    Fetch a Wikipedia page and its top sections.
    """
    page = wiki.page(title)
    if not page.exists():
        return None
    
    # Collect top-level sections
    sections = {s.title: s.text[:1000] for s in page.sections[:section_limit]}

    return {
        "title": page.title,
        "summary": page.summary[:500],  # short summary
        "sections": sections,
        "full_text": page.text[:5000]   # optional: truncated full text
    }