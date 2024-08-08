import pandas as pd
import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro
from vizro.tables import dash_ag_grid
from vizro.actions import export_data, filter_interaction
import plotly.graph_objects as go
from vizro.models.types import capture

Vizro._reset()

def create_intro():
    """Introduction Page""" 
    
    page_intro = vm.Page(
        title="Intro",
        layout=vm.Layout(grid=[[0, 0, 1]]),
        components=[
            vm.Card(
                text="""
 ![](assets/logo.<extension>.png#icon)

# **🇳🇿Welcome to Your Ultimate Guide to New Zealand Universities!🇳🇿**
---

### **Hey there school leavers - the future university students! 🌟 Are you nervous about choosing the right university for you? Are you worried you’ll miss out on amazing opportunities right here in New Zealand? Well, worry no more! We present you, the ultimate dashboard showing detailed information on New Zealand universities. **

## What’s This All About?


We know that picking a university can be overwhelming, especially when it feels like overseas options might be better. However, it might be because you did not get informed enough on the various options domestically. But guess what? New Zealand universities have SO much to offer, and our fun, interactive dashboard is here to show you exactly that! The offers of our universities will be compared with international standards so worry not about the quality of the education you are about to receive. 

## Why Should You Care?

Our mission is to help you discover all the scores and rankings of universities across New Zealand, to show you the actual position of our universities compared to the world. You can also see which university excels at which aspect, helping you to make informed decisions for yourself. We want you to feel confident and excited about studying close to home, knowing that you’re getting top-notch education and awesome experiences.

## How Does It Work?

Our dashboard is packed with awesome features to help you find your perfect university match! Here’s what you can explore:

- **Uni Scores on the Global Stage** 🌍: Curious about how our universities stack up internationally? Check out individual scores on key metrics from QS, covering academic reputation, research quality, and job prospects. You'll see how each university excels in different areas!

- **Rankings Over the Years** 📈: Ever wondered which New Zealand universities are climbing the global ranks? Track their performance over the years with data from THE (Times Higher Education) and QS rankings. See who’s leading the chart nationally and internationally, and discover the rising stars!

- **Top Subject Fields** 🏆: Want to know which university is best for your dream major? Whether it’s engineering, technology, or any other field, our dashboard shows you the top-ranked universities in specific subjects. Find out where you’ll get the best education for your chosen career path!

## The Big Picture

By using this tool, you'll not only find the perfect university for you, but you'll also be supporting local education, helping our universities grow, and keeping New Zealand's academic community vibrant and thriving.

So dive in, explore, and find your future right here at home! 🌏✨


                """,
            ),
             vm.Card(
                text="""
                ![](assets/images/unilogo.png#my-image)
            """,
            ),
            
        ],
    )
    return page_intro

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from vizro import Vizro
import vizro.models as vm
from vizro.models.types import capture

# Vizro._reset()
gapminder = pd.read_csv('uni.csv', header=0, usecols=[
    "University Name", 
    "Academic reputation (QS25)", 
    "Teaching quality (THE24)", 
    "Employment Outcomes (QS25)", 
    "Research quality (THE24)", 
    "International Research Network (QS25)", 
    "Employer Reputation (QS25)"
])

gapminder_1 = pd.DataFrame(dict(
    r=[82.2, 39.7, 92.9, 88.3, 87.4, 44.7],
    r_otago=[45, 35.6, 59.1, 75.8, 79.5, 24.6],
    r_massey=[30.1, 28.7, 49.2, 60.5, 85.1, 14],
    r_victoria=[42.8, 28.6, 71.6, 69.4, 70.7, 21.4],
    r_waikato=[19.1, 26.1, 46.4, 74.3, 55.1, 11.7],
    r_canterbury=[34.7, 28.6, 82.3, 62.4, 63, 27.3],
    r_lincoln=[8.2, 33.9, 40, 68.4, 20.2, 5],
    r_aut=[19.3, 23.8, 12.4, 84, 52.6, 11.2],
    theta=['Academic reputation', 'Teaching quality', 'Employment Outcomes', 'Research quality', 'International Research Network', 'Employer Reputation']
))

