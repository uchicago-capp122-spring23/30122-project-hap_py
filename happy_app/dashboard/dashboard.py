#Author: Raúl Santiago Castellanos Guzmán 

#importing packages 
import dash
from dash import dcc
from dash import html
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go

#importing functions from other files 
from happy_app.analysis.hhs_visits import plot_hhs_visits
from happy_app.analysis.covid_cases import plot_covid_cases
from happy_app.analysis.social_referrals import get_social_referral_frequency
from happy_app.analysis.domain_visits import plot_domain_visits
from happy_app.analysis.traffic_sources import plot_traffic_sources
from happy_app.analysis.domain_visits import plot_domain_visits
from happy_app.analysis.cdc_visits import plot_cdc_visits
from happy_app.analysis.languages import plot_languages
from happy_app.analysis.dashboard_math import get_yearly_percentage


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
"""
Creates a Dash application and adds it to a Flask server.
"""
def generate_title_container(title_text, subtitle_text, scrolldown_text):
    """
    This function generates a container containing a title and subtitle.

    Inputs: 
    - title_text: (str)
        The text to be used for the main title.
    - subtitle_text: (str)
        The text to be used for the subtitle.

    Returns: 
    - dbc.Container
        A Dash container that will be the title. 
    """
    title_container = dbc.Container(
        fluid=True,
        style={
            "height": "100vh",
            "background-color": "#005aae",
            "color": "white",
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "center",
            "align-items": "center"
        },
        children=[
            html.H1(title_text, style={"font-size": "8rem", "text-align": "center"}),
            html.Br(),
            html.Br(),
            html.H2(subtitle_text, style={"font-size": "2rem", "text-align": "center"}),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H3(scrolldown_text, style={"font-size": "1rem", "text-align": "center"}),
            html.Img(src='https://cdn3.iconfinder.com/data/icons/faticons/32/arrow-down-01-512.png', className="white-arrow", style={"width": "50px", "margin-left": "10px"}),
            html.Br(),
        ],
        className="title-container"
    )
    return title_container




def generate_subtitle_container(subtitle_text, background_color, text_color):
    """
    This function generates containers that are subtitles 

    Inputs: 
    - subtitle_text: (str)
        The text to be used for the subtitle.
    - background_color: (str)
        The background color to be used for the subtitle container.
    - text_color: (str)
        The color to be used for the subtitle text.

    Returns: 
    - dbc.Container
        A Dash container that will be the subtitles of the app. 
    """
    subtitle_container = dbc.Container(
        fluid=True,
        style={
            "height": "20vh",
            "background-color": background_color,
            "color": text_color,
            "display": "flex",
            "flex-direction": "column",
            "justify-content": "center",
            "align-items": "flex-start"
        },
        children=[
            dbc.Row(
                dbc.Col(
                    html.H1(subtitle_text, style={"font-size": "3rem", "color": "white"}),
                    width=12,
                    style={"display": "flex", "justify-content": "center", "align-items": "center"}
                )
            )
        ]
    )
    return subtitle_container


def generate_graph_container_one(title_text, 
                                 paragraph_text,
                                 graph_component, 
                                 graph_title, 
                                title_color):
    """
    This function generates a graph container with only one static graph. 

    Inputs: 
    - title_text: (str)
        The text to be used for the title of the graph component. 
    - paragraph_text: (str)
        The text to be used for the paragraph.
    - graph_component: imported graph 
        A graph imported as a dcc object 
    - graph_title: (str)
        Text to be used as the title of the graph 
    - title_color : str
        The color to be used for the title text.

    Returns: 
    - dbc.Container
        A Dash container that will be used to display and give context for one graph

    """
    graph_container = dbc.Container(
        fluid=True,
        children=[
            dbc.Row([
                dbc.Col([
                    html.H1(title_text, style={"text-align": "left", "color": title_color, "font-size": "2rem"}),
                    dcc.Markdown(paragraph_text, style={"font-size": "1rem"})
                ], width=3),
                dbc.Col([
                    html.H2(graph_title, style={"text-align": "left", "color": title_color, "font-size": "2rem"}),
                    graph_component, 
                ], width=9)
            ])
        ]
    )
    return graph_container


