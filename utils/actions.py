# # import time
# # from utils.logger import get_logger
# # from utils.excel_report import save_step
# # from utils.context import TEST_CONTEXT

# # logger = get_logger()
# # STEP_DELAY = 1


# # def record_step(description, steps, expected, actual, status="PASS", remarks=""):
# #     data = {
# #         "project": TEST_CONTEXT["project"],
# #         "application": TEST_CONTEXT["application"],
# #         "micro_application": TEST_CONTEXT["micro_application"],
# #         "title": TEST_CONTEXT["title"],
# #         "description": description,
# #         "steps": steps,
# #         "expected_result": expected,
# #         "actual_result": actual,
# #         "status": status,
# #         "remarks": remarks,
# #         "task_id": "",
# #         "ticket_id": "",
# #         "comments": ""
# #     }
# #     save_step(data)


# # # =========================
# # # CLICK ACTION
# # # =========================
# # def step_click(locator, desc):
# #     try:
# #         time.sleep(STEP_DELAY)

# #         logger.info(f"CLICK -> {desc}")

# #         locator.wait_for(state="visible", timeout=10000)
# #         locator.click()

# #         record_step(
# #             desc,
# #             f"Click on {desc}",
# #             "Element should be clickable",
# #             "Clicked successfully"
# #         )

# #     except Exception as e:
# #         logger.error(f"FAIL CLICK -> {desc} | {str(e)}")

# #         record_step(
# #             desc,
# #             f"Click on {desc}",
# #             "Element should be clickable",
# #             str(e),
# #             "FAIL"
# #         )
# #         raise


# # # =========================
# # # FILL ACTION
# # # =========================
# # def step_fill(locator, value, desc):
# #     try:
# #         time.sleep(STEP_DELAY)

# #         logger.info(f"FILL -> {desc}: {value}")

# #         locator.wait_for(state="visible", timeout=10000)
# #         locator.fill(value)

# #         record_step(
# #             desc,
# #             f"Enter value in {desc}",
# #             "Field should accept input",
# #             f"Entered value: {value}"
# #         )

# #     except Exception as e:
# #         logger.error(f"FAIL FILL -> {desc} | {str(e)}")

# #         record_step(
# #             desc,
# #             f"Enter value in {desc}",
# #             "Field should accept input",
# #             str(e),
# #             "FAIL"
# #         )
# #         raise
# import time
# from utils.logger import get_logger
# from utils.excel_report import save_step
# from utils.context import TEST_CONTEXT

# logger = get_logger()
# STEP_DELAY = 1


# def record_step(description, steps, expected, actual, status="PASS"):
#     data = {
#         "Project": TEST_CONTEXT["project"],
#         "Application": TEST_CONTEXT["application"],
#         "Micro_Application": TEST_CONTEXT["micro_application"],
#         "Title": TEST_CONTEXT["title"],
#         "Description": description,
#         "Steps": steps,
#         "Expected_Result": expected,
#         "Actual_Result": actual,
#         "Status": status,
#         "Remark": ""
#     }
#     save_step(data)


# def step_click(locator, desc):
#     try:
#         locator.wait_for(state="visible", timeout=15000)
#         locator.scroll_into_view_if_needed()

#         logger.info(f"CLICK -> {desc}")
#         locator.click(force=True)   # 🔥 force click

#         record_step(desc, f"Click {desc}", "Should click", "Clicked")

#     except Exception as e:
#         logger.error(f"FAIL CLICK -> {desc} | {e}")
#         record_step(desc, f"Click {desc}", "Should click", str(e), "FAIL")
#         raise


# def step_fill(locator, value, desc):
#     try:
#         time.sleep(STEP_DELAY)
#         locator.wait_for(state="visible", timeout=10000)
#         logger.info(f"FILL -> {desc}: {value}")
#         locator.fill(value)

#         record_step(desc, f"Fill {desc}", "Should accept input", f"Entered {value}")

#     except Exception as e:
#         logger.error(f"FAIL FILL -> {desc} | {e}")
#         record_step(desc, f"Fill {desc}", "Should accept", str(e), "FAIL")
#         raise
import time
from datetime import datetime
from utils.logger import get_logger
from utils.excel_report import save_step
import utils.context as ctx

logger = get_logger()
STEP_DELAY = 1


# def record_step(description, steps, expected, actual, status="PASS"):
#     step_no = TEST_CONTEXT.get("step_no", 1)

#     data = {
#         "Step_No": step_no,
#         "Project": TEST_CONTEXT["project"],
#         "Requirements" : ["id"],
#         "Application": TEST_CONTEXT["application"],
#         "Micro_Application": TEST_CONTEXT["micro_application"],
#         "Title": TEST_CONTEXT["title"],
#         "Description": description,
#         "Steps": steps,
#         "Expected_Result": expected,
#         "Actual_Result": actual,
#         "Status": status,
#         "Time": datetime.now().strftime("%H:%M:%S"),
#         "Remark": ""
#     }

#     TEST_CONTEXT["step_no"] = step_no + 1
#     save_step(data)
def record_step(description, steps, expected, actual, status="PASS"):
    step_no = ctx.TEST_CONTEXT.get("step_no", 1)

    print("READ CONTEXT:", ctx.TEST_CONTEXT)  # 🔥 DEBUG

    data = {
        "Step_No": step_no,
        "Project": ctx.TEST_CONTEXT["project"],
        "Application": ctx.TEST_CONTEXT["application"],
        "Micro_Application": ctx.TEST_CONTEXT["micro_application"],
        "Title": ctx.TEST_CONTEXT["title"],
        "Description": description,
        "Steps": steps,
        "Expected_Result": expected,
        "Actual_Result": actual,
        "Status": status,
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Remark": ""
    }

    ctx.TEST_CONTEXT["step_no"] = step_no + 1
    save_step(data)


# =========================
# CLICK ACTION
# =========================
def step_click(locator, desc):
    try:
        locator.first.wait_for(state="visible", timeout=15000)
        locator.first.scroll_into_view_if_needed()

        logger.info(f"CLICK -> {desc}")
        locator.first.click()

        record_step(desc, f"Click {desc}", "Should click", "Clicked")

    except Exception as e:
        logger.error(f"FAIL CLICK -> {desc} | {e}")
        record_step(desc, f"Click {desc}", "Should click", str(e), "FAIL")
        raise


# =========================
# FILL ACTION
# =========================
def step_fill(locator, value, desc):
    try:
        time.sleep(STEP_DELAY)
        locator.wait_for(state="visible", timeout=10000)

        logger.info(f"FILL -> {desc}: {value}")
        locator.fill(value)

        record_step(desc, f"Fill {desc}", "Should accept input", f"Entered {value}")

    except Exception as e:
        logger.error(f"FAIL FILL -> {desc} | {e}")
        record_step(desc, f"Fill {desc}", "Should accept input", str(e), "FAIL")
        raise