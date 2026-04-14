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
