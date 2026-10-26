from django.shortcuts import render

# Create your views here.

import os 

import psycopg
from psycopg.types.json import Jsonb

conn = psycopg.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSD'),
)

cur = conn.cursor()

# Please change directory path to fit file position on your file manager
file = open(r'C:\Users\USER\OneDrive\Documents\Chijioke_Ofili_Second_Test\bincom_test.sql', 'r')

cur.execute(file.read())

def home_page(request):
    
    context = {
        
    }
    return render(request, 'Templates/home.html', context)