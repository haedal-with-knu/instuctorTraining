# CSS

**본인도 잘 모른다!!!!!!**
## 1. 개요
 **C**ascading **S**tyle **S**heet 의 줄임말로, 우리말로는 내림차순 스타일 시트라고 번역한다.~~그러면 내스시네?~~  
이 글을 읽고 있는 여러분들은 html이 뭔지 ~~대충~~ 알 것이다. 아니라고? 그러면 [이 문서](html.md)부터 읽고오길 바란다. 건물을 지을 때도 철근으로 뼈대를 세워놓고 겉에 콘트리트를 바르지 않는가?  
방금도 말했듯이, 건물을 짓는것에 비유하자면 HTML은 뼈대고, CSS는 살이다. 한 번 더 사람에 비유해보면, HTML이 사람의 얼굴이라고 했을 때, CSS는 화장이라고 할 수 있을 것이다. 그러니까 결국엔, HTML로 페이지의 뼈대와 들어갈 내용을 구성한다면, CSS로는 그 뼈대와 내용을 어떻게 꾸며줄 것인지에 대해 정해주는 것이다. 

## 2. 본문
### 2-1. 대충 2-1 제목 지어야함
위에 ~~내맘대로~~ 내림차순 스타일 시트라고 번역해 놨지만, 이는 CSS의 속성을 나타내는 것이다. 이게 무슨 소리냐 하고 물으신다면, ~~대답해 드리는게 인지상정~~ 늦게 선언된 스타일일수록 우선순위가 위에 있다는 뜻이다! 다음 html 코드를 보자.
```
<style>

  p {
    color: red;
  }

  p {
    color:blue;
  }

</style>

<div>

  <p>Hello Haedal!</p>
  
</div>
```
위와 같은 html이 있을 때, 글자 색을 지정하는 코드가 처음에 빨강, 그 다음에 파랑이다. 파랑이 늦게 선언되었기 때문에 글자 색은 파랑이 된다. 뒤에 있는 것이 우선순위가 높기 때문에 내림차순이라고 내맘대로 붙인 것이다!

### 2-2. CSS 선언
HTML에서 CSS를 사용하는 방법에는
* inline 방식
* internal 방식
* external 방식

으로 세 가지가 있다. inline 방식부터 찬찬히 살펴보자.
#### inline 방식
HTML 문서의 태그 안에 style 속성을 직접 기술하는 방식이다.
한 두 장짜리 페이지를 만들 때는 덜 귀찮겠지만, 페이지가 많아질수록, 그리고 중복되는 서식이나 구조가 많아질수록 같은 내용을 계속해서 써 줘야 하기 때문에 귀찮아진다. 초심자들이 CSS에 익숙해질 때까지 쓰는 것은 괜찮을 듯.

#### internal(style tag) 방식
HTML 문서 내부에 style 태그를 사용하여, 내용과 스타일을 분리한 형식. inline 형식보다 코드가 훨씬 간결할 것이다!

#### external 방식
CSS를 별도의 파일로 분리하여 HTML 문서에 링크하는 방식
문법적으로는 style tag와 동일하지만, 연결된 CSS파일만 교체해주면 스타일을 변경할 수 있다.(유지보수 편리)

### 2-3. CSS 선택자
CSS 선택자라는 단어가 나왔으니, 우리는 선택자가 무엇을 뜻하는 것인지부터 알아야 한다. 거창한 것은 아니고,, 무엇인가에 스타일을 주고자 할 때 대상을 지정해야 하는데, 그 지정해 주는 특정 요소를 선택자라고 한다. CSS로 나타낼 때 구문은 다음과 같다.
```
선택자 { 속성: 속성값; }
selector { property: value; }
```
그냥 저렇게 봐서는 전혀 감도 오지 않을 것 같으니, 선택자의 종류와 예시를 같이 들면서 보면 될 것이다.
#### CSS 선택자의 종류
* 기본 선택자
    - &#42;(전체 선택자)
    - type(요소 선택자)
    - id
    - class
* 조합 선택자
    - 자식 선택자
    - 자손 선택자

등이 있다.
##### 기본 선택자
* 전체 선택자와 요소 선택자
```
/* CSS */
* { margin: 0; text-decoration: none; }
h2 { font-size: 50px; }
p { font-family: "궁서체"; color: #ccc; }

<!-- HTML -->  
<p>p태그 선택자(Type Selector)</p>
<h2>h2태그 선택자(Type Selector)</div>
<div>div태그 선택자(Type Selector)</div>
```
전체 선택자는 HTML문서 내부의 모든 요소에 대해 같은 속성을 적용하기 때문에, margin, padding 등의 기본값을 설정해줄 때 유용하다. 하지만 반대로, 문서 내의 모든 요소를 읽어들여야 하기 때문에 남용하게 되면 문서의 로딩 속도가 느려지는 등의 문제가 생길 수도 있다.  
요소 선택자는 HTML 요소를 직접 지정한는 가장 간단한 선택자다. 위의 예제 코드에서, h2 태그와 p 태그에 대한 스타일이 지정이 되어 있으므로 해당 요소들은 각각 font size와 font family, color에 대한 속성을 지니게 된다. 하지만 div 태그에 대해서는 지정된 바가 없기 때문에 전체 선택자의 속성을 따른다. 또한, 태그 선택자, type 선택자 등 여러 가지 이름이 있는데 다 같은 것을 지칭하는 말이다.
* id 선택자
```
/* CSS */
#id1 { background: yellowgreen; color: darkgreen; }
div#id2 { background: darkgreen; color: yellowgreen; }

<!-- HTML -->
<p id="id1">ID 선택자(ID Selector)</p>
<p id="id2">ID 선택자(ID Selector)</p>
<div id="id2">ID 선택자(ID Selector)</div>
```
#myID { 속성; }
* class 선택자
```
/* CSS */
.class1 { background: yellowgreen; color: darkgreen; }
div.class2 { background: darkgreen; color: yellowgreen; }

<!-- HTML -->  
<p class="class1">클래스 선택자(Class Selector)</p>
<p class="class2">클래스 선택자(Class Selector)</p>
<div class="class1 class2">클래스 선택자(Class Selector)</div>

```
.myClass { 속성; }   
class 선택자는 속성값을 두 개 이상 지정해 줄 수 있다.
척 봐도 생긴것도 비슷하게 생겼고, 실제로 위의 id선택자와 class선택자는 같은 결과를 출력한다. 그렇다면 언제 id 선택자를 사용하고 언제 class 선택자를 사용하는지를 정해야 할 텐데, 정확한 기준은 없는 듯 하다. ~~마음대로 하면 된다는 말~~ 하지만 어느 정도의 가이드라인은 있는 듯 하니, 여기다 적어 보겠다.
* 한 페이지 내에서 여러 번 반복될 필요가 있는 스타일은 class 선택자를 사용하고, 단 한번 유일하게 적용될 스타일은 id 선택자를 사용하는 것이 좋다. 실제로 class와 id의 뜻도 class는 학급, 계층 등의 뭉텡이 같은 느낌이고, id는 개별적인 느낌이 든다.
* class 선택자는 글자색이나 글자 굵기 등 나중에 다른 곳에도 적용할 수 있는 스타일을 지정하고, id 선택자는 웹 문서 안에서 요소의 배치 방법을 지정할 때 자주 사용한다.
id 선택자와 class 선택자의 이름을 생성할 때 몇 가지 규칙이 있다.
1. 영문자와 숫자로 작성
1. 첫 글자에는 숫자 사용 불가
1. 특수문자는 "&#95;"와 "&#37;" 두 가지만 사용("&#95;" 권장)

##### 복합 선택자
복합 선택자는 두 개 이상의 선택자 요소가 모인 선택자이다.
* 하위 선택자와 자식 선택자
```
이부분은 이해가 잘 가지 않는군!
```


#### CSS 우선순위
1. `!important`
2. `css inline` 선언
3. `id`
4. `class`
5. `tag`
6. `parent`에 의해 상속
순서인데, 같은 요소로 동일한 선택자로 서로 다른 값이 적용될 경우 가장 마지막에 적용된 값이 우선된다(**C**ascading).

```css
/* CSS comment */
/* 1.tag name */
header {
  color: red;
  font-size: 20px;
}
/* 2. select all */
* {
  margin: 0;
  padding: 0;
}
/* 3. id selector */
#foot {
  background-color: black;
  color: white;
}
/* 4. class selector */
.art {
  font-size: 30px;
  color: green;
}
/* 5. parent child */
ol > li {
  color: yellow;
}
p > b {
  color: gray;
}
```

  
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <style>
    /* CSS의 우선순위를 파악하자*/
    /* 6.상위 객체에 의해 상속된 속성 */
    div {
      color: red;
    }
    /* 5.태그 이름으로 지정한 속성 */
    h1{
      color: blue;
    }
    /* 4.클래스 이름으로 지정한 속성 */
    .hello{
      color: brown;
    }
    /* 3. id로 지정한 속성 */
    #mulcam{
      color: yellow;
    }
    /* 2. HTML에서 style을 직접 지정한 속성 */
    /* 1. 속성값 위에 !important를 붙인 속성 */
    h1{
      color: black !important;
    }
  </style>
</head>
<body>
  <div>
    <h1 id="mulcam" class="hello" style="color: green;">Hello, Multicampus!</h1>
  </div>
</body>
</html>
```
여기까지 우리는 CSS 선택자에 대해 알아보았다. 이제 우리가 실제로 읽는 글을 어떻게 꾸미는지 알아보자. 글자.. 우리는 글자를 꾸밀 것이다. '글자를 써 놓은 모양'을 서체라고 한다. 서체가 영어로 뭐지? font다!
  - font-size
  - font-style
  - font-weight
  - font-family
  
위 네 가지 기본적인 속성에 대해 알아보자.

##### font-size
말그대로 폰트의 크기를 관장한다.
```
/* CSS */
h1 { font-size: 250%; }
h2 { font-size: 200%; }
p { font-size: 100%; }
```
부모 요소의 크기에 비례하게 하려면 백분율 값을 지정해 주면 된다.  
구체적인 크기를 지정해 주려면 픽셀 값을 지정해 주면 되지만, 실제 보여지는 페이지에서는 사용자가 창의 크기를 조정함에 따라 브라우저가 글자를 확대하거나 축소하기 때문에 어떤 크기로 글자가 보여질지는 정확하게 알 수 없다.
###### 속성값
* xx-small
* x-small
* small
* medium
* large
* x-large
* xx-large
* smaller
* larger
* %(퍼센트)
* initial(기본값)
* inherit(부모 요소로부터 상속)

등이 있다.

##### font-style
글꼴의 모양을 관장한다.
```
/* CSS */
p.normal {font-style:normal;}
p.italic {font-style:italic;}
p.oblique {font-style:oblique;}
```
###### 속성값
* normal(기본값)
* italic(이탤릭)
* oblique(비스듬한 모양)
* inherit(부모 요소로부터 상속)

##### font-weight
글꼴의 두께를 관장한다.
```
/* CSS */
p.normal {font-weight:normal;}
p.thick {font-weight:bold;}
p.thicker {font-weight:900;}
```
###### 속성값
* normal(기본값)
* bold(굵은 글꼴 지정)
* bolder(더 굵은 글꼴 지정)
* lighter(기본값보다 얇게 지정)
* 100, 200, …, 900(400이 normal, 700이 bold)

##### font-family
글꼴 종류를 지정하며 값이 상속된다.
```
/* CSS */
body { font-family :'나눔고딕', 'Malgun Gothic', sans-serif;}
```
콤마로 글꼴을 구별하며 맨 앞에 지정한 것 부터 브라우저가 글꼴을 탐색하고, 있다면 그 글꼴을 적용시키고 없다면 뒤로 넘어간다.
###### 속성값
* 글꼴 이름
* inherit(부모 요소로부터 상속)




#### GOOGLE FONT
구글에서는 많은 종류의 웹폰트를 지원하고 있고, 우리는 그것을 가져다 쓸 수 있다!~~개꿀~~ 코드 몇 줄만 추가해 주면 내 페이지의 가독성이 더 좋아질 것이다. [여기](https://fonts.google.com/)에서 마음에 드는 폰트를 골라보자.(Language에서 Korean을 선택하면 한글 폰트가 있다)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
  <link href="https://fonts.googleapis.com/css?family=Nanum+Myeongjo|Ubuntu&display=swap" rel="stylesheet">
  <style>
    .font{
      font-size: 40px;
      font-style: italic;
      font-weight: 400;
      /* font-family: 'Times New Roman', Times, serif; */
      font-family: 'Ubuntu', 'Nanum Myeongjo', serif;
    }
  </style>
</head>
<body>
  <p class="font">Lorem ipsum dolor sit amet consectetur adipisicing elit. Dolorum incidunt excepturi vel velit explicabo illo. Perferendis dolor animi consequuntur dolorem culpa est non corrupti libero quibusdam eveniet magni rem, odio nesciunt consectetur, repellendus at eius expedita ad aliquam quo amet molestiae? Deserunt veritatis voluptatibus, ut dolore soluta natus porro nulla similique assumenda numquam exercitationem ratione unde accusamus quis corporis quos. Possimus, at libero! Harum molestias magni cum nam itaque magnam quibusdam dolorem! Assumenda, voluptatem non blanditiis inventore error cupiditate expedita modi quidem tempora officia aut dicta accusamus, nihil, vero vel. Nesciunt dignissimos similique odio quidem quibusdam hic reiciendis, totam quis!</p>
  <p class="font">Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum dignissimos illum pariatur repudiandae assumenda tempore facilis necessitatibus, perspiciatis minus beatae non ipsa nesciunt suscipit id, molestiae iste neque deleniti ex excepturi ipsam officiis sunt? Fugit, debitis animi numquam placeat sint harum, quidem sequi ad obcaecati quis maiores voluptatem alias temporibus.</p>
</body>
</html>
```
코딩 결과는 다음과 같다.  
![coding_result](./img/ex_result.PNG)  
덧붙이자면 IE에서는 기본적으로 구글 웹폰트를 사용할 수 없다.~~크롬 안쓰는 흑우없제?~~ IE에서 구글 웹폰트를 사용하고 싶다면 [이 글](https://www.codingfactory.net/10453)을 참고하도록 하자.

### BOOTSTRAP
CSS의 아주 기본을 공부해 보았다. 근데 우리가 이거를 처음부터 다 만들어야 할까? 고맙게도 능력자~~변태~~들이 다 만들어서 우리에게 잘 쓰라고 만들어놓은 것들이 있는데, 그것이 부트스트랩이다. [여기](makeOpensourceProject.md)를 보면 대충 사용법이 있다.


## 3. 결론
CSS에 대해 좀 알게 되었나? 그렇다면 아주 다행이다! ~~왜냐하면 나도 아직 잘 모르겠거든~~