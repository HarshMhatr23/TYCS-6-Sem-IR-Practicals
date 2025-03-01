from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
document = ["some land is hill",
            "some mammals are flurry",
            "cats are the mammals",
            "mountains are some land",
            "peoples are human",
            "humans are good persons"]


vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(document)

num_cluster = 3
kmeans = KMeans(n_clusters = num_cluster, random_state=42)
kmeans.fit(tfidf_matrix)

labels = kmeans.labels_
for i , doc in enumerate(document):
     print(f"Documnets{i+1}:{doc}")
     print(f"Cluter:{labels[i]}\n")
silhouette_avg=silhouette_score(tfidf_matrix,labels)
print(f"Silhouette Score:{silhouette_avg:3f}")
     
