[Figure: Two line charts comparing Vanilla RAG and Order-Preserve RAG as the number of retrieved chunks increases. Left: EN.QA with F1 score; right: EN.MC with Accuracy.]

Figure 4: Comparisons between the proposed order-preserve RAG and vanilla RAG. The evaluations are conducted on En.QA and EN.MC datasets of ∞Bench, using Llama3.1-70B model.

irrelevant distractions.

**Order-preserve RAG versus vanilla RAG.** As shown in Figure 4, when the number of retrieved chunks are small (e.g., 8), the advantage of the proposed order-preserve RAG over vanilla RAG is not considerably. In contrast, when the number of retrieved chunks is large, our order-preserve RAG significantly outperforms vanilla RAG. To be specific, on EN.QA dataset, when the number of retrieved chunk is 128, vanilla RAG only achieves 38.40 F1-score whereas our order-preserve RAG achieves 44.43 F1-score. On EN.MC dataset, retrieving 192 chunks, vanilla RAG only achieves 81.22 accuracy whereas our order-preserve RAG obtains 88.65 accuracy.

### 4.4 Main Results

We compare the proposed order-preserve RAG with two types of baselines. The first category of approaches uses the long-context LLM without RAG. As shown in Table 1, without RAG, LLM takes a huge number of tokens as input, which is inefficient and costly. In contrast, the proposed order-preserve RAG not only significantly reduces the number of tokens, but also significantly improves the answer quality. For instance, using Llama3.1-70B model, the approach without RAG only achieves a 34.26 F1 score on EN.QA with an average of 117K tokens as input. In contrast, our OP-RAG with 48K tokens as input attains a 47.25 F1 score. The second category of baselines takes the SELF-ROUTE mechanism (Li et al., 2024), which routes queries to RAG or long-context LLM based on the model self-reflection. As shown in Table 1, ours significantly outperforms than using much fewer tokens in the input of LLMs.

| Method | EN.QA F1 Score | EN.QA Tokens | EN.MC Acc. | EN.MC Tokens |
|---|---:|---:|---:|---:|
| Llama3.1-70B | 34.26 | 117K | 71.62 | 117K |
| GPT-4O | 32.36 | 117K | 78.42 | 117K |
| Gemini-1.5-Pro | 43.08 | 196K | 85.57 | 188K |
| GPT-4O | 34.95 | 85K | 77.29 | 62K |
| Gemini-1.5-Pro | 37.51 | 83K | 76.86 | 62K |
| OP-RAG-16K | 44.43 | 16K | 84.72 | 16K |
| OP-RAG-24K | 45.45 | 24K | 88.65 | 24K |
| OP-RAG-48K | 47.25 | 48K | 85.59 | 48K |

Table 1: Comparisons among the long-context LLM without RAG, SELF-ROUTE mechanism (Li et al., 2024) and the proposed order-preserve (OP) RAG.

cantly outperforms than using much fewer tokens in the input of LLMs.

### 5 Conclusion

In this paper, we have revisited the role of retrieval-augmented generation (RAG) in the era of long-context language models (LLMs). While recent trends have favored long-context LLMs over RAG for their ability to incorporate extensive text sequences, our research challenges this perspective. We argue that extremely long contexts in LLMs can lead to a diminished focus on relevant information, potentially degrading answer quality in question-answering tasks. To address this issue, we proposed the order-preserve retrieval-augmented generation (OP-RAG) mechanism. Our extensive experiments on public benchmarks have demonstrated that OP-RAG significantly improves the