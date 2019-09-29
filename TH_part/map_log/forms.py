from django import forms
from .models import Story, Area # 각 모델 import

class StoryForm(forms.ModelForm): # Story 모델 폼 정의
    model = Story # 가져올 테이블 정의 (Story 테이블)
    fields = ['title', 'author', 'written_date', 'traveled_start_date', 'traveled_end_date', 'region', 'spot', 'color']
    
class AreaForm(forms.ModelForm): # Story 모델 폼 정의
    model = Area # 가져올 테이블 정의 (Story 테이블)
    fields = ['region', 'base_color']    
