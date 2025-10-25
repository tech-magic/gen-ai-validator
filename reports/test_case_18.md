### 🧪 Test Case 18

##### 🧾 Input Prompt
```text
Which continent is Australia located on?
```
##### ✅ Expected Answer
```text
Australia is located on the continent of Australia.
```
##### 🤖 AI-generated Answer
```text
Australia
```
##### 📘 Source of Truth
```text
# Input Prompt:
Which continent is Australia located on?

---

# Expected Answer:
Australia is located on the continent of Australia.
```
##### 🔍 AI-inferred Truth
```text
# Input Prompt:
Which continent is Australia located on?

---

# AI-generated Answer:
Australia
```
### 📊 Evaluation Metrics

##### AnswerRelevancy
- **Score:** 0.00
- **Reason:** The score is 0.00 because the output 'Australia' does not address the question about the continent on which Australia is located, making it completely irrelevant.

##### ContextualPrecision
- **Score:** 0.00
- **Reason:** The score is 0.00 because the first node in retrieval contexts, which states 'The retrieval context only provides the name \"Australia\" without specifying that it is both a country and a continent, hence it is not sufficiently informative to determine the expected output.', is irrelevant and should be ranked lower.

##### ContextualRecall
- **Score:** 1.00
- **Reason:** The score is 1.00 because the retrieval context perfectly aligns with the expected output, providing a clear and accurate response to the query.

##### ContextualRelevancy
- **Score:** 0.00
- **Reason:** The score is 0.00 because the context only mentions 'Australia' without providing any relevant information about the continent it is located on.

##### Hallucination
- **Score:** 1.00
- **Reason:** The score is 1.00 because the actual output 'Australia' contradicts the expected context which requires stating that 'Australia is located on the continent of Australia.' This incomplete and inaccurate response leads to a high hallucination score.

