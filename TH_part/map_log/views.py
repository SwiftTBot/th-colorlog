from django.views.generic.base import TemplateView #GenericView base 중 TemplateView 사용
from django.views.generic import CreateView
from django.shortcuts import render

from .models import Story, Region #Model 'Story', 'Region' 사용

#메인페이지 보여주는 View
class MainPageView(TemplateView): 
	
	template_name = "map_log/index.html"
	
	def get_context_data(self, **kwargs): # context변수 index.html로 넘겨주기
		context = super(MainPageView, self).get_context_data(**kwargs)
		region_list = Region.objects.values('region', 'base_color') # region과 base_color값만 가져와서 리스트로 생성하는 부분
	
		'''
		Logic {'지역번호' : '기본색상'}로 하는 딕셔너리 생성
		< region_list = [{'region' : 'base_color'}] 형태로 만들기 >
		'''
		regions=[] # 지역 리스트
		base_colors=[] # 색상 리스트
		
		for i in region_list:
			regions.append(i.get('region'))
			base_colors.append(i.get('base_color'))
		
		colors = dict(zip(regions, base_colors)) # 두 리스트를 하나는 key값, 다른 하나는 value값으로 해서 딕셔너리 생성
		
		# Context 변수에 딕셔너리 넘기기
		context = {
			'colors':colors
		}
		
		# Template에 Context변수 넘기기
		return context
	

#글 쓰기 폼 뷰 
class StoryCreateView(CreateView):
	model = Story
	fields = ['title', 'author', 'content', 'written_date', 'traveled_start_date', 'traveled_end_date', 'region', 'spot', 'color']
	
	success_url = "/"


