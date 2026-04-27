# from utils.actions import step_click, step_fill
# from utils.context import TEST_CONTEXT
# from utils.excel_report import save_excel
# from utils.config import BASE_URL
# from playwright.sync_api import sync_playwright
# import pytest

# @pytest.fixture(scope="session")
# def page():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context(storage_state="storage_state.json")

       

#         page = context.new_page()

#         page.goto(BASE_URL, timeout=60000)
#         page.wait_for_load_state("domcontentloaded")

#         yield page

#         context.close()
#         browser.close()


# def test_profile_dictionary_flow(page):

#     TEST_CONTEXT["application"] = "Profile Dictionary"
#     TEST_CONTEXT["micro_application"] = "Navigation"
#     TEST_CONTEXT["title"] = "Open Profile Dictionary from Dashboard"

#     # ================= DASHBOARD =================
#     page.goto(BASE_URL)
#     page.wait_for_selector("text=Profile Dictionary", timeout=20000)

#     profile_text = page.get_by_text("Profile Dictionary").first
#     step_click(profile_text, "Click Profile Dictionary Card")

#     go_to_app = page.get_by_role("button", name="Go to App").first
#     step_click(go_to_app, "Click Go to App")

#     # ================= PROFILE LIST VIEW =================
#     step_click(
#         page.get_by_role("button", name="Profile List View"),
#         "Open Profile List View"
#     )

#     # 🔥 WAIT FOR UI (IMPORTANT)
#     page.wait_for_timeout(3000)

#     # ================= ARROW BUTTON DEMO =================

#     # 👉 RIGHT ARROW
#     right_arrow = page.locator("button").filter(has=page.locator("svg")).nth(1)
#     if right_arrow.count() > 0:
#         step_click(right_arrow, "Click Right Arrow")
#         page.wait_for_timeout(1000)

#     # 👉 LEFT ARROW
#     left_arrow = page.locator("button").filter(has=page.locator("svg")).nth(0)
#     if left_arrow.count() > 0:
#         step_click(left_arrow, "Click Left Arrow")
#         page.wait_for_timeout(1000)

#     # ================= CLICK CENTER CARD =================
#     cards = page.locator("div:has-text('RMS Value')")

#     if cards.count() == 0:
#         raise Exception("❌ No graph cards found")

#     card = cards.nth(2)  # center visible card
#     card.scroll_into_view_if_needed()
#     step_click(card, "Click Center Graph Card")

#     # ================= CLICK EYE ICON =================
#     eye_icon = card.locator("button").last

#     step_click(eye_icon, "Open Full Screen Graph")

#     # ================= VALIDATION =================
#     page.wait_for_timeout(2000)

#     if not page.locator("text=Time").first.is_visible():
#         raise Exception("❌ Full screen graph not opened")

#     # ================= CLOSE FULL SCREEN =================
#     page.keyboard.press("Escape")
#     page.wait_for_timeout(1000)

#     # ================= REGISTER PROFILE =================
#     step_click(
#         page.get_by_role("button", name="Register Profile"),
#         "Open Register Profile"
#     )

#     # ================= FORM =================
#     step_fill(
#         page.get_by_role("textbox", name="e.g. Profile A"),
#         "Testing Profile",
#         "Profile Name"
#     )

#     step_fill(
#         page.get_by_role("textbox", name="Enter control class"),
#         "burst",
#         "Control Class"
#     )

#     step_fill(
#         page.get_by_role("textbox", name="Type here..."),
#         "1234567890",
#         "Input Data"
#     )

#     step_click(
#         page.get_by_role("button", name="Propose options"),
#         "Click Propose Options"
#     )

#     page.wait_for_timeout(2000)

#     # ================= CAROUSEL (OPTIONS) =================
#     right_arrow = page.locator(".absolute.right").first
#     if right_arrow.count() > 0:
#         right_arrow.click()
#         page.wait_for_timeout(1000)

#     # ================= SELECT OPTION B =================
#     option_b = page.locator("text=Option B").first
#     step_click(option_b, "Select Option B")

#     page.wait_for_timeout(1000)

#     # ================= SIMILARITY =================
#     check_similarity_btn = page.get_by_role("button", name="Check Similarity")

#     page.wait_for_function(
#         """() => {
#             const btns = [...document.querySelectorAll('button')];
#             const btn = btns.find(b => b.innerText.includes('Check Similarity'));
#             return btn && !btn.disabled;
#         }""",
#         timeout=15000
#     )

#     step_click(check_similarity_btn, "Check Similarity")

#     # ================= PREVIEW =================
#     preview_btn = page.get_by_role("button", name="Preview")
#     preview_btn.wait_for(state="visible", timeout=30000)

#     # 🔥 GRAPH INTERACTION
#     graph_points = page.locator(".highcharts-point")
#     if graph_points.count() > 0:
#         graph_points.first.click()

#     step_click(preview_btn, "Preview Profile")

#     step_click(
#         page.get_by_role("button", name="Confirm"),
#         "Confirm Profile"
#     )

#     if page.get_by_role("button", name="Yes").count() > 0:
#         step_click(
#             page.get_by_role("button", name="Yes"),
#             "Confirm Yes"
#         )


# def teardown_module(module):
#     save_excel()
import pytest
from playwright.sync_api import sync_playwright
from utils.config import BASE_URL
from utils.excel_report import save_excel


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        context = browser.new_context(
            storage_state="storage_state.json"
        )

        page = context.new_page()
        page.goto(BASE_URL)

        yield page

        context.close()
        browser.close()


# 🔥 ALWAYS SAVE EXCEL (even if test fails)
def pytest_sessionfinish(session, exitstatus):
    print("\n📊 Saving Excel Report...")
    save_excel()