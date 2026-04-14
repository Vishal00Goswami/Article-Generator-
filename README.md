# Article-Generator
### Article Generator using LangGraph, Ollama, and Streamlit

This project is a simple AI-powered article generator built using LangGraph workflow, Ollama models, and Streamlit UI.

**How it works**
1. The user enters a topic in the Streamlit interface.
2. The topic is passed into a LangGraph workflow.
3. The first node generates an outline for the given topic using the Ollama model.
4. The second node uses that outline to generate a complete article.
5. The final article is displayed on the web interface.
   
**Tech Stack**
1. LangGraph (for workflow orchestration)
2. Ollama (LLM for text generation)
3. Streamlit (frontend UI)

This project demonstrates how to chain multiple LLM steps into a structured workflow to generate better and more organized content.


<img width="1919" height="1014" alt="Screenshot 2026-04-14 201638" src="https://github.com/user-attachments/assets/fd59fe21-448d-4d0b-b28d-aaf55372f809" />
<img width="1915" height="1014" alt="Screenshot 2026-04-14 201654" src="https://github.com/user-attachments/assets/5cddde88-c585-4640-8f38-8a77e81e9cd8" />
<img width="1919" height="1000" alt="Screenshot 2026-04-14 201709" src="https://github.com/user-attachments/assets/93bb823d-d06b-4a97-8db6-c894ec651ac6" />



