# # import re
# # from playwright.sync_api import Playwright, sync_playwright, expect


# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False)
# #     context = browser.new_context()
# #     page = context.new_page()
# #     page.goto("http://103.204.95.218:7050/")
# #     page.get_by_role("textbox", name="Enter your email id").click(modifiers=["ControlOrMeta"])
# #     page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
# #     page.locator("div:nth-child(2) > .h-full").click()
# #     page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
# #     page.get_by_role("button", name="LOGIN").click()

# #     # ---------------------
# #     context.close()
# #     browser.close()


# # with sync_playwright() as playwright:
# #     run(playwright)
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
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
#     page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
#     page.get_by_role("button", name="LOGIN").click()
#     page.get_by_role("button", name="Go to App").first.click()
#     page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]").click()
#     page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]").click()
#     page.locator(".absolute.right-\\[0\\.7vw\\] > .w-\\[1\\.5vw\\]").click()
#     page.locator(".w-\\[1\\.5vw\\]").first.click()
#     page.locator(".w-\\[1\\.5vw\\]").first.click()
#     page.get_by_role("button", name="Filter").click()
#     page.get_by_role("button", name="Sort Sort By").click()
#     page.locator(".flex.items-center.justify-center.cursor-pointer.rounded-lg").click()
#     page.get_by_role("button", name="Register Profile").click()
#     page.get_by_role("textbox", name="e.g. Profile A").click()
#     page.get_by_role("textbox", name="e.g. Profile A").fill("testing")
#     page.get_by_role("textbox", name="Enter control class").click()
#     page.get_by_role("textbox", name="Enter control class").fill("brust")
#     page.get_by_role("textbox", name="Type here...").click()
#     page.get_by_role("textbox", name="Type here...").fill("1234567qwert")
#     page.get_by_role("button", name="Propose options").click()
#     page.locator("div:nth-child(2) > .flex.items-center.gap-\\[0\\.6vw\\] > .w-\\[0\\.9vw\\]").click()
#     page.get_by_role("button", name="Check Similarity").click()
    
#     page.locator(".flex.justify-between > .p-\\[0\\.08vw\\] > .w-\\[2vw\\]").click()
#     page.get_by_text("Option B — balanced /").click()
#     page.get_by_role("button", name="Check Similarity").click()
#     page.locator(".w-\\[2vw\\]").first.click()
#     page.locator(".w-\\[2vw\\]").first.click()
#     page.locator(".highcharts-tracker-line").first.click()
#     page.locator(".highcharts-markers.highcharts-series-1 > .highcharts-point").first.click()
#     page.locator(".highcharts-markers.highcharts-series-1 > .highcharts-point").first.click()
#     page.locator(".highcharts-markers.highcharts-series-1.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-point").click()
#     page.locator(".highcharts-markers.highcharts-series-1.highcharts-line-series.highcharts-tracker.highcharts-series-hover > .highcharts-point").click()
#     page.get_by_role("button", name="Preview").click()
#     page.locator(".highcharts-tracker-line").click()
#     page.locator(".highcharts-tracker-line").click()
#     page.get_by_role("button", name="Confirm").click()
#     page.get_by_role("button", name="Cancel").click()
#     page.get_by_role("button", name="Confirm").click()
#     page.get_by_role("button", name="Yes").click()
#     page.get_by_role("button", name="User Generated Profiles").click()
#     page.locator(".absolute.right-\\[0\\.7vw\\]").click()
#     page.locator(".absolute.right-\\[0\\.7vw\\]").click()
#     page.locator(".w-\\[2vw\\].h-\\[2vw\\].flex.items-center.justify-center.rounded-\\[0\\.5vw\\].bg-\\[linear-gradient\\(90deg\\,\\#0D405D_0\\%\\,\\#316D90_100\\%\\)\\].cursor-pointer").click()
#     page.locator(".highcharts-point").click()
#     page.locator(".highcharts-point").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email = page.get_by_role("textbox", name="Enter your email id")
        self.password = page.get_by_role("textbox", name="Enter your password")
        self.login_btn = page.get_by_role("button", name="LOGIN")

    def load(self, url):
        self.page.goto(url)

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_btn.click()