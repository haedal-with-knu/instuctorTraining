# CSS

```
목차
1. 개요
2. 본론
  2-1.
  2-2. 문법
3. 결론
```
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
한 두 장짜리 페이지를 만들 때는 덜 귀찮겠지만, 어쩌고 저쩌고

#### internal(style tag) 방식
HTML 문서 내부에 style 태그를 사용하여, 내용과 스타일을 분리하고, 어쩌고 저쩌고

#### external 방식
CSS를 별도의 파일로 분리하여 HTML 문서에 링크하는 방식
문법적으로는 style tag와 동일하지만, 파일만 교체해주면 스타일을 변경할 수 있음(유지보수 편리)

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
전체 선택자와 요소 선택자
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
* class 선택자
```
/* CSS */
.class1 { background: yellowgreen; color: darkgreen; }
div.class2 { background: darkgreen; color: yellowgreen; }

<!-- HTML -->  
<p class="class1">클래스 선택자(Class Selector)</p>
<p class="class2">클래스 선택자(Class Selector)</p>
<div class="class2">클래스 선택자(Class Selector)</div>
```

#### CSS 우선순위
 1. `!important`
  2. `css inline` 선언
  3. `id`
  4. `class`
  5. `tag`
  6. `parent`에 의해 상속
## 3. 결론



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
`font`
  - `font-size`
  - `font-style`
  - `font-weight`
  - `font-family`

`google font`

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

`Bootstrap` 도입
      
