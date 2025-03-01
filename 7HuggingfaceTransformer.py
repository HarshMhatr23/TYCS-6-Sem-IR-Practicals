from transformers import pipeline
summarizer = pipeline("summarization",model="facebook/bart-large-cnn")

text= """
Quantum computing is one of the most exciting fields of modern technology. it aims to use the principles of quantum mechanics to perform calculations at
speeds far beyond those of traditional computers. While classical computers rely on binary bits (0s and 1s), quantum computers use
quantum bits, or qubits, which can exits in mutiple states simultanrously, thanks to superposition.
This , prperty , combined with quantum entanglement, allows quantum computers to solve certian problems exponentially faster than thier
classical counterparts. However , the devlopment of quantum computing is still in its early stages, and significant technical challenges
remain, such as error correctio and qubit coherence. Despite these hurdles, the potential applications of quantum computing in areas
like cryptography, drugs discovery, and optimization are vast ,and reasearchers are optimistics about the future """

summary = summarizer(text,max_length= 100 , min_length= 50 , do_sample=False)
print("Summarizaton Model Used:",summarizer.model.name_or_path)
print("\n Summary of the Text:")
print(summary[0]['summary_text'])
