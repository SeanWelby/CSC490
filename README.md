# LiveJournal Social Network Analysis

## Overview
This project aims to analyze large-scale social networks to identify influential individuals using Python programming and advanced network analysis tools. The primary focus is on the LiveJournal dataset from the SNAP (Stanford Network Analysis Project).

## Goals
- Use Python to analyze large social networks.
- Identify influential people within these networks.

## Resources
- [SNAP.py](https://snap.stanford.edu/snappy/index.html)
- [SNAP.py tutorial](https://snap.stanford.edu/snappy/doc/tutorial/index-tut.html)
- [SNAP Dataset - LiveJournal](https://snap.stanford.edu/data/soc-LiveJournal1.html)
- [Relative Documents](http://www.cs.cornell.edu/home/kleinber/kdd06-comm.pdf)
- [Relative Documents](http://arxiv.org/abs/0810.1355)

## Week-by-Week Progress

### Week of 5/27/2024
- Conducted initial research on the SNAP project and its datasets.
- Encountered installation issues with the SNAP project due to Python version incompatibility.
- Resolved by using Anaconda Navigator to create an environment with Python 3.8.19 for installing the SNAP project.

### Week of 6/3/2024
- Selected the LiveJournal dataset for analysis.
- Developed a Python script to perform basic analyses like calculating the number of nodes and edges, degree distribution, and identifying connected components.
- Visualized results using Matplotlib.

### Week of 6/10/2024
- Downloaded an updated version of the LiveJournal dataset.
- Created a NetworkX graph from the dataset and calculated influence metrics.
- Identified Node 37356 as the most influential node in both datasets from June 11 and June 16.

### Week of 6/17/2024
- Further analysis using Karate Club and the DeepWalk algorithm for node embedding.
- Calculated PageRank scores to identify influential nodes based on their structural importance within the network.
- Found Node 4362 as the most influential node using DeepWalk embeddings, contrasting with Node 37356 identified using traditional metrics.

### Week of 6/24/2024
- Applied Karate Club to analyze the LiveJournal Twitter dataset.
- Demonstrated the effectiveness of Karate Club and DeepWalk in identifying influential nodes through advanced graph analysis techniques.

## Summary
This project successfully explored the LiveJournal Twitter dataset using Python and advanced graph analysis techniques. By employing tools like Karate Club, influential nodes were identified, providing insights into their structural importance and connectivity patterns. The research highlighted the differences in influential nodes identified through traditional metrics versus advanced embedding techniques like DeepWalk. This underscores the importance of using diverse analytical methods for a comprehensive understanding of network influence.


## Installation
1. Install Anaconda Navigator.
2. Create a new environment with Python 3.8.19:
   ```bash
   conda create -n SnapEnv python=3.8.19
   conda activate SnapEnv
3. Install SNAP
   pip install snap-stanford
5. Install Karate Club
   pip install karateclub
