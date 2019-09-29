from django.db import models
from django.utils import timezone


# 지역별로 지역번호를 튜플의 첫 번째 요소로 저장.
# ('첫번째요소','두번째요소') : 첫 번째 요소는 DB에 저장되는 값, 두 번째 요소는 기본양식이나 위젯에 표시되는 값
BIG_REGION = (
	   ('02','서울'),
	   ('051','부산'),
	   ('053','대구'),
	   ('032','인천'),
	   ('062','광주'),
	   ('042','대전'),
	   ('052','울산'),
	   ('044','세종'),
	   ('031','경기'),
	   ('033','강원'),
	   ('043','충북'),
	   ('041','충남'),
	   ('063','전북'),
	   ('061','전남'),
	   ('054','경북'),
	   ('055','경남'),
	   ('064','제주'),
   )

	# 색상은 일단 10가지로 제한
COLOR = (
	   ('red', 'red'),
	   ('orange', 'orange'),
	   ('yellow', 'yellow'),
	   ('green', 'green'),
	   ('sky', 'sky'),
	   ('blue', 'blue'),
	   ('purple', 'purple'),
	   ('white', 'white'),
	   ('gray', 'gray'),
	   ('black', 'black')
   )

# Story 테이블
class Story(models.Model):
	title = models.CharField(max_length=50) # 제목
	author = models.CharField(max_length=20) # 작성자
	content = models.TextField(blank=True)  # 내용 (빈칸 허용)
	written_date = models.DateTimeField(default=timezone.now) # 작성날짜 (auto_now_add=True) usage. (default=timezone.now)
	traveled_start_date = models.DateTimeField(auto_now=False) # 여행시작날짜
	traveled_end_date = models.DateTimeField(auto_now=False)   # 여행종료날짜
	region = models.CharField(max_length=10, choices=BIG_REGION) # 지역
	spot = models.CharField(max_length=50) # 세부장소 - 추후 지도에서 (세부지역 선택기능 or 검색기능) 추가 / ? 이 부분을 ForeignKey로 해야할 지 고민
	color = models.CharField(max_length=15, choices=COLOR) # 색상
	
	def __str__(self):
		return self.title
	
	# save메서드 재정의: Story 추가 시, Region모델의 color값을 변경하기 위함.
	def save(self, *args, **kwargs):
		if not self.pk:
			Region.objects.filter(region=self.region).update(base_color=self.color)
		super().save(*args, **kwargs)

# Area 테이블
# 아예 이 곳에서 일괄 update 가능? 
class Region(models.Model):
	region = models.CharField(max_length=10, choices=BIG_REGION) # 지역
	base_color = models.CharField(max_length=15, default='gray') # 기본 색상 (gray)
    
	def __str__(self):
		return self.region