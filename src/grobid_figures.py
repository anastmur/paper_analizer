from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join

def grobid_figures(xml_out):

    xml_results = [f for f in listdir(xml_out) if isfile(join(xml_out, f))] # Takes all results by grobid

    n_of_figures = []

    for xml_file in xml_results:
        source = join(xml_out, xml_file)
        tree = ET.parse(source)

        root = tree.getroot()

        n = len(root.findall("./{http://www.tei-c.org/ns/1.0}text/{http://www.tei-c.org/ns/1.0}body/{http://www.tei-c.org/ns/1.0}figure"))
        n_of_figures.append({xml_file : n})

    return n_of_figures