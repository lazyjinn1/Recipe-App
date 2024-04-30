from recipes.models import Recipe
from io import BytesIO 
import base64
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

cooking_time_range = [0.0, 25.0, 50.0, 75.0, 100.0]

def get_graph():
    buffer = BytesIO() #create a BytesIO buffer for the image     
    plt.savefig(buffer, format='png') #create a plot with a bytesIO object as a file-like object. Set format to png
    buffer.seek(0) #set cursor to the beginning of the stream
    image_png = buffer.getvalue() #retrieve the content of the file
    graph = base64.b64encode(image_png) #encode the bytes-like object
    graph = graph.decode('utf-8') #decode to get the string as output
    buffer.close() #free up the memory of buffer
    return graph #return the image/graph

# def get_pie_chart(data):
#     plt.figure(figsize=(8, 6))
#     plt.pie(data, labels=data['difficulty'], autopct='%1.1f%%', startangle=140)
#     plt.axis('equal')
#     plt.show()
#     return


def get_chart(chart_type, data, **kwargs):
   plt.switch_backend('AGG')

   #specify figure size
   fig, ax = plt.subplots(figsize=(11,5))
   
   #select chart_type based on user input from the form
   if chart_type == 'line':
        plt.title("Cooking Time by Recipe")
        ax.plot(data['recipe_name'], data['cooking_time'], "or-")
        ax.set_xticklabels(data['recipe_name'], rotation=90)
        ax.set_yticks(data['cooking_time'])

   elif chart_type == 'pie':
        plt.title("Cooking Time by Recipe")

   elif chart_type == 'bar':
        plt.title("Cooking Time by Recipe")
        ax.bar(data['recipe_name'], data['cooking_time'])
        ax.set_xticklabels(data['recipe_name'], rotation=90)
        ax.set_yticks(data['cooking_time'])
   else:
        print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart = get_graph() 
   return chart       
