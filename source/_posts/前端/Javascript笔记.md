---
title: Javascript笔记
date: 2023-05-24 23:18:11
tags: [javascript,async,await]
categories: [javascript,异步]
---

![](./Javascript%E7%AC%94%E8%AE%B0/bg.jpg)
# Javascript篇
[leetcode14天js编程挑战](https://leetcode.cn/circle/discuss/jE87x7/)

## 闭包
>函数对象可以通过作用域链相互关联起来，函数体内部的变量都可以保存在函数作用域内，这种特性在计算机科学文献中称为“闭包”。
——出自《JavaScript权威指南(第六版)》
闭包（closure）是一个函数以及其捆绑的周边环境状态（lexical environment，词法环境）的引用的组合。换而言之，闭包让开发者可以从内部函数访问外部函数的作用域。在 JavaScript 中，闭包会随着函数的创建而被同时创建。
>>三个作用
（1）外部可以读取函数内部的变量。 
（2）封闭数据，实现数据私有，防止变量被污染。 
（3）让这些变量的值始终保持在内存中
```js
function init() {
  var name = "Mozilla"; // name 是一个被 init 创建的局部变量
  function displayName() { // displayName() 是内部函数，一个闭包
      alert(name); // 使用了父函数中声明的变量
  }
  displayName();
}
init();
```
- 闭包主要是用返回值，但使用一定要合理
- 如果不是某些特定任务需要使用闭包，在其他函数中创建函数是不明智的，因为闭包在处理速度和内存消耗方面对脚本性能具有负面影响。
- 会产生内存泄漏问题，如果需要回收这些变量，我们可以手动把这些变量设为 `null`。

例题：
>请你写一个函数 createCounter. 这个函数接收一个初始的整数值 init  并返回一个包含三个函数的对象。
这三个函数是：
increment() 将当前值加 1 并返回。
decrement() 将当前值减 1 并返回。
reset() 将当前值设置为 init 并返回。

```js
var createCounter = function(init) {
    let n=init;
    let increment= ()=>++n;
     let decrement= ()=>--n;
    let reset= ()=> n = init;
    return { increment,decrement,reset};
};
/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
```
## 内存泄漏
- **不再用到的内存，没有及时释放，就叫做内存泄漏（memory leak）**。 内存泄漏是指程序执行时，一些变量没有及时释放，一直占用着内存 而这种占用内存的行为就叫做内存泄漏。

- 作为一般的用户，根本感觉不到内存泄漏的存在。真正有危害的是内存泄漏的堆积，这会最终消耗尽系统所有的内存。从这个角度来说，一次性内存泄漏并没有什么危害，因为它不会堆积。

- 内存泄漏如果一直堆积，最终会导致**内存溢出问题**。

## js实现继承的方式
1、原型链继承 ...
2、借用构造函数继承（也称伪造对象或经典继承） ...
3、组合继承（也称伪经典继承） ...
4、原型式继承 ...
5、寄生式继承 ...
["继承方式"](https://www.cnblogs.com/Leophen/p/11401734.html#:~:text=%E4%BA%8C%E3%80%81JavaScript%E5%AE%9E%E7%8E%B0%E7%BB%A7%E6%89%BF%E7%9A%84%E6%96%B9%E5%BC%8F%201%201%E3%80%81%E5%8E%9F%E5%9E%8B%E9%93%BE%E7%BB%A7%E6%89%BF%20...%202%202%E3%80%81%E5%80%9F%E7%94%A8%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0%E7%BB%A7%E6%89%BF%EF%BC%88%E4%B9%9F%E7%A7%B0%E4%BC%AA%E9%80%A0%E5%AF%B9%E8%B1%A1%E6%88%96%E7%BB%8F%E5%85%B8%E7%BB%A7%E6%89%BF%EF%BC%89%20...%203,4%E3%80%81%E5%8E%9F%E5%9E%8B%E5%BC%8F%E7%BB%A7%E6%89%BF%20...%205%205%E3%80%81%E5%AF%84%E7%94%9F%E5%BC%8F%E7%BB%A7%E6%89%BF%20...%206%206%E3%80%81%E5%AF%84%E7%94%9F%E7%BB%84%E5%90%88%E5%BC%8F%E7%BB%A7%E6%89%BF%20)

## 一次笔试题，五个人五排看手机电量够玩多久
```js
function demo(arr){
    let a=0;
    for(let i=0;i<arr.length;i++){
        for(let j=i+1;j<arr.length;j++){
            if(arr[i]<arr[j]){
                let temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
    }
    console.log(arr);
    while(arr[4]!=0){
        a+=arr[4];
        console.log(arr);
        for(let i=0;i<5;i++){
            arr[i]=arr[i]-arr[4];
        }        
        for(let i=0;i<arr.length;i++){
            for(let j=i+1;j<arr.length;j++){
                if(arr[i]<arr[j]){
                    let temp=arr[i];
                    arr[i]=arr[j];
                    arr[j]=temp;
                }
            }
        }
    }
    console.log(a);
}

demo([100,10,5,50,10,100,100])
```