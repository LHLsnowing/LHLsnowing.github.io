---
title: java小记
date: 2023-06-06 15:52:22
tags: java小记
categories: [Java,Java第二篇]
---

## java中s.length() 和 s.length区别
- s.length是针对java中数组的，length是数组的一个属性，用来表示数组的长度
- s.length()则是字符串的一个方法，用来返回字符串的长度的

## 类的五大成员
[属性、方法、构造器、代码块、内部类]
内部类还分为局部内部类（通常在方法中）、匿名内部类（无类名）
- 局部内部类：作用域在方法或者代码块中、不能添加访问修饰符、但是可以使用final
外部其他类不能访问局部内部类，如果外部类和局部内部类的成员重名时候，遵循就近原则，
如果想访问外部类成员可以用（外部类名.this.成员）
- （Anonymous匿名的）匿名内部类：同时还是一个对象，系统jdk会分配个名字
```java
IA tiger = new IA(){
    @Override
    public void cry(){
        System.out.println("老虎叫---")；
    }
}
tiger.cry();
```