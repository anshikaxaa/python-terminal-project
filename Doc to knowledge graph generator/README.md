# Document-to-Knowledge Graph Generator

This project is a system to convert unstructured documents (PDF, Word, text) into a knowledge graph using Google Gemini API for entity extraction and RDFLib for graph generation.

## Tech Stack

- FastAPI (Python) for backend API
- Google Gemini API for NLP entity & relationship extraction
- RDFLib for knowledge graph generation
- PyPDF2 for PDF parsing
- python-docx for DOCX parsing

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd doc-to-knowledge-graph-generator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up Google Gemini API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Set the environment variable:
     ```bash
     export GEMINI_API_KEY=your_api_key_here
     ```

## Running the Application

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

- `GET /`: Root endpoint with welcome message
- `POST /upload/`: Upload a document (PDF, DOCX, TXT) for processing
- `GET /graph/{filename}`: Retrieve the knowledge graph for a processed document

## Usage Example

1. Upload a document:
   ```bash
   curl -X POST "http://127.0.0.1:8000/upload/" -F "file=@sample.pdf"
   ```

2. Get the knowledge graph:
   ```bash
   curl "http://127.0.0.1:8000/graph/sample.pdf"
   ```

## Project Status

- [x] Initial FastAPI setup and repo structure
- [x] Document upload endpoint with parsing (PDF, DOCX, TXT)
- [x] Gemini API integration for entity extraction
- [x] Generate knowledge graph using RDFLib
- [x] Add endpoint to retrieve knowledge graph

## Future Enhancements

- Graph database integration (GraphDB)
- Query API
- Graph visualization (React + D3.js)
- Docker setup
