from playwright.sync_api import sync_playwright

def test_toggle_scorers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        
        # 1️⃣ Go to main page
        page.goto("https://www.bbc.co.uk/sport/football/scores-fixtures")

        # 2️⃣ Because when it's early morning the match page don't have the Show Scorers botton,so I need to do the test on previous day.
        date_button = page.locator("a[data-testid='datepicker-date-link-2025-02-26']")
        date_button.click()
        print("✅ 'Wed 26' botton clicked")

        # 3️⃣ wait for refresh
        page.wait_for_timeout(2000)  

        # 4️⃣ search "Show Scorers" botton
        show_scorers_button = page.locator("button:has-text('Show Scorers')")

        # 5️⃣ click "Show Scorers"
        show_scorers_button.click()
        print("✅ 'Show Scorers' clicked")

        # 6️⃣ wait for change
        page.wait_for_selector(".ssrcss-uq6ar7-KeyEventsAway.evc6ssb0", timeout=5000)
        page.wait_for_selector(".ssrcss-1gpz3ae-KeyEventsHome.evc6ssb1", timeout=5000)

        # 7️⃣ get info of Scorers for both sides
        away_scores = page.locator(".ssrcss-uq6ar7-KeyEventsAway.evc6ssb0")
        home_scores = page.locator(".ssrcss-1gpz3ae-KeyEventsHome.evc6ssb1")

        # make sure at least one was found
        assert away_scores.count() > 0, "❌ Away team score not found"
        assert home_scores.count() > 0, "❌ Home team score not found"

        # select the first one found
        away_score_visible = away_scores.nth(0).is_visible()
        home_score_visible = home_scores.nth(0).is_visible()

        assert away_score_visible, "❌ Away team score not be shown"
        assert home_score_visible, "❌ home team score not be shown"

        print("✅ the Scorers info was shown correctly!")

        # 8️⃣ Click “Hide Scorers” botton
        hide_scorers_button = page.locator("button:has-text('Hide Scorers')")
        hide_scorers_button.click()
        print("✅ 'Hide Scorers' clicked")

        # 9️⃣ wait for hide
        page.wait_for_timeout(2000)  # refresh

        # 🔟 identify if the Scorers info was hidden
        away_score_hidden = away_scores.nth(0).is_hidden()
        home_score_hidden = home_scores.nth(0).is_hidden()

        assert away_score_hidden, "❌ Away team score not be hidden"
        assert home_score_hidden, "❌ home team score not be hidden"

        print("✅ the Scorers info was hidden correctly! ")

        browser.close()

# Run
if __name__ == "__main__":
    test_toggle_scorers()