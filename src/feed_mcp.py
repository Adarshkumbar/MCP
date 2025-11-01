import os
import sys

# Ensure project root (one level above src/) is on sys.path so local
# packages placed alongside `src/` (such as our development shim `fastmcp`)
# can be imported when running `python src\feed_mcp.py` from the repo root.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastmcp import FastMCP
import feedparser

mcp = FastMCP(name="ADKM Feed Searcher", version="1.0")


@mcp.tool()
# def fcc_news_search(query: str, max_results: int = 5) -> str:
#     """
#     Search for news articles related to the Chainsaw Man Anime and Reze Arc Movie
#     using Google News RSS feed.
#     """
#     feed_url = "https://news.google.com/rss/search?q=Chainsaw+Man+Anime"
#     feed = feedparser.parse(feed_url)

#     results = []
#     for entry in feed.entries:
#         if (
#             query.lower() in entry.title.lower()
#             or query.lower() in entry.summary.lower()
#         ):
#             results.append(
#                 f"Title: {entry.title}\nLink: {entry.link}\nSummary: {entry.summary}\n"
#             )
#             if len(results) >= max_results:
#                 break

#     if not results:
#         return "No relevant news articles found."

#     return "\n".join(results)
def fcc_news_search(query: str, max_results: int = 5) -> str:
    """
    Search for news articles related to the Chainsaw Man Anime and Reze Arc Movie
    using multiple RSS feeds (Google News and Anime News Network).
    Returns debug info if no results are found.
    """
    feeds = [
        "https://news.google.com/rss/search?q=Chainsaw+Man+Anime"
    ]
    results = []
    debug_titles = []
    query_lower = query.lower()
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            title = getattr(entry, "title", "")
            summary = getattr(entry, "summary", "")
            debug_titles.append(title)
            if query_lower in title.lower() or query_lower in summary.lower():
                results.append(
                    f"Title: {title}\nLink: {getattr(entry, 'link', '')}\nSummary: {summary}\n"
                )
                if len(results) >= max_results:
                    break
        if len(results) >= max_results:
            break

    if not results:
        debug_info = f"No relevant news articles found.\nSearched titles: {debug_titles[:10]}..."
        return debug_info

    return "\n".join(results)


@mcp.tool()
def fcc_youtube_search(query: str, max_results: int = 3):
    """Search FreeCodeCamp Youtube channel via RSS by title

    Returns a list of dicts with keys `title` and `url`, or
    `[{"message": "No videos found"}]` when there are no matches.
    """
    feed = feedparser.parse(
        "https://www.youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ"
    )

    results = []
    query_lower = query.lower()
    for entry in feed.entries:
        # feedparser entries behave like dicts and objects; use .get when
        # available to match the screenshot implementation.
        title = entry.get("title", "") if hasattr(entry, "get") else getattr(entry, "title", "")
        if query_lower in title.lower():
            url = entry.get("link", "") if hasattr(entry, "get") else getattr(entry, "link", "")
            results.append({"title": title, "url": url})
        if len(results) >= max_results:
            break  # unlikely to occur but keeps behavior bounded

    return results or [{"message": "No videos found"}]

if __name__ == "__main__":
    mcp.run()  #STDIO