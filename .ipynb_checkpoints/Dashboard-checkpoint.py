#!/usr/bin/env python
# coding: utf-8

# <header style="padding:3px;border-top:3px solid #E37C4D">
# 
# ## 📊 🚀 Advanced Analytics Dashboard 🌟

# In[1]:


import vizro.models as vm
from vizro import Vizro


# <header style="padding:3px;border-top:3px solid #E37C4D">
# 
# ## 📊 1. Home Page

# In[2]:


def create_home_page():
    """Function returns the Home page."""

    tab_1 = vm.Container(
        title="💹 Visual Analytics",
        layout=vm.Layout(grid=[[0, 1], [2, 3]], row_gap="18px", col_gap="18px"),
        components=[
            
            vm.Card(
                text="""
                    ### 📈 University's metrics

                """,
                href="/pm25-variable-analysis-for-penrose",
            ),
            vm.Card(
                text="""
                        ### 📊 Rankings through the years
                    """,
                href="/feature-correlation-visualization",
            ),
            vm.Card(
                text="""
                    ### 💹 **RQ3.** 333
                """,
                href="/executive-summary",
            ),
            vm.Card(
                text="""
                    ### 🧠 **RQ2.** Rankings by subject field
                """,
                href="/predictive-analytics-models-and-algorithms",
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


# <header style="padding:3px;border-top:3px solid #E37C4D">
# 
# ## 📊 2. Page 2

# <header style="padding:3px;border-top:3px solid #E37C4D">
# 
# ## 📊 Dashboard

# In[3]:


IS_JUPYTERLAB = 'false'
Vizro._reset()

dashboard = vm.Dashboard(
    title="New Zealand University Dashboard",
    pages=[
        create_home_page(),
    ],
    navigation=vm.Navigation(
        nav_selector=vm.NavBar(
            items=[
                vm.NavLink(label="Home", pages=["Home"], icon="Home")
            ]
        ),
    ),
)

if not IS_JUPYTERLAB:
    app = Vizro().build(dashboard)
    server = app.dash.server
    
    if __name__ == "__main__":  
        app.run(port=8081)
else:
    Vizro(assets_folder="assets").build(dashboard).run(port=8083)


# In[ ]:




