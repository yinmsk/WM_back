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


## 2. 사용 기술
* Python 3.7
* Django REST Framework 3.13
* javascript
<br><br/>


## 3. API 명세서
<a href="https://typingmylife.notion.site/MakeMigrations-API-88de2c1a1ccd457c9059c8b55ee3dc70">API 명세서 자료</a>
<br><br/>


## 4. ERD 설계
![wm_erd](https://user-images.githubusercontent.com/104487608/186808469-be6b3f37-376e-4249-ada7-be28f86a7eff.png)
<br><br/>


## 5. 기능 소개
<details>
  <summary>좋아요 팔로우 기능 <a href="https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L87">📄코드</a></summary>
  <div markdown="1">
 
![좋아요](https://user-images.githubusercontent.com/104487608/188048493-aa99b0ab-1343-4b11-a48b-5d1924e9faf2.png)
* 좋아요 팔로우를 한 사람을 구분하기 위해 boolean 을 사용하였습니다.</a>
  </div>
</details>

<details>
  <summary>방명록 기능 <a href="https://github.com/yinmsk/WM_back/blob/db4aa5df5a123046a8a3b7d58ac0d7143cb14ac9/myroom/views.py#L53">📄코드</a></summary>
  <div markdown="1">
 
![방명록](https://user-images.githubusercontent.com/104487608/188050467-f77909d7-3144-46d6-bd97-d8538a5a7dce.png)
* 방명록 작성, 조회, 삭제가 가능하다.
  </div>
</details>

<details>
  <summary>보유 가구 불러오기 기능 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L119">📄코드</a></summary>
  <div markdown="1">
 
![가구 조회](https://user-images.githubusercontent.com/104487608/188050146-81259de4-be87-428d-a462-b7f2084c9c77.png)
* 유저는 상점을 통해 구매한 가구만을 이용해 방을 꾸밀 수 있습니다. 
  </div>
</details>

<details>
  <summary>상점 페이지에서 가구 구매 기능 <a href="https://github.com/cmjcum/WM_back/blob/master/myroom/views.py#L161">📄코드</a></summary>
  <div markdown="1">
 
![가구 구매](https://user-images.githubusercontent.com/104487608/188049573-c76bbc0b-4644-4ab9-9287-af684d2e2936.png)
* 선택한 가구를 유저 보유 가구에 추가하고 보유 코인을 차감합니다. 만약 보유 코인이 구매하려는 가구의 가격보다 적다면 구매할 수 없습니다. 
  </div>
</details>
<br><br/>


## 6. 트러블 슈팅
<details>
  <summary>상대방에게 좋아요 버튼을 누르면 상대방에게만 좋아요가 추가 되는 것이 아닌 나에게도 좋아요가 추가 되었다.</summary>
  <div markdown="1">
 
![simitical](https://user-images.githubusercontent.com/104487608/188049841-c90880bc-f149-45af-b7ab-900f0b3b5e26.png)
* symmetrical=False 로 바꾸어 주어 양쪽이 아닌 한쪽의 사람만 추가 될 수 있도록 하였다. <br>
[📄코드](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/user/models.py#L39)
  </div>
</details>

<details>
  <summary>OrderedDict([('A', 1)]) 형태의 데이터를 가져오지 못해 좋아요, 팔로우 유무를 출력할 수 없었다.</summary>
  <div markdown="1">
 
* 반복문을 리스트 형태로 저장해주는 리스트 컴프리헨션을 사용해 데이터를 가져올 수 있었다. <br>
[📄코드](https://github.com/yinmsk/WM_back/blob/6a362ffd597ea4796884e87a10c9ccb6c34e6a35/myroom/views.py#L33)
  </div>
</details>

<details>
  <summary>처음 배포를 한 상태에서는 XSS 공격 가능성을 전혀 고려하지 못해 웹사이트가 XSS 공격을 받았습니다.</summary>
  <div markdown="1">
 
* 사용자가 조회할 수 있는 텍스트들을 저장할 때 부등호 기호(<, >)를 전부 html 특수문자 코드로(&lt;, &gt;) 바꾸어 저장했습니다.
* Seralizer를 통해 저장할 때 validator를 커스텀 해 replace 함수로 문자열을 바꿔주었습니다. <br>
[📄코드](https://github.com/yinmsk/WM_back/blob/95aa8105cdb965d4f195934fac5bab6d305545d4/myroom/seriailzers.py#L125)
  </div>
</details>
<br><br/>


## 7. 회고 느낀점
* 최종프로젝트는 이전의 프로젝트에 비해 프로젝트 기간이 길어서 이전에 사용하지 못했던 여러 기능들을 사용할 수 있어서 좋았습니다. <br>
  특히 해킹은 생각지도 못했는데 이번일로 보기능 구현만이 아니라 보안도 정말 중요하다는걸 직업 체험하면서 느끼게 되었습니다
  * 해킹 방지, 자바스크립트 feach 기능 등 기능을 사용할 수 있었다.
* 배포를 하며 여러 피드백을 받으면서 더 많이 성장할 수 있었습니다. <br>
  대부분의 피드백이 프론트 ui/ux 이긴 했지만, 피드백 없이 만들었을때는 좋아보였던 것들이 <br>
  실제 사용자 입장에서는 불편함이 많았던 부분들이 있다는걸 알게되어 사용자 입장에서 생각하게 되는 좋은 시간이었습니다.
  
