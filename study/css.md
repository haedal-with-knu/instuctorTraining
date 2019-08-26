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
 **C**ascading **S**tyle **S**heet 의 줄임말로, 우리말로는 내림차순 스타일 시트라고 번역한다.~~스타일이랑 시트는?~~ ~~심지어 Cascading은 내림차순도 아니다!~~  
각설하고, 이 글을 읽고 있는 여러분들은 html이 뭔지 ~~대충~~ 알 것이다. 아니라고? 그러면 [이 문서](html.md)부터 읽고오길 바란다. 건물을 지을 때도 철근으로 뼈대를 세워놓고 겉에 콘트리트를 바르지 않는가?
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

  <p>Hello Haedal</p>
  
</div>
```
위와 같은 html이 있을 때 글자 색은 blue가 된다. 뒤에 있는 것이 우선순위가 높기 때문에 내림차순!

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

### 2-3. 

## 3. 결론



`css` 선택자
  - `tag`
  - `*`
  - `id`
  - `class`
  - `parent > child`
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


`css` 우선순위
  1. `!important`
  2. `css inline` 선언
  3. `id`
  4. `class`
  5. `tag`
  6. `parent`에 의해 상속
  
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
      
