import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import dash


dash.register_page(__name__, path="/page-4", order=4)
layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Markdown("# About the Author", style={"textAlign": "left"}),
                        dcc.Markdown(
                            "\n\n"
                            "#### Artificial intelligence (AI) systems already greatly impact our lives.\n"
                            "#### DON MICHAEL OMBISI.\n"
                            "#### Here you will find charts of AI-related metrics and get AI-generated insights. \n"
                            "\n\n\n",
                            # "### Do you want to know more?... Let'chat with data!\n",
                            style={"textAlign": "left", "white-space": "pre"},
                        ),
                        html.Hr(),
                        html.Img(
                            src=dash.get_asset_url("DON.jpeg"),
                        ),
                        html.Hr(),
                    ],
                    width=8,
                )
            ]
        )
    ]
)
