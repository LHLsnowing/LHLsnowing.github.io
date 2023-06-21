---
title: Servlet
top: true
cover: false
date: 2023-06-20 14:16:40
summary: Servlet是一种技术，用来创建一个web应用程序；是一个API，提供许多接口和类，包括文档；是一个接口，创建任何servlet都必须实现这个接口；是一个扩展了服务器功能的类，响应任何请求；是一个网络组件，创建一个动态网页
tags: [Java,Servlet]
categories: [Java,Servlet]
---

# Servlet学习
与CGI（创建进程，占用资源多）相比，servlet（创建的是线程）有更好的性能、可移植性、稳健（JVM管理servlet）、安全

[servlet实例](https://www.runoob.com/servlet/servlet-first-example.html)
## Servlet API 
- javax.servlet
- javax.servlet.http:包含只负责http请求的接口和类

## servlet 接口
提供了三个必须实现方法 `init` `service` `destory`

## servletConfig 接口
Web容器为每个Servlet创建一个`ServletConfig`对象，这个对象可以从`web.xml`种获取配置信息，
如果配置信息从web.xml中被修改，我们不需要改变servlet

## RequestDispatcher 接口
RequestDispatcher接口提供了将请求分配给另一个资源的功能，它可能是html、servlet或jsp。这个接口也可以用来包括另一个资源的内容，他是Servlet协作的一种方式
- 两个method
1. forward：将一个请求从servlet转发到服务器上的另一个资源
2. include：在响应中包括一个资源的内容

## HttpServletResponse接口
HttpServletResponse 接口的`sendRedirect()`方法可以用来重定向响应到另一个资源，它可以是servlet、jsp或html文件
它接收相对和绝对的URL。他在客户端工作，因为它使用浏览器的URL栏进行另一个请求，因此它可以在服务器内部或外部工作

## Servlet 生命周期
>servlet类被加载
创建servlet实例
init方法被调用
service方法被调用
调用destroy方法

## Servlet 中会话跟踪
几种技术
1. Cookies
2. 隐藏表单域
3. URL重写
4. HttpSession

## war文件 
网络档案war文件包含网络应用所有内容
节省时间
创建，进入项目目录（WEB-INF之外），`jar -cvf projectname.war *`

## jsp
<% java代码 %>