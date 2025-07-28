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

