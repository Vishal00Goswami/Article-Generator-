from langgraph.graph import StateGraph, START, END 
from langchain_ollama import ChatOllama
from typing import TypedDict 

# create model 
model = ChatOllama(model="llama3.2:1b")

# define state 
class BlogState(TypedDict):
    Topic : str 
    outline : str 
    article : str 

# define functions for generating outline of article 
def gen_outline(state : BlogState) -> BlogState:
    prompt = f"Generate an outline for a article on the topic: {state['Topic']}"
    outline = model.invoke(prompt).content
    state['outline'] = outline 

    return state 

# define functions for generating article 
def gen_article(state : BlogState) -> BlogState:
    topic = state['Topic']
    outline = state['outline'] 
    prompt = f"Generate an article on: {topic} \n\nBased on outline:\n{outline}"
    article = model.invoke(prompt).content

    state['article'] = article 
    return state


# define state graph 
graph = StateGraph(BlogState) 

# add nodes 
graph.add_node('gen_outline', gen_outline)
graph.add_node('gen_article', gen_article)
# add edges
graph.add_edge(START,'gen_outline')
graph.add_edge('gen_outline','gen_article')
graph.add_edge('gen_article',END)

# compile the graph into a workflow
workflow = graph.compile()

