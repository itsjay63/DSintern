# Importing the libraries
import pandas as pd
import webbrowser #open webbrowser automatically 
# !pip install dash
import dash
import dash_html_components as html

# favicon  == 16x16 icon ----> favicon.ico  ----> assests

# Declaring Global variables
project_name = None
app = dash.Dash() #dash: is a library and Dash is a class .

# Defining My Functions
def load_model():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')
    
def create_app_ui():
    main_layout = html.Div(
    [
    html.H1(children = "Sentiment Analysis with Insights"),
    html.H5(children = "This is awesome.....")
    ]    
    )
    
    return main_layout

# Main Function to control the Flow of your Project
def main():
    print("Start of your project")
    load_model()
    open_browser()
    
    global scrappedReviews
    global project_name
    global app
    
    project_name = "Sentiment Analysis with Insights"
    #print("My project name = ", project_name)
    #print('my scrapped data = ', scrappedReviews.sample(5) )
    
    
    app.title = project_name
    app.layout = create_app_ui()
    app.run_server() #it is a blocking statement 
    #below 4 line will not be execuated until the server is running
    
    
    
    print("End of my project")
    project_name = None
    scrappedReviews = None
    app = None
    
        
# Calling the main function 
if __name__ == '__main__':
    main()
    
    
    