def generate_numbers_container(title_text, paragraph_text, number1, explanation1, number2, explanation2, 
                               number3, explanation3, numbers_title, title_color='black', number_color='black'):

    """
    This function generates a graph container that displays numbers. 

    Inputs: 
    - title_text: (str)
        The text to be used for the title of the graph component. 
    - number_1 to number_3: (int)
        The numbers to be displayed. 
    - explanation_1 to eexplanation_3: (sstr)
        An explanation for the number. 
    - title_color: (str)
        Color for the title, default at black.  
    - number_color: (str)
        The color to be used for the number, default at black.

    Returns: 
    - dbc.Container
        A Dash container that will be used to display and give context for one graph

    """
    container = dbc.Container(
        fluid=True,
        style={'height': '50vh'},
        children=[ 
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H1(title_text, style={"color": title_color, "font-size": "2rem"}), 
                            dcc.Markdown(paragraph_text, style={"font-size": "1rem"})
                        ],
                        width=4,
                        style={'height': '40vh', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}
                    ),
                    dbc.Col(
                        [
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            html.H1(f"{number1}%", style={'text-align': 'center', 'font-size': '6rem', 'color': number_color}),
                                            html.P(explanation1, style={'text-align': 'center'})
                                        ],
                                        width=4,
                                        style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}
                                    ),
                                    dbc.Col(
                                        [
                                            html.H1(f"{number2}%", style={'text-align': 'center', 'font-size': '6rem', 'color': number_color}),
                                            html.P(explanation2, style={'text-align': 'center'})
                                        ],
                                        width=4,
                                        style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}
                                    ),
                                    dbc.Col(
                                        [
                                            html.H1(f"{number3}%", style={'text-align': 'center', 'font-size': '6rem', 'color': number_color}),
                                            html.P(explanation3, style={'text-align': 'center'})
                                        ],
                                        width=4,
                                        style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}
                                    ),
                                ],
                                style={'height': '50%', 'margin-top': '1rem'}
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.H2(numbers_title, style={"text-align": "center", "color": title_color, "font-size": "2rem"}),
                                    style={'height': '10vh', 'display': 'flex', 'flex-direction': 'column', 'justify-content': 'center'}
                                )
                            )
                        ],
                        width=8,
                        style={'display': 'flex', 'flex-direction': 'column', 'justify-content': 'space-between'}
                    )
                ],
                style={'height': '100%'}
            )
        ]
    )
    return container




def generate_footer_container(title_text, bg_color, github_link):
    """
    This function generates a graph container that displays the footer of the page. 

    Inputs: 
    - title_text: (str)
        The text to be used for the title of the graph component. 
    - title_color: (str)
        Color for the background.  
    - github_link: (str)
        The github of our repository. 

    Returns: 
    - dbc.Container
        A Dash container that will be used to display our github and the name of our team.

    """
    container = dbc.Container(
        fluid=True,
        style={'height': '15vh', 'background-color': bg_color},
        children=[
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.A(html.H5(title_text, style={'color': 'white', 'font-size': '1rem', 'margin-bottom': '2rem', 'text-align': 'right'}),
                                   href=github_link, target='_blank', style={'color': 'white', 'text-decoration': 'none'}),
                        ],
                        width=12,
                        style={'display': 'flex', 'flex-direction': 'row', 'justify-content': 'flex-end', 'align-items': 'center'}
                    )
                ],
                style={'height': '100%'}
            )
        ]
    )
    return container


def generate_graph_container_interactive_two(title_text, paragraph_text,
                                              graph_component_1, graph_component_2, 
                                              graph_component_3, graph_component_4,
                                              graph_component_5, graph_component_6,
                                              title_color, graph_title, 
                                              first_label, 
                                              second_label, 
                                              third_label):
    """
    This function generates a graph container that has a dropdown that allows 

    Inputs: 
    - title_text: (str)
        The text to be used for the title of the graph component. 
    - title_color: (str)
        Color for the background.  
    - github_link: (str)
        The github of our repository. 

    Returns: 
    - dbc.Container
        A Dash container that will be used to display our github and the name of our team.

    """
    graph_container = dbc.Container(
        fluid=True,
        children=[
            dbc.Row([
                dbc.Col([
                    html.H1(title_text, style={"text-align": "left", "color": title_color, "font-size": "2rem"}),
                    dcc.Markdown(paragraph_text, style={"font-size": "1rem"})
                ], width=3),
                dbc.Col([
                    html.H2(graph_title, style={"text-align": "left", "color": title_color, "font-size": "2rem"}),
                    dcc.Dropdown(
                        id='graph-dropdown-1',
                        options=[
                            {'label': first_label, 'value': 'graph1'},
                            {'label': second_label, 'value': 'graph2'},
                            {'label': third_label, 'value': 'graph3'}
                        ],
                        value='graph1'
                    ),
                    html.Div(
                        id='graph-container-1',
                        children=[graph_component_1, graph_component_2]
                    )
                ], width=9)
            ])
        ]
    )
    return graph_container




