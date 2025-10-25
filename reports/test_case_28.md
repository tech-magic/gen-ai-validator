### 🧪 Test Case 28

##### 🧾 Input Prompt
```text
Summarize: 'The mitochondria are the powerhouses of the cell.'
```
##### ✅ Expected Answer
```text
Mitochondria generate energy for cells.
```
##### 🤖 AI-generated Answer
```text
They produce energy for the cell.
```
##### 📘 Source of Truth
```text
# Input Prompt:
Summarize: 'The mitochondria are the powerhouses of the cell.'

---

# Expected Answer:
Mitochondria generate energy for cells.
```
##### 🔍 AI-inferred Truth
```text
# Input Prompt:
Summarize: 'The mitochondria are the powerhouses of the cell.'

---

# AI-generated Answer:
They produce energy for the cell.
```
### 📊 Evaluation Metrics

##### AnswerRelevancy
- **Score:** 1.00
- **Reason:** The score is 1.00 because the summary perfectly captures the essence of the input statement without any irrelevant information. Great job!

##### ContextualPrecision
- **Score:** 1.00
- **Reason:** The score is 1.00 because the first node in retrieval contexts, which is relevant and states 'They produce energy for the cell,' is perfectly aligned with the input and is ranked highest.

##### ContextualRecall
- **Score:** 1.00
- **Reason:** The score is 1.00 because the expected output aligns perfectly with the information provided in the 1st node of the retrieval context, which confirms that mitochondria generate energy for cells.

##### Hallucination
- **Score:** 0.00
- **Reason:** The score is 0.00 because the actual output aligns perfectly with the provided context, indicating no hallucinations.

