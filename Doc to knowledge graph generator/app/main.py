from fastapi import FastAPI, File, UploadFile, HTTPException
import os
from app.services.document_parser import parse_document
from app.services.gemini_service import extract_entities
from app.services.knowledge_graph_service import create_knowledge_graph, serialize_graph

app = FastAPI(title="Document to Knowledge Graph Generator")

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# In-memory storage for graphs
graphs = {}

@app.get("/")
async def root():
    return {"message": "Welcome to the Document to Knowledge Graph Generator API"}

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    allowed_extensions = {".pdf", ".docx", ".txt"}
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()
    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Unsupported file type")
    file_location = os.path.join(UPLOAD_DIR, filename)
    with open(file_location, "wb") as f:
        content = await file.read()
        f.write(content)

    # Parse the document
    text = parse_document(file_location)

    # Extract entities
    entities = extract_entities(text)

    # Generate knowledge graph
    graph = create_knowledge_graph(entities)
    graphs[filename] = graph

    return {
        "filename": filename,
        "message": "File uploaded and processed successfully",
        "entities": entities
    }

@app.get("/graph/{filename}")
async def get_graph(filename: str, format: str = "turtle"):
    if filename not in graphs:
        raise HTTPException(status_code=404, detail="Graph not found")
    graph = graphs[filename]
    serialized = serialize_graph(graph, format)
    return {"filename": filename, "graph": serialized}
