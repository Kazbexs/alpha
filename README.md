Project of Ziyagul Kazbek ge57tap@mytum.de

1.  Implementation of Alpha Algorithm: A Process Discovery Algorithm with Implementation of a Webservice
It takes the .xes file as input and generates a Petri Net model from Event-Log

2. I started to write my project on Python 3.8.8, but switched to 3.10.9 version, because I needed to use itertools.pairwise(iterable) function for my helper function for relations.find_directly_follows(log) to find all pairs of activities in a @directly follows relations
For the frontend I used HTML (flask-server/templates/index.html) and CSS (flask-server/static/main.css). The window should be opened as a Full Screen.

3. Requirements are written in requirements.txt
To activate the virtual environment: source venv/bin/activate
Install requirements in virtual environment: pip install -r requirements.txt
To run the main.py: python /Users/kazbexs/Documents/Project/kazbexs/flask-server/main.py

4. I wrote this project following the functional programming.
In relations.py there are helper functions to detect all Log Based Ordering Relations. I used this functions for fourth and fifth steps which form the core of the alpha algrithm. I used the itertools module very often, because it provides a necessary functions to find pairs, sequences, subsequences and some of them also returns the result as combination tuples.
In alpha.py you can find the steps of alpha algortihm
In operations.py there are helper functions for alpha algorithm.
In petrinet.net there is a function to build a Petri Net process model which is required as an output on our webservice. I used the Graphviz and the DOT Language. https://graphviz.org/doc/info/lang.html as recommended on slides. I created a petri_net list there, because it was needed to detect and save all activities (nodes) and transitions. I am using digraph because the edges between nodes have a direction.
In reader.py there are functions to detect all activities from .xes file and reader.read_data(data) returns an Event Log. I used the xml.etree.
ElementTree module here following the recomendations given in TUM-Moodle.
templates and static folders are for the frontend of my project. You can find index.html and main.css files there.
