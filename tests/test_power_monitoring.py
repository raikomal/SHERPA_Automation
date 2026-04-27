# # import re
# # from playwright.sync_api import Playwright, sync_playwright, expect


# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("http://103.204.95.218:7050/")
# #     page.get_by_role("textbox", name="Enter your email id").click()
# #     page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
# #     page.locator(".flex.flex-col.gap-\\[2vh\\] > div:nth-child(2)").click()
# #     page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
# #     page.get_by_role("button", name="LOGIN").click()
# #     page.locator("div:nth-child(8) > .relative > .mt-auto > .flex.justify-between > .rounded-\\[0\\.4vw\\].p-\\[0\\.06vw\\] > .rounded-\\[0\\.4vw\\]").click()
    
# #     page.locator(".highcharts-point.highcharts-point-hover").click()
# #     page.locator(".highcharts-point.highcharts-point-hover").click()
# #     page.locator(".highcharts-point.highcharts-point-hover").first.click()
# #     page.locator(".highcharts-point.highcharts-point-hover").first.click()
# #     page.locator(".highcharts-halo.highcharts-color-undefined").click()
# #     page.locator(".highcharts-markers > .highcharts-point").click()

# #     # ---------------------
# #     context.close()
# #     browser.close()


# # with sync_playwright() as playwright:
# #     run(playwright)
# from playwright.sync_api import sync_playwright
# import re


# def run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False, slow_mo=800)
#         page = browser.new_page()

#         # ================= LOGIN =================
#         page.goto("http://103.204.95.218:7050/")

#         page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
#         page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
#         page.get_by_role("button", name="LOGIN").click()

#         # ================= DASHBOARD =================
#         page.wait_for_selector("text=Power Quality Analytics", timeout=20000)

#         # 👉 CLICK APP CARD (YOUR LINE)
#         page.locator("div").filter(
#             has_text=re.compile(r"^Power Quality Analytics$")
#         ).click()

#         # 👉 CLICK GO TO APP (VERY IMPORTANT)
#         page.locator(
#             "div:nth-child(8) > .relative > .mt-auto > .flex.justify-between > .rounded-\\[0\\.4vw\\].p-\\[0\\.06vw\\] > .rounded-\\[0\\.4vw\\]"
#         ).click()

#         # ================= WAIT FOR GRAPH =================
#         page.wait_for_selector(".highcharts-container", timeout=20000)

#         # ================= HOVER GRAPH =================
#         points = page.locator(".highcharts-point")

#         total = points.count()
#         print("Total points:", total)

#         for i in range(min(8, total)):
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

#         page.wait_for_timeout(5000)
#         browser.close()


# run()