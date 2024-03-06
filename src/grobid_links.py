from grobid_client.grobid_client import GrobidClient
import xml.etree.ElementTree as ET
from os import listdir
from os.path import isfile, join

def grobid_links(xml_out):

    xml_results = [f for f in listdir(xml_out) if isfile(join(xml_out, f))] # Takes all results by grobid

    links = []

    for xml_file in xml_results:
        source = join(xml_out, xml_file)
        tree = ET.parse(source)

        root = tree.getroot()

        p = root.find("./{http://www.tei-c.org/ns/1.0}text/{http://www.tei-c.org/ns/1.0}back/{http://www.tei-c.org/ns/1.0}div/{http://www.tei-c.org/ns/1.0}listBibl/{http://www.tei-c.org/ns/1.0}biblStruct/{http://www.tei-c.org/ns/1.0}monogr/{http://www.tei-c.org/ns/1.0}ptr")
        if p is not None:
            links.append({xml_file : p.get('target')})

    return links