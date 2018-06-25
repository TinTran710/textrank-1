from summa import summarizer
from summa import keywords
import time

# text = 'Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another.'

with open('output1.txt', 'r') as myfile:
    data = myfile.read().replace('\n', '')
start_time = time.time()

print(keywords.keywords(data, 'vietnamese'))

elapsed_time = time.time() - start_time
print (elapsed_time)
# print(keywords.keywords(text))

