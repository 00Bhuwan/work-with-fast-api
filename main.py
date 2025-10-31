from typing import Union

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://9843lalitpur_db_user:9fNHUfa3yBZ1Wp3p@gettingstart.xnzwm9y.mongodb.net")





