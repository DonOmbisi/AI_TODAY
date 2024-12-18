import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback, State, ctx
import dash

# import plotly.express as px
# import pandas as pd

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent # type: ignore
from langchain_openai import ChatOpenAI, OpenAI # type: ignore

# local imports
from components.get_components_page1 import get_components_page1
from utils.settings import getEnvVar

# env variables
API_KEY = getEnvVar()

# get data and viz
dfList, vizList, tableList = get_components_page1()

dash.register_page(__name__, path="/page-1", order=1)


plot = dbc.Container(
    children=[
        dcc.Graph(
            figure=vizList[0],
            id="plot-id",
            style={"backgroundColor": "#254e6f", "height": "50vh"},
        ),
    ],
    fluid=True,
)

collapse = dbc.Container(
    [
        dbc.Button(
            "Show Data Table",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            children=[tableList[0]],
            id="collapse",
            is_open=False,
        ),
    ]
)
layout = (
    dbc.Container(
        [
            dbc.Row(
                [
                    dcc.Markdown(
                        "# Technical Performances", style={"textAlign": "left"}
                    ),
                    html.Hr(),
                    dbc.Pagination(
                        id="pagination", max_value=len(vizList), active_page=1
                    ),
                    html.Hr(),
                ],
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [dbc.Container([plot], id="pagination-contents", className="")],
                        width=10,
                    )
                ]
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            collapse,
                        ],
                        width=10,
                    )
                ]
            ),
            html.Hr(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Markdown(
                                "#### Any question?... ask to the AI\n",
                                style={"textAlign": "left", "white-space": "pre"},
                            ),
                            dbc.Input(
                                id="input-id",
                                placeholder="Type your question...",
                                type="text",
                            ),
                            dbc.Col(
                                [
                                    dbc.Button(
                                        id="btn",
                                        children="Get Insights",
                                        className="m-3",
                                    ),
                                    dbc.Button(
                                        id="btn-reset",
                                        children="Reset",
                                        className="m-3",
                                    ),
                                ],
                            ),
                            html.Br(),
                            dcc.Loading(children=html.P(id="output-id")),
                        ],
                        width=10,
                    ),
                ]
            ),
        ],
    ),
)


@callback(
    Output("plot-id", "figure"),
    [Input("pagination", "active_page")],
    prevent_initial_call=True,
)  # [Input("page-change", "value")])
def change_page(active_page):
    return vizList[active_page - 1]


@callback(
    Output("collapse", "is_open"),
    Output("collapse", "children"),
    [Input("collapse-button", "n_clicks")],
    [
        State("collapse", "is_open"),
        State("pagination", "active_page"),
    ],
    prevent_initial_call=True,
)
def toggle_collapse(n, is_open, active_page):
    if n:
        return not is_open, tableList[active_page - 1]


@callback(
    Output("output-id", "children"),
    [Input("btn", "n_clicks"), Input("btn-reset", "n_clicks")],
    State("pagination", "active_page"),
    State("input-id", "value"),
    prevent_initial_call=True,
)
def data_insights(
    _,
    _reset,
    active_page,
    value,
):
    button_clicked = ctx.triggered_id
    if button_clicked == "btn":
        chat = ChatOpenAI(openai_api_key=API_KEY, model_name="gpt-4", temperature=0.0)
        dataset = dfList[active_page - 1]
        agent = create_pandas_dataframe_agent(chat, dataset, verbose=True)
        if value is None:
            resp_output = "no question provided"
        else:
            question = f"{value}"
            try:
                response = agent.invoke(question)
                resp_output = f"{response['output']}"
            except:
                resp_output = "Sorry, your question is out of context"
        return resp_output
    elif button_clicked == "btn-reset":
        return ""
