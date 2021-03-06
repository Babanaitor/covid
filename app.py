
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import os
import numpy as np
from datetime import datetime as dt

df = pd.read_excel('ca/covid.xlsx')
df = df.dropna(thresh=4)
df.reset_index(inplace=True, drop=True)
df.sort_values(by='Country')
countries = df['Country']
countries = sorted(countries.to_list())
population = {'China': 1439323776
    , 'India': 1380004385
    , 'United States': 331002651
    , 'Indonesia': 273523615
    , 'Pakistan': 220892340
    , 'Brazil': 212559417
    , 'Nigeria': 206139589
    , 'Bangladesh': 164689383
    , 'Russia': 145934462
    , 'Mexico': 128932753
    , 'Japan': 126476461
    , 'Ethiopia': 114963588
    , 'Philippines': 109581078
    , 'Egypt': 102334404
    , 'Vietnam': 97338579
    , 'DR Congo': 89561403
    , 'Turkey': 84339067
    , 'Iran': 83992949
    , 'Germany': 83783942
    , 'Thailand': 69799978
    , 'The United Kingdom': 67886011
    , 'France': 65273511
    , 'Italy': 60461826
    , 'Tanzania': 59734218
    , 'South Africa': 59308690
    , 'Myanmar': 54409800
    , 'Kenya': 53771296
    , 'South Korea': 51269185
    , 'Colombia': 50882891
    , 'Spain': 46754778
    , 'Uganda': 45741007
    , 'Argentina': 45195774
    , 'Algeria': 43851044
    , 'Sudan': 43849260
    , 'Ukraine': 43733762
    , 'Iraq': 40222493
    , 'Afghanistan': 38928346
    , 'Poland': 37846611
    , 'Canada': 37742154
    , 'Morocco': 36910560
    , 'Saudi Arabia': 34813871
    , 'Uzbekistan': 33469203
    , 'Peru': 32971854
    , 'Angola': 32866272
    , 'Malaysia': 32365999
    , 'Mozambique': 31255435
    , 'Ghana': 31072940
    , 'Yemen': 29825964
    , 'Nepal': 29136808
    , 'Venezuela': 28435940
    , 'Madagascar': 27691018
    , 'Cameroon': 26545863
    , "Côte d'Ivoire": 26378274
    , 'North Korea': 25778816
    , 'Australia': 25499884
    , 'Niger': 24206644
    , 'Taiwan': 23816775
    , 'Sri Lanka': 21413249
    , 'Burkina Faso': 20903273
    , 'Mali': 20250833
    , 'Romania': 19237691
    , 'Malawi': 19129952
    , 'Chile': 19116201
    , 'Kazakhstan': 18776707
    , 'Zambia': 18383955
    , 'Guatemala': 17915568
    , 'Ecuador': 17643054
    , 'Syria': 17500658
    , 'Netherlands': 17134872
    , 'Senegal': 16743927
    , 'Cambodia': 16718965
    , 'Chad': 16425864
    , 'Somalia': 15893222
    , 'Zimbabwe': 14862924
    , 'Guinea': 13132795
    , 'Rwanda': 12952218
    , 'Benin': 12123200
    , 'Burundi': 11890784
    , 'Tunisia': 11818619
    , 'Bolivia': 11673021
    , 'Belgium': 11589623
    , 'Haiti': 11402528
    , 'Cuba': 11326616
    , 'South Sudan': 11193725
    , 'Dominican Republic': 10847910
    , 'Czech Republic (Czechia)': 10708981
    , 'Greece': 10423054
    , 'Jordan': 10203134
    , 'Portugal': 10196709
    , 'Azerbaijan': 10139177
    , 'Sweden': 10099265
    , 'Honduras': 9904607
    , 'United Arab Emirates': 9890402
    , 'Hungary': 9660351
    , 'Tajikistan': 9537645
    , 'Belarus': 9449323
    , 'Austria': 9006398
    , 'Papua New Guinea': 8947024
    , 'Serbia': 8737371
    , 'Israel': 8655535
    , 'Switzerland': 8654622
    , 'Togo': 8278724
    , 'Sierra Leone': 7976983
    , 'Hong Kong': 7496981
    , 'Laos': 7275560
    , 'Paraguay': 7132538
    , 'Bulgaria': 6948445
    , 'Libya': 6871292
    , 'Lebanon': 6825445
    , 'Nicaragua': 6624554
    , 'Kyrgyzstan': 6524195
    , 'El Salvador': 6486205
    , 'Turkmenistan': 6031200
    , 'Singapore': 5850342
    , 'Denmark': 5792202
    , 'Finland': 5540720
    , 'Congo': 5518087
    , 'Slovakia': 5459642
    , 'Norway': 5421241
    , 'Oman': 5106626
    , 'State of Palestine': 5101414
    , 'Costa Rica': 5094118
    , 'Liberia': 5057681
    , 'Ireland': 4937786
    , 'Central African Republic': 4829767
    , 'New Zealand': 4822233
    , 'Mauritania': 4649658
    , 'Panama': 4314767
    , 'Kuwait': 4270571
    , 'Croatia': 4105267
    , 'Moldova': 4033963
    , 'Georgia': 3989167
    , 'Eritrea': 3546421
    , 'Uruguay': 3473730
    , 'Bosnia and Herzegovina': 3280819
    , 'Mongolia': 3278290
    , 'Armenia': 2963243
    , 'Jamaica': 2961167
    , 'Qatar': 2881053
    , 'Albania': 2877797
    , 'Puerto Rico': 2860853
    , 'Lithuania': 2722289
    , 'Namibia': 2540905
    , 'Gambia': 2416668
    , 'Botswana': 2351627
    , 'Gabon': 2225734
    , 'Lesotho': 2142249
    , 'North Macedonia': 2083374
    , 'Slovenia': 2078938
    , 'Guinea-Bissau': 1968001
    , 'Latvia': 1886198
    , 'Bahrain': 1701575
    , 'Equatorial Guinea': 1402985
    , 'Trinidad and Tobago': 1399488
    , 'Estonia': 1326535
    , 'Timor-Leste': 1318445
    , 'Mauritius': 1271768
    , 'Cyprus': 1207359
    , 'Eswatini': 1160164
    , 'Djibouti': 988000
    , 'Fiji': 896445
    , 'Réunion': 895312
    , 'Comoros': 869601
    , 'Guyana': 786552
    , 'Bhutan': 771608
    , 'Solomon Islands': 686884
    , 'Macao': 649335
    , 'Montenegro': 628066
    , 'Luxembourg': 625978
    , 'Western Sahara': 597339
    , 'Suriname': 586632
    , 'Cabo Verde': 555987
    , 'Maldives': 540544
    , 'Malta': 441543
    , 'Brunei': 437479
    , 'Guadeloupe': 400124
    , 'Belize': 397628
    , 'Bahamas': 393244
    , 'Martinique': 375265
    , 'Iceland': 341243
    , 'Vanuatu': 307145
    , 'French Guiana': 298682
    , 'Barbados': 287375
    , 'New Caledonia': 285498
    , 'French Polynesia': 280908
    , 'Mayotte': 272815
    , 'Sao Tome & Principe': 219159
    , 'Samoa': 198414
    , 'Saint Lucia': 183627
    , 'Channel Islands': 173863
    , 'Guam': 168775
    , 'Curaçao': 164093
    , 'Kiribati': 119449
    , 'Micronesia': 115023
    , 'Grenada': 112523
    , 'St. Vincent & Grenadines': 110940
    , 'Aruba': 106766
    , 'Tonga': 105695
    , 'U.S. Virgin Islands': 104425
    , 'Seychelles': 98347
    , 'Antigua and Barbuda': 97929
    , 'Isle of Man': 85033
    , 'Andorra': 77265
    , 'Dominica': 71986
    , 'Cayman Islands': 65722
    , 'Bermuda': 62278
    , 'Marshall Islands': 59190
    , 'Northern Mariana Islands': 57559
    , 'Greenland': 56770
    , 'American Samoa': 55191
    , 'Saint Kitts & Nevis': 53199
    , 'Faeroe Islands': 48863
    , 'Sint Maarten': 42876
    , 'Monaco': 39242
    , 'Turks and Caicos': 38717
    , 'Saint Martin': 38666
    , 'Liechtenstein': 38128
    , 'San Marino': 33931
    , 'Gibraltar': 33691
    , 'British Virgin Islands': 30231
    , 'Caribbean Netherlands': 26223
    , 'Palau': 18094
    , 'Cook Islands': 17564
    , 'Anguilla': 15003
    , 'Tuvalu': 11792
    , 'Wallis & Futuna': 11239
    , 'Nauru': 10824
    , 'Saint Barthelemy': 9877
    , 'Saint Helena': 6077
    , 'Saint Pierre & Miquelon': 5794
    , 'Montserrat': 4992
    , 'Falkland Islands': 3480
    , 'Niue': 1626
    , 'Tokelau': 1357
    , 'Holy See': 801

              }