@capture("graph")
def radarchart(data_frame, r, theta, title=None, markers=None, hover_name=None, line_close=None, template=None): 
    fig_radar = px.line_polar(data_frame=data_frame, r=r, theta=theta, title=title, markers=markers, hover_name=hover_name, line_close=line_close, template=template)
    
    fig_radar.update_layout(
        legend=dict(
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        ),
        annotations=[
            dict(
                xref='paper', 
                yref='paper',
                x=0.5, 
                y=-0.1,  # Position below the chart
                showarrow=False,
                text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>, <a href='https://www.timeshighereducation.com/world-university-rankings'>THE Rankings</a>",
                font=dict(
                    family="Georgia, serif",
                    size=12,
                ),
            )
        ]
    ) 
    
    fig_radar.update_traces(fill='toself')

    fig_radar.update_layout(
        font_family="Georgia, serif",
        title_font_family="Georgia, serif",
    )
    return fig_radar

def create_metrics():
    """Function returns a page to show scores of different metrics on each university."""
    page_years = vm.Page(
        title="Universities' Scores in metrics",
        description="Discovering how different NZ universities are scored with different metrics",
        layout=vm.Layout(grid=[[0],]),
        components=[
            vm.Tabs(
                tabs=[
                    vm.Container(
                        title="Auckland",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="uoa",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r",
                                    theta="theta",
                                    title="University of Auckland",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True, 
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                ![](assets/images/uoa2.png#my-image2)

                    
                                
                                The University of Auckland is New Zealand’s leading university, located in the country’s largest city. 
                                
                                It offers a comprehensive range of programs and is known for its strong emphasis on research and innovation. 

                                 > ## WHAT DOES THIS MEAN? 

                                > - **Academic Reputation (82.2)**: The University of Auckland is known around the world for its high academic standards. You'll be able to learn from some of the greatest minds in the world.

                                > - **Employment Outcomes (92.9)**: you will have good job chances and exciting career options right after you graduate.

                                > - **Research Quality (88.3)**: At UOA, you can dive into cutting-edge research, where new projects and findings happen every day. You'll be a part of a university that challenges what people think they know.

                                > - **International Research Network (87.4)**: Work with the best experts in the world. Because UOA has strong international ties, you'll get a global view and useful training.  
                                
                                If you choose the University of Auckland, you'll be choosing a university that is highly regarded, has great job prospects, and does great study. 
                                You'll accomplish well in school and at work there, and you'll still be close to the exciting city life of Auckland. 🌟📚🌍

         
                                """,
                
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Otago",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="otago",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_otago",
                                    theta="theta",
                                    title="University of Otago",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/otago.png#my-image3)
                                
                                The University of Otago is New Zealand’s oldest university, located in the scenic city of Dunedin. 
                                
                                It offers a rich variety of programs and is renowned for its vibrant campus life and strong research focus.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (59.1)**: Otago graduates are highly sought after by employers, leading to strong job prospects and successful career paths right after graduation.
                                
                                > - **Research Quality (75.8)**: Engage in high-impact research at Otago, where students and faculty work on innovative projects that drive forward scientific and academic knowledge.
                                
                                > - **International Research Network (79.5)**: Otago boasts strong international collaborations, giving students the opportunity to participate in global research initiatives and broaden their academic horizons.
                                
                                Choosing the University of Otago means joining a university that values academic excellence, offers significant research opportunities, and fosters a supportive and dynamic student community. It's a place where you'll not only grow academically but also enjoy a vibrant and fulfilling university experience in a beautiful setting. 🌟📚🌏
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Massey",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="massey",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_massey",
                                    theta="theta",
                                    title="Massey University",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/massey.png#my-image4)
                                
                                ### Massey University
                                Massey University is renowned for its innovative teaching methods and extensive research programs, with campuses in Palmerston North, Albany, and Wellington.
                                
                                It offers a wide range of programs and emphasizes practical, hands-on learning experiences.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **International Research Network (85.1)**: Massey has an extensive international research network, allowing students to collaborate on global projects and gain international experience.
                                
                                > - **Research Quality (60.5)**: Engage in high-quality research at Massey, where innovative projects and discoveries are highly encouraged.
                                
                                > - **Employment Outcomes (49.2)**: Massey graduates are well-prepared for the workforce, with solid job prospects after graduation.
                                
                                Choosing Massey University means embracing innovation and benefiting from a global perspective, with numerous opportunities for international collaboration. 🌟🌐📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Victoria @ Wellington",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="victoria",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_victoria",
                                    theta="theta",
                                    title="Victoria University of Wellington",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn"
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/victoria.png#my-image5)
                                
                                ### Victoria University of Wellington
                                Victoria University of Wellington is celebrated for its strong emphasis on research and academic excellence. Located in New Zealand's capital, it offers unique opportunities for engagement with government and industry.
                                
                                It offers a diverse range of programs and is known for its vibrant campus life and strong community engagement.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (71.6)**: Graduates from Victoria have strong employment prospects, with many finding successful careers shortly after graduation.
                                
                                > - **Research Quality (69.4)**: Victoria excels in research, providing students with opportunities to participate in cutting-edge projects.
                                
                                > - **International Research Network (70.7)**: Victoria's strong international connections mean students can participate in global research initiatives and gain a global perspective.
                                
                                Choosing Victoria University of Wellington means gaining access to excellent academic programs and strong career opportunities in the heart of New Zealand's capital. 🌟🏙️📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Waikato",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="waikato",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_waikato",
                                    theta="theta",
                                    title="University of Waikato",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/waikato.png#my-image6)
                                
                                ### University of Waikato
                                The University of Waikato, located in Hamilton, is known for its innovative approach to education and strong ties to the community.
                                
                                It offers a diverse range of programs and emphasizes research excellence and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (74.3)**: Waikato excels in research, providing students with opportunities to participate in cutting-edge projects and innovations.
                                
                                > - **International Research Network (55.1)**: The university's global connections mean you'll have access to a diverse range of research opportunities and collaborations.
                                
                                Choosing the University of Waikato means joining a university that values research and practical experience. It's a place where you can engage in high-quality research while being part of a supportive and innovative community. 🌟🔬📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Canterbury",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="canterbury",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_canterbury",
                                    theta="theta",
                                    title="University of Canterbury",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/canterbury.png#my-image7)
                                
                               ### University of Canterbury
                                The University of Canterbury, located in Christchurch, is renowned for its strong engineering and science programs.
                                
                                It offers a wide range of academic programs and is committed to providing a high-quality education through research and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Employment Outcomes (82.3)**: Canterbury graduates are highly sought after by employers, ensuring strong job prospects and exciting career opportunities.
                                
                                > - **International Research Network (63)**: The university's international collaborations provide students with opportunities to engage in global research projects.
                                
                                Choosing the University of Canterbury means being part of a respected institution with excellent job prospects and strong international research connections. It's a place where you can thrive academically and professionally. 🌟🔧📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="Lincoln",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="lincoln",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_lincoln",
                                    theta="theta",
                                    title="Lincoln University",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/lincoln.png#my-image8)
                                
                                ### Lincoln University
                                Lincoln University, located near Christchurch, is a specialist land-based university with a strong focus on agriculture and environmental science.
                                
                                It offers unique programs tailored to these fields and emphasizes research and practical learning.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (68.4)**: Lincoln excels in research, particularly in areas related to agriculture and environmental science, providing students with opportunities to contribute to significant discoveries.
                                
                                Choosing Lincoln University means gaining expertise in specialized fields with strong research support. It's a place where you can engage in high-quality research while being close to nature. 🌟🌱📚
                                """,
                            ),
                        ],
                    ),
                    vm.Container(
                        title="AUT",
                        layout=vm.Layout(grid=[[1, 0, 0]]),
                        components=[
                            vm.Graph(
                                id="aut",
                                figure=radarchart(
                                    gapminder_1,
                                    r="r_aut",
                                    theta="theta",
                                    title="AUT",
                                    markers=True,
                                    hover_name="theta",
                                    line_close=True,
                                    template="seaborn",
                                ),
                            ),
                            vm.Card(
                                text="""
                                # ![](assets/images/aut.png#my-image9)
                                
                                ### Auckland University of Technology (AUT)
                                Auckland University of Technology (AUT), located in Auckland, is known for its innovative teaching methods and strong industry connections.
                                
                                It offers a dynamic learning environment with a focus on practical skills and real-world experience.
                                
                                > ### SO WHAT DOES THIS MEAN? 
                                
                                > - **Research Quality (84)**: AUT's commitment to research excellence provides students with opportunities to engage in high-impact projects and innovations.
                                
                                > - **International Research Network (52.6)**: AUT's strong international connections mean you'll have access to a global perspective and valuable experience.
                                
                                Choosing AUT means embracing innovation and benefiting from strong industry ties. It's a place where you can receive a forward-thinking education and gain practical skills for your future career. 🌟💡📚
                                """,
                            ),
                        ],
                    ),
                ],
            )
        ]
    )
    return page_years

