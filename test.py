# %%
print('Hello, world!')
# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import softmax

# Simulated dot products before scaling
np.random.seed(42)
dot_products = np.random.normal(loc=50, scale=15, size=100)

# Scaled dot products
d_k = 512  # Example embedding dimension
scaled_dot_products = dot_products / np.sqrt(d_k)

# Apply softmax
attention_no_scaling = softmax(dot_products)
attention_with_scaling = softmax(scaled_dot_products)

# Plot the attention distributions
plt.figure(figsize=(12, 6))

# Before scaling
plt.subplot(1, 2, 1)
plt.plot(attention_no_scaling, label='No Scaling', color='red')
plt.title('Attention Distribution (No Scaling)')
plt.xlabel('Movies')
plt.ylabel('Attention Score')
plt.legend()

# After scaling
plt.subplot(1, 2, 2)
plt.plot(attention_with_scaling, label='With Scaling', color='blue')
plt.title('Attention Distribution (With Scaling)')
plt.xlabel('Movies')
plt.ylabel('Attention Score')
plt.legend()

plt.tight_layout()
plt.show()

# %%
