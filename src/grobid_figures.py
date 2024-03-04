from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join

client = GrobidClient(config_path='./config.json')
client.process("processFulltextDocument", "./example_papers", output="./out")


xml_results = [f for f in listdir('out') if isfile(join('out', f))] # Takes all results by grobid

for xml_file in xml_results:
    source = join('out',xml_file)
    tree = ET.parse(source)

    root = tree.getroot()

    n_of_figures = len(root.findall("./{http://www.tei-c.org/ns/1.0}text/{http://www.tei-c.org/ns/1.0}body/{http://www.tei-c.org/ns/1.0}figure"))
    print(n_of_figures)

    # Y ahora cuenta figuras