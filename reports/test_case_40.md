### 🧪 Test Case 40

##### 🧾 Input Prompt
```text
Translate 'How are you?' to Japanese.
```
##### ✅ Expected Answer
```text
お元気ですか？ (Ogenki desu ka?)
```
##### 🤖 AI-generated Answer
```text
Ogenki desu ka?
```
##### 📘 Source of Truth
```text
# Input Prompt:
Translate 'How are you?' to Japanese.

---

# Expected Answer:
お元気ですか？ (Ogenki desu ka?)
```
##### 🔍 AI-inferred Truth
```text
# Input Prompt:
Translate 'How are you?' to Japanese.

---

# AI-generated Answer:
Ogenki desu ka?
```
### 📊 Evaluation Metrics

##### AnswerRelevancy
- **Score:** 1.00
- **Reason:** The score is 1.00 because the translation provided is accurate and directly relevant to the input request with no irrelevant statements.

##### ContextualPrecision
- **Score:** 1.00
- **Reason:** The score is 1.00 because the first node in the retrieval contexts, which provides the translation 'Ogenki desu ka?', is directly relevant and useful for the input, with no irrelevant nodes present.

##### ContextualRecall
- **Score:** 1.00
- **Reason:** The score is 1.00 because the sentence 'お元気ですか？ (Ogenki desu ka?)' is perfectly matched in the 1st node of the retrieval context.

##### ContextualRelevancy
- **Score:** 1.00
- **Reason:** The score is 1.00 because the retrieval context perfectly matches the input with the translation 'Ogenki desu ka?' for 'How are you?' in Japanese, demonstrating complete relevance and accuracy.

##### Hallucination
- **Score:** 0.00
- **Reason:** The score is 0.00 because the actual output 'Ogenki desu ka?' perfectly aligns with the provided context, indicating no hallucinations.

