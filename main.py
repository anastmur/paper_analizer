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

grobid_client = GrobidClient(config_path=CONFIG)
grobid_client.process("processHeaderDocument", PAPERS, output=bubbles_path)
grobid_client.process("processFulltextDocument", PAPERS, output=figures_path)
grobid_client.process("processReferences", PAPERS, output=links_path)

num_figures = grobid_figures(xml_out=figures_path)
with open("n_of_figures.txt","w") as figures_file:
    figures_file.write("Number of figures per paper:\n")
    tot = 0
    for paper, num in num_figures:
        paper_name = paper.split(".")[0]
        figures_file.write(f"{paper_name}: {num} figure(s)\n")
        tot += num
    figures_file.write(f"Total number of figures is: {tot}")

all_links = grobid_links(xml_out=links_path)
with open("list_of_links.txt","w") as links_file:
    links_file.write("List of links:\n")
    for link  in all_links:
        links_file.write(f"{link}\n")

grobid_bubbles(xml_out=bubbles_path)