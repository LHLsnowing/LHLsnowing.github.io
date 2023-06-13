---
title: TypeScript
date: 2023-06-11 10:17:23
summary: TS的一些类型，运行方式、promise写法
tags:   TypeScript
categories: TypeScript
---

# 文档非官方的
[TS入门](http://ts.xcatliu.com/)

## 一、快速编译运行
- ts-node **.ts

## 二、枚举类型
```ts
enum NumberType{
    one=1, //不赋值默认为0，以下依次递增
    two,
    three,  // 可以自定义赋值
    four="four".length, //计算所得项 需要放置在已经确定赋值得枚举项之前，未赋值不能放
}
console.log(NumberType.one); //1
console.log(NumberType.two); //2
```
转换成js后 `tsc **.ts`, 运行js的话 `node **.js`
```js
var NumberType;
(function (NumberType) {
    NumberType[NumberType["one"] = 1] = "one";
    NumberType[NumberType["two"] = 2] = "two";
    NumberType[NumberType["three"] = 3] = "three";
    NumberType[NumberType["four"] = 4] = "four";
})(NumberType || (NumberType = {}));
console.log(NumberType.one);
console.log(NumberType.two);
```

## 三、泛型<T>
```ts
// keyof 生成其键名
function getProp<Type,Key extends keyof Type>(obj:Type,key:Key){
    return obj[key]
}
let str:string=getProp({name:'aaa',phone:123}, 'name')
console.log(str); //aaa
console.log(getProp(12,'toFixed')); //Function
```

## 四、Partial 可选
```ts
interface Props{
    id:string,
    children:number[]
}

type PartialProps=Partial<Props>
class newC implements PartialProps{
    id:string // 可选择
}
```

## 五、Readonly 只读
```ts
interface Props{
    id:string,
    children:number[]
}

type ReadonlyProps = Readonly<Props>

let propsa: ReadonlyProps ={
    id:'a',
    children:[1,2,3]
}
// props.id='b' 错
```

## 六、Pick 直选
```ts
interface Propsa{
    id:string
    title:string
    children:number[]
}
type PickProps=Pick<Propsa,'id'|'title'>
```

## 七、Record
源码
```ts
/**
 * Construct a type with a set of properties K of type T
 */
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```
将K中的每个属性([P in K]),都转为T类型。常用的格式如下：
`type proxyKType = Record<K,T>`
会将K中的所有属性值都转换为T类型，并将返回的新类型返回给proxyKType，K可以是联合类型、对象、枚举等
eg:
```ts
type Recordobj=Record<'a'|'b',number>
let Reobj:Recordobj={
    a:1,
    b:2
}
```

## 八、TS中promise写法
```ts
interface DataItf{
    a:number;
    b:number;
}

interface ResItf{
    code:number;
    data: DataItf[];   //也可以这样写{a:number,b:number}[];
    message:string;
}

//promise对象 p:Promise <res的类型>
let p:Promise<ResItf> = new Promise((resolve,reject)=>{
    resolve({
        code:0,
        data:[{a:1,b:2},{a:11,b:22}],
        message:""
    })
})
p.then(res=>{
    if(res.code==0){
        res.data.map(item=>item.a);
    }
})
```