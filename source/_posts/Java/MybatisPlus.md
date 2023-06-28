---
title: MybatisPlus
top: false
cover: false
toc: true
mathjax: true
date: 2023-06-21 11:14:06
summary:
tags: [Java,MybatisPlus]
categories: [Java,MybatisPlus]
---

## 一、ORM 介绍
- ORM （Object Relational Mapping，对象关系映射），为了解决面向对象与关系数据库存在的互不匹配现象的一种技术
- ORM 通过使用描述对象和数据库之间映射的元数据将程序的对象自动持久化到关系数据库中
- ORM 框架的本质是简化编程中操作数据库的编码
![ORM](./MybatisPlus/image.png)

## 二、Mybatis
MyBatis 是一种基于 Java 的 ORM (Object Relational Mapping) 框架，可以将 SQL 映射到 Java 对象上，使用 XML 或注释的方式配置 SQL 语句，使得开发人员可以通过简单的配置完成对数据库的操作。MyBatis 具有轻量、易学易用、可插拔等优点，在 Java Web 开发中得到广泛使用。

- 以下是 MyBatis 的一些基础知识：
1. MyBatis 核心组件：`SqlSession、Configuration、Executor、StatementHandler、ParameterHandler、ResultSetHandler、MappedStatement、SqlSource、BoundSql`

2. MyBatis 中的映射文件有两种：**Mapper 映射文件和全局配置文件**。其中 Mapper 映射文件用来描述 SQL 语句和映射规则，全局配置文件用来配置一些全局性的配置。

3. 在 Mapper 映射文件中，可以使用 **XML 或注解**的方式来配置 SQL 语句。使用 XML 中的 ${} 占位符引用参数，使用 #{} 占位符代替常规的 Java 传参方式，防止 SQL 注入。

4. MyBatis 中**支持插件机制**，用户可以自己编写插件，在 SQL 执行前后进行一些操作，比如记录执行时间、拦截 SQL 执行等。

5. MyBatis 除了支持原生的 JDBC 操作外，还支持集成一些开源的数据库连接池，比如 C3P0、 Druid 等。

6. MyBatis 中的缓存主要分为一级缓存和二级缓存，**一级缓存是 SqlSession 级别的缓存，二级缓存是 SqlSessionFactory 级别的缓存**，可以在多个 SqlSession 之间共享。

7. MyBatis 提供了多种方式来生成主键，比如使用数据库自动生成、使用 MyBatis 内置的序列机制、手工编写主键生成策略等。
## 三、Mybatis-Plus介绍
- MyBatis是一款优秀的数据持久层ORM框架，被广泛地应用于系统
- MyBatis能够非常灵活地实现动态SQL，可以使用XML或注解来配置和映射原生信息，能够轻松地将Java的POJO（Plain Ordinary Java Object，普通java对象）与数据库中的表和字段进行映射关联
- MyBatis-Plus是一个MyBatis 的增强工具，在MyBatis的基础上做了增强，简化了开发

[文档](https://thexb.notion.site/Mybatis-73730a62229347d08b1b4a021ae86eb4)