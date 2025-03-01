import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity(x,y):
    if len(x)!=len(y):
        return None
    dot_product=np.dot(x,y)
    print("dot product is of goven x and y:", {dot_product})
    magnitude_x = np.sqrt(np.sum(x**2))    
    print("Magnitude of x:", magnitude_x)
    magnitude_y = np.sqrt(np.sum(y**2))
    print("Magnitude of y:", magnitude_y)
    cosine_similarity = dot_product/(magnitude_x * magnitude_y)
    return cosine_similarity
corpus=['data science is one of the most important field of science','this is one of the best data science courses','data Scientists analyse data']
x = CountVectorizer().fit_transform(corpus).toarray()
print(x)
cos_sim1_2 = cosine_similarity(x[0,:],x[1,:])
cos_sim1_3 = cosine_similarity(x[0,:],x[2,:])
cos_sim2_3 = cosine_similarity(x[1,:],x[2,:])

print("cosine Similarities:")
print("\t Document1 and 2 :",cos_sim1_2)
print("\t Document1 and 3 :",cos_sim1_3)
print("\t Document2 and 3 :",cos_sim2_3)

