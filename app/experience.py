import dash_mantine_components as dmc
from dash import html
from dash_iconify import DashIconify

from config import app_config


class ExperienceMoment:
    def __init__(self, config):
        self.title = config.get('title')
        self.main_description = config.get('main_description')
        self.bullet_points = config.get('bullet_points')
        self.logo = config.get('logo')
        self.company = config.get('company')
        self.location = config.get('location')
        self.years = config.get('years')
        self.keywords = config.get('keywords')

    def __render_institution(self):
        style_description = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'margin-top': '20px'}
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}

        layout = dmc.Stack(
            children=[
                html.Img(
                    src=self.logo['path'],
                    width=self.logo['width'],
                ),
                dmc.Text(f'{self.company["display_name"]}', c='dimmed', style=style_description),
                dmc.Group(
                    children=[
                        dmc.Badge(kw, radius=0, style=style_keywords,
                                  color='gray', variant='outline'
                                  ) for kw in self.company["keywords"]
                    ],
                    justify='center',
                    style={'margin-top': '20px'}
                ),
            ],
            align='center',
        )

        return layout

    def __render_description(self):
        style_keywords = {'font-size': '12px', 'font-weight': '300', 'font-style': 'italic', 'padding': '16px 16px'}
        style_title = {'font-size': '30px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'left'}
        style_subtitle = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'justify'}
        style_bullet_points = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-align': 'left'}
        style_metadata = {'font-size': '20px', 'font-weight': '500', 'font-style': 'italic', 'line-height': '1', 'text-justify': 'inter-word'}

        from_to = f'{self.years["from"]} - {self.years["to"]}'

        bullets_points = dmc.List()
        if self.bullet_points:
            bullets_points = dmc.List(
                children=[
                    dmc.ListItem(
                        dmc.Text(f'{d}', c='dimmed', style=style_bullet_points)
                    )
                    for d in self.bullet_points
                ],
                style={'text-align': 'left'}
            )

        layout = dmc.Stack(
            children=[
                dmc.Grid(
                    children=[
                        dmc.GridCol(
                            children=[
                                dmc.Stack(
                                    children=[
                                        dmc.Text(self.title, c='primary', style=style_title),
                                    ]
                                )
                            ],
                            span={"base": 12, "lg": 8},
                            style={'margin-bottom': '35px'}
                        ),
                        dmc.GridCol(
                            children=[
                                dmc.Stack(
                                    children=[
                                        dmc.Text(from_to, c='primary', style=style_metadata),
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
                    className='experience-moment-period'
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=dmc.Text(f'{self.main_description}', c='dimmed', style=style_subtitle),
                            style={'flex-grow': '1'}
                        ),
                    ],
                    align='start',
                    style={'margin-bottom': '20px'}
                ),
                dmc.Group(
                    children=[
                        dmc.Stack(
                            children=bullets_points,
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

        # layout = dmc.Grid(
        #     children=[
        #         dmc.GridCol(
        #             children=[
        #                 dmc.Card(
        #                     children=[
        #                         self.__render_institution()
        #                     ],
        #                     radius=0,
        #                     p=30,
        #                     style={
        #                         'text-align': 'center',
        #                         'height': '100%'
        #                     }
        #                 )
        #             ],
        #             span=4
        #         ),
        #         dmc.GridCol(
        #             children=[
        #                 dmc.Card(
        #                     children=[
        #                         self.__render_description()
        #                     ],
        #                     radius=0,
        #                     p=50,
        #                     style={
        #                         'text-align': 'center',
        #                         'height': '100%'
        #                     }
        #                 )
        #             ],
        #             span=8
        #         ),
        #     ],
        #     gutter="xl"
        # )

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


class Experience:
    def __init__(self, config):
        self.experience_moments = [ExperienceMoment(config=em) for em in config]

    def render_layout(self):
        # layout = dmc.Stack(
        #     children=[em.render_layout() for em in self.experience_moments],
        #     gap='xl'
        # )

        layout = dmc.Grid(
            children=[em.render_layout() for em in self.experience_moments],
            gutter={"base": 'xs', "sm": 'md', "lg": 'lg'}
        )

        return layout


experience = Experience(config=app_config['experience'])
experience_layout = experience.render_layout()