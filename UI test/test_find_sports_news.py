from playwright.sync_api import sync_playwright

def test_search_sports_articles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        
        # 1️⃣ Go to main page
        page.goto("https://www.bbc.co.uk/sport/football/scores-fixtures")

        # 2️⃣ Click search botton to next search page
        search_button = page.locator("span.ssrcss-1lc3dkf-IconWrapper-SearchIconWrapper")
        search_button.click()

        # 3️⃣ wait for page change
        page.wait_for_url("https://www.bbc.co.uk/search*", timeout=5000)  
        page.wait_for_selector("input#searchInput", timeout=5000)  

        # 4️⃣ input sports and enter
        search_input = page.locator("input#searchInput")  # chose the new search botton
        search_input.fill("sports")
        search_input.press("Enter")

        # 5️⃣ wait for page
        page.wait_for_selector(".ssrcss-1kkage4-PromoLink:link", timeout=5000)  # 
        
        # 6️⃣ get all titles 
        articles_locator = page.locator(".ssrcss-1kkage4-PromoLink:link")
        article_titles = articles_locator.all_text_contents()

        # 7️⃣ output [0] and [-1] , first and last one.
        if article_titles:
            print("🔍 search 'sports' related articles:")
            print(f"📌 the first article: {article_titles[0]}")
            print(f"📌 the last article: {article_titles[-1]}")
        else:
            print("❌ no articles related to 'sports' ")

        browser.close()

# run
if __name__ == "__main__":
    test_search_sports_articles()