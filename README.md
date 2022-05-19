
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

![ss](https://user-images.githubusercontent.com/71556009/169291408-94719721-55af-4fe4-8c68-64aeca31d6e9.PNG)

<br/>

- 클릭하여 번호를 하나하나 직접 입력할 수 있고, restart 버튼을 누르면 번호가 랜덤으로 자동 배치된다.
- 번호를 클릭하면 번호가 빨간색으로 변하는데, 이는 이 번호가 고정됬다는 뜻이며, restart 를 눌러도 빨간색 버튼은 자리가 변하지 않는다.
- 빨간색 버튼을 다시 누르면 하얀색 버튼(정상 버튼) 이 된다.
- 위의 메뉴바에 있는 File 버튼을 누르면 save 와 load 버튼이 존재하며, 각각 자리배치결과를 저장하고 불러온다.

<br/>

# More

<br/>

- 처음에, 자리를 직접 입력할 수 있는 기능을 추가할 예정이다. (완료)
- 랜덤으로 돌려서 나온 자리를 저장하고, 다시 불러올 수 있는 기능을 추가할 예정이다. (완료)

<br/>