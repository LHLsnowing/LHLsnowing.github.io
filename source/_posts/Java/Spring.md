---
title: Spring
top: false
cover: false
toc: true
mathjax: true
date: 2023-06-24 12:53:30
id: 1
summary: Spring划分、特点,IOC,AOP
tags: [Java,Spring,IOC,AOP]
categories: [Java,Spring]
---

# Spring
## 广义的 Spring
- 有多个不同的子项目:
Spring FrameWork（其他子项目的基础）、Spring MVC、SpringBoot、Spring Cloud、 Spring Data、Spring Security
## 狭义的 Spring：SPring FrameWork
- Spring框架是一个分层的、面向切面的java应用程序的一站式轻量级解决方案
Spring 有两个最核心模块：IOC和AOP
>IoC：（Inverse of Control）,"控制反转"，指把创建对象过程交给Spring管理
AOP：(Aspect Oriented Programming),译为"面向切面编程"，AOP用来封装多个类的公共行为，将那些与业务无关，却为业务模块所共同调用的逻辑封装起来、减少系统的重复代码、降低模块间耦合度。另外，AOP还解决一些系统层面上的问题，比如日志、事务、权限等。

## Spring 特性
- 非侵入式：基于Spring开发的应用中的对象可以不依赖于Spring的API
- 控制反转：IOC——Inversion of Control，指的是将对象的创建权交给 Spring 去创建。使用 Spring 之前，对象的创建都是由我们自己在代码中new创建。而使用 Spring 之后。对象的创建都是给了 Spring 框架。
- 依赖注入：DI——Dependency Injection，是指依赖的对象不需要手动调用 setXX 方法去设置，而是通过配置赋值。
- 面向切面编程：Aspect Oriented Programming——AOP
- 容器：Spring 是一个容器，因为它包含并且管理应用对象的生命周期
- 组件化：Spring 实现了使用简单的组件配置组合成一个复杂的应用。在 Spring 中可以使用XML和Java注解组合这些对象。
- 一站式：在 IOC 和 AOP 的基础上可以整合各种企业应用的开源框架和优秀的第三方类库（实际上 Spring 自身也提供了表现层的 SpringMVC 和持久层的 Spring JDBC）

## 如何使用返回创建的对象
```java
package org.atguigu.spring6;
// User类
public class User {
    public User(){
        System.out.println("无参构造");
    }
    public void add(){
        System.out.println("add ...");
    }
    public static void main(String[] args) {

    }
}
```
```xml
<!-- bean.xml文件 -->
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!--    完成user对象创建
        bean标签
            id属性 ：唯一标识
            class属性：要创建对象所在类的全路径（包名称=类名称）
       -->
    <bean id="user" class="org.atguigu.spring6.User"></bean>
</beans>
```
>1. 加载bean.xml配置文件
2. 对xml文件进行解析操作
3. 获取xml文件bean标签属性值 id属性值和class属性值
4. 使用反射根据类全路径创建对象
```java
package org.atguigu.spring6;

import org.junit.jupiter.api.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class TestUser {
    @Test
    public void testUserObject(){
        //加载spring配置文件，对象创建
        ApplicationContext context = new ClassPathXmlApplicationContext("bean.xml");
        // 获取创建的对象
        User user = (User) context.getBean("user");
        System.out.println(user);
        //使用对象调用方法进行测试
        user.add();
    }
    //反射创建对象
    @Test
    public void testUserObject1() throws Exception{
        //获取Class对象
        Class clazz = Class.forName("org.atguigu.spring6.User");
        //调用方法创建对象
        //Object o = clazz.newInstance(); jdk9废除
        User user = (User) clazz.getDeclaredConstructor().newInstance();
        System.out.println(user);
        /*  无参构造
            org.atguigu.spring6.User@281e3708
         */
        }
}
```
- 创建的对象放到哪里？
源码里  `Map<String, BeanDefinition> `
`private final Map<String, BeanDefinition> beanDefinitionMap;`
## Log4j2日志框架
1. 日志优先级
TRACE<DEBUG<INFO<WARN<ERROR<FATAL(严重错误)
    
### 简单配置 log4j2.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss,SSS} %5p %c{1}:%L - %m%n" />
        </Console>
    </Appenders>
    <Loggers>
        <Root level="info">
            <AppenderRef ref="Console" />
        </Root>
    </Loggers>
</Configuration>
```
## 容器:IoC
- 由IoC容器管理的Java对象称为 **Spring Bean**，与使用关键字new创建的Java对象**没有任何区别**

把对象创建 和 对象与对象之间的关系 都交给了IoC

## IoC容器在Spring的实现
### BeanFactory
IoC基本实现，是spring内部使用的接口，面向spring本身，不提供给开发人员
### ApplicationContext
BeanFactory的子接口，提供了更多高级特性。面向spring的使用者。
![ApplicationContext实现类](./Spring/App1.png)

## DI（Dependency Injection）：依赖注入
- 依赖注入实现了控制反转的思想
- 指Spring创建对象的过程中，将对象依赖属性通过配置进行注入
依赖注入常见的实现方式两种：
>1.set注入
2.构造注入

IoC就是一种控制反转的思想，DI是对IoC的一种具体实现。