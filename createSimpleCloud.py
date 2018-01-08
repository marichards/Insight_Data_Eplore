from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create the cloud from a bag of words ('words') and plot it
my_cloud = WordCloud().generate(words)

plt.imshow(my_cloud, interpoloation = 'bilinear')
plt.axis("off")
plt.show()
