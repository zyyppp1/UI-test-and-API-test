from playwright.sync_api import sync_playwright

def test_today_football_teams():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 
        page = browser.new_page()
        page.goto("https://www.bbc.co.uk/sport/football/scores-fixtures")

        try:
            # Wait for team name appear
            page.wait_for_selector("span.ssrcss-1p14tic-DesktopValue", timeout=5000)
        except:
            team_names = []
        else:
            # Get all team names
            teams_locator = page.locator("span.ssrcss-1p14tic-DesktopValue")
            team_names = [name.strip() for name in teams_locator.all_text_contents()]

        # Output
        if team_names:
            print("Football team that have a match today:")
            for name in team_names:
                print(name)
        else:
            print("No football match today。")

        browser.close()

# Run 
if __name__ == "__main__":
    test_today_football_teams()