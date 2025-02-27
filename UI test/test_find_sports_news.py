from playwright.sync_api import sync_playwright

def test_search_sports_articles():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 启动有头模式，方便观察
        page = browser.new_page()
        
        # 1️⃣ 进入 BBC 体育页面
        page.goto("https://www.bbc.co.uk/sport/football/scores-fixtures")

        # 2️⃣ 点击搜索按钮（此操作会跳转到新的搜索页面）
        search_button = page.locator("span.ssrcss-1lc3dkf-IconWrapper-SearchIconWrapper")
        search_button.click()

        # 3️⃣ 等待页面跳转并加载新的搜索输入框
        page.wait_for_url("https://www.bbc.co.uk/search*", timeout=5000)  # 等待 URL 变化
        page.wait_for_selector("input#searchInput", timeout=5000)  # 确保搜索框加载完成

        # 4️⃣ 输入 "sports" 并按回车
        search_input = page.locator("input#searchInput")  # 选择新的搜索框
        search_input.fill("sports")
        search_input.press("Enter")

        # 5️⃣ 等待搜索结果页面加载
        page.wait_for_selector(".ssrcss-1kkage4-PromoLink:link", timeout=5000)  # 确保结果加载
        
        # 6️⃣ 获取所有文章标题
        articles_locator = page.locator(".ssrcss-1kkage4-PromoLink:link")
        article_titles = articles_locator.all_text_contents()

        # 7️⃣ 输出结果
        if article_titles:
            print("🔍 搜索 'sports' 相关文章:")
            print(f"📌 第一篇文章标题: {article_titles[0]}")
            print(f"📌 最后一篇文章标题: {article_titles[-1]}")
        else:
            print("❌ 没有找到任何 'sports' 相关文章")

        browser.close()

# 直接运行
if __name__ == "__main__":
    test_search_sports_articles()