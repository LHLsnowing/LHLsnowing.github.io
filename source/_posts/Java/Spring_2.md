---
title: Spring_2
top: true
cover: false
toc: true
mathjax: true
date: 2023-06-30 17:54:40
summary: SpringMVC、事务
tags: [Java,Spring,SpringMVC]
categories: [Java,Spring]
---

# SSM常用注解
- 在SSM（Spring + Spring MVC + MyBatis）框架中，有很多常用的注解用来简化配置和增强开发效率。以下是一些常用的注解：
>`@Component`：用于标识一个普通的Java类为Spring容器的组件。
`@Controller`：用于标识一个类为Spring MVC的控制器。
`@RequestMapping`：用于映射请求路径到控制器的处理方法。
`@Service`：用于标识一个类为服务层的组件，用于定义业务逻辑。
`@Repository`：用于标识一个类为持久层的组件，通常用于访问数据库。
`@Autowired`：用于自动注入依赖，可以用在构造方法、属性或方法上。
`@Qualifier`：结合@Autowired使用，用于指定注入的Bean的名称。
`@Value`：用于注入属性值。
`@RequestParam`：用于获取请求参数的值。
`@ResponseBody`：用于将方法返回的对象转换为指定的格式（如JSON）并响应给客户端。
`@PathVariable`：用于获取请求路径中的占位符的值。
`@Valid`：用于开启方法参数的校验。
`@Transactional`：用于标识一个方法或类需要进行事务管理。
`@Aspect`：用于定义切面（Aspect）。
`@Pointcut`：用于定义切入点（Pointcut）。

![](./Spring_2/0.jpg)
## 一、事务
- @Transactional
- mybatis内部使用jdbc的事务，事务主要是为了同成功或者同失败，eg：银行转账，并记录日志

- 事务管理员：发起事务方    开启事务的方法
- 事务协调员：加入事务方，通常为   数据层方法，也可以是业务层方法

- 事务传播
![事务传播](./Spring_2/1-1.png)

## 二、SpringMVC

### 1.SpringMVC概述
- SpringMVC是一种基于Java实现MVC模型的轻量级Web框架
![轻量级Web框架](./Spring_2/2-1.png)

### 2.bean加载控制
- ![bean加载控制](./Spring_2/2-2.png)
- 主要有excludeFilters， includeFilters
![利用Filter细节](./Spring_2/2-3.png)

#### 白学之路——化简了
![简化开发](./Spring_2/2-3-1.png)

### 3.设置请求映射路径
- 为了避免冲突
- /user/save
- /book/save

### 4.json数据传递参数
- @RequestBody和@RequestParam的区别
![@RequestBody和@RequestParam的区别](./Spring_2/2-4-1.png)

## 三、jetty服务器_切换web服务器
![Jetty换tomcat配置](./Spring_2/3-1.png)

## 四、三种配置文件格式
### 1.优先级及格式配置
 - 优先级：`application.yml`  < `application.yaml` < `application.properties`
![提示功能消失解决方案](./Spring_2/4-1.png)
![几种格式](./Spring_2/4-2.png)

### 2.yaml语法
 >yaml主流-数据序列化格式，下面为语法格式
 >>1.大小写敏感
2.属性层级关系使用多行描述，每行结尾使用冒号（：）结束
3.使用缩进表示层级关系，同层级左侧对齐，只允许空格（不允许用tab）
4.属性值前面添加空格（属性名和属性值之间用 冒号+空格 分隔
5.# 表示注释

### 3.读取方式
>数据读取 ： `@Value(${..})`   ,
 自定义封装的指定数据  `@ConfigurationProperties(prefix="enterprise")` ,
 Environment

## 五、 多环境开发配置
### 1.基础配置，多环境启动
- 带划线的为过时的
![](./Spring_2/5-1.png)

### 2.propertie多环境启动_承接上面
![](./Spring_2/5-2.png)

### 3.配置文件分类
- config文件夹下的配置文件优先级更高
![](./Spring_2/5-3.png)


## 六、Lombok
引入lombok
要使用 ` @Data`注解要先引入lombok?，lombok 是什么，它是一个工具类库，可以用简单的注解形式来简化代码，提高开发效率。

在maven中添加依赖
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
    <scope>provided</scope>
</dependency>
```

用@Data的写法：
```java
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Person {
    private String name;
    private String address;
    private Integer age;
    private String hobbit;
    private String phone;
}
```
常用的几个注解：
`@Data` ： 注在类上，提供类的get、set、equals、hashCode、canEqual、toString方法
`@AllArgsConstructor` ： 注在类上，提供类的全参构造
`@NoArgsConstructor` ： 注在类上，提供类的无参构造
`@Setter` ： 注在属性上，提供 set 方法
`@Getter` ： 注在属性上，提供 get 方法
`@EqualsAndHashCode` ： 注在类上，提供对应的 equals 和 hashCode 方法
`@Log4j/@Slf4j` ： 注在类上，提供对应的 Logger 对象，变量名为 log

- **原理**
Lombok本质上就是一个实现了“JSR 269 API”的程序。在使用javac的过程中，它产生作用的具体流程如下：

javac对源代码进行分析，生成了一棵抽象语法树（AST）
运行过程中调用实现了“JSR 269 API”的Lombok程序
此时Lombok就对第一步骤得到的AST进行处理，找到@Data注解所在类对应的语法树（AST），然后修改该语法树（AST），增加getter和setter方法定义的相应树节点
javac使用修改后的抽象语法树（AST）生成字节码文件，即给class增加新的节点（代码块）

- **优缺点**
**优点：**
能通过注解的形式自动生成构造器、getter/setter、equals、hashcode、toString等方法，提高了一定的开发效率
让代码变得简洁，不用过多的去关注相应的方法
属性做修改时，也简化了维护为这些属性所生成的getter/setter方法等

**缺点：**
不支持多种参数构造器的重载
虽然省去了手动创建getter/setter方法的麻烦，但大大降低了源代码的可读性和完整性，降低了阅读源代码的舒适度
像 lombok 这种插件，已经不仅仅是插件了，它在编译器编译时通过操作AST（抽象语法树）改变字节码生成，变相的说它就是在改变java语法，它改变了你编写源码的方式，它不像 spring 的依赖注入一样是运行时的特性，而是编译时的特性。如果一个项目有非常多这样的插件，会极大的降低阅读源代码的舒适度。
lombok 只是省去了一些人工生成代码的麻烦，但是这些getter/setter等等的方法，用IDE的快捷键也可很方便的生成。况且，有时通过给getter/setter加一点点业务代码（但通常不建议这么加），能极大的简化某些业务场景的代码。