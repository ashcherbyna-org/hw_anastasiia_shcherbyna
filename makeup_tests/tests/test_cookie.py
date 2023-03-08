def test_cookie(dashboard):
    dashboard.cookies.add("_tt_enable_cookie", ".makeup.com.ua", "1")
    get_cookies = dashboard.cookies.get("_tt_enable_cookie")
    assert get_cookies["name"] == "_tt_enable_cookie"
    assert get_cookies["domain"] == ".makeup.com.ua"
    assert get_cookies["value"] == "1"
