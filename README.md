# AI_TODAY
Multipage Dash app showing Interactive Charts on Artificial Intelligence trends.
## App purpose
Multipage Dash app  showing Interactive Charts on Artificial Intelligence trends.<br>
Each page focus on different topic<br>
Final Goal is to embed AI capabilities to generate plots description on demand<br>
Data insights can be generated through Langchain Pandas Agents than interact with Pandas Dataframes.<br>
llm model gpt-4 is used under the hood. You need to have proper OPEN_AI_API suitable to run this model.<br>
the Agent has been tested with gpt-3.5-turbo but with lower insights quality and success rate.<br>



## App structure

```bash
dash-app-structure

|-- .env
|-- .gitignore
|-- License
|-- README.md
|-- assets  
|-- components
|   |-- get_components_page1.py
|   |-- get_components_page2.py
|   |-- get_components_page3.py
|-- pages
|   |-- home.py
|   |-- Technical Perfomances.py
|   |-- Industry and Domains.py
|   |-- Society.py
|   |-- About the Author.py
|-- utils
|   |-- settings.py
|-- MainApp.py
|-- requirements.txt

```

<br>

## utils
code to retrieve the environment vars (OPENAI_API_KEY)
## components
data prep and vizs code for each page. Each page is stand-alone
## pages
page layout code and callbacks
## python version
python310
