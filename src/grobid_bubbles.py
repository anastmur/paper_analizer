from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def grobid_bubbles(xml_out):

    xml_results = [f for f in listdir(xml_out) if isfile(join(xml_out, f))] # Takes all results by grobid

    text = ""

    for xml_file in xml_results:
        source = join(xml_out,xml_file)
        tree = ET.parse(source)

        root = tree.getroot()

        p = root.find("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}profileDesc/{http://www.tei-c.org/ns/1.0}abstract/{http://www.tei-c.org/ns/1.0}p")

        text += p.text

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the generated word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
