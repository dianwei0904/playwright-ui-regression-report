from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context()
    page = context.new_page()

    test_name = request.node.name.replace("/", "_").replace(" ", "_")
    trace_path = Path("traces") / f"{test_name}.zip"

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    request.node.page = page

    yield page

    context.tracing.stop(path=trace_path)
    context.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = getattr(item, "page", None)

        if page:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            screenshot_name = f"{item.name}.png".replace("/", "_").replace(" ", "_")
            screenshot_path = screenshot_dir / screenshot_name

            page.screenshot(path=screenshot_path, full_page=True)