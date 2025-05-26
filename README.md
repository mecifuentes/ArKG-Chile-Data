# ArKG-Chile-DataPipeline
Collaborative tool that extracts archaeological data from scanned PDFs using LlamaParse and OpenAI's o4-mini API to populate archaeology knowledge graph database. Transforms complex archaeological documentation into structured CSV datasets for research and preservation effort

## Requirements

- Python 3.10 or higher
- GIT
- pip (Python package installer)
- LlamaParse API key
- OpenAI API key

## Installation
### Standard Python Installation

Clone this repository:
```
git clone https://github.com/mecifuentes/ArKG-Chile-Data.git
cd ArKG-Chile-Data
```
Create and activate a virtual environment (recommended):
```
# On Windows
python3 -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies:
```
pip install -r requirements.txt
```

### Set up API keys:
Create a .env file in the project root with your API keys:
```
LLAMA_CLOUD_API_KEY=your_llamaparse_key
OPENAI_API_KEY=your_openai_key
```

## Usage
This work consist in two steps, extraction of data and then format of data to save in a DB.

### Extraction of data
The entire logic of this step is contained in `pdf_extractor.py`.

This script deploys a graphic interface that allows the user select a Document, only .pdf for now, to extract the information.

There is an example of usage:
```
python pdf_extractor.py
```
