# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://103.204.95.218:7050/")
#     page.locator(".gradient-input").first.click()
#     page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
#     page.locator(".flex.flex-col.gap-\\[2vh\\] > div:nth-child(2)").click()
#     page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
#     page.get_by_role("button", name="LOGIN").click()
#     page.locator("div").filter(has_text=re.compile(r"^Profile Dictionary$")).click()
#     page.get_by_role("button", name="Go to App").first.click()
#     page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]").click()
#     page.locator(".w-\\[1\\.5vw\\]").first.click()
#     page.locator(".w-\\[2vw\\].h-\\[2vw\\].flex.items-center.justify-center.rounded-\\[0\\.5vw\\].bg-\\[linear-gradient\\(90deg\\,\\#0D405D_0\\%\\,\\#316D90_100\\%\\)\\].cursor-pointer").click()
#     page.get_by_role("button", name="Back").click()
#     page.get_by_role("button", name="Register Profile").click()
#     page.get_by_role("textbox", name="e.g. Profile A").click()
#     page.get_by_role("textbox", name="e.g. Profile A").fill("testing")
#     page.get_by_role("textbox", name="Enter control class").click()
#     page.get_by_role("textbox", name="Enter control class").fill("burst")
#     page.get_by_role("textbox", name="Type here...").click()
#     page.get_by_role("textbox", name="Type here...").fill("123456789000")
#     page.get_by_role("button", name="Propose options").click()
#     page.locator("div:nth-child(2) > .flex.items-center.gap-\\[0\\.6vw\\] > .w-\\[0\\.9vw\\]").click()
#     page.locator(".absolute.right-\\[1vw\\].z-50").click()
#     page.locator(".absolute.right-\\[1vw\\].z-50").click()
#     page.get_by_role("button", name="Check Similarity").click()
#     # page.locator("div:nth-child(2) > .w-\\[2vw\\]").first.click()
#     # page.locator("div:nth-child(2) > .w-\\[2vw\\]").first.click()
    
#     page.get_by_role("button", name="Preview").click()
    
#     page.get_by_role("button", name="Confirm").click()
#     page.get_by_role("button", name="Cancel").click()
#     page.get_by_role("button", name="Confirm").click()
#     page.get_by_role("button", name="Yes").click()
#     page.get_by_role("button", name="User Generated Profiles").click()
#     page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]").click()
#     page.locator(".w-\\[2vw\\].h-\\[2vw\\].flex.items-center.justify-center.rounded-\\[0\\.5vw\\].bg-\\[linear-gradient\\(90deg\\,\\#0D405D_0\\%\\,\\#316D90_100\\%\\)\\].cursor-pointer").click()
#     page.get_by_role("button", name="Back").click()
#     page.get_by_role("button").first.click()
#     page.locator("div").filter(has_text=re.compile(r"^Power Monitoring$")).first.click()
#     page.get_by_role("button", name="Go to App").nth(2).click()
#     page.locator("div").filter(has_text=re.compile(r"^A3$")).click()
#     page.locator("div").filter(has_text=re.compile(r"^A4$")).click()
#     page.get_by_role("button", name="Isolated System View (Single").click()
#     page.get_by_role("button", name="A1").click()
#     page.get_by_text("A4", exact=True).click()
#     page.get_by_role("button", name="Zoom").click()
#     page.get_by_role("button", name="Close").click()
#     page.get_by_text("35%").click()
#     page.get_by_text("25%").click()
#     page.get_by_text("PeakPeak").click()
#     page.locator(".highcharts-point.highcharts-color-0").first.click()
#     page.get_by_role("button", name="Distributed System View (").click()
#     page.get_by_role("heading", name="Deployment Status").click()
#     # page.locator(".highcharts-series.highcharts-series-6 > .highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-series.highcharts-series-6 > .highcharts-point.highcharts-point-hover").click()
#     page.wait_for_timeout(2000)
#     page.locator(".absolute.left-\\[0\\.15vw\\]").click()
#     page.wait_for_timeout(2000)
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     page.get_by_role("button", name="Power Quality Analytics Power").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-series.highcharts-series-2 > .highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-series.highcharts-series-2 > .highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-markers > .highcharts-point").click()
#     # page.locator(".highcharts-markers > .highcharts-point").click()
#     page.locator(".highcharts-point.highcharts-color-1").first.click()
#     # page.locator(".highcharts-point.highcharts-color-0.highcharts-point-hover").click()
   
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-series.highcharts-series-2 > .highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-series.highcharts-series-2 > .highcharts-point.highcharts-point-hover").click()
#     # page.locator(".highcharts-markers > .highcharts-point").click()
#      # ================= WAIT FOR GRAPH =================
#     page.wait_for_selector(".highcharts-container", timeout=20000)

#         # ================= HOVER GRAPH =================
#     points = page.locator(".highcharts-point")

#     total = points.count()
#     print("Total points:", total)

#     for i in range(min(8, total)):
#             point = points.nth(i)

#             point.scroll_into_view_if_needed()

#             box = point.bounding_box()

#             if box:
#                 page.mouse.move(
#                     box["x"] + box["width"] / 2,
#                     box["y"] + box["height"] / 2
#                 )

#                 print(f"Hovering on point {i}")
#                 page.wait_for_timeout(2000)

#     page.get_by_role("button").nth(3).click()
#     page.get_by_role("button", name="Yes").click()


#     # # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)







        # -----new code------

