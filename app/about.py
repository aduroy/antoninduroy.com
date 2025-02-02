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
                    c="dimmed",
                    style={'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '0'}
                ),
                dmc.Progress(value=skill_global.get('progress'), size='xl', radius=0, style={'margin-bottom': '10px'}),
            ]

        description_card = dmc.Card(
            dmc.Grid(
                children=[
                    dmc.GridCol(
                        children=[
                            dmc.Text(
                                'Hi,',
                                c='dimmed',
                                style={'font-size': '30px', 'font-weight': '500', 'font-style': 'italic',
                                       'line-height': '1'}
                            ),
                            html.P(
                                self.text,
                                style=style_description,
                            )
                        ],
                        span={"base": 12, "sm": 6, "lg": 8}
                    ),
                    dmc.GridCol(
                        children=[
                            dmc.Stack(
                                children=skills_global
                            )
                        ],
                        span={"base": 12, "sm": 6, "lg": 4}
                    )
                ],
                gutter='100px',
                align='center'
            ),
            radius=0,
            p=50,
        )

        grid_column = dmc.GridCol(
            children=[
                description_card
            ],
            span=12
        )

        grid_columns = [grid_column]

        return grid_columns

    def __render_skills(self):

        skill_name_style = {'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'margin-bottom': '40px', 'margin-top': '10px'}
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}

        grid_columns = []
        for s in self.skills:
            keywords = dmc.Group(
                children=[
                    dmc.Badge(
                        kw,
                        radius=0,
                        variant='primary',
                        style=style_keywords
                    ) for kw in s.get('keywords')
                ],
                justify='center'
            )

            elmt = dmc.GridCol(
                children=[
                    dmc.Card(
                        children=[
                            dmc.GridCol(
                                children=[
                                    DashIconify(icon=s.get('icon'), height=50, color='rgb(25, 113, 194)'),
                                    dmc.Text(s.get('name'), c="primary", style=skill_name_style),
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
                span={"base": 12, "sm": 6, "lg": 4}
            )
            grid_columns.append(elmt)

        return grid_columns

    def render_layout(self):

        skills = self.__render_skills()
        description = self.__render_description()
        grid_columns = description + skills

        layout = dmc.Stack(
            children=[
                dmc.Grid(
                    children=grid_columns,
                    gutter={"base": 'xs', "sm": 'md', "lg": 'lg'}
                )
            ],
            gap='xl'
        )

        return layout


about = About(config=app_config['about'])
about_layout = about.render_layout()