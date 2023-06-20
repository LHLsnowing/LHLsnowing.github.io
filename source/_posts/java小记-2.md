---
title: java小记_2
top: false
cover: false
date: 2023-06-20 09:07:04
summary: java第三篇
tags: [java,List]
categories: [Java,java第三篇]
---

# java的第三篇啦
有部分笔记不是很详细，记在心里即可

## 一、List接口
实现List接口的常用三个类
ArrayList、LinkedList、Vector
```java
public class List_ {
    public static void main(String[] args) {
        // 1. List集合类中元素有序（取出和添加顺序一样）
        List list = new ArrayList();
        list.add("丹青");
        list.add("锦绣");
        System.out.println(list);
        // 2. List 索引从0开始
        System.out.println(list.get(1));//锦绣
    }
}
```
List三种遍历方式  
>1. 使用iterator
2. 增强for
3. 普通for

### ArrayList
ArrayList可以加null，源码由数组实现数据存储
效率高，不安全
扩容倍数：有参构造直接1.5倍，     无参构造第一次10，第二次1.5倍
### Vector
扩容倍数：指定大小直接2倍          无参默认10，第二次2倍
安全，效率低
```java
public class Vector_ {
    public static void main(String[] args) {
        Vector vector = new Vector();
        for(int i=0;i<10;i++){
            vector.add(i);
        }
        Iterator iterator= vector.iterator();
        while(iterator.hasNext()){
            Object obj = iterator.next();
            System.out.println(obj);//0-9
        }
    }
}
```
### LinkedList_双向链表
1. LinkedList底层实现了双向**链表**和双端**队列**
2. 可以添加任意元素（可重复），包括null
3. 线程不安全，没有实现同步

## 二、Set 接口
方法和collection类似
1. 无序，无索引
2. 不允许有重复数据，最多一个null
3. 实现类有 HashSet TreeSet等等
一般 `Set set = new HashSet();`

### HashSet 实现了 Set接口
下面有意思
```java
set.add(new String("lhl"));//ok
set.add(new String("lhl"));//不能加入到set中 都在常量池中
```
- HashSet底层是HashMap，HashMap底层是（数组+链表+红黑树）

## 三、Map 接口
存key-value
![](./java%E5%B0%8F%E8%AE%B0-2/Map.jpg)
常用方法，基础用法
```java
public class Map_ {
    public static void main(String[] args) {
        Map map = new HashMap<String,String>();
        map.put("1","王宝强");
        map.put("2","花戎");
        map.put(null,"??");
        map.put(null,null);
        System.out.println(map);//{null=null, 1=王宝强, 2=花戎}
        map.remove("1");
        System.out.println(map);//{null=null, 2=花戎}
        // map.clear(); 清空
        System.out.println(map.containsKey(0));//false
    }
}
```
### Hashtable 实现了 Map
1. k-v都不允许为null
2. hashtable线程安全，hashmap线程不安全
3. 方法几乎和hashmap一致

### Properties 实现了 Map
- Properties类继承自Hashtable类并且实现了Map接口，也是k-v存储

## 四、泛型
1. 编译时，检查元素类型，提高安全性
2. 减少类型转换次数
`ArrayList<Dog> arraylist = new ArrayList<Dog> ();`

### 自定义泛型类
TS差不多
```java
class 类型<T,R...>{ //也可以是接口
    成员
}
```

## 五、JUnit 5
1. java语言单元测试框架
2. 多数开发环境已经集成了
![Alt+Enter快捷键](./java%E5%B0%8F%E8%AE%B0-2/JUnit.png)

## 六、java绘图
__P572 暂留__
- component类提供两个和绘图相关的重要的方法
1.` paint（Graphics g）`绘制组件的外观
2. `repaint（）`刷新组件的外观

- 当组件第一次在屏幕显示的时候，程序会自动的调用paint（）方法来绘制
- 一下情况paint（）会被调用
1. 窗口最小化，再最大化
2. 窗口的大小发生变化
3. repaint函数被调用
```java
package com.draw;

import javax.swing.*;
import java.awt.*;

public class DrawCircle extends  JFrame{ //窗口
    private  MyPanel mp = null;
    public static void main(String[] args) {
        new DrawCircle();
    }
    public DrawCircle(){
        mp = new MyPanel();
        this.add(mp);
        this.setSize(400,300);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//点×退出
        this.setVisible(true);
    }
}

class MyPanel extends JPanel{
    //g 画笔  MyPanel 画板
    @Override
    public void paint(Graphics g){
        super.paint(g);//调用父类完成初始化
        // 画圆形
        g.drawOval(10,10,100,100);
    }
}
```
## 线程 Thread
外记快捷键 打开structure ： alt+7
- Thread 实现了 Runnable接口
>两种方法使用：
1. 实现Runnable接口
2. 集成Thread类
```java
package com.thread;

public class Thread01 {
    public static void main(String[] args) {
        Cat cat = new Cat();
        cat.start();
    }
}

class Cat extends Thread{

    @Override
    public void run(){
        while (true){
            System.out.println("喵喵");
            // try catch   ctrl+alt+t
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```
## Synchronized
加入synchronized同步 上锁