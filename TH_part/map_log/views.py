from django.views.generic.base import TemplateView #GenericView 중 TemplateView 사용
from django.shortcuts import render

from .models import Story, Region #Model 'Story', 'Region' 사용

class MainPageView(TemplateView): #메인페이지 보여주는 View
	
	template_name = "map_log/index.html"
	
	def get_context_data(self, **kwargs): # context변수 index.html로 넘겨주기
		context = super(MainPageView, self).get_context_data(**kwargs)
		region_list = Region.objects.values('region', 'base_color') # []부분 이해 필요 = html에서 사용할 변수의 이름같음.
	
		# < region_list = [{region : base_color}] 형태로 만들기 >
		regions=[] # 지역 리스트
		base_colors=[] # 색상 리스트
		
		for i in region_list:
			regions.append(i.get('region'))
			base_colors.append(i.get('base_color'))
		
		colors = dict(zip(regions, base_colors)) # 두 리스트를 하나는 key값, 다른 하나는 value값으로 해서 딕셔너리 생성
		context = {
			'colors':colors
		}
		
		return context
	


