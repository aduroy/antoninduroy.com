import dash_mantine_components as dmc
from dash import html, dcc
from dash_iconify import DashIconify

from config import app_config


class SideQuests:
    def __init__(self, config):
        self.side_quests = config.copy()

    def __render_skills(self):

        skill_name_style = {'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'margin-bottom': '20px', 'margin-top': '10px'}
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'text-align': 'center', 'margin-bottom': '20px'}
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}

        grid_elmts = []
        for sq in self.side_quests:
            links = dmc.Group(
                children=[
                    html.A(
                        l['name'],
                        href=l['url'],
                        target='_blank'
                    ) for l in sq.get('links')
                ],
                position='center',
                style={'margin-bottom': '30px'}
            )

            keywords = dmc.Group(
                children=[
                    dmc.Badge(
                        kw,
                        radius=0, style=style_keywords) for kw in sq.get('keywords')
                ],
                position='center'
            )

            elmt = dmc.Col(
                children=[
                    dmc.Card(
                        children=[
                            dmc.Col(
                                children=[
                                    DashIconify(icon=sq.get('icon'), height=50, color='rgb(25, 113, 194)'),
                                    dmc.Text(sq.get('name'), color="primary", style=skill_name_style),
                                    dmc.Text(sq.get('description'), color="dimmed", style=style_subtitle),
                                    links,
                                    keywords
                                ]
                            ),

                        ],
                        radius=0,
                        p=30,
                        style={
                            'text-align': 'center',
                            'height': '100%'
                        }
                    )
                ],
                lg=4,
                md=6
            )
            grid_elmts.append(elmt)

        layout = dmc.Grid(
            children=grid_elmts,
            gutter="xl"
        )

        return layout

    def render_layout(self):
        layout = dmc.Stack(
            children=[
                self.__render_skills(),
            ],
            spacing='xl'
        )

        return layout


side_quests = SideQuests(config=app_config['side_quests'])
side_quests_layout = side_quests.render_layout()