import os
import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=True
    )
    yield browser
    browser.close()


@pytest.fixture
def page(browser, request):
    context = browser.new_context()

    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    page = context.new_page()

    yield page

    # If test failed, save trace
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("artifacts", exist_ok=True)

        page.screenshot(
            path=f"artifacts/{request.node.name}.png",
            full_page=True
        )

        context.tracing.stop(
            path=f"artifacts/{request.node.name}-trace.zip"
        )
    else:
        context.tracing.stop()

    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)