genders = {'Male': '', 'Female': ''}
diseases_d = {'None': 0.9, 'Cardiovascular Disease': 10.5, 'Diabetes': 7.3, 'Respiratory Disease': 6.3,
              'High Blood Pressure': 6, 'Cancer': 5.6}
age_0 = 0
age_10 = 0.2
age_20 = 0.2
age_30 = 0.2
age_40 = 0.4
age_50 = 1.3
age_60 = 3.6
age_70 = 8
age_80 = 14.8

app = dash.Dash(__name__, external_stylesheets=['assets/codepen.css'])
server = app.server

app.layout = html.Div(style={'backgroundColor': '#ffffff', 'textAlign': 'center', }, children=[
    html.Br(),
    html.Div([
        html.H3(children='Corona Survival Calculator (Live Update)',
                style={'display': 'inline-block', 'width': '70%', 'textAlign': 'center'}), ]),
    html.Br(),
    html.Br(),
    html.Div([
        html.H1(children='', style={'width': '20%'}),

        dcc.RadioItems(
            id='gender',
            options=[{'label': k, 'value': k} for k in genders.keys()],
            value='Male',
            style={'textAlign': 'center', 'width': '60%', 'display': 'inline-block'}
        ), ]),
    html.Br(),
    html.Div([
        html.H1(children='', style={'width': '20%'}),
        dcc.Dropdown(
            id='diseases',
            options=[{'label': k, 'value': k} for k in diseases_d.keys()],
            placeholder="Select Applicable Diseases",
            multi=True,
            value="",
            style={'textAlign': 'center', 'width': '60%', 'display': 'inline-block'}
        ), ]),
    html.Div([
        html.H1(children='', style={'width': '20%'}),
        html.Br(),
        dcc.Dropdown(
            id='country',
            options=[{'label': n, 'value': n} for n in countries],
            placeholder="Select Country",
            style={'textAlign': 'center', 'width': '60%', 'display': 'inline-block'}
        ), ]),
    html.Div([
        html.H1(children='', style={'width': '20%'}),
        html.Br(),
        dcc.Input(id="age", type="number", placeholder="Age",
                  style={'textAlign': 'center', 'width': '20%', 'display': 'inline-block'}
                  ), ]),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Div(id='out'),
])


