import requests
import time

# API 端点
BASE_URL = "https://v6.exchangerate-api.com/v6/1fc80820c72b0163bc9c7536/latest/USD"

# 预期的主要货币列表（部分示例）
EXPECTED_CURRENCIES = {
    "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "HKD", "SGD",
    "NZD", "INR", "RUB", "BRL", "ZAR", "SEK", "NOK", "MXN"
}

# 1️⃣ **测试 API 是否返回 200 OK，且响应时间低于 10 秒**
def test_api_status():
    start_time = time.time()  # 记录开始时间
    response = requests.get(BASE_URL)
    response_time = time.time() - start_time  # 计算响应时间

    assert response.status_code == 200, f"❌ API 请求失败，状态码: {response.status_code}"
    assert response_time < 10, f"❌ API 响应时间过长: {response_time:.2f} 秒"
    
    print(f"✅ API 返回 200 OK，响应时间: {response_time:.2f} 秒")

# 2️⃣ **测试 API 返回的货币数量**
def test_currency_count():
    response = requests.get(BASE_URL)
    json_data = response.json()
    
    assert "conversion_rates" in json_data, "❌ API 响应中缺少 'conversion_rates' 字段"
    
    currency_count = len(json_data["conversion_rates"])
    assert currency_count > 0, f"❌ API 返回的货币数量无效: {currency_count}"
    
    print(f"✅ API 返回的货币数量: {currency_count}")

# 3️⃣ **测试 GBP 是否存在于 API 响应**
def test_gbp_exists():
    response = requests.get(BASE_URL)
    json_data = response.json()
    
    assert "conversion_rates" in json_data, "❌ API 响应中缺少 'conversion_rates' 字段"
    assert "GBP" in json_data["conversion_rates"], "❌ API 响应中未找到 GBP 货币"
    
    print(f"✅ GBP 存在于 API 响应中，当前汇率: {json_data['conversion_rates']['GBP']}")

# 4️⃣ **测试 API 返回的货币列表是否完整**
def test_expected_currencies():
    response = requests.get(BASE_URL)
    json_data = response.json()

    assert "conversion_rates" in json_data, "❌ API 响应中缺少 'conversion_rates' 字段"
    
    missing_currencies = EXPECTED_CURRENCIES - set(json_data["conversion_rates"].keys())
    
    assert not missing_currencies, f"❌ API 响应中缺少以下货币: {missing_currencies}"
    
    print(f"✅ API 响应包含所有预期的货币 ({len(EXPECTED_CURRENCIES)} 种)")

# 5️⃣ **运行所有测试**
def main():
    print("\n=== 🚀 运行 API 测试 ===")
    try:
        test_api_status()
        test_currency_count()
        test_gbp_exists()
        test_expected_currencies()
        print("\n🎉 所有 API 测试通过！")
    except AssertionError as e:
        print(f"\n❌ 测试失败: {e}")

# 直接运行
if __name__ == "__main__":
    main()