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
This project involved designing a practical, rule-based system to recommend recipes based on user inputs. The system uses logical conditions (e.g., exact and partial matches) to evaluate user-provided ingredients against recipes in the dataset.

### Challenges:
- **Handling Partial Matches:**  
  Deciding on a threshold (75%) that balances flexibility with accuracy was challenging.
- **Common Ingredients:**  
  Ensuring common ingredients like salt and water don’t skew the results. I resolved this by excluding them from the missing ingredient list.

### Comparison to Machine Learning:
- Unlike machine learning models, this system relies entirely on prewritten rules rather than learning from data.  
- **Advantages:** Simplicity and transparency.  
- **Limitations:**  
  - Limited scalability.  
  - Adding complex logic or handling ambiguous inputs (e.g., "bread" vs. "whole-grain bread") requires extensive manual rule updates, which machine learning could handle more flexibly.













