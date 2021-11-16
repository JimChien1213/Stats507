# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 

# ## Contents
# + [Pandas Table Visualization](#Pandas-Table-Visualization) 

# ## Pandas Table Visualization
# **Author:** Cheng Chun, Chien  
# **Email:**　jimchien@umich.edu  
# [PS6](https://jbhender.github.io/Stats507/F21/ps/ps6.html)

# ## Introduction
# - The slide shows visualization of tabular data using the ***Styler*** class
# - The ***Styler*** creates an HTML table and leverages CSS styling language to control parameters including colors, fonts, borders, background, etc.
# - Following contents will be introduced.
#     1. Formatting Values
#     2. Table Styles
#     3. Bulitin Styles

# ## Formatting Values
# - Styler can distinguish the ***display*** and ***actual*** value
# - To control the display value, use the *.format()* method to manipulate this according to a format spec string or a callable that takes a single value and returns a string.
# - Functions of *.format()*
#     - *precision*: formatting floats
#     - *decimal / thousands*: support other locales
#     - *na_rep*: display missing data
#     - *escape*: displaying safe-HTML or safe-LaTeX

# ## Table Styles
# - Recommend to be used for broad styling, such as entire rows or columns at a time.
# - 3 primary methods of adding custom CSS styles
#     - *.set_table_styles()*: control broader areas of the table with specified internal CSS. Cannot be exported to Excel.
#     - *.set_td_classes()*: link external CSS classes to data cells. Cannot be exported to Excel.
#     - *.apply() and .applymap()*: add direct internal CSS to specific data cells. Can export to Excel.
# - Also used to control features applying to the whole table by generic hover functionality, *:hover*.
# - List of dicts is the format to pass styles to .set_table_styles().

# ## Builtin Styles
# - *.highlight_null*: identifying missing data.
# - *.highlight_min / .highlight_max*: identifying extremeties in data.
# - *.background_gradient*: highlighting cells based or their, or other, values on a numeric scale.
# - *.text_gradient*: highlighting text based on their, or other, values on a numeric scale.
# - *.bar*: displaying mini-charts within cell backgrounds.

import numpy as np
import pandas as pd
# Example of table bar chart
np.random.seed(0)
df = pd.DataFrame(np.random.randn(5,4), columns=['A','B','C','D'])
df.style.bar(subset=['A', 'B'], color='#d65f5f')


