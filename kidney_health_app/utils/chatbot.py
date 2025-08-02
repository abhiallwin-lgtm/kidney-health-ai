# utils/chatbot.py

def kidney_chatbot(user_input):
    msg = user_input.lower()

    if "symptom" in msg:
        return ("Common CKD symptoms include:\n"
                "- Swelling in legs/ankles\n"
                "- Fatigue\n"
                "- Nausea\n"
                "- Frequent urination\n"
                "- High blood pressure")

    elif "cure" in msg or "treatment" in msg:
        return ("CKD cannot be fully cured, but it can be managed.\n"
                "Early stages can be controlled with:\n"
                "- Medication\n"
                "- Diet changes\n"
                "- Regular monitoring")

    elif "stage" in msg:
        return ("CKD has 5 stages. Stage 1 is mild, Stage 5 is end-stage renal disease (requires dialysis or transplant).\n"
                "Detection in early stages is crucial.")

    elif "motivate" in msg or "motivation" in msg:
        return ("💪 Stay strong! Many people live long and healthy lives with CKD by managing it well.\n"
                "You're not alone, and help is always available.")

    elif "diet" in msg:
        return ("CKD-friendly diets are usually low in:\n"
                "- Sodium\n"
                "- Potassium\n"
                "- Phosphorus\n"
                "Always consult a renal dietitian.")

    else:
        return ("I'm here to help you understand Chronic Kidney Disease.\n"
                "You can ask things like:\n"
                "- 'What are CKD symptoms?'\n"
                "- 'What stage is dangerous?'\n"
                "- 'Give me motivation'\n"
                "- 'How to manage CKD?'")
