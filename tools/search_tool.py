# code for search tool for dummy
from duckduckgo_search import DDGS

def search_tool(query: str, max_results: int = 3) -> str:
    with DDGS() as ddgs:
        results = ddgs.text(query)
        snippets = []
        for i, r in enumerate(results):
            snippets.append(f"{i+1}. {r['title']} - {r['body']}")
            if i + 1 >= max_results:
                break
        return "\n".join(snippets) if snippets else "No results found."
