import pytest

from pages.login_page import LoginPage
from test_data.login_cases import LOGIN_CASES


@pytest.mark.parametrize(
    "case",
    LOGIN_CASES,
    ids=[case["case_id"] for case in LOGIN_CASES],
)
def test_login_cases(page, case):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(case["username"], case["password"])

    if case["expected_result"] == "success":
        assert login_page.get_page_title() == case["expected_text"]

    if case["expected_result"] == "error":
        assert login_page.get_error_message() == case["expected_text"]