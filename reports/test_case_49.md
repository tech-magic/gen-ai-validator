### 🧪 Test Case 49

##### 🧾 Input Prompt
```text
What is the opposite of 'increase'?
```
##### ✅ Expected Answer
```text
The opposite of 'increase' is 'decrease'.
```
##### 🤖 AI-generated Answer
```text
Decrease.
```
##### 📘 Source of Truth
```text
# Input Prompt:
What is the opposite of 'increase'?

---

# Expected Answer:
The opposite of 'increase' is 'decrease'.
```
##### 🔍 AI-inferred Truth
```text
# Input Prompt:
What is the opposite of 'increase'?

---

# AI-generated Answer:
Decrease.
```
### 📊 Evaluation Metrics

##### ContextualPrecision
- **Score:** 1.00
- **Reason:** The score is 1.00 because all relevant nodes, such as the first node which states 'Decrease' as the opposite of 'increase', are ranked higher than any irrelevant nodes.

##### ContextualRecall
- **Score:** 1.00
- **Reason:** The score is 1.00 because the sentence 'The opposite of 'increase' is 'decrease'.' is perfectly supported by the 1st node in the retrieval context, which is 'Decrease.' Great job!

##### ContextualRelevancy
- **Score:** 1.00
- **Reason:** The score is 1.00 because the retrieval context directly provides the relevant statement 'Decrease.' which is the exact opposite of 'increase', making it perfectly aligned with the input query.

##### Hallucination
- **Score:** 0.00
- **Reason:** The score is 0.00 because the actual output aligns perfectly with the provided context without any contradictions.

