def check_risk(location, movement):

    high_risk_areas = ["Unknown Area", "High Crime Zone"]

    if location in high_risk_areas:
        return "⚠ Warning: You are in a High Risk Area!"

    if movement == "Running":
        return "⚠ Sudden Movement Detected!"

    if movement == "Falling":
        return "🚨 Possible Accident Detected!"

    if movement == "No Movement":
        return "⚠ No Movement Detected for Long Time!"

    return "✅ You are Safe"
