[Figure: Two line charts comparing Llama3.1-8B and Llama3.1-70B on EN.QA (F1 score) and EN.MC (Accuracy) versus context length (K).]

Figure 3: The influence of context length on the performance of RAG. The evaluations are conducted on En.QA and EN.MC datasets of ∞Bench.

where cos(·, ·) denotes the cosine similarity function and emb(·) denotes the embedding function.

We retrieve the top k chunks with the highest similarity scores with the query and denote the indices of top k chunks by 𝒥 = {j_i}^k_{i=1}. We preserve the order of chunks in the original long context d, that is, we constrain

j_l > j_m ⇔ l > m. (2)

Figure 2 visualizes the difference between the vanilla RAG and the proposed order-preserve RAG. Different from vanilla RAG placing the chunks in the order of similarity descending, the proposed order-preserve RAG keep the order of chunks in the original document.

# 4 Experiments

## 4.1 Datasets.

We conduct experiments on EN.QA and EN.MC datasets of ∞Bench (Zhang et al., 2024) benchmark, specially designed for long-context QA evaluation. To be specific, En.QA consists of 351 human-annotated question-answer pairs. On average, the long context in En.QA contains 150,374 words. We use F1-score as metric for evaluation on En.QA. EN.MC consists of 224 question-answer pairs, which are annotated similarly to En.QA, but each question is provided with four answer choices. On average, the long context in En.MC contains 142,622 words. We use accuracy as metric for evaluation on En.QA. We notice there is another benchmark termed LongBench (Bai et al., 2023). Nevertheless, the average context length of LongBench is below 20K words, which is not long enough to evaluate the recent long-context LLMs supporting 128K-token window size.

## 4.2 Implementation details.

We set the chunk size as 128 tokens on all datasets. Chunks are non-overlapped. We use BGE-large-en-v1.5 (Xiao et al., 2023) to extract the embedding of queries and chunks, by default.

## 4.3 Ablation Study

**The influence of context length.** We evaluate the influence of the context length on the performance of the proposed order-preserve RAG. Since each chunk contains 128 tokens, the context length is 128m, where m is the number of the retrieved chunks as the context for generating the answer. As shown in Figure 3, as the context length increases, the performance initially increases. This is because more context might have a greater chance of covering the relevant chunk. Nevertheless, as the context length further increases, the answer quality drops since more irrelevant chunks are used as distractions. To be specific, Llama3.1-8B model achieves the performance peak when the context length is 16K on both EN.QA dataset and EN.MC dataset, whereas the best performance of Llama3.1-70B model is achieved at 48K on EN.QA and 32K on EN.MC. The fact that the peak point of Llama3.1-70B comes later than Llama3.1-8B model might be because the larger-scale model has a stronger capability to distinguish the relevant chunks from