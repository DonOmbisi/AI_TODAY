# package imports
from dash import Dash, html, page_container # type: ignore
import dash_bootstrap_components as dbc # type: ignore
import dash # type: ignore


app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.SUPERHERO, dbc.icons.BOOTSTRAP],
    use_pages=True,
    pages_folder="pages",
)


navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="AI Topics",
    ),
    className="mb-3 h3 fw-bold",
)
content = html.Div(id="page-content", children=[page_container], className="content")

app.layout = dbc.Container(
    [dbc.Row([dbc.Col([navbar, content], width=12)])], fluid=True, style={}
)


if __name__ == "__main__":
    app.run_server(debug=True)
