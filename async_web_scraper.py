import asyncio
import logging
from typing import List, Optional
from contextlib import asynccontextmanager
import aiohttp
from aiohttp import ClientSession
from bs4 import BeautifulSoup

# Configure logging for professional output
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

# Custom decorator for timing async functions
def time_execution(func):
    async def wrapper(*args, **kwargs):
        start_time = asyncio.get_event_loop().time()
        result = await func(*args, **kwargs)
        elapsed = asyncio.get_event_loop().time() - start_time
        logger.info(f"{func.__name__} took {elapsed:.2f} seconds")
        return result
    return wrapper

# Async context manager for HTTP session
@asynccontextmanager
async def managed_session():
    async with aiohttp.ClientSession() as session:
        try:
            yield session
        except Exception as e:
            logger.error(f"Session error: {e}")
            raise

class WebScraper:
    """A professional async web scraper with error handling and logging."""
m/.results
    def __init__(self, urls: List[str], max_concurrency: int = 5):
        self.urls = urls
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.results = []

    async def fetch_page(self, session: ClientSession, url: str) -> Optional[str]:
        """Fetch a single page with semaphore to limit concurrency."""
        async with self.semaphore:
            try:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        return await response.text()
                    logger.warning(f"Failed to fetch {url}: Status {response.status}")
                    return None
            except Exception as e:
                logger.error(f"Error fetching {url}: {e}")
                return None

    @time_execution
    async def scrape(self) -> List[dict]:
        """Scrape all URLs and extract page titles."""
        async with managed_session() as session:
            tasks = [self.fetch_page(session, url) for url in self.urls]
            pages = await asyncio.gather(*tasks, return_exceptions=True)

            for url, page in zip(self.urls, pages):
                if isinstance(page, str):
                    soup = BeautifulSoup(page, "html.parser")
                    title = soup.title.string.strip() if soup.title else "No title"
                    self.results.append({"url": url, "title": title})
                else:
                    self.results.append({"url": url, "title": None})

            return self.results

async def main():
    # Example usage
    urls = [
        "https://python.org",
        "https://aiohttp.readthedocs.io",
        "https://www.example.com",
    ]
    scraper = WebScraper(urls)
    results = await scraper.scrape()

    for result in results:
        logger.info(f"URL: {result['url']} | Title: {result['title']}")

if __name__ == "__main__":
    asyncio.run(main())
