PaperAnalizer
=============

|DOI|

Table of Contents
-----------------

-  `PaperAnalizer <#paperanalizer>`__

   -  `Table of Contents <#table-of-contents>`__
   -  `Introduction <#introduction>`__
   -  `Requirements <#requirements>`__

      -  `Python <#python>`__
      -  `Dependencies <#dependencies>`__
      -  `Grobid <#grobid>`__

         -  `Running Grobid <#running-grobid>`__

   -  `How to use <#how-to-use>`__

      -  `Steps <#steps>`__
      -  `Results <#results>`__

Introduction
------------

**PaperAnalizer** takes research papers an processes them, creating a
word cloud based on key words that can be found in the abstract, a list
of all the links that can be found in the selected papers and a file
that shows the number of figures per paper and the sum of all of them.
## Requirements ### Python The code runs on **Python 3.10^**, so it must
be installed in the system to be able to use PaperAnalizer. ###
Dependencies Dependencies can be installed by using
`Poetry <https://python-poetry.org/>`__. You simply must go to the root
directory of the repository and run:

::

   poetry install

Or install all dependencies with pip using requirements.txt in the root
directory of the repository by running:

::

   pip install -r requirements.txt

Grobid
~~~~~~

PaperAnalizer connects to a Grobid Server to analize the papers, so you
must install `Grobid
0.8.0 <https://grobid.readthedocs.io/en/latest/>`__. You should use one
of the available `Docker <https://www.docker.com/>`__ images to run
Grobid:

Full image: https://hub.docker.com/r/grobid/grobid

Light image: https://hub.docker.com/r/lfoppiano/grobid/

Running Grobid
^^^^^^^^^^^^^^

To run Grobid use either:

::

   docker run --rm --gpus all --init --ulimit core=0 -p 8070:8070 grobid/grobid:0.8.0

Or:

::

   docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0

Depending on which image you have downloaded.

How to use
----------

Steps
~~~~~

To correctly run PaperAnalizer you must follow the following steps:

1. In PDF format, put the papers you want to analize in the **papers/**
   folder, found in the root directory of the repository. There are some
   example papers already there.
2. Run a Grobid Server by using the commands described in `Running
   Grobid <#running-grobid>`__.
3. Run the **main.py** script with Python.

Results
~~~~~~~

After running the **main.py** script an image of a word cloud based on
the keywords found in the abstract will open up, it can either be saved
or simply closed. In the root directory of the repository two files will
be created: + **n_of_figures.txt**: which contains the number of figures
found per paper and the total amount of them. + **list_of_links.txt**:
which contains a list of all links found in the papers.

.. |DOI| image:: https://zenodo.org/badge/765249347.svg
   :target: https://zenodo.org/doi/10.5281/zenodo.10778312
