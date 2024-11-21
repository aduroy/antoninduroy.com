import dash_mantine_components as dmc
from dash import Dash

from app.header import header_layout
from app.about import about_layout
from app.experience import experience_layout
from app.education import education_layout
from app.side_quests import side_quests_layout
from app.achievements import achievements_layout


app = Dash(
    __name__,
    external_stylesheets=[
        # "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;900&display=swap"
        # "https://fontsgeek.com/fonts/helvetica-neue-97-black-condensed-oblique"
        "https://fonts.cdnfonts.com/css/helvetica-neue-55"
    ],
)

server = app.server


NAV_TAB_TEXT_STYLE = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '0'}
NAV_TAB_STYLE = {'border-radius': '0px', 'padding': '20px 20px'}
NAV_TABSLISTS = dmc.TabsList(
    children=[
        dmc.Tab(
            dmc.Text('ABOUT', style=NAV_TAB_TEXT_STYLE),
            value="about", style=NAV_TAB_STYLE
        ),
        dmc.Tab(
            dmc.Text('EXPERIENCE', style=NAV_TAB_TEXT_STYLE),
            value="experience", style=NAV_TAB_STYLE
        ),
        dmc.Tab(
            dmc.Text('SIDE QUESTS', style=NAV_TAB_TEXT_STYLE),
            value="side_quests", style=NAV_TAB_STYLE
        ),
        dmc.Tab(
            dmc.Text('EDUCATION', style=NAV_TAB_TEXT_STYLE),
            value="education", ml="auto", style=NAV_TAB_STYLE
        ),
        dmc.Tab(
            dmc.Text('ACHIEVEMENTS', style=NAV_TAB_TEXT_STYLE),
            value="achievements", style=NAV_TAB_STYLE
        ),
    ],
    style={'margin-bottom': '16px'}
)


app.layout = dmc.MantineProvider(
    theme={
        "fontFamily": "'Helvetica Neue', sans-serif",
        # "primaryColor": "indigo",
        "colorScheme": "dark"
    },
    inherit=True,
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dmc.Container(
            children=[
                dmc.Stack(
                    children=[
                        header_layout,
                        dmc.Space(h=0),
                        dmc.Tabs(
                            children=[
                                NAV_TABSLISTS,
                                dmc.TabsPanel(children=[about_layout], value="about"),
                                dmc.TabsPanel(children=[experience_layout], value="experience"),
                                dmc.TabsPanel(children=[education_layout], value="education"),
                                dmc.TabsPanel(children=[side_quests_layout], value="side_quests"),
                                dmc.TabsPanel(children=[achievements_layout], value="achievements"),
                            ],
                            variant='pills',
                            value='about'
                        ),
                    ],
                ),
            ],
            style={
                "marginTop": 20,
                "marginBottom": 20,
            },
            fluid=False,
            size='xl',
        )
    ],
)


if __name__ == "__main__":
    app.run_server(debug=False, use_reloader=True)