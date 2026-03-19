# from openpyxl import Workbook
# from datetime import datetime
# import os

# os.makedirs("reports/excel", exist_ok=True)

# wb = Workbook()
# ws = wb.active
# ws.title = "Test Results"

# headers = [
#     "Project", "Application", "Micro_Application",
#     "Title", "Description", "Steps",
#     "Expected_Result", "Actual_Result",
#     "Status", "Remark", "Task_ID", "Ticket_ID", "Notes"
# ]

# ws.append(headers)


# def save_step(data):
#     ws.append([
#         data["project"],
#         data["application"],
#         data["micro_application"],
#         data["title"],
#         data["description"],
#         data["steps"],
#         data["expected_result"],
#         data["actual_result"],
#         data["status"],
#         data["remarks"],
#         data["task_id"],
#         data["ticket_id"],
#         data["comments"]
#     ])


# def save_excel():
#     file = f"reports/excel/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
#     wb.save(file)
import pandas as pd
import os
from datetime import datetime

data_store = []

def save_step(data):
    data_store.append(data)

def save_excel():
    if not os.path.exists("reports/excel"):
        os.makedirs("reports/excel")

    df = pd.DataFrame(data_store)

    file_name = f"reports/excel/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(file_name, index=False)

    print(f"Excel saved: {file_name}")