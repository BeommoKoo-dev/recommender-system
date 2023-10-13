# Example Code for testing t-SNE
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Generate 100 random 5-dimensional word vectors
word_vectors = np.random.rand(100, 5)

# Generate some sample words for the labels
words = [f'word{i}' for i in range(100)]

# Perform t-SNE
tsne = TSNE(n_components=2, random_state=0)
word_vectors_2d = tsne.fit_transform(word_vectors)

# Plot the word vectors in 2D space
plt.figure(figsize=(10, 10))
plt.scatter(word_vectors_2d[:, 0], word_vectors_2d[:, 1])

# Add labels to the points
for word, (x, y) in zip(words, word_vectors_2d):
    plt.annotate(word, (x, y), alpha=0.5)

plt.title('t-SNE Visualization of Word Vectors')
plt.show()