import re
from playwright.sync_api import Playwright, sync_playwright
from utils.actions import step_click
from utils.context import set_context


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # ================= CONTEXT =================
    set_context(
        app="Peak Prediction",
        micro="End to End Flow",
        title="Complete Automation Flow"
    )

    # ================= LOGIN =================
    page.goto("http://103.204.95.218:7050/")

    step_click(page.locator(".gradient-input").first, "Click Email Field")
    page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")

    step_click(page.locator(".flex.flex-col.gap-\\[2vh\\] > div:nth-child(2)"), "Click Password Field")
    page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")

    step_click(page.get_by_role("button").filter(has_text=re.compile(r"^$")), "Click Login Icon")
    step_click(page.get_by_role("button", name="LOGIN"), "Click LOGIN Button")

    # ================= PROFILE DICTIONARY =================
    step_click(page.locator("div").filter(has_text=re.compile(r"^Profile Dictionary$")), "Open Profile Dictionary")
    step_click(page.get_by_role("button", name="Go to App").first, "Click Go To App")

    step_click(page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]"), "Click Right Arrow")
    step_click(page.locator(".w-\\[1\\.5vw\\]").first, "Click Left Arrow")

    step_click(
    page.locator("div").filter(has_text="RMS Value").nth(0),
    "Click Graph Card"
)

    
    page.wait_for_selector("text=Register Profile", timeout=20000)

    # ================= REGISTER PROFILE =================
    step_click(page.get_by_role("button", name="Register Profile"), "Open Register Profile")
    page.wait_for_selector("input[placeholder='e.g. Profile A']", timeout=20000)

    step_click(page.get_by_role("textbox", name="e.g. Profile A"), "Click Profile Name")
    page.get_by_role("textbox", name="e.g. Profile A").fill("testing")

    step_click(page.get_by_role("textbox", name="Enter control class"), "Click Control Class")
    page.get_by_role("textbox", name="Enter control class").fill("burst")

    step_click(page.get_by_role("textbox", name="Type here..."), "Click Input Field")
    page.get_by_role("textbox", name="Type here...").fill("123456789000")

    step_click(page.get_by_role("button", name="Propose options"), "Click Propose Options")

    step_click(
        page.locator("div:nth-child(2) > .flex.items-center.gap-\\[0\\.6vw\\] > .w-\\[0\\.9vw\\]"),
        "Select Option"
    )

    step_click(page.locator(".absolute.right-\\[1vw\\].z-50"), "Click Carousel Right")
    step_click(page.locator(".absolute.right-\\[1vw\\].z-50"), "Click Carousel Right Again")

    step_click(page.get_by_role("button", name="Check Similarity"), "Click Check Similarity")

    # ================= PREVIEW =================
    step_click(page.get_by_role("button", name="Preview"), "Click Preview")
    step_click(page.get_by_role("button", name="Confirm"), "Click Confirm")
    step_click(page.get_by_role("button", name="Cancel"), "Click Cancel")
    step_click(page.get_by_role("button", name="Confirm"), "Click Confirm Again")
    step_click(page.get_by_role("button", name="Yes"), "Click Yes")

    # ================= USER GENERATED =================
    step_click(page.get_by_role("button", name="User Generated Profiles"), "Open User Generated Profiles")

    step_click(page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]"), "Click Right Arrow")
    step_click(
        page.locator(".w-\\[2vw\\].h-\\[2vw\\].flex.items-center.justify-center.rounded-[0\\.5vw].bg-[linear-gradient(90deg,#0D405D_0%,#316D90_100%)]"),
        "Click Card"
    )

    step_click(page.get_by_role("button", name="Back"), "Click Back")

    # ================= POWER MONITORING =================
    step_click(page.get_by_role("button").first, "Open Menu")
    step_click(page.locator("div").filter(has_text=re.compile(r"^Power Monitoring$")).first, "Open Power Monitoring")
    step_click(page.get_by_role("button", name="Go to App").nth(2), "Go To Power Monitoring App")

    step_click(page.locator("div").filter(has_text=re.compile(r"^A3$")), "Select A3")
    step_click(page.locator("div").filter(has_text=re.compile(r"^A4$")), "Select A4")

    step_click(page.get_by_role("button", name="Isolated System View (Single"), "Open Isolated View")
    step_click(page.get_by_role("button", name="A1"), "Select A1")
    step_click(page.get_by_text("A4", exact=True), "Select A4")

    step_click(page.get_by_role("button", name="Zoom"), "Click Zoom")
    step_click(page.get_by_role("button", name="Close"), "Close Zoom")

    # ================= GRAPH =================
    step_click(page.get_by_text("35%"), "Click 35%")
    step_click(page.get_by_text("25%"), "Click 25%")
    step_click(page.get_by_text("PeakPeak"), "Click PeakPeak")

    step_click(page.locator(".highcharts-point.highcharts-color-0").first, "Click Graph Point")

    step_click(page.get_by_role("button", name="Distributed System View ("), "Open Distributed View")
    step_click(page.get_by_role("heading", name="Deployment Status"), "Open Deployment Status")

    page.wait_for_timeout(2000)
    step_click(page.locator(".absolute.left-\\[0\\.15vw\\]"), "Click Back Arrow")

    page.wait_for_timeout(2000)

    step_click(page.get_by_role("button", name="Power Quality Analytics Power"), "Open Power Quality")
    step_click(page.locator(".highcharts-point.highcharts-color-1").first, "Click Graph Point")

    # ================= CLOSE =================
    step_click(page.get_by_role("button").nth(3), "Click Close Button")
    step_click(page.get_by_role("button", name="Yes"), "Confirm Close")

    context.close()
    browser.close()


def test_peak_prediction():
    with sync_playwright() as playwright:
        run(playwright)