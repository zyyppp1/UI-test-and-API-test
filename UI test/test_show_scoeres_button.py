from playwright.sync_api import sync_playwright

def test_toggle_scorers():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 启动可视化模式
        page = browser.new_page()
        
        # 1️⃣ 进入 BBC 体育 Scores & Fixtures 页面
        page.goto("https://www.bbc.co.uk/sport/football/scores-fixtures")

        # 2️⃣ 选择日期：点击 "Wed 26"（2025-02-26）
        date_button = page.locator("a[data-testid='datepicker-date-link-2025-02-26']")
        date_button.click()
        print("✅ 'Wed 26' 日期按钮已点击")

        # 3️⃣ 等待页面加载新的数据
        page.wait_for_timeout(2000)  # 等待页面更新

        # 4️⃣ 查找 "Show Scorers" 按钮
        show_scorers_button = page.locator("button:has-text('Show Scorers')")

        # 5️⃣ 点击 "Show Scorers"
        show_scorers_button.click()
        print("✅ 'Show Scorers' 按钮已点击")

        # 6️⃣ 等待比分信息加载
        page.wait_for_selector(".ssrcss-uq6ar7-KeyEventsAway.evc6ssb0", timeout=5000)
        page.wait_for_selector(".ssrcss-1gpz3ae-KeyEventsHome.evc6ssb1", timeout=5000)

        # 7️⃣ 获取特定比赛的比分元素
        away_scores = page.locator(".ssrcss-uq6ar7-KeyEventsAway.evc6ssb0")
        home_scores = page.locator(".ssrcss-1gpz3ae-KeyEventsHome.evc6ssb1")

        # 确保至少有一个比分元素
        assert away_scores.count() > 0, "❌ 未找到客队比分"
        assert home_scores.count() > 0, "❌ 未找到主队比分"

        # 选择 **第一个比赛的比分**
        away_score_visible = away_scores.nth(0).is_visible()
        home_score_visible = home_scores.nth(0).is_visible()

        assert away_score_visible, "❌ 客队比分未能显示"
        assert home_score_visible, "❌ 主队比分未能显示"

        print("✅ 比分信息正确显示")

        # 8️⃣ 点击 “Hide Scorers” 按钮
        hide_scorers_button = page.locator("button:has-text('Hide Scorers')")
        hide_scorers_button.click()
        print("✅ 'Hide Scorers' 按钮已点击")

        # 9️⃣ 等待比分信息隐藏
        page.wait_for_timeout(2000)  # 等待页面更新

        # 🔟 断言比分信息是否隐藏
        away_score_hidden = away_scores.nth(0).is_hidden()
        home_score_hidden = home_scores.nth(0).is_hidden()

        assert away_score_hidden, "❌ 客队比分未能隐藏"
        assert home_score_hidden, "❌ 主队比分未能隐藏"

        print("✅ 比分信息正确隐藏")

        browser.close()

# 直接运行
if __name__ == "__main__":
    test_toggle_scorers()