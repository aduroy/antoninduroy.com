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

        layout = dmc.GridCol(
            children=[
                dmc.Stack(
                    children=[
                        # dmc.Image(src=self.avatar_path, h=300, style={'border': '4px solid rgb(193, 194, 197)'}),
                        html.Img(src=self.avatar_path, width=300, style={'border': '4px solid rgb(193, 194, 197)'}),
                        dmc.Group(
                            children=[
                                dmc.Stack(
                                    children=[
                                        dmc.Group(
                                            children=[
                                                DashIconify(icon="jam:heart", color='rgb(144, 146, 150)',
                                                            # style={'font-size': 'min(5vw, 35px)'}),
                                                            height=35),
                                                dmc.Text(f'{age} HP', c='primary',
                                                         # style={'font-size': 'min(5vw, 25px)', 'font-weight': '500',
                                                         #        'font-style': 'italic', 'line-height': '1.0'})
                                                         style={'font-size': '25px', 'font-weight': '500',
                                                                'font-style': 'italic', 'line-height': '1.0'})
                                            ]
                                        ),
                                    ]
                                ),
                                dmc.Stack(
                                    children=[
                                        dmc.Group(
                                            children=[
                                                DashIconify(icon="pixelarticons:briefcase", height=35,
                                                            color='rgb(144, 146, 150)'),
                                                dmc.Text(f'{xp} XP', c='primary',
                                                         style={'font-size': '25px', 'font-weight': '500',
                                                                'font-style': 'italic', 'line-height': '1.0'})
                                            ]
                                        ),
                                    ],
                                    # style={'margin-right': '8px'}
                                ),
                            ],
                            style={'width': '290px', 'margin-right': '8px'},
                            justify='space-between'
                        ),
                    ],
                    align='center',
                    # style={'width': '300px'}
                ),
            ],
            span={"base": 12, "sm": 5, "lg": 4},
        )

        grid_columns = [layout]

        return grid_columns

    def __render_description(self):
        # style_name = {'font-size': 'min(max(3.5vw, 20px), 45px)', 'font-weight': '900'}
        # style_subtitle = {'font-size': 'min(max(3.5vw, 12px), 20px)', 'font-weight': '500', 'font-style': 'italic', 'line-height': '0'}
        style_subtext = {'font-size': 'min(max(3.5vw, 20px), 30px)', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1'}

        layout = dmc.GridCol(
            children=[
                dmc.Group(
                    children=[
                        DashIconify(icon=self.flag_icon, className='header-name'),
                        dmc.Text(
                            f'{self.first_name} "{self.nick_name}" {self.last_name}',
                            className='header-name'
                        ),
                    ],
                    className='header-name-group'
                    # style={'margin-bottom': 'min(max(5vw, 30px), 70px)'}
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=[
                                dmc.Text('ROLE', c="dimmed", className='header-subtitle'),
                                dmc.Group(
                                    children=[
                                        dmc.Text(self.role, c='primary', className='header-subtext'),
                                    ],
                                ),
                            ],
                            style={'flex': 2}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Text('CONTACT', c="dimmed", className='header-subtitle'),
                                dmc.Group(
                                    children=[
                                        html.A(
                                            DashIconify(icon=c['icon'], className='header-subtext', color='rgb(193, 194, 197)'),
                                            href=c['link'],
                                            target='_blank'
                                        ) for c in self.contact
                                    ]
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
                                dmc.Text('LOCATION', c="dimmed", className='header-subtitle'),
                                dmc.Group(
                                    children=[
                                        DashIconify(icon=self.location.get('icon'), className='header-subtext'),
                                        dmc.Text(self.location.get('name'), c='primary', className='header-subtext')
                                    ],
                                    align='center'
                                ),
                            ],
                            style={'flex': 2}
                        ),
                        dmc.Stack(
                            children=[
                                dmc.Text('LANGUAGES', c="dimmed", className='header-subtitle'),
                                dmc.Group(
                                    children=[DashIconify(icon=language_icon, className='header-subtext') for language_icon in self.language_icons]
                                ),
                            ],
                            style={'flex': 1}
                        ),
                    ],
                ),
            ],
            # style={'flex-grow': '1'}
            span={"base": 12, "sm": 7, "lg": 8}
        )

        grid_columns = [layout]

        return grid_columns

    def render_layout(self):
        avatar = self.__render_avatar()
        description = self.__render_description()

        grid_columns = avatar + description

        layout = dmc.Card(
            dmc.Grid(
                children=grid_columns,
                align='start',
                # style={'gap': '50px'},
                # gutter='100px',
                gutter={"base": '50px', "lg": '100px'}
            ),
            withBorder=True,
            radius=0,
            p=50,
        )

        return layout


header = Header(config=app_config['header'])
header_layout = header.render_layout()