# Rationale

This document explains the reasons behind the solutions proposed by this Software and how the results have been validated.

## Table of contents

- [Rationale](#rationale)
  - [Table of contents](#table-of-contents)
  - [Extracting metadata and parsing the results](#extracting-metadata-and-parsing-the-results)
  - [Creation of the wordcloud](#creation-of-the-wordcloud)
  - [Counting the figures](#counting-the-figures)
  - [Creating the list of links](#creating-the-list-of-links)


## Extracting metadata and parsing the results
Grobid has been used to extract metadata from the PDF files. The resulting XML files were parsed using the [Python ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html).

## Creation of the wordcloud
The code takes the abstract of each paper and unites all texts creating one big text that is then given to the [wordcloud](https://pypi.org/project/wordcloud/) python library to generate the final wordcloud based on all the abstracts.

The way the results have been validated is by simply manually comparing the results of the wordcloud with the abstracts of the papers used.

## Counting the figures
With Grobid, the full text of the papers is taken, then parsed to find all figures, which are identified as such in the XML files.

The number of figures that appears in the text has been checked to be the actual amount of figures in the paper. 
## Creating the list of links
The links are taken from the References sections of the papers. Links are identified by the Grobid processing, which allows them to be easily extracted.

The links found by the program have been checked to correspond with the ones found in the References sections of the papers.
