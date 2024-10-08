#!/usr/bin/python
import getpass
import os
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph import END, MessageGraph
from langchain_core.output_parsers import StrOutputParser
from typing import Annotated, List, Tuple, Union


OPENAI_API_KEY = "#"
LANGCHAIN_API_KEY = "#"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
output_parser = StrOutputParser()


# model = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)

# graph = MessageGraph()

# prompt = ChatPromptTemplate.from_messages({
#     "system": "You are a robot who speaks in beeps and boops.",
#     "user": "{input}"
# })

# chain = prompt | model | output_parser

# adds "oracle" node to the model and then connects an edge to the end
# graph.add_node("oracle", chain)
# graph.add_edge("oracle", END)

# graph.set_entry_point("oracle")

# runnable = graph.compile()

# test_result = chain.invoke({"input": "When was Obama born?"})
# ---------------------------------------------------------------

# SIMPLE CHAT BOT WITH MEMORY:

# llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a robot who speaks with occasional beeps and boops."),
#     ("user", "{input}")
# ])

# output_parser = StrOutputParser()

# # output_parser transforms the output of the model just the string
# chain = prompt | llm | output_parser
# test = chain.invoke({"input":"When was Obama born?"})
# print(test)

# ---------------------------------------------------------------
# PARSER

from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder

llm = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, llm_model="gpt-4-turbo")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert at parsing information from requests regarding the BRENDA enzyme database. Based on \
     the BRENDA SOAP API documentation, analyze the following request and try to extrapolate EC numbers, organism names, and any other relevant \
     information for querying the API if possible. For instance, if the user mentions an enzyme, use background knowledge of the \
     BRENDA database to assign that an EC number.\
     Organism names should be rewritten as Binomial nomenclature. \
     Return the result in a JSON format. Make sure you specify the actual question/data being requested by the user in a field called \"data_requested:\". \
     Replace a field with None if nothing can be extrapolated for that field: "),
    ("user", "{input}"),
])

output_parser = StrOutputParser()

# output_parser transforms the output of the model just the string
chain = prompt | llm | output_parser
test1 = chain.invoke({"input":"What is the molecular weight of DNA-directed DNA polymerase in humans?"})

print(test1)