# **Lectura**

## **Overview**
The **Lecture Summarizer** is an AI-powered tool designed to extract, transcribe, and summarize lecture videos into structured and well-organized content. It leverages speech-to-text transcription, optical character recognition (OCR), and large language models (LLMs) to generate concise lecture notes. The summarized content is then formatted into a structured PDF for easy reference.

## **Features**
- **Speech-to-Text Transcription:** Converts spoken content from lectures into text using Whisper ASR.
- **OCR for Board Content:** Extracts text from slides, whiteboards, and handwritten notes.
- **LLM-Based Summarization:** Utilizes AI models (Gemini Pro) to generate structured and concise notes.
- **PDF Generation:** Creates well-formatted PDF documents with key points from the summarized content.
- **Efficient Text Processing:** Implements intelligent text chunking to limit the output to approximately three pages.
- **Automated Quiz Generation:** Extracts key points from the summary and formulates five important questions.

## **Project Structure**
```
Lecture-Summarizer/
│── Audio_Processing/
│   │── Convert.py          # Converts lecture videos to audio
│   │── Helper.py           # Handles transcription logic
│   │── Transcribe.py       # Main transcription module
│
│── Video_Processing/
│   │── Main_keyframes.py   # Extracts keyframes from video
│   │── OCR_Helper.py       # Performs OCR on extracted keyframes
│
│── Summarization/
│   │── Summary.py          # Generates structured summaries using LLM
│
│── Quiz_Thing/
│   │── Quiz.py             # Generates five important questions from summarized content
│   │── quiz_questions.json  # Stores generated quiz questions
│
│── templates/
│   │── index.html
│
│── requirements.txt        # Project dependencies
│── README.md               # Project documentation
│── APP.py                  # Main script to run the summarization pipeline
```

### **Install dependencies:**
```bash
pip install -r requirements.txt
```

### **Run the Lecture Summarizer:**
```bash
python APP.py
```

## **How It Works**
### **1. Audio & Visual Content Extraction**
- Converts lecture videos into audio.
- Extracts keyframes from the video.

### **2. Text Extraction**
- Uses Whisper ASR to transcribe spoken content.
- Runs OCR on keyframes to extract text from slides and boards.

### **3. Summarization**
- Merges transcribed speech and extracted text.
- Uses LLM (Gemini Pro) to summarize content into structured notes.
- Limits summaries to approximately three pages.

### **4. PDF Generation**
- Converts the summarized content into a structured PDF.

### **5. Automated Quiz Generation**
- Extracts key information from the summary.
- Generates five relevant questions.
- Stores quiz questions in `quiz_questions.json`.

## **Results**
- Organized lecture notes with clear headings, bullet points, and key takeaways.
- PDF output for easy sharing and reference.
- Automatically generated quiz questions to test comprehension.

## **Future Improvements**
- **Speaker Identification:** Differentiating multiple speakers in transcriptions.
- **Diagram & Chart Recognition:** Enhancing visual content extraction.
- **Expanded LLM Support:** Integration with models like GPT-4 and Claude for improved summarization.


## **Contact**
For any queries, reach out priyadharshininrs@gmail.com


