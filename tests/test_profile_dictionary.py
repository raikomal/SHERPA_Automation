# import re
# from utils.actions import step_click, step_fill
# from utils.context import TEST_CONTEXT
# from utils.excel_report import save_excel


# def login(page):
#     page.goto("http://103.204.95.218:7050/")
#     page.evaluate("localStorage.clear()")
#     page.evaluate("sessionStorage.clear()")

#     page.get_by_role("textbox", name="Enter your email id").fill("sherpa@local.com")
#     page.get_by_role("textbox", name="Enter your password").fill("sherpa@123")
#     page.get_by_role("button", name="LOGIN").click()

#     page.wait_for_selector("text=Profile Dictionary", timeout=20000)


# def test_profile_dictionary_flow(page):

#     TEST_CONTEXT["application"] = "Profile Dictionary"

#     login(page)

#     # ================= DASHBOARD =================
#     step_click(page.get_by_text("Profile Dictionary").nth(0), "Open Profile Dictionary")
#     step_click(page.get_by_role("button", name="Go to App").first, "Go to App")

#     # ================= PROFILE LIST VIEW =================
#     page.wait_for_selector("text=Profiles", timeout=20000)

#     # 👉 ARROWS
#     arrows = page.locator(".w-\\[1\\.5vw\\]")

#     if arrows.count() >= 2:
#         step_click(arrows.nth(1), "Right Arrow")
#         step_click(arrows.nth(0), "Left Arrow")

#     # 👉 EYE ICON (GRAPH)
#     eye_icon = page.locator(".cursor-pointer").nth(0)

#     if eye_icon.count() > 0:
#         step_click(eye_icon, "Open Graph")
#         page.wait_for_selector(".highcharts-container", timeout=10000)

#         if page.get_by_role("button", name="Back").count() > 0:
#             step_click(page.get_by_role("button", name="Back"), "Close Graph")

#     # ================= SWITCH TO REGISTER PROFILE =================
#     step_click(page.get_by_text("Register Profile"), "Open Register Profile")

#     # ================= FORM =================
#     step_fill(page.get_by_role("textbox", name="e.g. Profile A"), "Test", "Profile Name")
#     step_fill(page.get_by_role("textbox", name="Enter control class"), "burst", "Control Class")
#     step_fill(page.get_by_role("textbox", name="Type here..."), "12345678", "Input Data")

#     step_click(page.get_by_role("button", name="Propose options"), "Propose Options")

#     # ================= SELECT OPTION (FIXED) =================
#     options = page.locator("div").filter(has_text=re.compile("Pattern"))

#     if options.count() > 0:
#         step_click(options.first, "Select Option")
#     else:
#         raise Exception("❌ Option not found")

#     # ================= SLIDER =================
#     if page.locator(".absolute.right-\\[1vw\\]").count() > 0:
#         step_click(page.locator(".absolute.right-\\[1vw\\]").first, "Slider Right")

#     # ================= SIMILARITY =================
#     step_click(page.get_by_role("button", name="Check Similarity"), "Check Similarity")

#     page.wait_for_timeout(3000)

#     # 👉 IMPORTANT FILTERS
#     if page.get_by_text("burst").count() > 0:
#         step_click(page.get_by_text("burst").first, "Select Burst")

#     if page.get_by_text("Description:").count() > 0:
#         step_click(page.get_by_text("Description:").first, "Select Description")

#     step_click(page.get_by_role("button", name="Check Similarity"), "Re-Check Similarity")

#     page.wait_for_timeout(4000)

#     # ================= SUGGESTION =================
#     suggestion = page.locator("text=Sustained")

#     if suggestion.count() == 0:
#         raise Exception("❌ Suggestion NOT generated")

#     step_click(suggestion.first, "Select Suggestion")

#     # ================= PREVIEW =================
#     step_click(page.get_by_role("button", name="Preview"), "Preview")

#     # ================= CONFIRM =================
#     if page.get_by_role("button", name="Confirm").count() > 0:
#         step_click(page.get_by_role("button", name="Confirm"), "Confirm")

#     if page.get_by_role("button", name="Yes").count() > 0:
#         step_click(page.get_by_role("button", name="Yes"), "Yes")


# def teardown_module(module):
#     save_excel()