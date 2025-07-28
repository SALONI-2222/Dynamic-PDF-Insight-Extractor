# Dynamic-PDF-Insight-Extractor

# 📄 Dynamic PDF Insight Extractor

This project processes a folder of PDF documents, categorizes meaningful content, and generates dynamic JSON outputs tailored for specific user personas and tasks. It is especially suited for persona-driven document intelligence challenges (e.g., hackathons).

---

## 🧠 Core Functionality

1. **Generate Input Metadata**: Creates a `challenge1b_input.json` file describing the document set and persona.
2. **PDF Text Extraction**: Extracts paragraphs from PDFs using `PyMuPDF`, filtering only informative sentences.
3. **Categorization**: Classifies content into categories like *conversion*, *editing*, *forms*, *exporting*, etc.
4. **Output Generation**: Writes structured insights in `challenge1b_output.json`.

---

## 📂 Project Structure
├── main.py # Main script: generates input/output JSON from PDFs
├── requirements.txt # Python dependencies
├── Dockerfile # For containerized execution
├── input/ # Place input PDF files here
├── output/ # Output folder for JSON files

yaml
Copy
Edit

---

## 🐍 Local Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the script:

bash
Copy
Edit
python main.py
🐳 Docker Usage
Build the image:

bash
Copy
Edit
docker build -t pdf-insight-extractor .
Run the container:

bash
Copy
Edit
docker run --rm -v $PWD/input:/app/input -v $PWD/output:/app/output pdf-insight-extractor
🧾 Input Format
PDFs placed in the /input directory.

Each file will be listed in the generated challenge1b_input.json:

json
Copy
Edit
{
  "challenge_info": {
    "challenge_id": "round_1b_dynamic",
    "test_case_name": "acrobat_dynamic"
  },
  "documents": [
    {
      "filename": "doc1.pdf",
      "title": "doc1"
    }
  ],
  "persona": {
    "role": "HR professional"
  },
  "job_to_be_done": {
    "task": "Create and manage fillable forms for onboarding and compliance."
  }
}
📤 Output Format
The output file (challenge1b_output.json) contains:

json
Copy
Edit
{
  "metadata": {
    "input_documents": ["doc1.pdf"],
    "persona": "HR professional",
    "job_to_be_done": "Create and manage fillable forms...",
    "processing_timestamp": "2025-07-28T22:00:00"
  },
  "extracted_sections": [
    {
      "document": "doc1.pdf",
      "section_title": "Forms Insight",
      "importance_rank": 1,
      "page_number": 2
    }
  ],
  "subsection_analysis": [
    {
      "document": "doc1.pdf",
      "refined_text": "This form allows new hires to...",
      "page_number": 2
    }
  ]
}
✅ Categories Handled
conversion — e.g., "convert to PDF"

editing — e.g., "edit layout"

forms — e.g., "fill out form"

exporting — e.g., "save as Word"

sharing — e.g., "send or collaborate"

general — fallback

📚 Dependencies
PyMuPDF==1.22.5 – for reading and parsing PDFs

📝 Notes
Ignores short lines and non-informative content.

Designed to run entirely offline (no network calls).

Easy to extend with new classification categories.
