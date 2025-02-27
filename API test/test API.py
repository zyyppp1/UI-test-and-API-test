import requests
import time

# API Endpoint
BASE_URL = "https://v6.exchangerate-api.com/v6/1fc80820c72b0163bc9c7536/latest/USD"

# Assumed expected currencies
EXPECTED_CURRENCIES = {
    "USD", "EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "HKD", "SGD",
    "NZD", "INR", "RUB", "BRL", "ZAR", "SEK", "NOK", "MXN"
}

# 1️⃣ **Verify the HTTP status is 200 and the response time is below 10 seconds**
def test_api_status():
    start_time = time.time()  # record start time
    response = requests.get(BASE_URL)
    response_time = time.time() - start_time  # calculate response time

    assert response.status_code == 200, f"❌ API request fail，Status code: {response.status_code}"
    assert response_time < 10, f"❌ API Response time: {response_time:.2f} s"
    
    print(f"✅ API Status code is {response.status_code}，response time: {response_time:.2f} 秒")

# 2️⃣ **Count the total number of currencies returned within the response**
def test_currency_count():
    response = requests.get(BASE_URL)
    json_data = response.json()
    
    assert "conversion_rates" in json_data, "❌ API response do not have 'conversion_rates' text"
    
    currency_count = len(json_data["conversion_rates"])
    assert currency_count > 0, f"❌ fail to get any currency: {currency_count}"
    
    print(f"✅ Total number of currencies returned within the response: {currency_count}")

# 3️⃣ **Verify the currency ‘GBP’ is shown within the response**
def test_gbp_exists():
    response = requests.get(BASE_URL)
    json_data = response.json()
    
    assert "conversion_rates" in json_data, "❌ API response lack 'conversion_rates' test"
    assert "GBP" in json_data["conversion_rates"], "❌ API response not find GBP currency"
    
    print(f"✅ GBP in response,the rate is : {json_data['conversion_rates']['GBP']}")

# 4️⃣ **Verify response has all the expected currencies**
def test_expected_currencies():
    response = requests.get(BASE_URL)
    json_data = response.json()

    assert "conversion_rates" in json_data, "❌ API response lack 'conversion_rates' text"
    
    missing_currencies = EXPECTED_CURRENCIES - set(json_data["conversion_rates"].keys())
    
    assert not missing_currencies, f"❌ API Response missing expected currencies: {missing_currencies}"
    
    print(f"✅ API Response have all expected currencies({len(EXPECTED_CURRENCIES)} kinds)")

# 5️⃣ **Run all tests**
def main():
    print("\n=== 🚀 run API test ===")
    try:
        test_api_status()
        test_currency_count()
        test_gbp_exists()
        test_expected_currencies()
        print("\n🎉 all API tests pass！")
    except AssertionError as e:
        print(f"\n❌ test fail: {e}")

# Run
if __name__ == "__main__":
    main()