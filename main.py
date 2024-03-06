import sys
import os
sys.path.append('src')
from grobid_bubbles import *
from grobid_figures import *
from grobid_links import *


PAPERS = 'papers'
CONFIG = 'config.json'
XML_OUT = 'out'
BUBBLES_OUT = "headers"
FIGURES_OUT = "fulltexts"
LINKS_OUT = "references"

bubbles_path = os.path.join(XML_OUT, BUBBLES_OUT)
figures_path = os.path.join(XML_OUT, FIGURES_OUT)
links_path = os.path.join(XML_OUT, LINKS_OUT)

print(bubbles_path)
print(figures_path)
print(links_path)

grobid_client = GrobidClient(config_path=CONFIG)
grobid_client.process("processHeaderDocument", PAPERS, output=bubbles_path)
grobid_client.process("processFulltextDocument", PAPERS, output=figures_path)
grobid_client.process("processReferences", PAPERS, output=links_path)

grobid_bubbles(xml_out=bubbles_path)
num_figures = grobid_figures(xml_out=figures_path)
print(num_figures)
all_links = grobid_links(xml_out=links_path)
print(all_links)