# Load the data
gapminder = pd.read_csv('uni.csv')

# Select only the specified columns
columns_to_keep = ["University Name", "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
gapminder = gapminder[columns_to_keep]

# Melt the year columns into a single column
gapminder_line = gapminder.melt(id_vars=["University Name"], 
                                var_name="Year", 
                                value_name="International Rankings")

# Calculate the national rankings for each year
gapminder_line["National Rankings"] = gapminder_line.groupby("Year")["International Rankings"].rank(ascending=True).astype(int)


@capture("graph")
def linechart(data_frame, x, y, color=None, title=None,labels=None, markers=None, hover_name=None, template=None): 
    fig = px.line(data_frame=data_frame, x=x, y=y, color=color, title=title, labels=labels, markers=markers, hover_name=hover_name, template=template)
    
    fig.update_layout(
        title=go.layout.Title(
            text="New Zealand Uni rankings",
            font=dict(
                family="Georgia, serif, bold",
                size=25,

            ),
            xref="paper",
            x=0
            ),
    
            legend=dict(
                font=dict(
                    family="Georgia, serif",
                    size=12,
                    # color="black"
        )
    ),
  
    annotations=[
        dict(
            xref='paper', 
            yref='paper',
            x=0, 
            y=-0.2,
            showarrow=False,
            text="Source: <a href='https://www.topuniversities.com/universities/university-auckland'>QS Rankings</a>",
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        )
    ],
        
        yaxis=dict(autorange='reversed'))
    
    return fig
    
def create_rankings_years():
    """Function returns a page to perform analysis on university level."""
  
    columnsDefs = [
        {"field": "Year"},
        {"field": "University Name"},
        {"field": "International Rankings"},
        {"field": "National Rankings"},
    ]
   
    # Benchmark analysis
    page_years = vm.Page(
        title="Rankings through the years",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout(grid=[[3, 1, 1]] *2 + [[0, 1, 1]] * 5 + [[2, 1, 1]]),
        components=[
            vm.AgGrid(
                title="Click on a cell in University Name column:",
                figure=dash_ag_grid(data_frame=gapminder_line, columnDefs=columnsDefs, dashGridOptions={"pagination": True}),
                actions=[vm.Action(function=filter_interaction(targets=["line_university"]))],
            ),
            vm.Graph(
                id="line_university",
                figure=linechart(
                    gapminder_line,
                    x="Year",
                    y="International Rankings",
                    color="University Name",
                    labels={"Year": "Year", "International Rankings": "International Ranking", "National Rankings": "National Ranking"},
                    markers=True,
                    hover_name="University Name",
                    template="simple_white", 
                ),
                
                 # Use the customized figure here
            ),
            # Uncomment the following lines if needed
            vm.Button(text="Export data", actions=[vm.Action(function=export_data(targets=["line_university"]))]),
            vm.Card(
                                text="""
                                Our line chart vividly illustrates the international rankings of New Zealand universities over the years. Most universities, including the University of Auckland, the University of Waikato, and Massey University, show an upward trend in their global standings, reflecting their increasing reputation and quality.

                                A higher international ranking means that New Zealand universities are offering competitive, high-quality education compared to others worldwide. These rankings are based on rigorous criteria by QS, one of the most prestigious ranking systems globally, which evaluates universities on Academic Reputation, Teaching Quality, Employment Outcomes, Research Quality, International Research Network, and Employer Reputation.

                                Seeing universities climb in these rankings indicates that they are consistently improving and maintaining high standards, making them reliable choices for students. On the other hand, some universities have seen a decrease, providing a complete picture of the dynamic educational landscape.
                                """,
                            ),
            
        ],
        # Uncomment the following lines if needed
        controls=[
            vm.Filter(column="University Name", selector=vm.Dropdown(value="ALL", multi=True, title="Select University")),
            # vm.Filter(column="Year", selector=vm.RangeSlider(title="Select Year", step=1, marks=None)),
            vm.Parameter(
                targets=["line_university.y"],
                selector=vm.Dropdown(
                    options=["International Rankings", "National Rankings"], multi=False, value="International Rankings", title="Choose between International and National Rankings"
                ),
            ),
            
        ],
    )
    return page_years

gapminder = pd.read_csv('uni.csv',
                        header=0,
                        usecols=["University Name", "Arts and humanities ranking THE2024", "Engineering & Technology ranking THE24", "Natural science rankings QS24", "Life science/ medical rankings QS24", "Economics & Business Rankings THE24"])

@capture("graph")
def barchart(data_frame, x, y, title=None, text=None, template=None):
    fig_bar = px.bar(data_frame=data_frame, x=x, y=y, title=title, text=text, template=template)
    
    fig_bar.update_layout(barmode='stack', xaxis={'categoryorder':'total ascending'})
    
    fig_bar.update_layout(
        title=go.layout.Title(
        text="*Smaller number means higher national ranking",
        font=dict(
            family="Georgia, serif",
            size=25,
        ),
        xref="paper",
        x=0
    ),
    legend=dict(
        font=dict(
            family="Georgia, serif",
            size=12,
            # color="black"
        )
    ),
    annotations=[
        dict(
            xref='paper', 
            yref='paper',
            x=0, 
            y=-0.2,
            showarrow=False,
            font=dict(
                family="Georgia, serif",
                size=12,
            )
        )
    ],
  
)
    fig_bar.update_layout(
        font_family="Georgia, serif",
    )

    return fig_bar


def create_subject():
    """Function returns a page to perform analysis on university level."""

    page_subject = vm.Page(
        title="Uni rankings by subject",
        description="Discovering how different NZ universities are ranked through the years",
        layout=vm.Layout( grid=[[1, 1, 1, 1, 1]] + [[0, 0, 0, 0, 0]] * 4,
            row_min_height="100px",
            row_gap="24px",),
        components=[
            vm.Graph(
                id="barchart",
                figure=barchart(
                    gapminder,
                    x="University Name",
                    y="Arts and humanities ranking THE2024",
                    text="Arts and humanities ranking THE2024",
                    template="simple_white", 
                ),
            ),
            vm.Card(
            text="""
               scroll down! 
               ### National rankings of universities based on subject field
               
                #### - Subject fields to choose from: 
                
                 
                > - 🏛️ Arts and humanities: Art, History, Philosophy, Literature, Classics, Media Studies, Film studies 
                    
                > - ⚙️ Engineering & Technology: Electronic, Computer engineering, Biomedical engineering, Computer Science, IT, Food Technology
                    
                > - 🔬 Natural science: Physics, Chemistry, Biology 
                    
                > - 🩺 Life science/ medical: Pharmaceuticals, Biotechnology, Biomedical Science 
                    
                > - 🏭 Economics & Business: Economics, Marketing, Finance
                
                    
                >
                >  Choose subject field in selector on your left. 
                >
                
                Source: 
                - https://www.topuniversities.com
                - https://www.timeshighereducation.com/world-university-rankings
                
             
            
            """,
        ),
        ],
        controls=[
            vm.Parameter(
                targets=["barchart.y"],
                selector=vm.Dropdown(
                    options=["Arts and humanities ranking THE2024", "Engineering & Technology ranking THE24", "Natural science rankings QS24", "Life science/ medical rankings QS24", "Economics & Business Rankings THE24"], multi=False, value="Arts and humanities ranking THE2024", title="Choose subject field"
                ),
            ),
             vm.Parameter(
                targets=["barchart.text"],
                selector=vm.Dropdown(
                    options=["Arts and humanities ranking THE2024", "Engineering & Technology ranking THE24", "Natural science rankings QS24", "Life science/ medical rankings QS24", "Economics & Business Rankings THE24"], multi=False, value="Arts and humanities ranking THE2024", title="Choose subject field to see specific rankings on the bars"
                ),
            ),
        ],
    )
    return page_subject


import vizro.models as vm
import vizro.plotly.express as px
from vizro import Vizro

def create_home_page():
    """Function returns the Home page."""

    tab_1 = vm.Container(
        title="🧑‍🎓 Visual Analytics of NZ universities",
        layout=vm.Layout(grid=[[0, 1], [2, 3]], row_gap="18px", col_gap="18px"),
        components=[
            
            vm.Card(
                text="""
                    ###  Introduction page 
                    Start Here: Discover Your Path!
                """,
                href="intro",
            ),
            vm.Card(
                text="""
                       ### 📈 Universities' Metrics 
                        Uni Scores: Explore the Leaders!
                    """,
                href="/universities-scores-in-metrics",
            ),
            vm.Card(
                text="""
                    ### 📊 Rankings through the years
                    Ranking Trends: See the yearly trends
                   
                """,
                href="/rankings-through-the-years",
            ),
            vm.Card(
                text="""
                    ### 🧠 Rankings by subject field
                    Find Your Niche: Top Unis by Subject
                """,
                href="/uni-rankings-by-subject",
            ),
        ],
    )


    page_home = vm.Page(
        title="Home",
        # description="Intelligence Dashboard for Analytics-Experience project.",
        description="[Research Project] Predicting Air Particulate Matter at Scale.",
        # components=[vm.Tabs(tabs=[tab_1, tab_2, tab_3, tab_4, tab_5])], 
        components=[vm.Tabs(tabs=[tab_1])], 
                   # controls=[
                   #     # vm.Filter(column='Site', selector=vm.Dropdown(value=['ALL'])),
                   #     vm.Filter(column='Site', selector=vm.Dropdown(value="Penrose", multi=False, title="Select Location")),
                   # ],
        )

    return page_home

IS_JUPYTERLAB = 'true'



dashboard = vm.Dashboard(
    pages=[
        create_home_page(),
        create_intro(),
        create_rankings_years(),
        create_metrics(),
        create_subject(),
        
    ],
    navigation=vm.Navigation(
        nav_selector=vm.NavBar(
            items=[
                vm.NavLink(label="Home", pages=["Home"], icon="Home"),  # Added comma here
                vm.NavLink(label="Introduction", pages=["Intro"], icon="Waving Hand"),
                vm.NavLink(
                    label="Rankings through the years",
                    pages=["Rankings through the years"],
                    icon="Timeline",
                ),
                 vm.NavLink(
                    label="Universities' Metrics",
                    pages=["Universities' Scores in metrics"],
                    icon="Grade",
                ),
                vm.NavLink(
                    label="Rankings of subject field",
                    pages=["Uni rankings by subject"],
                    icon="Auto Stories",
                ),
            ]
        ),
    ),
)

if not IS_JUPYTERLAB:
    app = Vizro().build(dashboard)
    server = app.server
    # server = app.dash.server
    
    if __name__ == "__main__":  
        # app.run(port=8080)
        app.run()
else:
    # Vizro(assets_folder="assets").build(dashboard).run(port=8085)
    Vizro(assets_folder="assets").build(dashboard).run()

