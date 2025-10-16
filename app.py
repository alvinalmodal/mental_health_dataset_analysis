import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc, html
from queries.demographics import get_gender_distribution, get_country_distribution, get_occupation_distribution
from queries.prevalence import get_family_history_pct, get_treatment_pct, get_stress_distribution, get_mood_swing_distribution
from queries.workplace_environment import get_work_interest_correlation, get_interview_attitude, get_care_options_distribution
from queries.insights_and_correlations import get_history_treatment_correlation, get_coping_social_correlation

# demographics data
gender_distribution_df = get_gender_distribution()
country_distribution_df = get_country_distribution()
occupation_distribution_df = get_occupation_distribution()

fig_gender = px.pie(gender_distribution_df, values='Values', names='Gender', title='Gender Distribution')

fig_country = px.bar(country_distribution_df, x='Country', y='Number of Respondents', title='Top 10 Countries by Respondents')
fig_occupation = px.bar(occupation_distribution_df.sort_values('Number of Participants'), y='Occupation', x='Number of Participants', orientation='h', title='Top 10 Occupations')

# prevalence
family_history_pct = get_family_history_pct()
treatment_pct = get_treatment_pct()
stress_distribution_df = get_stress_distribution()
mood_swings_df = get_mood_swing_distribution()
fig_stress = px.pie(stress_distribution_df, values='count', names='Growing_Stress', title='Self-Reported Growing Stress', hole=0.4)
fig_mood = px.pie(mood_swings_df, values='count', names='Mood_Swings', title='Reported Mood Swings', hole=0.4)

# workplace and environment
work_interest_corr_df = get_work_interest_correlation()
fig_work_interest = px.bar(work_interest_corr_df, barmode='group', title='Work Interest vs. Seeking Treatment')
interview_attitude_df = get_interview_attitude()
fig_interview = px.bar(interview_attitude_df, x='mental_health_interview', y='count', title='Attitude: Discussing Mental Health in Interviews')
care_options_dist_df = get_care_options_distribution()
fig_care_options = px.bar(care_options_dist_df, x='care_options', y='count', title='Awareness of Employer-Provided Care Options')

# key insights and correlations
history_treatment_corr_df = get_history_treatment_correlation()
fig_history_treatment = px.bar(history_treatment_corr_df, x='family_history', y=['Sought Treatment', 'Did Not Seek Treatment'], barmode='stack', title='Family History vs. Seeking Treatment (%)')

coping_social_corr_df = get_coping_social_correlation()
fig_coping_social = px.imshow(coping_social_corr_df, text_auto=True, aspect="auto", title='Coping Struggles vs. Social Weakness (%)',
                              labels=dict(x="Social Weakness", y="Coping Struggles", color="Percentage"))

# web server initialization
app = dash.Dash(__name__)

# styling
colors = { 'background': '#F0F8FF', 'text': '#003366', 'header': '#002244' }
styles = {
    'section': {'padding': '20px', 'margin': '10px', 'border-radius': '5px', 'background-color': '#FFFFFF', 'box-shadow': '0 2px 4px 0 rgba(0,0,0,0.1)'},
    'h1': {'textAlign': 'center', 'color': colors['header']},
    'h2': {'color': colors['header']},
    'paragraph': {'color': colors['text']},
    'column': {'display': 'inline-block', 'width': '48%', 'padding': '1%'}
}

app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text'], 'font-family': 'Arial, sans-serif'}, children=[
    html.H1(children='Mental Health in the Workplace: An Infographic', style=styles['h1']),
    html.P("An analysis of workplace attitudes and the prevalence of mental health concerns.", style={'textAlign': 'center'}),
    # Section 1: Introduction
    html.Div(style=styles['section'], children=[
        html.H2("1. The Importance of Mental Health at Work", style=styles['h2']),
        html.P("Mental well-being is crucial for a productive, healthy, and positive workplace. This infographic explores the state of mental health among professionals based on self-reported data, highlighting key trends and challenges.", style=styles['paragraph'])
    ]),
    # Section 2: Demographic Profile
    html.Div(style=styles['section'], children=[
        html.H2("2. Demographic Profile of Respondents", style=styles['h2']),
        html.Div([
            html.Div(dcc.Graph(figure=fig_gender), style=styles['column']),
            html.Div(dcc.Graph(figure=fig_country), style=styles['column'])
        ]),
        html.Div([dcc.Graph(figure=fig_occupation)])
    ]),
    # Section 3: Prevalence of Concerns
    html.Div(style=styles['section'], children=[
        html.H2("3. Prevalence of Mental Health Concerns", style=styles['h2']),
        html.H3(f"{family_history_pct:.1f}% of respondents have a family history of mental illness.", style={'textAlign': 'center'}),
        html.H3(f"{treatment_pct:.1f}% of respondents have sought treatment for a mental health condition.", style={'textAlign': 'center'}),
        html.Div([
            html.Div(dcc.Graph(figure=fig_stress), style=styles['column']),
            html.Div(dcc.Graph(figure=fig_mood), style=styles['column'])
        ]),
    ]),
    # Section 4: The Workplace Environment
    html.Div(style=styles['section'], children=[
        html.H2("4. The Workplace Environment", style=styles['h2']),
        html.Div([
            html.Div(dcc.Graph(figure=fig_work_interest), style=styles['column']),
            html.Div(dcc.Graph(figure=fig_care_options), style=styles['column'])
        ]),
        # html.Div([dcc.Graph(figure=fig_interview)])
    ]),
    # Section 5: Key Insights & Correlations
    html.Div(style=styles['section'], children=[
        html.H2("5. Key Insights and Correlations", style=styles['h2']),
        html.Div([
            html.Div(dcc.Graph(figure=fig_history_treatment), style=styles['column']),
            html.Div(dcc.Graph(figure=fig_coping_social), style=styles['column'])
        ]),
    ]),
    # Section 6: Recommendations
    html.Div(style=styles['section'], children=[
        html.H2("6. Recommendations for Employers", style=styles['h2']),
        html.Ul([
            html.Li("Promote Open Dialogue: Create a culture where employees feel safe discussing mental health without fear of stigma."),
            html.Li("Improve Access to Care: Ensure employees are aware of available mental health resources and benefits."),
            html.Li("Train Leadership: Equip managers to recognize signs of distress and support their team members effectively."),
            html.Li("Offer Flexibility: Flexible work arrangements can help employees manage stress and balance work-life demands.")
        ])
    ]),
    # Section 7: Conclusion
    html.Div(style=styles['section'], children=[
        html.H2("7. Conclusion", style=styles['h2']),
        html.P("The data reveals a clear need for greater focus on mental health in the workplace. By fostering a supportive and open environment, employers can not only improve the well-being of their employees but also enhance overall productivity and retention.", style=styles['paragraph'])
    ]),
])

# run server
if __name__ == '__main__':
    app.run(debug=True)
