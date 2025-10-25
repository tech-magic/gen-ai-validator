### 🧪 Test Case 43

##### 🧾 Input Prompt
```text
Summarize the plot of 'The Lion King' in one sentence.
```
##### ✅ Expected Answer
```text
A young lion named Simba overcomes adversity to reclaim his rightful place as king.
```
##### 🤖 AI-generated Answer
```text
Simba learns to be king after his father's death.
```
##### 📘 Source of Truth
```text
# Input Prompt:
Summarize the plot of 'The Lion King' in one sentence.

---

# Expected Answer:
A young lion named Simba overcomes adversity to reclaim his rightful place as king.
```
##### 🔍 AI-inferred Truth
```text
# Input Prompt:
Summarize the plot of 'The Lion King' in one sentence.

---

# AI-generated Answer:
Simba learns to be king after his father's death.
```
### 📊 Evaluation Metrics

##### ContextualPrecision
- **Score:** 1.00
- **Reason:** The score is 1.00 because the first node in the retrieval contexts, which provides a relevant summary of 'The Lion King', is perfectly aligned with the input request. No irrelevant nodes are present, making the ranking ideal.

##### ContextualRecall
- **Score:** 1.00
- **Reason:** The score is 1.00 because the retrieval context perfectly aligns with the expected output, specifically mentioning 'Simba' and his journey to 'be king', which directly supports the sentence about Simba overcoming adversity to reclaim his place as king.

##### ContextualRelevancy
- **Score:** 1.00
- **Reason:** The score is 1.00 because the retrieval context perfectly aligns with the input, as evidenced by the relevant statement: 'Simba learns to be king after his father's death.' This succinctly captures the essence of 'The Lion King's' plot, making it a perfect match.