@app.callback(
    dash.dependencies.Output('out', 'children'),
    [dash.dependencies.Input('age', 'value'),
     dash.dependencies.Input('gender', 'value'),
     dash.dependencies.Input('diseases', 'value'),
     dash.dependencies.Input('country', 'value')])
def update_output(age, gender, diseases, country):
    global df
    if age and country and diseases is not None:
        diseases_calc = 1
        if len(diseases) == 1:
            diseases_calc = diseases_d[diseases[0]]
        elif len(diseases) == 2:
            diseases_calc = diseases_d[diseases[0]] + diseases_d[diseases[1]]
        elif len(diseases) == 3:
            diseases_calc = diseases_d[diseases[0]] + diseases_d[diseases[1]] + diseases_d[diseases[2]]
        elif len(diseases) == 4:
            diseases_calc = diseases_d[diseases[0]] + diseases_d[diseases[1]] + diseases_d[diseases[2]] + \
                            diseases_d[diseases[3]]
        elif len(diseases) == 5:
            diseases_calc = diseases_d[diseases[0]] + diseases_d[diseases[1]] + diseases_d[diseases[2]] + \
                            diseases_d[diseases[3]] + diseases_d[diseases[4]]

        if 20 > age > 9 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_20 * diseases_calc, 6))
        if 30 > age > 19 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))
        if 40 > age > 29 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))
        if 50 > age > 39 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))
        if 60 > age > 49 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))
        if 70 > age > 59 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))
        if 150 > age > 69 and gender == 'Male':
            return 'Your chances of getting infected are "{}" % '.format(df.loc[(df['Country'] == country).idxmax(),
                                                                                    'Total cases'] / population[country]
                                                                         ) + \
                   'Your chances of dying if infected is "{}" %'.format(round(age_30 * diseases_calc, 6))

if __name__ == '__main__':
    app.run_server()
