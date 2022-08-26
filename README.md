![image](https://user-images.githubusercontent.com/71905164/182584327-171cf850-0bd8-4d62-bdec-1ba090eb9b71.png)
# 🚀MakeMigrations
딥페이크를 이용하여 움직이는 사진을 생성, 지구 밖 행성으로 이주한 사람들의 시민권을 만들어주는 웹사이트

커뮤니티 기능 및 마이 페이지에서 방 꾸미는 기능 등
***
<br><br/>


## 1. 개발 기간, 참여 인원
* 개발기간: 2022.07.06 - 2022.08.16
* **Team** <a href="https://github.com/cmjcum"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
김동근 <a href="https://github.com/yinmsk"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
노을 <a href="https://github.com/minkkky"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이정아 <a href="https://github.com/zeonga1102"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
이현경 <a href="https://github.com/LULULALA2"><img src="https://img.shields.io/badge/Github-000000?style=flat-square&logo=github&logoColor=white"/></a>
* **S.A** <a href="https://cold-charcoal.tistory.com/118">블로그로 이동(☞ﾟヮﾟ)☞</a>
***
<br><br/>


## 2. 사용 기술(버전 적기)
* Python 3.7
* Django REST Framework 3.13
* Docker
* Docker-compose
<br><br/>

## 3. API 명세서
<a href="https://typingmylife.notion.site/MakeMigrations-API-88de2c1a1ccd457c9059c8b55ee3dc70">API 명세서 자료</a>
<br><br/>

## 4. ERD 설계
![wm_erd](https://user-images.githubusercontent.com/104487608/186808469-be6b3f37-376e-4249-ada7-be28f86a7eff.png)
<br><br/>


## 5. 핵심 기능
게시판과 마이홈을 통한 회원들 간의 소통과 상점에서 구입한 가구를 통해 방을 꾸미는 기능.
* JWT를 이용한 로그인
* 딥페이크를 통한 움직이는 사진 생성
* 게시판 별 게시글과 댓글 CRUD
* 가구 상점과 상점에서 구매한 가구로 방 꾸미기
<br><br/>

## 6. 맡은 기능
<details>
  <summary>좋아요 팔로우를 한 사람을 구분하기 위한 boolean <a href="https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L31">📄코드</a></summary>
  <div markdown="1">
 
* 유저의 아이디 안에 좋아요, 팔로우를 한 사람의 아이디 유무에 따라 참 거짓을 보내준다.
* 리스트 컴프리헨션을 사용했다.
  </div>
</details>

<details>
  <summary>방명록 작성 기능 <a href="https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L64">📄코드</a></summary>
  <div markdown="1">
 
* 시리얼라이저의 정보를 가져오고 .is_vaild() 를 통해 유효성을 검사 후 .save() 를 통해 저장 하였다.
  </div>
</details>

<details>
  <summary>방명록 삭제 기능 <a href="https://github.com/yinmsk/WM_back/blob/db4aa5df5a123046a8a3b7d58ac0d7143cb14ac9/myroom/views.py#L77">📄코드</a></summary>
  <div markdown="1">
 
* .objects.get 을 통해 작성한 방명록 글을 가져와주고 .delete() 를 통해 삭제 하였다.
  </div>
</details>

<details>
  <summary>방명록 조회 기능 <a href="https://github.com/yinmsk/WM_back/blob/db4aa5df5a123046a8a3b7d58ac0d7143cb14ac9/myroom/views.py#L56">📄코드</a></summary>
  <div markdown="1">
 
* objects.filter() 를 통해 해당 유저의 방명록을 가져와주고 .order_by('-create_date') 를 통해 최근 생성일로 조회가 가능하게 해 주었다.
* model 에서 최근 생성일로 가져온 정보를 시리얼라이저에 담아서 return 해 주었다.
  </div>
</details>

<details>
  <summary>좋아요 기능 <a href="https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L87">📄코드</a></summary>
  <div markdown="1">
 
* .exists() 를 통해 좋아요를 누른 유저의 존재를 확인해서 존재한다면 해당 유저를 삭제하고, 좋아요한 유저가 없다면 유저를 추가해 주었다.
  </div>
</details>
<br><br/>


## 7. 트러블 슈팅
<details>
  <summary>좋아요, 팔로우를 누른 사람과 받는 사람 모두에게 좋아요, 팔로우가 추가 되었다.</summary>
  <div markdown="1">
 
* like 와 follow 필드를 M to M 필드로 했었는데 그렇게 한다면 symmetrical 이 기본적으로 True 이여서 모두에게 추가 되었었다.
* symmetrical=False 로 바꾸어 주어 양쪽이 아닌 한쪽의 사람만 추가 될 수 있도록 하였다.
[📄코드](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/user/models.py#L39)
  </div>
</details>

<details>
  <summary>OrderedDict([('A', 1)]) 형태의 데이터를 가져오지 못해 좋아요, 팔로우 유무를 출력할 수 없었다.</summary>
  <div markdown="1">
 
* 반복문을 리스트 형태로 저장해주는 리스트 컴프리헨션을 사용해 데이터를 가져올 수 있었다.
[📄코드](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L33)
  </div>
</details>

<details>
  <summary>게시글 및 방명록 해킹 시도가 있었다.</summary>
  <div markdown="1">
 
* 처음 배포를 한 상태에서는 XSS 공격 가능성을 전혀 고려하지 못해 우리 웹사이트가 XSS 공격을 받았습니다.
* 사용자가 조회할 수 있는 텍스트들을 저장할 때 부등호 기호(<, >)를 전부 html 특수문자 코드로(&lt;, &gt;) 바꾸어 저장했습니다.
* Seralizer를 통해 저장할 때 validator를 커스텀 해 replace 함수로 문자열을 바꿔주었습니다.
[📄코드](https://github.com/yinmsk/WM_back/blob/95aa8105cdb965d4f195934fac5bab6d305545d4/myroom/seriailzers.py#L125)
  </div>
</details>
<br><br/>

## 8. 회고 느낀점
* 최종프로젝트는 기간이 길어서 여러 기능들을 구현해 볼 수 있었던 점이 가장 좋았습니다.
* 이전에 사용하지 못했던 여러 기능들을 사용할 수 있었습니다.
* 해킹 방지, 자바스크립트 feach 기능 등 기능을 사용할 수 있었다.
* 전에 사용했던 기능들은 더 깊게 알게되는 시간이 되었고 사용해보지 못했던 여러 기능들도 익히는 시간이 되었다.
