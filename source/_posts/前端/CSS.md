---
title: CSS
top: false
cover: false
toc: true
mathjax: true
date: 2023-06-28 11:15:14
summary:
tags: [CSS,垂直居中]
categories: [前端,CSS]
---

## 一、css垂直居中——面试老问
- 垂直居中是一种常见的布局需求，下面介绍几种实现垂直居中的方法：

- **1.使用 Flexbox：**使用 `display: flex;` 来创建一个弹性布局容器，并通过设置 `align-items: center;` 来使子元素在垂直方向上居中。
```css
.container {
  display: flex;
  align-items: center;
  justify-content: center; /* 可选，水平居中 */
  height: 100vh; /* 确保容器高度占满整个屏幕 */
}

.centered-content {
  /* 样式规则 */
}
```
- **2.使用表格布局：**使用 `display: table;` 来创建一个表格布局，通过 `display: table-cell;` 和 `vertical-align: middle;` 来使子元素在垂直方向上居中。
```css
.container {
  display: table;
  width: 100%;
  height: 100vh; /* 确保容器高度占满整个屏幕 */
  text-align: center; /* 水平居中 */
}

.centered-content {
  display: table-cell;
  vertical-align: middle;
  /* 样式规则 */
}
```
- **3.使用绝对定位和负边距：**将要居中的元素设置为绝对定位，并通过负边距和 `top: 50%;` 来使其在垂直方向上居中。同时使用 `transform: translateY(-50%);` 将元素向上移动自身的一半高度，以完全居中。
```css
.container {
  position: relative;
  height: 100vh; /* 确保容器高度占满整个屏幕 */
  text-align: center; /* 水平居中 */
}

.centered-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* 样式规则 */
}
```
## 二、vw和vh
vw 和 vh 是CSS中的相对长度单位，它们代表**视窗宽度（Viewport Width）**和**视窗高度（Viewport Height）**的百分比。

1vw 表示视窗宽度的1%，而 1vh 表示视窗高度的1%。这两个单位可以用于设置元素的尺寸或位置，相对于当前视窗的大小。 以下是一些示例用法：

>设置元素的宽度为视窗宽度的50%：
```css
.element {
  width: 50vw;
}
```
>设置元素的高度为视窗高度的75%：
```css
.element {
  height: 75vh;
}
```
>设置元素的左边距相对于视窗宽度的10%：
```css
.element {
  margin-left: 10vw;
}
```
>设置元素的顶部位置相对于视窗高度的25%：
```css
.element {
  top: 25vh;
  position: absolute;
}
```
使用 vw 和 vh 单位可以使得元素在不同视窗大小下保持一致的比例关系，因此在响应式设计中非常有用。需要注意的是，这两个单位的兼容性较好，但在一些旧的浏览器版本可能存在兼容性问题，因此在使用时需要进行兼容性考虑。
