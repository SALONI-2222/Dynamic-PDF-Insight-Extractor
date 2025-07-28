import os
import json
import fitz  # PyMuPDF
from datetime import datetime
from collections import defaultdict

# Step 1: Generate input JSON dynamically
def generate_input_json(pdf_dir, output_path, persona="HR professional", job_task="Create and manage fillable forms for onboarding and compliance."):
    documents = []
    for file in os.listdir(pdf_dir):
        if file.lower().endswith(".pdf"):
            documents.append({
                "filename": file,
                "title": os.path.splitext(file)[0]
            })

    input_data = {
        "challenge_info": {
            "challenge_id": "round_1b_dynamic",
            "test_case_name": "acrobat_dynamic",
            "description": "Dynamic PDF content processing"
        },
        "documents": documents,
        "persona": {
            "role": persona
        },
        "job_to_be_done": {
            "task": job_task
        }
    }

    with open(output_path, "w") as f:
        json.dump(input_data, f, indent=2)
    return input_data

# Step 2: Extract text from PDFs
def extract_text_from_pdfs(pdf_dir):
    categorized = defaultdict(list)
    for file in os.listdir(pdf_dir):
        if file.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_dir, file)
            doc = fitz.open(filepath)
            for page_num, page in enumerate(doc, start=1):
                text = page.get_text()
                for para in text.split("\n"):
                    para = para.strip()
                    if len(para.split()) > 6:  # only keep meaningful sentences
                        key = classify_paragraph(file.lower(), para)
                        categorized[key].append({
                            "file": file,
                            "page": page_num,
                            "text": para
                        })
    return categorized

# Step 3: Classify paragraph based on file name or keywords
def classify_paragraph(filename, paragraph):
    text = paragraph.lower()
    if "convert" in text or "create pdf" in text:
        return "conversion"
    elif "edit" in text or "format" in text:
        return "editing"
    elif "export" in text or "save as" in text:
        return "exporting"
    elif "fill" in text or "sign" in text or "form" in text:
        return "forms"
    elif "share" in text or "collaborate" in text:
        return "sharing"
    else:
        return "general"

# Step 4: Build output JSON dynamically
def generate_output(categorized, input_json, output_json):
    with open(input_json) as f:
        context = json.load(f)

    extracted_sections = []
    subsection_analysis = []

    # Take first 1-2 paragraphs per category for insights
    rank = 1
    for category, entries in categorized.items():
        for item in entries[:2]:
            extracted_sections.append({
                "document": item["file"],
                "section_title": f"{category.title()} Insight",
                "importance_rank": rank,
                "page_number": item["page"]
            })
            subsection_analysis.append({
                "document": item["file"],
                "refined_text": item["text"][:400],
                "page_number": item["page"]
            })
            rank += 1

    final_output = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in context["documents"]],
            "persona": context["persona"]["role"],
            "job_to_be_done": context["job_to_be_done"]["task"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open(output_json, "w") as f:
        json.dump(final_output, f, indent=2)

# Step 5: Run
if __name__ == "__main__":
    
    input_dir = "input"
    os.makedirs("output", exist_ok=True)

    input_json_path = "output/challenge1b_input.json"
    output_json_path = "output/challenge1b_output.json"
    
    #  TO WORK WITH THE INPUT OF INPUT2
    #input_dir = "input2"
    #os.makedirs("output2", exist_ok=True)

    #input_json_path = "output2/challenge1b_input.json"
    #output_json_path = "output2/challenge1b_output.json"
    
    #  TO WORK WITH THE INPUT OF INPUT3
    #input_dir = "input3"
    #os.makedirs("output3", exist_ok=True)

    #input_json_path = "output3/challenge1b_input.json"
    #output_json_path = "output3/challenge1b_output.json"

    # Generate dynamic input.json
    generate_input_json(input_dir, input_json_path)

    # Extract categorized text
    categorized_text = extract_text_from_pdfs(input_dir)

    # Generate dynamic output.json
    generate_output(categorized_text, input_json_path, output_json_path)
