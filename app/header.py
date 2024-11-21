from datetime import datetime

import dash_mantine_components as dmc
from dash import Dash, html
from dash_iconify import DashIconify

from config import app_config


class Header:
    def __init__(self, config):
        self.flag_icon = config.get('flag_icon')
        self.first_name = config.get('first_name')
        self.last_name = config.get('last_name')
        self.nick_name = config.get('nick_name')
        self.avatar_path = config.get('avatar_path')
        self.date_of_birth = config.get('date_of_birth')
        self.date_of_first_employment = config.get('date_of_first_employment')
        self.role = config.get('role')
        self.contact = config.get('contact')
        self.location = config.get('location')
        self.language_icons = config.get('language_icons')

    def __render_avatar(self):
        current_year = datetime.now().year
        if self.date_of_birth and self.date_of_birth < current_year:
            age = current_year - self.date_of_birth
        else:
            age = '-'

        if self.date_of_first_employment and self.date_of_first_employment < current_year:
            xp = current_year - self.date_of_first_employment
        else:
            xp = '-'

        layout = dmc.Stack(
            children=[
                dmc.Image(src=self.avatar_path, width=300, style={'border': '4px solid rgb(193, 194, 197)'}),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Group(
                                    children=[
                                        DashIconify(icon="jam:heart", height=35, color='rgb(144, 146, 150)'),
                                        dmc.Text(f'{age} HP', color='primary', style={'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1.0'})
                                    ]
                                ),
                            ]
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Group(
                                    children=[
                                        DashIconify(icon="pixelarticons:briefcase", height=35, color='rgb(144, 146, 150)'),
                                        dmc.Text(f'{xp} XP', color='primary', style={'font-size': '25px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1.0'})
                                    ]
                                ),
                            ],
                            style={'margin-right': '8px'}
                        ),
                    ],
                    position='apart'
                ),
            ],
        )

        return layout

    def __render_description(self):
        style_name = {'font-size': '45px', 'font-weight': '900'}
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '0'}
        style_subtext = {'font-size': '30px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1'}

        layout = dmc.Stack(
            children=[
                dmc.Group(
                    children=[
                        DashIconify(icon=self.flag_icon, height=40),
                        dmc.Text(
                            self.first_name,
                            style=style_name
                        ),
                        dmc.Text(
                            f'"{self.nick_name}"',
                            style=style_name
                        ),
                        dmc.Text(
                            self.last_name,
                            style=style_name
                        ),
                    ],
                    style={'margin-bottom': '70px'}
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text('ROLE', color="dimmed", style=style_subtitle),
                                dmc.Group(
                                    children=[
                                        dmc.Text(self.role, color='primary', style=style_subtext),
                                    ],
                                ),
                            ],
                            style={'flex': 2}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Text('CONTACT', color="dimmed", style=style_subtitle),
                                dmc.Group(
                                    children=[html.A(DashIconify(icon=c['icon'], height=35, color='rgb(193, 194, 197)'), href=c['link'], target='_blank') for c in self.contact]
                                ),
                            ],
                            style={'flex': 1}
                        )
                    ],
                    style={'margin-bottom': '20px'}
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text('LOCATION', color="dimmed", style=style_subtitle),
                                dmc.Group(
                                    children=[
                                        DashIconify(icon=self.location.get('icon'), height=25),
                                        dmc.Text(self.location.get('name'), color='primary', style=style_subtext)
                                    ],
                                    align='center'
                                ),
                            ],
                            style={'flex': 2}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Text('LANGUAGES', color="dimmed", style=style_subtitle),
                                dmc.Group(
                                    children=[DashIconify(icon=language_icon, height=25) for language_icon in self.language_icons]
                                ),
                            ],
                            style={'flex': 1}
                        ),
                    ],
                ),
            ],
            style={'flex-grow': '1'}
        )

        return layout

    def render_layout(self):
        layout = dmc.Card(
            dmc.Group(
                children=[
                    self.__render_avatar(),
                    self.__render_description(),
                ],
                align='start',
                style={'gap': '50px'}
            ),
            withBorder=True,
            radius=0,
            p=50,
        )

        return layout


header = Header(config=app_config['header'])
header_layout = header.render_layout()