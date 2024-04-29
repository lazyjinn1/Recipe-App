from recipes.models import Recipe
from io import BytesIO 
import base64
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

difficulty_choices = ['Easy', 'Medium', 'Intermediate', 'Hard']


def get_graph():
    buffer = BytesIO() #create a BytesIO buffer for the image     
    plt.savefig(buffer, format='png') #create a plot with a bytesIO object as a file-like object. Set format to png
    buffer.seek(0) #set cursor to the beginning of the stream
    image_png = buffer.getvalue() #retrieve the content of the file
    graph = base64.b64encode(image_png) #encode the bytes-like object
    graph = graph.decode('utf-8') #decode to get the string as output
    buffer.close() #free up the memory of buffer
    return graph #return the image/graph

def get_line_chart(data):
    plt.plot(difficulty_choices, data['cooking_time'])
    return

def get_pie_chart(data):
    labels = difficulty_choices
    plt.pie(data['cooking_time'], labels=labels)
    return

def get_bar_chart(data):
    plt.bar(data['ingredients'], data['quantity'])
    return

def get_chart(chart_type, data, **kwargs):
   plt.switch_backend('AGG')

   #specify figure size
   fig = plt.figure(figsize=(6,3))

   #select chart_type based on user input from the form
   if chart_type == 'line':
        get_line_chart()

   elif chart_type == 'pie':
        get_pie_chart()

   elif chart_type == 'bar':
        get_bar_chart()

   else:
        print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart = get_graph() 
   return chart       
