# logic/criticality.py
def get_criticality(issue_text):
    text = issue_text.lower()
    if "system down" in text or "urgent" in text or "critical" in text:
        return "High"
    elif "slow" in text or "delay" in text:
        return "Normal"
    else:
        return "Low"
