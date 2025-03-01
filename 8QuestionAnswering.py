from transformers import pipeline
qa = pipeline("question-answering",model="deepset/roberta-base-squad2")
text = """Quantum computing is one of the most exciting fields of modern technology. It aims to use the principles of quantum mechanics 
to perform calculations at speeds far beyond those of traditional computers. While classical computers rely on binary bits 
(0s and 1s), quantum computers use quantum bits, or qubits, which can exist in multiple states simultaneously, thanks to 
superposition. This property, combined with quantum entanglement, allows quantum computers to solve certain problems exponentially 
faster than their classical counterparts. However, the development of quantum computing is still in its early stages, and significant 
technical challenges remain, such as error correction and qubit coherence. Despite these hurdles, the potential applications of 
quantum computing in areas like cryptography, drug discovery, and optimization are vast, and researchers are optimistic about its future.
"""

question1 = "What is quantun computing"
question2 = "What are the potential applications of qunatum computing?"
question3 = "What challenges does quantum computing face?"

answer1 = qa(question=question1,context=text)
answer2 = qa(question=question2,context=text)
answer3 = qa(question=question3,context=text)

print("Question Answring Model Used:",qa.model.name_or_path)
print("\n Question 1:", question1)
print("Answer:", answer1['answer'])
print("\nQuestion 2:",question2)
print("Answer:", answer2['answer'])
print("\nQuestion 3:",question3)
print("Answer:", answer3['answer'])
