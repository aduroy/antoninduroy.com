import dash_mantine_components as dmc
from dash import Dash, html
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
                dmc.Image(
                    src=self.logo['path'],
                    width=self.logo['size'],
                ),
                dmc.Text(f'{self.handle["display_name"]}', color='dimmed', style=style_subtitle),
            ],
            align='center',
            style={'height': '100%', 'width': '100%', 'justify-content': 'center'}
        )

        return layout

    def __render_description(self):
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}
        style_title = {'font-size': '30px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'left'}
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'justify', 'text-justify': 'inter-word'}

        layout = dmc.Stack(
            children=[
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text(self.title, color='primary', style=style_title),
                            ],
                            style={'flex-grow': '1'}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Group(
                                    children=[
                                        dmc.Text(f'{self.years["from"]} - {self.years["to"]}', color='primary', style=style_title)
                                    ],
                                    align='center',
                                    position='right'
                                ),
                            ],
                        )
                    ],
                    align='end',
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text(f'{self.subtitle}', color='dimmed', style=style_subtitle),
                            ],
                            style={'flex-grow': '1'}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Group(
                                    children=[
                                        dmc.Text(self.location['name'], color='primary', style=style_subtitle),
                                        DashIconify(icon=self.location['icon'], height=20),
                                    ],
                                    align='center',
                                    position='right'
                                ),
                            ]
                        )
                    ],
                    align='start',
                    style={'margin-bottom': '40px'}
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text(f'{self.description}', color='dimmed', style=style_subtitle),
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
        layout = dmc.Grid(
            children=[
                dmc.Col(
                    children=[
                        dmc.Card(
                            children=[
                                self.__render_institution()
                            ],
                            radius=0,
                            p=30,
                            style={
                                'text-align': 'center',
                                'height': '100%'
                            }
                        )
                    ],
                    span=4
                ),
                dmc.Col(
                    children=[
                        dmc.Card(
                            children=[
                                self.__render_description()
                            ],
                            radius=0,
                            p=50,
                            style={
                                'text-align': 'center',
                                'height': '100%'
                            }
                        )
                    ],
                    span=8
                ),
            ],
            gutter="xl"
        )

        return layout


class Education:
    def __init__(self, config):
        self.education_moments = [EducationMoment(config=em) for em in config]

    def render_layout(self):
        layout = dmc.Stack(
            children=[em.render_layout() for em in self.education_moments],
            spacing='xl'
        )

        return layout


education = Education(config=app_config['education'])
education_layout = education.render_layout()