from django.shortcuts import render
from .apps import FirstpageConfig
from django.http import JsonResponse
from rest_framework.views import APIView
import json
class call_model(APIView):
	def get(self,request):
		if request.method == 'GET':
			mname = request.GET.get('mname')
			print(mname)
			movie=FirstpageConfig.movie
			mquery=movie[movie['original_title']==mname]
			#print(mquery)
			prediction = FirstpageConfig.model.query(mquery,k=10)
			print('in if')
			print(prediction['reference_label'])
			#context={'a':'HelloWORLdnew'}
			#print(request.POST.get('moviename'))
			dic=dict()
			dic2=dict()
			i=0
			for name in prediction['reference_label']:
				dic2[i]=movie[movie['original_title']==name]['imdb_id'][0]
				i+=1

			i=0
			for name in prediction['reference_label']:
				dic[i]=name
				i+=1
			#moviejson=json.dumps(lst, indent=4, separators=(". ", " = "))JsonResponse(dic,safe=False),
			return render(request,'page2.html',{'dic': dic,'dic2':dic2})

def index(request):
	
	
	
	return render(request,'page.html')