##############
# Importing the data 
#############

#import graphs visits to cdc by year 
graph_2019_2020 = plot_hhs_visits(2020)
graph_2019_2021 = plot_hhs_visits(2021)
graph_2019_2022 = plot_hhs_visits(2022)

#import grpahs of covid cases by year 
graph_covid_2020 = plot_covid_cases(2020)
graph_covid_2021 = plot_covid_cases(2021)
graph_covid_2022 = plot_covid_cases(2022)

#import numbers of social referals
fb_number = get_social_referral_frequency("Facebook")
tw_number = get_social_referral_frequency("Twitter")
ig_number = get_social_referral_frequency("Instagram")

from happy_app.analysis.domain_visits import plot_domain_visits
from happy_app.analysis.cdc_visits import plot_cdc_visits


#import sites 
key_sites_cdc = ['vaccines.gov', 'vacunas.gov', 'covid.cdc.gov', 'covid.gov', 'covidtests.gov']
non_cdc_data_graph = plot_domain_visits()
cdc_data_graph = plot_cdc_visits()

#import traffic sources 
graph_traffic_sources = plot_traffic_sources()

#import language plot 
graph_language = plot_languages()



title_container = generate_title_container(
   title_text = "COVID-19 Online:", 
   subtitle_text =  "How were people interacting with COVID-19 goverment pages during the crisis?", 
   scrolldown_text = "Scroll down.")



subtitle_container_goverment_pages = generate_subtitle_container(
    subtitle_text = "How People Accessed HHS Sites",
 background_color = "#005aae", 
   text_color = "white"
     )


subtitle_container_forms_of_accesing = generate_subtitle_container(
  subtitle_text =  "Paths to HHS Websites",
 background_color = "#005aae", 
 text_color = "white")



graph_container_language = generate_graph_container_one(
title_text = "HHS Sites Viewed in 68 Languages", 
paragraph_text =  "HHS sites were **most viewed in English (74.3%)**, Spanish (13.4%), Chinese (3.8%) or French (1%). These proportions are consistent with languages spoken in the United States, [according to 2021 ACS estimates](https://data.census.gov/table?q=B16001:+LANGUAGE+SPOKEN+AT+HOME+BY+ABILITY+TO+SPEAK+ENGLISH+FOR+THE+POPULATION+5+YEARS+AND+OVER&g=0100000US&tid=ACSDT1Y2021.B16001&moe=true). \n\n Across all four years (2019-2022), users visited HHS websites in more than 68 languages." , 
graph_component = graph_language, 
title_color = "#808080", 
graph_title = "Languages with over 100M Visits")

graph_container_cdc_visits = generate_graph_container_one(
title_text = "Initial Lockdowns Drove Surge in CDC Traffic", 
paragraph_text =  f"The only large uptick in traffic to cdc.gov was in March 2020, after COVID-19 was declared a national emergency. \n\n In 2019, visits to cdc.gov accounted for only {get_yearly_percentage(2019, 'cdc.gov'):.1f}% of visits to all HHS websites compared to 2020, following the first year of the pandemic, visits to cdc.gov comprised **{get_yearly_percentage(2020, 'cdc.gov'):.1f}% of all traffic on HHS sites**. \n\n Across all four years, visits to cdc.gov accounted for **{get_yearly_percentage([2019, 2020, 2021, 2022], 'cdc.gov'):.1f}% of all web traffic on HHS websites**." , 
graph_component = cdc_data_graph, 
title_color = "#808080", 
graph_title = "Cumulative Visits to CDC.gov from 2019-2022")

graph_container_non_cdc_visits = generate_graph_container_one(
title_text = "Websites Born out of the Pandemic", 
paragraph_text =  "At the start of 2022, two new HHS sites were launched: **covidtests.gov** and **covid.gov**. Likely due to Omicron, covidtests.gov drew visitors instantly, achieving similar traffic numbers to longer-standing sites like vaccines.gov within weeks. \n\n Traffic to covidtests.gov plateaus after the launch of covid.gov in March 2022, which aggregated information on the pandemic to one website.", 
graph_component = non_cdc_data_graph, 
title_color = "#808080", 
graph_title = "Cumulative Visits to Other Pandemic-Related Websites from 2020-2022")


