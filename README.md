**BRENDAI**
Across most scientific fields, the quantity of data being made publicly available in large, global databases has substantially grown. Resources such as the Kyoto Encyclopedia of Genes and Genomes (KEGG), Global Natural Products Social Molecular Networking (GNPS), and the BRENDA enzyme database are populated by vast amounts of data in their respective biochemical niches. For instance, BRENDA contains over 8400 EC numbers alone, each of which can be further parsed to find data regarding their substrates, products, KM values, and more (“All enzymes in Brenda”). To navigate these large databases, researchers have developed effective online user interfaces by which users can easily reach specific data points (Chen et al. 2). However, for many who are not directly involved in the field, these interfaces can prove difficult to utilize to their full potential, often requiring a certain degree of domain knowledge to understand the results and their significance. Additionally, navigating these databases can be a tedious and cumbersome process, hindering the efficiency of researchers that may only want to access a small part of each enzyme’s page. 

Thus, large language models (LLMs) have the potential to revolutionize the methods by which scientists interact with and navigate through these large amounts of data. Large language models, like ChatGPT, are capable of taking a natural language prompt as input, analyze its meaning as a result of its context, and then produce a response that can be fine-tuned to suit a specific purpose. In a scientific setting, it should then be possible to leverage an LLM’s capabilities in order to easily and intuitively search through a database, such as BRENDA, and retrieve only the most relevant information for the user. 

BRENDAI is an LLM that is capable of processing natural language input, transforming the natural language input into a request for BRENDA’s SOAP API, and then returning those results in a natural language format. For instance, asking, “What is the pH stability of 5’-3’ DNA Helicase, EC number 5.6.2.3?” should result in the LLM returning “6.0-9.0.” To accomplish this, a multi-agent system (LLM-MA) (Guo et al. 2) was applied to the task, functioning as the primary architecture of the LLM tool.

**Instructions**
To run BRENDAI, simply first input your OPENAI API and LANGCHAIN API keys into their respective cells, and then run all cells in the Jupyter notebook provided, "llm_project.ipynb". 
Each cell, as commented, constructs the necessary agents/features using LangChain. 
To make a new call to the LLM, use:

'''
app = workflow.compile()
question = "What is the pH stability of 5’-3’ DNA Helicase, EC number 5.6.2.3?"
app.invoke({"messages":[("user",question)],"iterations":0})
'''

The LLM should then provide a response, formatted as a string at the end of the other messages shared between the agents.


**Known Issues**
Often, the agents will call incorrect function calls to the BRENDA API. In these cases, a query may need to be reworded or the agent's prompt adjusted to account for the edge case.


**Contact**
siavash_raissi@hms.harvard.edu
