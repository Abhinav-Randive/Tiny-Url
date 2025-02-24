import pytest

from httpsCheck import check_and_shorten_url

def test_https_url():
    url = "https://chatgpt.com/c/67bcbbb3-6ab0-800c-892f-73195ee0cae5"
    expected = "https://chatgpt.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_http_url():
    url = "http://www.example.com/path"
    expected = "http://example.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_no_www():
    url = "https://reddit.com/r/webdev/comments/10k3bhq/why_did_we_need_www_for_urls_and_why_dont_we_need/.com/path"
    expected = "https://reddit.com"
    result = check_and_shorten_url(url)
    assert result == expected

def test_no_path():
    url = "https://www.youtube.com"
    expected = "https://youtube.com"
    result = check_and_shorten_url(url)
    assert result == expected

# def test_invalid_url():
#     url = "example.com"
#     expected = "http://example.com" or "https://example.com" or "www.example.com"
#     result = check_and_shorten_url(url)
#     assert result == expected

if "__name__" == "__main__":
    pytest.main()