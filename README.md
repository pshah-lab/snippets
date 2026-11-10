# PshahLab snippets

Small, runnable code from the PshahLab "Tech in 60" Shorts. One folder per topic, named after the episode's subject, holding the code file shown in the video (named `epNNN-<topic>.<ext>`). The video's description says which folder and file to open.

| Episode | File | What it shows | Run |
| --- | --- | --- | --- |
| ep-016 | [rag-retrieval/ep016-retrieve.py](rag-retrieval/ep016-retrieve.py) | The retrieval step of RAG as a toy: pick the document that shares the most words with the question | `python3 rag-retrieval/ep016-retrieve.py` |
| ep-017 | [rag-metadata/ep017-metadata-filter.py](rag-metadata/ep017-metadata-filter.py) | Filter chunks by metadata (company, quarter) before ranking, so the right chunk wins | `python3 rag-metadata/ep017-metadata-filter.py` |

These are teaching toys, not production code. Licensed under MIT (see LICENSE).
