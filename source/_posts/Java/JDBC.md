---
title: JDBC
date: 2023-05-25 18:05:50
tags: [JDBC,Java]
categories: [Java,JDBC]
---

# JDBC

## JDBC概念
**JDBC ( Java DataBaseConnectivity java数据库连接)** 是一种用于执行SQL语句的Java API，可以为多种关系型数据库提供统一访问，它是由一组用Java语言编写的类和接口组成的。
**本质**：其实就是java官方提供的一套规范(接口)。用于帮助开发人员快速实现不同关系型数据库的连接!

直接上代码！
```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class JDBC_index1 {
    public static void main(String[] args) throws Exception {
        //注册驱动
        Class.forName("com.mysql.cj.jdbc.Driver");//MySQL5以后可直接省略
        //获取数据库连接
        Connection con= DriverManager.getConnection("jdbc:mysql://localhost:3306/cadastre","root","XXXXXX");
        //获取执行者对象
        Statement stat=con.createStatement();
        //执行sql语句并返回结果
        String sql="select * from 网易云热评";
        ResultSet re=stat.executeQuery(sql);
        //处理结果
        while (re.next()){
      System.out.println(re.getString("userId")+"\t"+re.getString("nickname")+"\t"+re.getString("content"));
        }
        //释放资源
        con.close();
    }
}
```

## JDBC功能详解
### 1、DriverManager驱动管理对象
#### (1)注册驱动:（mysql5以后可直接省略驱动）
1. 注册给定的驱动程序: `staticvoid registerDriver(Driver driver);`
2. 写代码使用:`Class.forName(“com.mysql.jdbc.Driver”);`
3. 在`com.mysql.jdbc.Driver`类中存在静态代码块
#### (2)获取数据库连接:
1. 获取数据库连接对象: `static ConnectiongetConnection(Stringurl, String user,String password);`
2. 返回值:Connection数据库连接对象
3. 参数
url:指定连接的路径。语法: jdbc:mysql://ip地址(域名):端口号/数据库名称
​ user:用户名
​ password:密码
### 2、Connection数据库连接对象
1. 获取执行者对象:
获取普通执行者对象: `Statement createStatement0;`
获取预编译执行者对象:`PreparedStatement prepareStatement(String sql);`
2. 管理事务
开启事务 : `setAutoCommit(boolean autoCommit);`参数为false，则开启事务
​ 提交事务:`commit();`
​ 回滚事务: `rollback();`
3. 释放资源
立即将数据库连接对象释放:`void close();`
### 3、Statement执行sql语句的对象
1. 执行DML语句: `int executeUpdate(String sql);`
返回值int :返回影响的行数。
参数sql:可以执行insert、update、delete语句。
2. 执行DQL语句:`ResultSet executeQuery(String sql);`
返回值ResultSet:封装查询的结果。
参数sql:可以执行select语句。
3. 释放资源
立即将数据库连接对象释放:`void close();`
### 4、ResultSet结果集对象
1. 判断结果集中是否还有数据: `boolean next();`
有数据返回true，并将索引向下移动一行。没有数据返回false。
2. 获取结果集中的数据:XXX getXxx(“列名”);XXX代表数据类型(要获取某列数据，这一列的数据类型)。
例如: `String getString(“name”);int getInt(" age");`
3. 释放资源
立即将结果集对象释放:`void close();`

---

待更...