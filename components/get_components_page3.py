from dash import dash_table
import plotly.express as px
import pandas as pd


def get_components_page3():

    df1 = pd.read_csv("./data/views-ai-impact-society-next-20-years-2021.csv")

    df2 = pd.read_csv(
        "./data/global-views-ai-impact-society-next-20-years-by-demographic-group-2021.csv"
    )

    fig1 = px.bar(
        df1,
        y="Country",
        x="Perc.%",
        color="Opinion",
        orientation="h",
        text_auto=True,
    )
    fig1.update_yaxes(showticklabels=True)
    # fig2.update_xaxes(showticklabels=True)
    fig1.update_traces(hovertemplate=" %{x:.2f}%", texttemplate=" %{x:.2f}%")  #
    fig1.update_layout(
        # template="seaborn",
        title="Views about AI's impact on society in the next 20 years by country-2021 ",
        showlegend=True,
        xaxis=dict(
            showticklabels=True,
        ),
        hoverlabel=dict(
            font_size=12,
        ),
    ),

    fig2 = px.bar(
        df2,
        y="Group",
        x="Perc.%",
        color="Opinion",
        orientation="h",
        text_auto=True,
    )
    fig2.update_yaxes(showticklabels=True)
    # fig2.update_xaxes(showticklabels=True)
    fig2.update_traces(hovertemplate=" %{x:.2f}%", texttemplate=" %{x:.2f}%")  #
    fig2.update_layout(
        # template="seaborn",
        title="Views about AI's impact on society in the next 20 years by demographic group-2021",
        showlegend=True,
        xaxis=dict(
            showticklabels=True,
        ),
        hoverlabel=dict(
            font_size=12,
        ),
    ),

    table1 = dash_table.DataTable(
        df1.to_dict("records"),
        [{"name": i, "id": i} for i in df1.columns],
        page_size=10,
        style_data={
            "color": "black",
            "backgroundColor": "white",
        },
        style_header={
            "color": "white",
            "backgroundColor": "black",
        },
        style_cell={
            "height": "auto",
            # all three widths are needed
            "minWidth": "180px",
            "width": "180px",
            "maxWidth": "180px",
            "whiteSpace": "normal",
        },
    )
    table2 = dash_table.DataTable(
        df2.to_dict("records"),
        [{"name": i, "id": i} for i in df2.columns],
        page_size=10,
        style_data={
            "color": "black",
            "backgroundColor": "white",
        },
        style_header={
            "color": "white",
            "backgroundColor": "black",
        },
        style_cell={
            "height": "auto",
            # all three widths are needed
            "minWidth": "180px",
            "width": "180px",
            "maxWidth": "180px",
            "whiteSpace": "normal",
        },
    )
    return ([df1, df2], [fig1, fig2], [table1, table2])
