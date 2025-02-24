import pytest

from httpsCheck import check_and_shorten_url

def test_https_url():
    url = "https://www.example.com/path"
    expected = "https://example.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_http_url():
    url = "http://www.example.com/path"
    expected = "http://example.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_no_www():
    url = "https://example.com/path"
    expected = "https://example.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_no_path():
    url = "https://www.example.com"
    expected = "https://example.com"
    result = check_and_shorten_url(url)
    assert result == expected

# def test_invalid_url():
#     url = "example.com"
#     expected = "http://example.com" or "https://example.com" or "www.example.com"
#     result = check_and_shorten_url(url)
#     assert result == expected

if "__name__" == "__main__":
    pytest.main()