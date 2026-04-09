[Figure: Two-panel line chart figure showing the influence of context length (x-axis, in K) on RAG performance. Left panel (a) EN.QA plots F1 score for Llama3.1-8B (blue circles) and Llama3.1-70B (orange triangles) across context lengths from about 4K to 96K; 8B peaks around 16K then declines, while 70B rises to the mid/high 40s and stays relatively high before tapering slightly. Right panel (b) EN.MC plots Accuracy for the same two models over similar context lengths; 8B peaks around 16K then declines, while 70B peaks around 24K–48K and then slowly decreases. Legends are shown inside each panel.]
Figure 3: The influence of context length on the performance of RAG. The evaluations are conducted on En.QA and EN.MC datasets of ∞Bench.

where cos(·, ·) denotes the cosine similarity func-
tion and emb(·) denotes the embedding function.

theless, the average context length of LongBench
is below 20K words, which is not long enough to
evaluate the recent long-context LLMs supporting
128K-token window size.

We retrieve the top k chunks with the highest
similarity scores with the query and denote the in-
dices of top k chunks by 𝒥 = {j_i}^k_{i=1}. We preserve
the order of chunks in the original long context d,
that is, we constrain

j_l > j_m  ⟺  l > m.

(2)

Figure 2 visualizes the difference between the
vanilla RAG and the proposed order-preserve RAG.
Different from vanilla RAG placing the chunks in
the order of similarity descending, the proposed
order-preserve RAG keep the order of chunks in
the original document.

## 4.2 Implementation details.

We set the chunk size as 128 tokens on all datasets.
Chunks are non-overlapped. We use BGE-large-en-
v1.5 (Xiao et al., 2023) to extract the embedding
of queries and chunks, by default.

## 4.3 Ablation Study

The influence of context length. We evaluate
the influence of the context length on the perfor-
mance of the proposed order-preserve RAG. Since
each chunk contains 128 tokens, the context length
is 128m, where m is the number of the retrieved
chunks as the context for generating the answer. As
shown in Figure 3, as the context length increases,
the performance initially increases. This is because
more context might have a greater chance of cover-
ing the relevant chunk. Nevertheless, as the context
length further increases, the answer quality drops
since more irrelevant chunks are used as distrac-
tions. To be specific, Llama3.1-8B model achieves
the performance peak when the context length is
16K on both EN.QA dataset and EN.MC dataset,
whereas the best performance of Llama3.1-70B
model is achieved at 48K on EN.QA and 32K on
EN.MC. The fact that the peak point of Llama3.1-
70B comes later than Llama3.1-8B model might
be because the larger-scale model has a stronger
capability to distinguish the relevant chunks from

## 4 Experiments

### 4.1 Datasets.

We conduct experiments on EN.QA and EN.MC
datasets of ∞Bench (Zhang et al., 2024) bench-
mark, specially designed for long-context QA eval-
uation. To be specific, En.QA consists of 351
human-annotated question-answer pairs. On av-
erage, the long context in En.QA contains 150,374
words. We use F1-score as metric for evaluation on
En.QA. EN.MC consists of 224 question-answer
pairs, which are annotated similarly to En.QA, but
each question is provided with four answer choices.
On average, the long context in En.MC contains
142,622 words. We use accuracy as metric for eval-
uation on En.QA. We notice there is another bench-
mark termed LongBench (Bai et al., 2023). Never-