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
* python 3.7.13
* Django 3.2.13
* DRF 3.13.1
* deepfake
* docker
* AWS
* postgreSQL
* javascript
 
<br><br/>


## 3. ERD 설계
![wm](https://user-images.githubusercontent.com/104487608/186304526-54d008c7-08a2-4e8d-82d7-fb581cc7a8cc.png)
<br><br/>


## 4. 핵심 기능
게시판과 마이홈을 통한 회원들 간의 소통과 상점에서 구입한 가구를 통해 방을 꾸미는 기능.
* JWT를 이용한 로그인
* 딥페이크를 통한 움직이는 사진 생성
* 게시판 별 게시글과 댓글 CRUD
* 가구 상점과 상점에서 구매한 가구로 방 꾸미기
<details>
  <summary>기능 자세히 알아보기</summary>
  <div markdown="1">
 
### 기능 소개
* 좋아요 팔로우를 한 사람을 구분하기 위한 boolean [코드 확인](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L31)
  * 유저의 아이디 안에 좋아요, 팔로우를 한 사람의 아이디 유무에 따라 참 거짓을 보내준다.
  * 리스트 컴프리헨션을 사용했다.
* 방명록 작성 기능 [코드 확인](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L64)
  * 시리얼라이저의 정보를 가져오고 .is_vaild() 를 통해 유효성을 검사 후 .save() 를 통해 저장 하였다.
* 좋아요 기능 [코드 확인](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L87)
  * .exists() 를 통해 좋아요를 누른 유저의 존재를 확인해서 존재한다면 해당 유저를 삭제하고, 좋아요한 유저가 없다면 유저를 추가해 주었다.
    
  </div>
</details>
<br><br/>


## 5. 트러블 슈팅
<details>
  <summary>좋아요, 팔로우를 누른 사람과 받는 사람 모두에게 좋아요, 팔로우가 추가 되었다.</summary>
  <div markdown="1">
 
* like 와 follow 필드를 M to M 필드로 했었는데 그렇게 한다면 symmetrical 이 기본적으로 True 이여서 모두에게 추가 되었었다.
* symmetrical=False 로 바꾸어 주어 양쪽이 아닌 한쪽의 사람만 추가 될 수 있도록 하였다.
[코드 확인](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/user/models.py#L39)
  </div>
</details>

<details>
  <summary>OrderedDict([('A', 1)]) 형태의 데이터를 가져오지 못해 좋아요, 팔로우 유무를 출력할 수 없었다.</summary>
  <div markdown="1">
 
* 반복문을 리스트 형태로 저장해주는 리스트 컴프리헨션을 사용해 데이터를 가져올 수 있었다.
[코드 확인](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L33)
  </div>
</details>
<br><br/>

## 6. 회고 느낀점
> 프로젝트 개발 회고 (https://github.com/yinmsk/portfolio)
최종프로젝트는 기간이 길어서 여러 기능들을 구현해 볼 수 있었던 점이 가장 좋았던것 같습니다
이전에는 회원가입 기능 구현과 아주 간단한 기능들을 구현하고 익히는게 어려
마지막 프로젝트를 통해 get post put delete 모든 기능들을 사용해 볼 수 있었고
해킹 방지, 자바스크립트 feach 기능등 이전에도 사용해 보았던 기능들도 있지만
전에 사용했던 기능들은 더 깊게 알게되는 시간이 되었고
사용해보지 못했던 여러 기능들도 익히는 시간이 되었다.
