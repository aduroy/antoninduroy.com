import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from config import app_config


class EducationMoment:
    def __init__(self, config):
        self.title = config.get('title')
        self.subtitle = config.get('subtitle')
        self.description = config.get('description')
        self.logo = config.get('logo')
        self.handle = config.get('handle')
        self.location = config.get('location')
        self.years = config.get('years')
        self.keywords = config.get('keywords')

    def __render_institution(self):
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'margin-top': '20px'}

        layout = dmc.Stack(
            children=[
                html.Img(
                    src=self.logo['path'],
                    width=self.logo['width'],
                ),
                dmc.Text(f'{self.handle["display_name"]}', c='dimmed', style=style_subtitle),
            ],
            align='center',
        )

        return layout

    def __render_description(self):
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}
        style_title = {'font-size': '30px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'left'}
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'justify', 'text-justify': 'inter-word'}
        style_metadata = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-justify': 'inter-word'}

        layout = dmc.Stack(
            children=[
                dmc.Grid(
                    children=[
                        dmc.GridCol(
                            children=[
                                dmc.Stack(
                                    children=[
                                        dmc.Text(self.title, c='primary', style=style_title),
                                        dmc.Text(f'{self.subtitle}', c='primary', style=style_subtitle),
                                    ]
                                )
                            ],
                            span={"base": 12, "lg": 8}
                        ),
                        dmc.GridCol(
                            children=[
                                dmc.Stack(
                                    children=[
                                        dmc.Text(f'{self.years["from"]} - {self.years["to"]}', c='primary', style=style_metadata),
                                        dmc.Group(
                                            children=[
                                                dmc.Text(self.location['name'], c='primary', style=style_metadata),
                                                DashIconify(icon=self.location['icon'], height=20),
                                            ],
                                        ),
                                    ]
                                )
                            ],
                            span='content'
                        )
                    ],
                    align='end',
                    justify='space-between',
                    style={'margin-bottom': '40px'},
                    className='education-moment-period'
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text(f'{self.description}', c='dimmed', style=style_subtitle),
                            ],
                            style={'flex-grow': '1'}
                        ),
                    ],
                    align='start',
                    style={'margin-bottom': '40px'}
                ),
                dmc.Group(
                    children=[
                        dmc.Badge(kw, radius=0, style=style_keywords) for kw in self.keywords
                    ],
                ),
            ],
            style={'flex': '1'}
        )

        return layout

    def render_layout(self):
        layout = dmc.GridCol(
            children=dmc.Grid(
                children=[
                    dmc.GridCol(
                        children=[
                            dmc.Card(
                                children=[
                                    self.__render_institution()
                                ],
                                radius=0,
                                p=30,
                                style={
                                    'justify-content': 'center',
                                    'height': '100%'
                                }
                            )
                        ],
                        span={"base": 12, "sm": 4}
                    ),
                    dmc.GridCol(
                        children=[
                            dmc.Card(
                                children=[
                                    self.__render_description()
                                ],
                                radius=0,
                                p=50,
                                style={
                                    'height': '100%'
                                }
                            )
                        ],
                        span={"base": 12, "sm": 8}
                    ),
                ],
                gutter={"base": 'xs', "sm": 'md', "lg": 'lg'}
            ),
            span=12
        )

        return layout


class Education:
    def __init__(self, config):
        self.education_moments = [EducationMoment(config=em) for em in config]

    def render_layout(self):
        # layout = dmc.Stack(
        #     children=[em.render_layout() for em in self.education_moments],
        #     gap='xl'
        # )

        layout = dmc.Grid(
            children=[em.render_layout() for em in self.education_moments],
            gutter={"base": 'xs', "sm": 'md', "lg": 'lg'}
        )

        return layout


education = Education(config=app_config['education'])
education_layout = education.render_layout()