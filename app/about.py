import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from config import app_config


class About:
    def __init__(self, config):
        self.text = config.get('text')
        self.skills = config.get('skills')
        self.skills_global = config.get('skills_global')

    def __render_description(self):
        style_description = {'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'padding-left': '50px',
                             'text-align': 'justify', 'text-justify': 'inter-word'}

        skills_global = []
        for skill_global in self.skills_global:
            skills_global += [
                dmc.Text(
                    skill_global.get('name'),
                    color="dimmed",
                    style={'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '0'}
                ),
                dmc.Progress(value=skill_global.get('progress'), size='xl', radius=0, style={'margin-bottom': '10px'}),
            ]

        layout = dmc.Card(
            dmc.Group(
                children=[
                    dmc.Stack(
                        children=[
                            dmc.Text(
                                'Hi,',
                                color='dimmed',
                                style={'font-size': '30px', 'font-weight': '500', 'font-style': 'italic',
                                       'line-height': '1'}
                            ),
                            html.P(
                                self.text,
                                style=style_description,
                            )
                        ],
                        align='start',
                        style={'flex': 2}
                    ),
                    dmc.Stack(
                        children=skills_global,
                        style={'flex': 1, 'margin-left': '100px'}
                    )
                ],
                style={'gap': '100px'},
            ),
            radius=0,
            p=50,
        )

        layout = dmc.Group(
            children=[
                dmc.Stack([
                    layout,
                ]),
            ],
            style={'flex-flow': 'nowrap'},
            align='start',
            grow=True
        )

        return layout

    def __render_skills(self):

        skill_name_style = {'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'margin-bottom': '40px', 'margin-top': '10px'}
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}

        grid_elmts = []
        for s in self.skills:
            keywords = dmc.Group(
                children=[
                    dmc.Badge(
                        kw,
                        radius=0, style=style_keywords) for kw in s.get('keywords')
                ],
                position='center'
            )

            elmt = dmc.Col(
                children=[
                    dmc.Card(
                        children=[
                            dmc.Col(
                                children=[
                                    DashIconify(icon=s.get('icon'), height=50, color='rgb(25, 113, 194)'),
                                    dmc.Text(s.get('name'), color="primary", style=skill_name_style),
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
                self.__render_description(),
                self.__render_skills(),
            ],
            spacing='xl'
        )

        return layout


about = About(config=app_config['about'])
about_layout = about.render_layout()