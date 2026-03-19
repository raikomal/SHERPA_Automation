# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("http://103.204.95.218:7050/")
#     page.get_by_role("textbox", name="Enter your email id").click()
#     page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
#     page.get_by_role("textbox", name="Enter your password").click()
#     page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
#     page.get_by_role("button", name="LOGIN").click()
#     page.locator("div").filter(has_text=re.compile(r"^Power Monitoring$")).first.click()
#     page.get_by_role("button", name="Go to App").nth(2).click()
#     page.get_by_text("1.73 MWAvg Total").click()
#     page.get_by_text("85 kWPeak TodaykWPeak 93").click()
#     page.get_by_text("%Avg Utilization Last 24 hoursSite-wide Power Capacity83%").click()
#     page.get_by_text("77Threshold Status● Critical").click()
#     page.get_by_role("button", name="Site").click()
#     page.get_by_role("button", name="Room").click()
#     page.get_by_role("button", name="Customer").click()
#     page.get_by_role("button", name="SLA Tier").click()
#     page.locator("rect").nth(1).click()
#     page.locator("div").filter(has_text=re.compile(r"^A2$")).click()
#     page.get_by_role("img", name="Eye").click()
#     page.get_by_role("button", name="A2").click()
#     page.get_by_text("A3", exact=True).click()
   
#     page.locator(".highcharts-plot-band").first.click()
#     page.get_by_text("40%").click()
#     page.get_by_text("35%").click()
#     page.get_by_text("25%").click()
#     page.get_by_role("button", name="Zoom").click()
#     page.get_by_role("button", name="Close").click()
#     page.get_by_text("PeakPeak").click()
#     page.locator(".highcharts-point.highcharts-color-0.highcharts-point-hover").click()
#     page.get_by_role("button", name="Back").click()
#     page.get_by_role("button", name="Back").click()
#     page.get_by_role("button", name="Power Monitoring", exact=True).click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
