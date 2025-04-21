# Define categorized symptoms
severe_symptoms = {
    "vomiting", "bloody stool", "swollen belly", "lethargy", "loss of appetite"
}
moderate_symptoms = {
    "limping", "itchy skin", "scratching ears", "hair loss", "frequent urination",
    "excessive thirst", "shaking", "aggression"
}
low_symptoms = {
    "sneezing", "coughing", "restlessness", "panting", "hiding"
}

# Prompt user for input
print("Welcome to the Pet Symptom Checker 🐾")
print("Please enter your pet's symptoms, separated by commas.")
user_input = input("Symptoms: ").lower()

# Split and clean input
reported_symptoms = {symptom.strip() for symptom in user_input.split(",")}

# Determine severity level
has_severe = any(symptom in severe_symptoms for symptom in reported_symptoms)
has_moderate = any(symptom in moderate_symptoms for symptom in reported_symptoms)
has_only_low = all(symptom in low_symptoms for symptom in reported_symptoms)

# Rule-based decision-making
print("\n🩺 Assessment:")
if has_severe:
    print("⚠️  Severe symptoms detected.")
    print("Recommendation: Please contact your veterinarian immediately.")
elif has_moderate:
    print("⚠️  Moderate symptoms detected.")
    print("Recommendation: Monitor your pet. Visit the vet if symptoms persist or worsen.")
elif has_only_low:
    print("ℹ️  Only low-level symptoms detected.")
    print("Recommendation: Monitor at home. Provide comfort and hydration. Seek help if symptoms escalate.")
else:
    print("❓ Symptoms not recognized.")
    print("Recommendation: Please consult a veterinarian for further evaluation.")

# Optional: show what symptoms were detected
print(f"\n🔍 Symptoms you reported: {', '.join(reported_symptoms)}")