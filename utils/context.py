TEST_CONTEXT = {
    "project": "SHERPA",
    "application": "",
    "micro_application": "",
    "title": "",
    "step_no": 1
}


def set_context(app=None, micro=None, title=None):
    if app:
        TEST_CONTEXT["application"] = app
    if micro:
        TEST_CONTEXT["micro_application"] = micro
    if title:
        TEST_CONTEXT["title"] = title

    # 🔥 DEBUG (important)
    print("UPDATED CONTEXT:", TEST_CONTEXT)