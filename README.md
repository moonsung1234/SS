
# Idea

<br/>

- 학급에서 한달에 한번씩 자리를 랜덤으로 교체하는 규칙에서 영감을 얻어, 랜덤으로 자리를 교체해주는 프로그램을 개발했다.

<br/>

# Code

<br/>

```python
from window import Window # get Window class from window pyfile
from setter import Setter # get Setter class from setter pyfile

width = 700 # 프로그램의 가로 길이(바꿀 수 있다.)
height = 700 # 프로그램의 세로 길이(바꿀 수 있다.)

sr = Setter(6, 5, 30) # 각각 (가로줄, 세로줄, 전체인원) 이다.

wd = Window(width, height, sr)
wd.set(sr.list)
wd.show()
```

<br/>

# Image

<br/>

![ss](https://user-images.githubusercontent.com/71556009/168117047-9287eb71-7661-4f64-b846-c7b767098e47.PNG)
