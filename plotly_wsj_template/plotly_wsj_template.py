import plotly.graph_objects as go
import plotly.io as pio

pio.templates["wsj"] = go.layout.Template(
    
    # LAYOUT
    #Set overall layout styles here
    layout = {
        # Colorways
        'colorway': ['#0098db', '#ffd63d', "#bfbfbf", "#e29320", "#333333"],
        
        # Margin
        'margin': dict(l=0, r=0, t=0, b=0),
        
        # Title
        'title':
            {'font': {'family': 'Retina Medium', 
                      'size':15,
                      'color': '#333',
                     },
             'xanchor': 'left',
             'x': 0,
            },
        
        # Legend
        'showlegend' : False,
        
        # Plot
        'colorscale':
            {'diverging': ['#0079ae', '#0098db', '#95cbee', '#c9e2f5', '#e6eff9', '#eeeff0', '#ffd63d', '#ffd63d', '#f9a224', '#ee3a43', '#ce3139'],
             'sequential': ['#e6eff9', '#c9e2f5', '#95cbee', '#0098db', '#0079ae'],
             'sequentialminus': ['#ffd63d', '#ffd63d', '#f9a224', '#ee3a43', '#ce3139'],
            },
        
        # Y-axis
        'yaxis': {       
            #Lines
            'gridcolor': '#e2e3e4',
            'gridwidth': 1,
            'linecolor': '#333333',
            'linewidth': 1,
            'zerolinecolor': '#333333',
            'zerolinewidth': 1,
                  
            #Ticks
            'ticks': '',
            'tickfont': {'color': '#333333', 'family': 'Retina Narrow Light', 'size': 13},
            'showtickprefix': 'last',
            'ticklen': 5,
            'ticklabelposition': "inside top",
            
            #Other
            'automargin': True,
        },
        
        # X-axis
        'xaxis': {
            #Lines
            'showgrid' : False,
            'gridcolor': '#e2e3e4',
            'gridwidth': 1,
            'linecolor': '#333333',
            'linewidth': 1,
            'zerolinecolor': '#333333',
            'zerolinewidth': 1,
            'zeroline': True,
                  
            #Ticks
            'ticks': 'outside',
            'tickfont': {'color': '#333333', 'family': 'Retina Narrow Light', 'size': 13},
            'showtickprefix': 'last',
            'ticklen': 5,
            
            #Other
            'automargin': True,
            
        },

    },
    
    # DATA
    # Set trace-specific styles here. Each graph object must be in a tuple or list for each trace
    data = {
        'bar': [go.Bar(
                    textposition='inside',
                    textfont={
                        'family': 'Retina',
                        'size': 15,
                        'color': '#333333'
                    }
         )],
        
        #Line and scatterplots
        'scatter': [go.Scatter(
                        line=dict(width=2),
        )],
    
    
    
    }
)