---
title: springboot学习
date: 2023-05-24 20:05:19
tags: springboot
categories: springboot
---

### springboot项目启动不自动启动内嵌tomcat问题

pom.xml需要按照以下顺序配置

```xml
<dependencies>
    <!-- 这个dependcy放在最前面 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>
```
---
### SPring Boot 提供  spring-boot-devtools 组件，使得无需手动重启Spring Boot应用即可重新编译启动项目，缩短编译启动时间

---
### Web入门
- Spring Boot将传统Web开发的mvc、json、tomcat等框架整合，提供了spring-boot-starter-web组件，简化了Web应用配置。
- 创建SpringBoot项目勾选Spring Web选项后，会自动将spring-boot-starter- web组件加入到项目中。
- spring-boot-starter-web启动器主要包括web、webmvc、json、tomcat等基础依赖组件，作用是提供Web开发场景所需的所有底层依赖。
- webmvc为Web开发的基础框架，json为JSON数据解析组件，tomcat为自带的容器依赖。

#### 控制器
- Spring Boot提供了@Controller和@RestController两种注解来标识此类负责接收和处理HTTP请求。
- 如果请求的是页面和数据，使用@Controller注解即可；如果只是请求数据，则可以使用@RestController注解。
![](./springboot%E5%AD%A6%E4%B9%A0/MVC.png)