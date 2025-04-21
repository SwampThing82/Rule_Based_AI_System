# Sample submission for the Building a Rule-Based AI System in Python project.

---

## Part 1: Initial Project Ideas

### 1. Project Idea 1: Rule-Based Movie Recommendation System
- **Description:** A simple expert system for personalized movie suggestions.  
- **Rule-Based Approach:**  
  - Recommends movies based on user preferences and a ruleset.
  - Could also set preferences based on age, previously watched movies, or a mini rule-editor so the the user can modify or add rules.

### 2. Project Idea 2: Medical Diagnostic Rool
- **Description:** A chatbot that simulates early expert systems like MYCIN (used for blood infections). Asks users about symptoms and suggest a diagnosis or action.  
- **Rule-Based Approach:**  
  - Responses are based on rules to match possible diagnoses  
  - For example, if the user says symptoms include "cough, fever, and shortness of breath", it would recommend "possible flu or COVID-19. See a doctor"

### 3. Project Idea 3: Symptom Checker for Pets
- **Description:** A system that uses observable symptoms to guide pet owners toward understanding possible conditions and treatment options.  
- **Rule-Based Approach:**  
  - The system uses rules to recommend suggested diagnoses.  
  - For example, if the user says the pet is "vomiting and lethargic", it would recommend "Potential ingestion of harmful substance. Seek veterinary care."

### **Chosen Idea:** Symptom Checker for Pets  
**Justification:** I chose this project because we have many pets in my home, and my wife works for an animal shelter and has a background in veterinary medicine. While we have easy access to this knowledge, I know that many don't and have to rely on google searches or potentially expensive vet trips for what could be simple solutions.

---

## Part 2: Rules/Logic for the Chosen System

The **Symptom Checker for Pets** system will follow these rules:

1. **Urgent Severity Rule:**  
   - **IF** any symptoms included are labeled as "severe" symptoms → **Recommend the vet.**

2. **Moderate Severity Rule:**  
   - **IF** no severe symptoms exist AND any symptoms included are labeled as "moderate" symptoms → **Recommend monitoring and vet visit if symptoms persist/worsen.**

3. **Low Severity Rule:**  
   - **IF** the only symptoms included are labeled as "low" symptoms → **Recommend monitoring at home, potential help.**

---

## Part 3: Rules/Logic for the Chosen System

Sample input and output: 

Symptoms: sneezing, coughing
🩺 Assessment:
ℹ️  Only low-level symptoms detected.
Recommendation: Monitor at home. Provide comfort and hydration. Seek help if symptoms escalate.

Symptoms: shaking, sneezing
🩺 Assessment:
⚠️  Moderate symptoms detected.
Recommendation: Monitor your pet. Visit the vet if symptoms persist or worsen.

Symptoms: lethargy, panting
🩺 Assessment:
⚠️  Severe symptoms detected.
Recommendation: Please contact your veterinarian immediately.

---

## Part 4: Reflection

### Project Overview:
This project involved designing a rule-based system to check pet health based on user input symptoms. The system uses defined symptom severity dictionaries to evaluate user-provided symptoms against potenial risks and care advice in the dataset.

### Challenges:
- **Finding a project to attempt:**  
  While ChatGPT offered many interesting ideas, like a Smart Home Rule Engine Simulator to help set automation of smart devices, it looked like it would quickly reach outside the parameters of this challenge (similar to the text-based adventure example in the lecture).
- **Setting symptom dictionaries:**  
  Many symptoms can overlap into other categories or issues, making them more or less concerning depending on the accompanying symptoms. Further logic and building out of the symptoms would help, but also add in a degree of difficulty/lack of simplicity expected for this project.

### Comparison to Machine Learning:
- Unlike machine learning models, this system relies entirely on prewritten rules and datasets rather than learning from data.  
- **Advantages:** Simplicity and transparency, easy to update and build on for the current intended purpose.  
- **Limitations:**  
  - Limited functionality - doesn't accept symptoms not in dataset.  
  - Adding complex logic or handling undefined symptoms requires time-consuming manual dataset and rule updates, which machine learning could handle more efficiently and with a broader scope.













