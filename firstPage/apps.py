from django.apps import AppConfig
from django.apps import AppConfig
from django.conf import settings
import turicreate
class FirstpageConfig(AppConfig):
	name = 'firstPage'
	# create path to models
	model=turicreate.load_model(settings.MODELS+'myModel1/')
	movie=turicreate.SFrame('~/machine/data/final_sub_movie_frame')


