# PshahLab snippets

Small, runnable code from the PshahLab "Tech in 60" Shorts. One flat file per episode, named `epNNN-<topic>.<ext>`. The video's description says which file to open.

| Episode | File | What it shows | Run |
| --- | --- | --- | --- |
| ep-016 | [ep016-retrieve.py](ep016-retrieve.py) | The retrieval step of RAG as a toy: pick the document that shares the most words with the question | `python3 ep016-retrieve.py` |
| ep-017 | [ep017-metadata-filter.py](ep017-metadata-filter.py) | Filter chunks by metadata (company, quarter) before ranking, so the right chunk wins | `python3 ep017-metadata-filter.py` |

These are teaching toys, not production code. Licensed under MIT (see LICENSE).
