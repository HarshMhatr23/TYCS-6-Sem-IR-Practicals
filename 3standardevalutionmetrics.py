from sklearn.metrics import precision_score,recall_score,f1_score

ground_truth = [1,0,1,0,1,1,0,0,1,1]
print("ground_truth:", ground_truth)
predicted_relevance = [1,1,1,0,0,1,0,1,1,0]
print("predicted_relevance:", predicted_relevance)
precision = precision_score(ground_truth , predicted_relevance)
print("precision:", precision)
recall = recall_score(ground_truth, predicted_relevance)
print("recall",recall)
f1_score = f1_score(ground_truth , predicted_relevance)
print("f1_score:",f1_score)
