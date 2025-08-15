# python-rag-demo

Various RAG demos.

For example documents, I'm using the SPSS Modeler 18.5 docs which can be downloaded as PDFs from https://www.ibm.com/support/pages/spss-modeler-185-documentation.


## Basic Setup
Install Python 3 then install Ollama:
```
brew install ollama
```
Run the server:
```
ollama serve
```

In another command window, make sure the Ollama can run your chosen model e.g.:
```
ollama run mistral
```

## pdf_demo
Based on https://auscunningham.medium.com/build-a-local-ai-rag-app-with-ollama-and-python-96f9df9c2a3e

```
cd pdf_demo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Now run the example:
```
cd src
python3 main.py
```