#order Twitter, Facebook, Instagram
social_numbers_container = generate_numbers_container(
    title_text = "Traffic Driven by Social Networks",
    paragraph_text = "Social media traffic can be split into two categories: social referrals and normal traffic. **Social referrals are visits driven by users clicking on links shared by friends on social networks,** instead of users clicking on ads or content pushed by the platform itself.\n\n This “social referral” proportion of traffic differed across social media platforms.\n\n In the two months around the three largest spikes of COVID cases, **99% of all HHS traffic from Twitter was due to social referrals.** Only 4 in 10 Facebook visits and less than 2 in 10 Instagram visits were driven by social referrals.", 
    number1 = tw_number,
    explanation1 = "from Twitter",
    number2 = fb_number, 
    explanation2 = "from Facebook", 
    number3 = ig_number, 
    explanation3 = "from Instagram", 
    title_color= "#808080",
    number_color= "#005aae", 
    numbers_title = "Percentage of Social Referrals")

subtitle_container_language = generate_subtitle_container(
  subtitle_text =  "Primary Languages of HHS Site Visitors",
 background_color = "#005aae", 
 text_color = "white")


graph_container_accesing = generate_graph_container_one(title_text = "Search Engines Served as Main Access Point",
                                                        paragraph_text = "In the first wave of the pandemic (March/April 2020), **63% of traffic** to HHS websites came from search engines, followed by direct links (15%). Only 0.7% of traffic to HHS websites came from social media websites during this time period. \n\n These trends remained true during the peak of COVID-19 cases in December 2021/January 2022, as well as when COVID-19 cases were not spiking in December 2020/January 2021.", 
                                                        graph_component = graph_traffic_sources, 
                                                        title_color = "#808080", 
                                                        graph_title = "Visits to HHS Websites by Source"
                                                        ) 

subtitle_container_most_visited_pages = generate_subtitle_container(
  subtitle_text =  "A Digital Response to the Pandemic", 
 background_color = "#005aae", 
 text_color = "white" )


footer_container = generate_footer_container(
        title_text="Powered by Happ.py",
        bg_color="#005aae", 
        github_link = "https://github.com/uchicago-capp122-spring23/30122-project-hap_py"
    )





interactive_cdc_covid_container = generate_graph_container_interactive_two(
    title_text = "Spikes in HHS Web Usage", 
    paragraph_text = "During the pandemic’s initial surge in March 2020, visits to [HHS websites](https://analytics.usa.gov/health-human-services/data/) increased sharply, with these sites witnessing **155 million visits per week** compared to the same time period in 2019. \n\n At its peak, traffic to HHS websites reached **234 million visits per week** in alignment with when COVID-19 was first declared a national emergency and lockdowns initially begun. \n\n Traffic remained steady throughout 2021 until January 2022, when visits peaked at **203 million more visits** coinciding with the pandemic’s Omicron wave of the pandemic.", 
    graph_component_1 = graph_2019_2020 , 
    graph_component_2 = graph_covid_2020, 
    graph_component_3 = graph_2019_2021, 
    graph_component_4 = graph_covid_2021, 
    graph_component_5 = graph_2019_2022, 
    graph_component_6 = graph_covid_2022, 
    title_color = "#808080", 
    graph_title = "Visits to the HHS Websites and Daily COVID Cases by Week", 
    first_label = 2020, 
    second_label = 2021, 
    third_label = 2022) 
   

app.layout = html.Div(children=[
    title_container,
    subtitle_container_goverment_pages,
    interactive_cdc_covid_container,
    subtitle_container_forms_of_accesing, 
    graph_container_accesing, 
    html.Br(), 
    social_numbers_container, 
    subtitle_container_most_visited_pages, 
    graph_container_cdc_visits,
    graph_container_non_cdc_visits,  
    subtitle_container_language, 
    graph_container_language, 
    footer_container
])



@app.callback(
    [dash.dependencies.Output('graph-container-1', 'children')],
    [dash.dependencies.Input('graph-dropdown-1', 'value')]
)

def update_graph_container(value1):
    if value1 == 'graph1':
        graph_container_1 = [graph_2019_2020, graph_covid_2020]
    elif value1 == 'graph2':
        graph_container_1 = [graph_2019_2021, graph_covid_2021]
    elif value1 == 'graph3':
        graph_container_1 = [graph_2019_2022, graph_covid_2022]
    
    return [graph_container_1]




# Run app
if __name__=='__main__':
    app.run_server(port=8049)