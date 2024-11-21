import dash_mantine_components as dmc
from dash_iconify import DashIconify

from config import app_config


class Achievements:
    def __init__(self, config):
        self.achievements = config.copy()

    def __render_achievements(self):

        achievement_name_style = {'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'margin-bottom': '20px', 'margin-top': '10px'}
        achievement_style = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'margin-bottom': '20px', 'margin-top': '10px'}
        achievement_context_style = {'font-size': '16px', 'font-weight': '500', 'font-style': 'italic', 'text-align': 'center', 'margin-bottom': '30px'}
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}

        grid_elmts = []
        for a in self.achievements:
            keywords = dmc.Group(
                children=[
                    dmc.Badge(
                        kw,
                        radius=0, style=style_keywords
                    ) for kw in a.get('keywords')
                ],
                position='center'
            )

            elmt = dmc.Col(
                children=[
                    dmc.Card(
                        children=[
                            dmc.Col(
                                children=[
                                    DashIconify(icon=a.get('icon'), height=50, color='rgb(25, 113, 194)'),
                                    dmc.Text(a.get('name'), color="primary", style=achievement_name_style),
                                    dmc.Text(a.get('achievement'), color="dimmed", style=achievement_style),
                                    dmc.Text(a.get('context'), color="dimmed", style=achievement_context_style),
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
                self.__render_achievements(),
            ],
            spacing='xl'
        )

        return layout


achievements = Achievements(config=app_config['achievements'])
achievements_layout = achievements.render_layout()