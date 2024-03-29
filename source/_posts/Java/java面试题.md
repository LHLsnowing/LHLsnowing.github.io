---
title: Java面试题
top: true
cover: false
toc: true
mathjax: true
date: 2023-07-16 13:20:50
summary: 记录一些java面试题
tags: [Java,Java面试题]
categories: [Java,Java面试题]
---

## 一、基础部分
### 1.Java 语言的特点
**Java 语言具有以下特点：**
- **简单易学**：Java 的语法相对简洁清晰，与C++相比去掉了一些复杂的特性（如指针），使得初学者更容易上手。
- **面向对象**：Java 是一种纯粹的面向对象编程语言，支持封装、继承和多态等面向对象的特性，使得代码更加模块化和可扩展。
- **跨平台性**：Java 采用“**一次编写，到处运行**”的原则，通过Java虚拟机（JVM）实现跨平台的能力。程序只需编译一次，就可以在任何支持Java的操作系统上运行。
- **高性能**：虽然Java是解释执行的语言，但通过即时编译和优化技术，Java 可以达到接近于本地代码的性能水平。
- **安全性**：Java 提供了安全管理机制，可以对代码进行访问控制和权限限制，防止恶意程序对系统造成损害。
- **大型的标准类库**：Java 提供了丰富的类库，包含了很多常用的功能和工具，开发人员可以直接使用这些类库来加快开发速度。
- **多线程支持**：Java 内置支持多线程编程，提供了线程的创建、同步和管理等功能，便于开发多线程应用程序。
- **开源生态系统**：Java 拥有庞大的开源社区和丰富的第三方库，开发者可以轻松获取各种开源工具和框架，加快开发速度。

### 2.比较 JVM 和 JDK 以及 JRE
>**JVM（Java Virtual Machine）、JDK（Java Development Kit）和JRE（Java Runtime Environment）**是 Java 平台的三个重要组成部分，它们在开发和运行 Java 程序中扮演不同的角色。下面是对它们进行比较的解释：
>>**JVM（Java虚拟机）**：JVM 是 Java 程序的运行环境，它负责将编译后的 Java 字节码转换为机器码并执行。**JVM 提供了内存管理、垃圾回收、线程管理**等功能。由于Java是跨平台的语言，JVM 的存在使得 Java 程序可以在不同的操作系统上运行，因为每个操作系统都有相应的 JVM 实现。
**JDK（Java开发工具包）**：**JDK 是用于开发 Java 程序的软件包**，其中包含了编译器（javac）、调试器（jdb）、构建工具（javap、jar）、文档生成工具（javadoc）等一系列开发工具。除了这些工具，JDK 还包含了 JRE。开发人员使用 JDK 来编写、编译和调试 Java 程序。
**JRE（Java运行时环境）**：**JRE 是 JVM 所需的运行时环境**，它包含了 JVM 和 Java 类库（Java API），以及其他支持文件和配置。当用户想要运行一个已经编译好的 Java 程序时，只需安装 JRE，而不需要安装 JDK。JRE 使得用户可以在自己的计算机上运行 Java 应用程序，但没有了开发和调试程序的工具。
简单来说，**JVM 是运行 Java 程序的虚拟机，JDK 是开发 Java 程序所需的工具包，而 JRE 则是运行已编译的 Java 程序所需的环境**。在开发过程中，通常需要安装 JDK，而在用户想要运行 Java 程序时，只需安装 JRE。

### 3.为什么说 Java 语言“解释与编译并存”?
- Java 语言被称为“解释与编译并存”，是因为 Java 编程语言和它的运行环境（JVM）采用了一种独特的执行模型，结合了解释执行和编译执行的优点。
1.**解释执行**：Java 程序在运行之前首先会通过 Java 编译器将源代码编译成字节码文件（以 .class 文件形式存在），这些字节码文件并不直接在硬件上执行，而是由 JVM 中的解释器逐条解释执行。解释执行的好处是可以实现跨平台性，因为字节码是与特定硬件无关的中间格式。
2.**即时编译（Just-In-Time Compilation, JIT）：为了提高 Java 程序的执行效率**，JVM 在解释器的基础上引入了即时编译器。即时编译器会将经过多次执行的热点代码（Hotspot Code）转换成本地机器码，并进行缓存，以后再次执行该代码时直接使用本地机器码执行，避免了重复解释执行的开销。这种动态编译技术可以大幅度提高程序的执行速度。(emm，简单理解就是用的多的转为本地机器码之后直接用，方便快捷)
- 因此，**Java 程序在运行时会先经历编译阶段将源代码转换成字节码，然后在解释器中解释执行字节码**。同时，JVM 还会根据代码的执行情况使用即时编译器将热点代码转换成本地机器码，提高程序的运行效率。这种混合的执行模型使得 Java 兼具跨平台性和高性能的特点。

### 4..Java 基本类型有哪几种，各占多少位？
>Java 的基本类型有以下几种：(8位一字节)
>>**byte**：占用 8 位，取值范围为 -128 到 127。
**short**：占用 16 位，取值范围为 -32,768 到 32,767。
**int**：占用 32 位，取值范围为 -2,147,483,648 到 2,147,483,647。
**long**：占用 64 位，取值范围为 -9,223,372,036,854,775,808 到 9,223,372,036,854,775,807。
**float**：占用 32 位，可表示浮点数，精度约为 6-7 位有效数字。
**double**：占用 64 位，可表示双精度浮点数，精度约为 15 位有效数字。
**boolean**：占用 1 位，只能取值 true 或 false。
**char**：占用 16 位，用于表示 Unicode 字符。

### 5.Java 泛型，类型擦除
Java 泛型是 Java 语言中的一项特性，它允许我们在创建类、接口和方法时使用参数化类型。**通过使用泛型，可以实现代码的重用性和类型安全性。**

然而，Java 的泛型实现中存在类型擦除（Type Erasure）的机制。类型擦除指的是在编译时期擦除泛型的具体类型信息，并将泛型类型替换为其边界或 Object 类型。这意味着在编译后的字节码中，并不保留泛型的具体类型信息。

类型擦除的主要原因是为了与 Java 早期版本的二进制兼容性保持一致。在引入泛型之前，Java 使用原始类型（raw types）来表示集合等数据结构。为了确保现有的非泛型代码继续有效，Java 在编译阶段会将泛型代码擦除为原始类型，以便向后兼容。

尽管类型擦除导致在运行时无法获取泛型的具体类型信息，但在编译时仍然会执行类型检查，以确保类型安全性。此外，通过反射和辅助工具类（如 TypeToken），可以在一定程度上绕过类型擦除并获取泛型的信息。

### 6.== 和 equals() 的区别
- `==` 运算符：== 是一个关系运算符，用于比较两个对象的引用是否相等。当使用 == 比较两个对象时，它会检查这两个对象是否指向内存中的同一块地址。换句话说，它比较的是对象的身份标识，即对象在内存中的位置。

- `equals() `方法：equals() 是一个方法，定义在 java.lang.Object 类中。它用于比较两个对象的内容是否相等。默认情况下，equals() 方法和 == 运算符的行为是相同的，即比较对象的引用是否相等。但是，**它可以被子类重写以提供自定义的相等性比较逻辑。例如，String 类重写了 equals() 方法，用于比较字符串的内容而不是引用**。

在使用时，通常应遵循以下准则：
- 如果需要比较对象的引用，以确定它们是否指向同一块内存，使用 == 运算符。
- 如果需要比较对象的内容，即判断它们是否在逻辑上相等，应使用 equals() 方法。但要注意，当使用 equals() 方法时，需要确保该方法已经被适当地重写，以便进行正确的内容比较。
eg:
```java
String str1 = new String("Hello");
String str2 = new String("Hello");

System.out.println(str1 == str2);          // false，比较的是引用
System.out.println(str1.equals(str2));     // true，比较的是内容

Integer num1 = 5;
Integer num2 = 5;

System.out.println(num1 == num2);          // true，比较的是值（基本数据类型）
System.out.println(num1.equals(num2));     // true，比较的是内容
```

### 7.hashCode() 和 equals() 
hashCode() 和 equals() 方法在 Java 中经常一起使用，用于实现对象的相等性判断和集合类的正确操作。

`hashCode() `方法：hashCode() 是定义在 `java.lang.Object` 类中的方法，用于返回对象的哈希码值。哈希码是一个整数，由对象的内容计算得出。可以将哈希码视为对象的 "数字指纹"，用于快速确定对象是否可能相等。

- **如果两个对象通过 equals() 方法比较相等**，那么它们的 **hashCode() 值必须相同**（但反之不成立）。
- 如果**两个对象的 hashCode() 值相同，它们并不一定相等**。
在**重写 equals() 方法时，通常也需要重写 hashCode() 方法**，以确保满足上述规则。这是因为在使用基于哈希表的数据结构（如 HashSet、HashMap 等）时，它们依赖于 hashCode() 方法来进行对象的存储和查找。

### 8.为什么重写 equals() 时要重写 hashCode() 方法？
为什么需要重写 hashCode() 方法呢？**这是因为在使用基于哈希表的数据结构（如 HashSet、HashMap 等）时，它们依赖于 `hashCode() `方法来进行对象的存储和查找。哈希表通过计算对象的哈希码值并将其映射到特定位置来存储对象。当我们使用 `HashSet` 来判断对象是否已经存在集合中时，它会先计算对象的哈希码，然后根据哈希码来快速查找对象。**如果两个对象通过 equals() 方法比较相等，那么它们的哈希码值必须相同，否则 HashSet 就无法正确地定位到已有的对象。

如果你只重写了 equals() 方法而没有重写 hashCode() 方法，可能会导致以下问题：

- **违反了对象相等性原则**：根据 equals() 的逻辑，可能认为两个对象是相等的，但它们的哈希码却不同。这会导致在基于哈希表的集合类中出现错误的行为。
- **无法正确地查找对象**：当尝试从哈希表中查找一个对象时，由于哈希码不匹配，哈希表会认为该对象不存在，即使实际上已经存在。
因此，为了保持对象的一致性和正确操作哈希表数据结构，必须同时重写 equals() 和 hashCode() 方法。确保在两个方法中使用相同的属性来计算哈希码值，以满足相等的对象具有相等的哈希码这一要求。这样可以确保对象在集合类中的正确存储和查找。

### 9.重载和重写的区别
- 重载：在同一个类中定义多个同名方法，但参数列表不同，返回值也可以不同，可以通过不同的方法签名来区分它们。
- 重写：子类继承父类，并定义了与父类**相同名称、相同参数列表和相同返回类型**的方法。**修饰符范围必须比父类大或同**
例如，如果父类方法是 `protected `访问修饰符，子类可以选择使用 `protected` 或 `public` 来重写该方法。

**重载是静态的**，编译时决定调用哪个方法；**重写是动态的**，运行时根据对象的实际类型决定调用哪个方法。

### 10.面向对象和面向过程的区别
面向对象编程（Object-Oriented Programming，OOP）和面向过程编程（Procedural Programming）是两种不同的编程范式。它们有以下区别：

1. 思维方式：面向对象编程强调将问题划分为相互独立的对象，每个对象具有自己的属性和方法，通过对象之间的交互来解决问题。面向过程编程则以线性的方式依次处理问题，将程序看作一系列的步骤或函数。
2. 数据抽象：面向对象编程使用类和对象来实现数据抽象，将数据和操作封装在一起，隐藏内部实现细节，只暴露必要的接口。而面向过程编程更关注数据的处理，将数据和操作分开处理。
3. 代码复用：面向对象编程提供继承和多态等特性，可以通过继承来重用已有的代码，并通过多态来实现动态行为。面向过程编程通常需要手动复制和粘贴代码来实现代码重用。
4. 可维护性：面向对象编程中，对象的封装性使得代码更易于理解和维护，修改一个对象的行为不会对其他对象造成影响。而面向过程编程中，由于数据和操作分离，当需求变化时可能需要修改多处代码。
5. 拓展性：面向对象编程可以通过继承和多态来实现代码的扩展，而不需要修改原有代码。面向过程编程通常需要修改已有的代码来支持新的需求。
6. 团队协作：面向对象编程使得多个开发人员可以并行工作，每个人负责不同的对象或类，通过接口定义彼此之间的交互。面向过程编程则更适合小规模、单人开发的项目。

### 11.成员变量与局部变量的区别
作用域：
- 成员变量的作用域是整个类，在类的任何方法中都可以直接访问。它们存储在对象中，每个对象都有自己的一份成员变量副本。
- 局部变量的作用域只限定在声明它的代码块内，通常是在方法、循环或条件语句中定义的变量。

声明位置：
- 成员变量在类的内部声明，通常位于类的字段部分。它们可以被多个方法访问和修改。
- 局部变量在方法中声明，也可以在代码块中声明。它们只能在声明的代码块内使用。

默认值：
- 成员变量会自动初始化为默认值，如整数为0，浮点数为0.0，布尔值为false，引用类型为null。可以手动赋予其他默认值。
- 局部变量不会自动初始化，需要在使用前进行显式初始化。

生命周期：
- 成员变量的生命周期与对象相同，当创建一个新对象时，成员变量就会被分配内存空间，并且在对象销毁时释放。
- 局部变量的生命周期仅存在于声明所在的代码块执行期间，当代码块执行完毕，局部变量的内存会被释放。

可访问性：
- 成员变量可以有不同的访问修饰符（如public、private、protected），控制对其的访问权限。
- 局部变量只能在声明它的代码块中访问，其他方法无法直接访问局部变量。

### 12.面向对象三大特性是什么。并解释这三大特性
面向对象编程有三大特性，分别是封装（Encapsulation）、继承（Inheritance）和多态（Polymorphism）：

- **封装（Encapsulation）**：封装是指将数据和对数据的操作封装在一个单元中，即类。通过封装，可以隐藏内部实现细节，只暴露必要的接口给外部使用。这样可以提高代码的可维护性和安全性。其他对象无法直接访问对象的内部数据，只能通过公共方法（getter和setter）来间接访问和修改数据。

- **继承（Inheritance）**：继承是指一个类（子类）从另一个类（父类）获取属性和方法。子类可以继承父类的所有非私有成员，包括字段、方法和属性。通过继承，子类可以重用父类的代码，并且可以在此基础上添加新的功能或修改已有的行为。继承还可以建立类之间的层次关系，更好地组织和管理代码。

- **多态（Polymorphism）**：多态是指同一种操作或方法可以在不同的对象上调用，**产生不同的行为**。多态通过继承和方法重写实现。对于一个方法调用，如果被调用对象是子类的实例，那么将执行子类中的方法；如果被调用对象是父类的实例，那么将执行父类中的方法。多态提高了代码的灵活性和可扩展性，可以通过统一的接口处理不同类型的对象。

### 13.String、StringBuffer 和 StringBuilder 的区别
String、StringBuffer和StringBuilder都是Java中用于处理字符串的类，它们之间有以下区别：

- 可变性： String是不可变的类，一旦创建后就不能修改。每次对String进行操作（如拼接、替换），都会生成一个新的String对象。而`StringBuffer`和`StringBuilder`是**可变的类**，可以直接修改其内部内容。

- 线程安全性： `String`是线程安全的，因为它的不可变性可以保证多个线程同时访问时数据不会被修改。`StringBuffer`是线程安全的，它的方法都使用了`synchronized`关键字进行同步，可以在多线程环境下安全地使用。而`StringBuilder`是非线程安全的，多个线程同时访问时可能导致数据不一致的问题。

- 性能效率： 由于String的不可变性，每次对String进行操作都会产生一个新的String对象，这种频繁的对象创建和销毁会消耗大量的内存和CPU资源。而`StringBuffer`和`StringBuilder`的可变性使得它们在**拼接大量字符串时更高效**，因为它们直接修改原始对象，避免了频繁的对象创建。

- 应用场景： 如果需要频繁对字符串进行拼接、插入或删除等操作，并在多线程环境下使用，应选择StringBuffer。如果在单线程环境下进行字符串操作，并且追求更高的性能，可以选择StringBuilder。如果字符串是固定不变的，不需要频繁修改，可以使用String。

综上所述，String适用于不需要频繁修改的场景；StringBuffer适用于多线程环境下频繁修改字符串的场景；StringBuilder适用于单线程下频繁修改字符串且对性能要求较高的场景。根据具体需求和场景选择合适的类会提高代码的效率和可维护性。

应用
下面是StringBuffer和StringBuilder的两个实例应用：

字符串拼接：
```java
String name = "John";
int age = 30;
StringBuffer stringBuffer = new StringBuffer();
stringBuffer.append("My name is ").append(name).append(" and I am ").append(age).append(" years old.");
String message = stringBuffer.toString();
System.out.println(message);
```
这个例子展示了使用`StringBuffer`来动态拼接字符串。通过调用append()方法将多个字符串进行连接，最后使用`toString()`方法将StringBuffer对象转换为String类型。

循环字符串拼接：
```java
StringBuilder stringBuilder = new StringBuilder();
for (int i = 1; i <= 10; i++) {
    stringBuilder.append(i).append(", ");
}
String numbers = stringBuilder.substring(0, stringBuilder.length() - 2); // 去除最后的逗号和空格
System.out.println(numbers);
```
这个例子展示了使用`StringBuilder`在循环中动态拼接数字字符串。每次迭代时，使用append()方法将当前数字添加到StringBuilder中，最后使用`substring()`方法去除最后的逗号和空格。

### 14.ArrayList和LinkedList
ArrayList和LinkedList是Java集合框架中List接口的两个实现类，它们之间有以下区别：

- **底层数据结构**： ArrayList使用数组作为底层数据结构，而LinkedList使用双向链表作为底层数据结构。这导致了它们在插入、删除和访问元素时的性能特点不同。
- **随机访问性能**： `ArrayList`可以通过索引直接访问元素，因为它底层使用数组存储元素，所以随机访问的时间复杂度为O(1)。而`LinkedList`则需要**从头或尾部开始遍历链表**才能找到指定位置的元素，所以随机访问的时间复杂度为O(n)。
- **插入和删除性能**： 在ArrayList中，插入和删除元素需要移动元素位置，如果在列表中间进行操作，会涉及到大量元素的移动，时间复杂度为O(n)。而LinkedList由于使用链表结构，在任意位置插入和删除元素的时间复杂度为O(1)，只需要调整相邻节点的指针即可。
- **空间占用**： ArrayList在内存上连续存储元素，每个元素需要固定大小的空间（对象引用），因此**它的空间占用比LinkedList更高**。而LinkedList的节点可以在内存中分散存储，每个节点除了元素本身外还需要额外的空间用于存储前后节点的引用。
- **迭代性能**： 在进行迭代操作（如遍历所有元素）时，ArrayList由于底层使用数组，可以通过索引直接访问元素，所以迭代速度较快。而LinkedList需要从头或尾部开始遍历链表，每次都需要获取下一个元素的引用，迭代速度较慢。

### 15.HashMap、HashTable、以及 ConcurrentHashMap 的区别   
_可以展开去讲在 Java7 和 Java8 中 HashMap 分别采用什么数据结构，为什么 Java8 把之前的头插法改成了尾插法，怎样实现扩容，为什么负载因子是 0.75，为什么要用红黑树等等一系列的东西_

HashMap、HashTable和ConcurrentHashMap都是Java集合框架中用于存储键值对的类，它们之间有以下区别：

1. **线程安全性**： `HashMap`是**非线程安全的**，不支持并发访问。而`HashTable`是线程安全的，它的方法是同步的（synchronized），可以在多线程环境下使用。`ConcurrentHashMap`也是线程安全的，但采用了更加精细的锁机制，可以支持高并发环境下的读写操作。

2. **空值（null）**： HashMap和ConcurrentHashMap允许使用null作为键或值，而`HashTable`不允许使用null，会抛出`NullPointerException`。

3. **性能**： 在单线程环境下，HashMap的性能通常比HashTable要好，因为HashTable的方法是同步的，会引入额外的开销。而ConcurrentHashMap通过使用分段锁（Segment）来实现高并发访问，并行处理不同的片段，因此在高并发环境下性能更好。

4. **迭代器**： HashMap和ConcurrentHashMap的迭代器都是快速失败的（fail-fast iterator），当在迭代过程中进行结构性修改时会抛出ConcurrentModificationException异常。而**HashTable的迭代器是安全**的（fail-safe iterator），不会抛出异常，但可能会返回旧数据或跳过某些元素。

5. **扩容机制**： HashMap和ConcurrentHashMap都支持自动扩容，当元素数量达到阈值时会进行扩容。HashMap和ConcurrentHashMap的默认初始容量和负载因子都不同，ConcurrentHashMap还允许指定并发级别。

综上所述，如果在多线程环境中需要线程安全的键值对存储，可以选择HashTable或ConcurrentHashMap。如果在单线程环境下，或者需要更好的并发性能，可以选择HashMap或ConcurrentHashMap。并根据具体需求考虑空值的使用和迭代器的行为。
- ConcurrentHashMapExample:
```java
import java.util.concurrent.ConcurrentHashMap;

public class ConcurrentHashMapExample {
    public static void main(String[] args) {
        // 创建ConcurrentHashMap实例
        ConcurrentHashMap<String, Integer> scores = new ConcurrentHashMap<>();

        // 添加键值对
        scores.put("Alice", 85);
        scores.put("Bob", 90);
        scores.put("Charlie", 95);

        // 获取键对应的值
        int aliceScore = scores.get("Alice");
        System.out.println("Alice的分数：" + aliceScore);

        // 替换指定键的值
        scores.replace("Bob", 92);

        // 删除指定键值对
        scores.remove("Charlie");

        // 遍历键值对
        for (String name : scores.keySet()) {
            int score = scores.get(name);
            System.out.println(name + "的分数：" + score);
        }
    }
}
```

---
## 二、进程线程部分

### 1.进程和线程的区别
_要答清楚什么是线程什么是进程，线程和进程各自的运行状态、线程的通信方式和进程的通信方式。_

>进程和线程的区别：

**进程（Process）**是计算机中运行的程序的实例。每个进程都有自己的内存空间、文件描述符、环境变量等资源，它们相互独立并且在操作系统中以进程为单位进行调度和管理。

**线程（Thread）**是在进程内部执行的一条执行路径。一个进程可以包含多个线程，它们共享进程的内存空间和其他资源。线程之间可以更快地切换执行，因此多线程的程序具有更高的并发性和响应性。

**主要区别如下**：

1. 资源占用： 进程拥有独立的内存空间和系统资源，而线程共享所属进程的内存空间和资源。
2. 创建销毁开销： 创建或销毁进程比创建或销毁线程更昂贵，并且进程之间的切换成本较高。
3. 通信代价： 进程间通信的代价较高，需要使用特定的IPC（进程间通信）机制，如管道、消息队列等。而线程之间可以通过共享内存等直接通信方式进行交互，通信代价较低。
4. 并发性： 多个线程可以在同一个进程中并发执行，共享进程的资源，而进程之间的并发性相对较低。
5. 容错性： 进程之间互不影响，一个进程崩溃不会影响其他进程；而线程之间共享进程资源，一个线程的错误可能导致整个进程崩溃。

通信方式：

- **进程通信**：进程间通信有多种方式，包括**管道、命名管道、消息队列、共享内存、信号量、套接字**等。这些通信方式可以在不同进程之间实现数据和控制信息的传递。

- **线程通信**：由于线程之间共享同一进程的内存空间，因此线程之间的通信更为简单直接。常见的线程通信方式包括**共享内存、锁机制（如互斥锁、读写锁）、条件变量、信号量**等。

运行状态：

- 进程运行状态主要有以下几种：创建、就绪、运行、阻塞和终止。

- 线程运行状态主要有以下几种：New（新建）、Runnable（可运行/就绪）、Running（运行）、Blocked（阻塞）、Waiting（等待）、Timed Waiting（计时等待）和Terminated（终止）。

### 2.线程详细运行状态
线程的运行状态主要包括以下几种：

1. New（新建）： 当创建一个Thread对象时，线程处于新建状态。此时线程还未启动，尚未分配系统资源。

2. Runnable（可运行/就绪）： 在调用线程的`start()`方法后，线程进入就绪状态。此时线程已经分配到了系统资源，但并不一定立即执行，需要等待CPU的调度。

3. Running（运行）： 当线程获得CPU的执行权时，进入运行状态。线程会执行相应的任务代码，执行期间可以进行计算、IO操作等。

4. Blocked（阻塞）： 在某些情况下，线程可能会暂时停止执行，进入阻塞状态。常见的阻塞情况包括等待锁、等待输入输出、等待其他线程的通知等。当满足阻塞条件解除时，线程会重新进入就绪状态，等待再次获得CPU的执行权。

5. Waiting（等待）： 线程进入等待状态是因为它在某个条件下主动释放了所占用的资源，并等待唤醒通知。等待状态的线程需要其他线程调用`notify()`或`notifyAll()`方法来唤醒它们。

6. Timed Waiting（计时等待）： 类似于等待状态，但有一个预期的等待时间。线程可以通过调用带有超时参数的`sleep()`、`join()`或者**等待I/O操作完成等方法**进入计时等待状态。

7. Terminated（终止）： 线程执行完任务后或者出现异常导致线程终止，进入终止状态。一旦线程处于终止状态，它将不再运行，并且不能被重启。

### 3.创建线程的四种方式
在Java中，创建线程有以下几种方式：

**继承Thread类**： 创建一个新的类并继承`Thread类`，重写`run()`方法来定义线程的任务代码。然后可以创建该类的实例，并调用`start()`方法启动线程。
```java
class MyThread extends Thread {
    public void run() {
        // 线程的任务代码
    }
}

// 创建线程并启动
MyThread thread = new MyThread();
thread.start();
```
**实现Runnable接口**： 创建一个新的类实现`Runnable接口`，并实现其`run()`方法来定义线程的任务代码。然后创建Thread对象，将Runnable实例作为参数传递给Thread构造函数，最后调用`start()`方法启动线程。
```java
class MyRunnable implements Runnable {
    public void run() {
        // 线程的任务代码
    }
}

// 创建线程并启动
MyRunnable runnable = new MyRunnable();
Thread thread = new Thread(runnable);
thread.start();
```
**使用匿名内部类**： 可以使用匿名内部类来创建线程，省去了单独定义一个类的步骤。通过直接在Thread构造函数中传入Runnable接口的实现或重写Thread类的子类的run()方法来定义线程的任务代码。
```java
// 使用匿名内部类创建线程并启动
Thread thread = new Thread(new Runnable() {
    public void run() {
        // 线程的任务代码
    }
});
thread.start();
```
**使用Lambda表达式**： Java 8及以上版本支持使用Lambda表达式来创建线程。与匿名内部类类似，可以直接在Thread构造函数中传入Runnable接口的实现或重写Thread类的子类的`run()`方法来定义线程的任务代码。
```java
// 使用Lambda表达式创建线程并启动
Thread thread = new Thread(() -> {
    // 线程的任务代码
});
thread.start();
```

### 4.什么是死锁，死锁如何产生，死锁如何避免
~梦回操作系统~

死锁是指多个线程或进程由于互相竞争资源而无法继续执行的状态，每个线程都在等待其他线程释放所需的资源，导致所有线程都被阻塞，无法继续执行下去。这种情况下，系统无法进行任何进一步的处理，需要通过干预来解除死锁。

**死锁产生的必要条件**包括以下四个条件**同时满足**：

- 互斥条件（Mutual Exclusion）： 至少有一个资源只能被一个线程或进程占用，其他线程或进程不能同时访问。
- 请求与保持条件（Hold and Wait）： 线程或进程至少持有一个资源，并且还在等待获取其他线程或进程占有的资源。
- 不可剥夺条件（No Preemption）： 已经分配给线程或进程的资源不能被强制剥夺，只能由持有者主动释放。
- 环路等待条件（Circular Wait）： 多个线程或进程之间形成一种循环等待资源的关系，即存在一个线程或进程的资源请求链条，使得最后一个线程或进程等待第一个线程或进程释放资源。

为了**避免死锁的发生**，可以采取以下几种方法：

- 破坏互斥条件： 如果资源允许被多个线程或进程同时访问，那么就不存在互斥条件，死锁也就不会发生。然而，并非所有情况下都能破坏互斥条件，因为有些资源确实只能被一个线程或进程占用。
- 破坏请求与保持条件： 一种方法是要求线程在请求资源时立即获得所有需要的资源，而不是在运行过程中逐个获取。另一种方法是当一个线程无法获得所需资源时，释放已经持有的资源，等待重新获取所有资源。
- 破坏不可剥夺条件： 强制抢占资源，即将某个线程或进程目前持有的资源剥夺，并分配给其他等待该资源的线程或进程。这种方式可能引入新的问题，需要慎重考虑。
- 破坏环路等待条件： 实现资源的有序分配，可以给每个资源分配一个全局唯一的编号，线程或进程按编号顺序申请资源，避免循环等待。

### 5.synchronized 锁升级流程(锁是懒加载的，需要升级时候才触发相应操作)
在Java中，`synchronized`关键字用于**实现线程同步和互斥访问共享资源**。当多个线程竞争同一个synchronized锁时，会发生锁的升级过程，即从`无锁状态到偏向锁、再到轻量级锁、最后到重量级锁`。

下面是synchronized锁升级的一般流程：

**无锁状态（Unlocked）**： 当线程首次进入synchronized代码块时，对象头的Mark Word字段标记为无锁状态。

**偏向锁（Biased Locking）**： 当只有一个线程访问同步块时，JVM会偏向该线程，将对象头的Mark Word字段修改为指向该线程的Thread ID，并设置标志位表示为偏向锁。之后，该线程可以直接进入临界区，无需进行额外的同步操作。

**轻量级锁（Lightweight Locking）**： 如果有多个线程竞争同步块，JVM会将锁升级为轻量级锁。此时，JVM会尝试使用CAS（比较并交换）操作，将对象头的Mark Word替换为指向锁记录的指针。如果CAS操作成功，线程获得锁，继续执行同步块。如果CAS操作失败，表示其他线程已经获取了锁，当前线程会尝试自旋（不释放CPU资源，反复尝试获取锁），以减少线程上下文切换带来的开销。

**重量级锁（Heavyweight Locking）**： 如果自旋等待仍然无法获得锁，JVM会将锁升级为重量级锁。在这个阶段，等待线程会被挂起，不再占用CPU资源，直到拥有锁的线程释放锁后，等待线程才会被唤醒重新竞争锁。

---
下面是一个简单的示例，展示synchronized锁的升级过程：

```java
public class LockUpgradeExample {
   private static int counter = 0;

   public static synchronized void increment() {
       counter++;
   }

   public static void main(String[] args) throws InterruptedException {
       Thread thread1 = new Thread(() -> {
           for (int i = 0; i < 100000; i++) {
               increment();
           }
       });

       Thread thread2 = new Thread(() -> {
           for (int i = 0; i < 100000; i++) {
               increment();
           }
       });

       thread1.start();
       thread2.start();

       thread1.join();
       thread2.join();

       System.out.println("Counter value: " + counter);
   }
}
```
在这个示例中，我们有一个静态的`counter`变量和两个线程，每个线程都会调用`increment()`方法对`counter`进行递增操作。`increment()`方法使用`synchronized`关键字来保证线程安全。

当运行该示例时，JVM会根据竞争情况自动触发锁的升级过程

### 6.volatile 关键字
volatile关键字和synchronized关键字有以下几点区别：

1. 可见性： `volatile`关键字用于保证变量的可见性，即当一个线程修改了被`volatile`修饰的变量的值时，其他线程能够立即看到最新的值。而`synchronized`关键字除了保证互斥访问，还可以确保可见性。通过获取锁和释放锁的操作，`synchronized`关键字在保护临界区代码的同时，也会将变量从线程的本地缓存写回主内存，使得其他线程能够读取到最新的值。

2. 原子性： `volatile`关键字不能保证对变量的复合操作具有原子性，而`synchronized`关键字可以通过获取锁来保证一段同步代码块的原子性执行。如果需要保证复合操作的原子性，应该使用`synchronized`关键字或者`java.util.concurrent.atomic`包提供的原子类。

3. 排他性： `volatile`关键字不提供排他性，多个线程可以同时读取和写入`volatile`变量的值。而`synchronized`关键字则提供了互斥访问的功能，同一时间只允许一个线程进入同步块执行，其他线程必须等待锁的释放。

4. 内存语义： 使用`volatile`关键字修饰的变量会禁止指令重排序，保证了读写操作的有序性。而`synchronized`关键字通过获取锁和释放锁来建立内存屏障，确保同步代码块的执行顺序符合预期。

总之，`volatile`关键字适用于对变量的可见性进行保证，而`synchronized`关键字适用于实现互斥访问和复合操作的原子性。根据具体的需求，选择合适的关键字来保证线程安全和数据一致性。

### 7.乐观锁和悲观锁的区别

乐观锁（Optimistic Locking）和悲观锁（Pessimistic Locking）是并发控制的两种不同策略，用于解决多线程环境下的数据一致性问题。它们的主要区别在于对于**并发访问冲突的处理方式**。

- 乐观锁： 乐观锁的策略是假设并发访问**不会引发冲突**，因此在读取数据时，并不加锁。在更新数据之前，会先检查数据是否被其他线程修改过。常见的实现方式是使用版本号或时间戳来标记数据的版本，每次更新时比较版本信息。如果版本匹配，则进行更新操作；若版本不匹配，则表示数据已经被其他线程修改过，需要进行相应的冲突处理，如重试操作或放弃更新。

乐观锁适用于读操作频繁、冲突较少的场景。由于不需要加锁，能够提供较高的并发性能。然而，当冲突较多时，频繁的版本检查和重试可能会增加额外的开销。

- 悲观锁： 悲观锁的策略是假设并发访问**会引发冲突**，因此在读取数据时会进行加锁操作，确保只有一个线程能够访问数据。悲观锁常见的实现方式是使用数据库的锁机制（如行级锁或表级锁）或使用 synchronized 关键字进行加锁。

悲观锁适用于写操作频繁、冲突较多的场景，能够保证数据的一致性。然而，由于加锁会导致其他线程阻塞等待，可能会降低并发性能。

### 8.ThreadLocal

`ThreadLocal` 是 Java 中的一个类，用于**在多线程环境中为每个线程保留一份独立的变量副本**,以解决**多个线程访问同一个变量时可能引发的线程安全问题**。每个线程都可以独立地访问和修改自己的副本，互不影响其他线程的副本。这样可以解决多个线程访问同一个变量时可能引发的线程安全问题。

`ThreadLocal` 类提供了以下主要方法：

`get()`：获取当前线程对应的变量副本。
`set(T value)`：设置当前线程对应的变量副本。
`remove()`：移除当前线程对应的变量副本。
`initialValue()（protected 方法）`：返回初始化的变量副本，默认实现返回 null，可以通过继承 ThreadLocal 并重写该方法来设置自定义的初始值。
>使用 ThreadLocal 的基本步骤如下：
1.创建一个 `ThreadLocal` 对象，指定泛型类型为要存储的变量类型。
2.通过 `set(value)` 方法为当前线程设置变量的值。
3.在任意需要访问该变量的地方，使用 `get() `方法获取当前线程的变量副本。

>`ThreadLocal` 的典型应用场景包括但不限于：
线程上下文信息传递：将当前线程相关的上下文信息存储在 ThreadLocal 变量中，在不同组件/方法间传递上下文信息，避免显式传参。
数据库连接管理：通过 ThreadLocal 存储与数据库连接相关的信息，确保每个线程使用独立的数据库连接，提高性能和资源利用。
全局变量的线程安全访问：将共享变量通过 ThreadLocal 使其成为线程私有的，从而避免了多线程竞争的问题。

需要注意的是，使用 ThreadLocal 时应**注意资源管理和内存泄漏问题**。由于 ThreadLocal 的特性，如果不及时清理 ThreadLocal 对象，可能导致长时间运行的线程持有过多的副本，造成内存占用过高。另外，使用线程池时，需要在任务执行完毕后手动调用 remove() 方法清理 ThreadLocal 值，以防止线程复用时出现数据混乱的情况。

### 9.线程池
- 线程池是一种**管理和复用线程的机制**，它可以**提高多线程程序的性能和效率**。

通常情况下，创建和销毁线程会带来较大的开销。而线程池通过**预先创建一定数量的线程**,并维护一个可用线程队列，来避免不断地创建和销毁线程，从而减少开销。

- 线程池主要包括以下几个组成部分：
**线程池管理器（ThreadPoolManager）**：负责维护线程池的状态和管理线程的生命周期。
**工作线程（WorkerThread）**：线程池中的线程，可用于执行具体的任务。
**任务队列（TaskQueue**）：用于存储待处理的任务，线程池从任务队列中获取任务并分配给空闲的工作线程进行处理。

- 使用线程池的**好处**包括：
提高性能和效率：通过重用线程，避免了线程的频繁创建和销毁，减少了系统开销。
控制并发数量：可以限制并发线程的数量，防止线程过多导致系统资源耗尽。
提供任务排队和调度：线程池可以管理任务队列，根据需要调度任务的执行顺序。
提供线程管理和监控：线程池可以统一管理线程的生命周期，并提供监控和统计信息，方便调试和优化。
总之，线程池是一种有效管理和利用线程资源的机制，可以提高多线程程序的性能和可靠性。在开发中，适当地使用线程池可以更好地控制并发，提高系统的吞吐量。

Java线程池是Java提供的一个用于管理和调度线程的工具。它位于`java.util.concurrent`包下，通过提供了一组操作线程池的类和接口，方便开发者使用多线程进行并发编程。

---
>Java线程池的主要类和接口如下：
`Executor` 接口：是线程池的顶层接口，定义了执行任务的方法。
`ExecutorService` 接口：继承自`Executor`接口，增加了对任务提交、线程池状态管理等方法的支持。
`ThreadPoolExecutor` 类：是`ExecutorService`接口的实现类，实现了一个灵活可配置的线程池，可以按需创建线程，并提供了各种线程池参数的设置。
`Executors` 类：提供了一些静态工厂方法，用于创建常见类型的线程池，如`newFixedThreadPool()`、`newCachedThreadPool()`、`newSingleThreadExecutor()`等。
`Future `和 `FutureTask`：用于异步获取线程执行结果的机制。

>使用Java线程池的步骤如下：
1.创建线程池对象：可以使用`Executors`类提供的静态工厂方法来创建线程池，或者直接使用`ThreadPoolExecutor`类的构造方法自定义线程池参数。
2.提交任务：通过调用`execute()`或`submit()`方法向线程池提交需要执行的任务。`execute()`方法用于提交**不需要返回结果**的任务，而`submit()`方法可提交**需要返回结果**的任务，并通过`Future`**对象获取任务的执行结果**。
3.线程池执行任务：线程池会根据配置的参数和任务队列的状态来选择合适的线程执行任务。
4.关闭线程池：在不需要使用线程池时，应调用线程池的`shutdown()`方法来优雅地关闭线程池，等待正在执行的任务完成并释放资源。
通过使用Java线程池，可以方便地管理线程、控制并发数量、调度任务执行顺序，提高程序的性能和可维护性。同时，线程池还提供了丰富的监控和调试工具，便于定位和解决多线程编程中的问题。

- 线程池例子 
```java
package com.example;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {

    public static void main(String[] args) {
        // 创建固定大小为 5 的线程池
        ExecutorService executor = Executors.newFixedThreadPool(5);

        // 提交任务到线程池
        for (int i = 0; i < 10; i++) {
            final int taskId = i;
            executor.execute(new Runnable() {
                @Override
                public void run() {
                    System.out.println("Task " + taskId + " is being executed by " + Thread.currentThread().getName());
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println("Task " + taskId + " is completed.");
                }
            });
        }
        // 关闭线程池
        executor.shutdown();
    }
}
```
该示例创建了一个固定大小为 5 的线程池，通过`execute()`方法提交了10个任务给线程池执行。每个任务都会打印自己的ID和所在线程的名称，并模拟耗时操作（这里使用`Thread.sleep()`方法模拟），然后标记任务完成。
```
Task 1 is being executed by pool-1-thread-2
Task 0 is being executed by pool-1-thread-1
Task 2 is being executed by pool-1-thread-3
Task 3 is being executed by pool-1-thread-4
Task 4 is being executed by pool-1-thread-5
Task 4 is completed.
Task 3 is completed.
Task 1 is completed.
Task 2 is completed.
Task 0 is completed.
Task 7 is being executed by pool-1-thread-2
Task 6 is being executed by pool-1-thread-4
Task 5 is being executed by pool-1-thread-5
Task 9 is being executed by pool-1-thread-1
Task 8 is being executed by pool-1-thread-3
Task 5 is completed.
Task 6 is completed.
Task 7 is completed.
Task 9 is completed.
Task 8 is completed.
```
接下来细说：
#### Java线程池提供了几种常见的线程池类型：

`newFixedThreadPool(int nThreads)`：创建一个**固定大小的线程池**，其中线程数量固定为指定的数量。优点是可以保证线程数量不会超过设定的值，适用于长期执行的任务，但如果任务数量过多，可能会导致任务等待时间增加。
`newCachedThreadPool()`：创建一个根据需要自动调整大小的线程池，适用于执行大量短期异步任务的场景。优点是能够根据任务负载动态调整线程池大小，缺点是当任务量过大时，可能导致系统资源耗尽。
`newSingleThreadExecutor()`：创建一个单线程的线程池，保证所有任务按照顺序执行。适用于需要保证任务串行执行的场景，例如顺序访问文件、数据库等资源。
`newScheduledThreadPool(int corePoolSize)`：创建一个支持定时任务和周期性任务的线程池。可以执行延迟任务或者周期性任务，通过`schedule()`和`scheduleAtFixedRate()`方法提交任务。
各种线程池的优缺点如下：

>`FixedThreadPool` 
优点：
控制并发线程数，不会过多消耗系统资源。
较好地实现任务执行的稳定性。
简化任务调度，按顺序执行任务。 
缺点：
可能会导致任务等待时间增加，如果任务数量过多。
> `CachedThreadPool`
优点：
根据实际任务负载**自动调整线程池大小**。
提供了较高的并发性能。 
缺点：
可能会占用大量系统资源，当任务量过大时，可能导致系统资源耗尽。

>`SingleThreadExecutor` 
优点：
保证任务按顺序执行，确保不会有线程安全问题。
简化编程模型，任务按顺序执行。 
缺点：
性能上可能不如其他线程池，因为只有一个线程在执行。

>`ScheduledThreadPool` 
优点：
可以执行延迟任务和周期性任务。
提供了灵活的任务调度功能。 
缺点：
线程数固定，不能根据需求自动调整。

#### 线程池的重要参数有以下几个：

**核心线程数（corePoolSize）**：线程池中保留的核心线程数量，即使线程处于空闲状态也不会被回收。
**最大线程数（maximumPoolSize）**：线程池允许创建的最大线程数。当任务数量超过核心线程数且任务队列已满时，线程池会创建新的线程来处理任务，直到达到最大线程数。
**任务队列（workQueue）**：用于存放等待执行的任务的阻塞队列，可以选择不同类型的队列，如LinkedBlockingQueue、ArrayBlockingQueue等。
**线程存活时间（keepAliveTime）**：当线程池中线程数量超过核心线程数时，多余的空闲线程在等待新任务到来的时间超过该值时会被回收。
**饱和策略（rejectedExecutionHandler）**：当任务提交给线程池被拒绝时的处理策略，默认有四种饱和策略可选。

#### 线程池的执行流程如下：

1. 当线程池接收到新的任务时，首先会判断核心线程是否已满。如果未满，则创建新的核心线程来执行任务。
2. 如果核心线程数已满，则将任务放入任务队列中等待执行。
3. 如果任务队列也已满，则根据**线程池的饱和策略**来处理任务。可能的饱和策略有直接抛出异常、丢弃任务、丢弃队列中最旧的任务等。
4. 如果线程池中的线程数量超过核心线程数，空闲的线程会等待一段时间，如果在该时间内没有新任务到达，且线程池中的线程数量大于核心线程数，则这些空闲线程会被回收。
5. 线程池的饱和策略决定了当任务提交给线程池被拒绝时的处理方式，

#### Java线程池提供了以下四种饱和策略：

`AbortPolicy`：默认的饱和策略，直接抛出`RejectedExecutionException`异常。
`CallerRunsPolicy`：调用线程自己执行被拒绝的任务。
`DiscardPolicy`：直接丢弃被拒绝的任务，不抛出异常。
`DiscardOldestPolicy`：丢弃队列中最旧的任务，并尝试重新提交被拒绝的任务。
设置线程池的大小可以通过指定核心线程数（corePoolSize）和最大线程数（maximumPoolSize）来实现。合理设置线程池的大小可以根据任务数量、任务执行时间和系统资源等因素考虑。一般来说，可以按照以下原则进行设置：

- 如果任务量一直很高，并且系统负载允许，可以适当增大线程池的最大线程数，以提高并行度和吞吐量。
- 如果任务量较小，或者需要限制并发线程数，可以设置较小的核心线程数和最大线程数，并结合合适的任务队列和饱和策略。

需要注意的是，过大或过小的线程池都可能带来一些问题，如过大的线程池会消耗过多的系统资源，而过小的线程池可能无法满足任务需求。因此，根据具体情况进行评估和调整，以获得最佳的性能和资源利用率。

### 10.ReentrantLock 和 AQS
**ReentrantLock 是 Java 中提供的一种可重入锁（Reentrant Lock）**，**而 AQS（AbstractQueuedSynchronizer）是在并发编程中提供同步机制的框架**。

- `ReentrantLock`： ReentrantLock 是一个**基于独占模式的锁**，提供了与 `synchronized` 关键字类似的功能，并且更加灵活和扩展。它支持可重入性，即同一个线程可以多次获取该锁，避免死锁等问题。ReentrantLock 还提供了公平性和非公平性两种获取锁的策略。

使用 ReentrantLock 需要明确调用  `lock()`方法来获取锁，并在合适的地方使用` unlock() `方法释放锁。通常使用 try-finally 块来确保锁一定会被释放，以防止异常情况下的资源泄漏。

- `AQS`： **AQS 是一个抽象类**，提供了实现同步器（Synchronizer）的基础框架，用于构建各种同步组件（如锁、信号量等）。AQS 内部通过一个状态变量来表示同步状态，提供了对该状态的原子更新和线程的阻塞/唤醒操作。

AQS 的核心是通过一个阻塞队列（CLH Queue）来管理等待获取锁的线程，并且采用了 CAS（Compare and Swap）操作保证并发安全性。具体的同步逻辑由子类实现，如 ReentrantLock 就是 AQS 的子类。

通过继承 AQS，并重写特定的方法（如 tryAcquire()、tryRelease()）可以实现自定义的同步器。

- 总结：
1. ReentrantLock 是一个可重入锁，提供了与 synchronized 关键字类似的功能，但更加灵活和扩展。
2. AQS 是一个抽象类，提供了实现同步器的基础框架，用于构建各种同步组件。
3. **ReentrantLock 是 AQS 的一个具体实现**，利用 AQS 的框架提供了可重入锁的功能。
4. AQS 通过阻塞队列和 CAS 操作实现并发安全性，用户可以通过继承 AQS 并重写特定方法来实现自定义的同步器。


## 三、类加载

> 类加载分为三个步骤：加载、连接、初始化。
### 1.加载
类加载指的是将class文件读入内存，并为之创建一个`java.lang.Class`对象，即程序中使用任何类时，系统都会为之建立一个`java.lang.Class`对象，系统中所有的类都是`java.lang.Class`的实例。
**类的加载由类加载器完成，JVM提供的类加载器叫做系统类加载器，此外还可以通过继承ClassLoader基类来自定义类加载器。**
**通常可以用如下几种方式加载类的二进制数据：**
1. 从本地文件系统加载class文件。
2. 从JAR包中加载class文件，如JAR包的数据库启驱动类。
3. 通过网络加载class文件。
4. 把一个Java源文件动态编译并执行加载。

### 2.连接
**连接阶段负责把类的二进制数据合并到JRE中，其又可分为如下三个阶段：**

**验证**：确保加载的类信息符合JVM规范，无安全方面的问题。
**准备**：为类的静态Field分配内存，并设置初始值。
**解析**：将类的二进制数据中的符号引用替换成直接引用。

### 3.初始化
**该阶段主要是对静态Field进行初始化，在Java类中对静态Field指定初始值有两种方式：**
声明时即指定初始值，如`static int a = 5`；
使用静态代码块为静态Field指定初始值，如：`static{    b = 5;    }` 

**JVM初始化一个类包含如下几个步骤**：
1. 假如这个类还没有被加载和连接，则**程序先加载并连接该类**。
2. 假如该类的直接父类还没有被初始化，则**先初始化其直接父类**。
3. 假如类中有初始化语句，则**系统依次执行这些初始化语句**。
所以JVM总是最先初始化`java.lang.Object`类。

**类初始化的时机（对类进行主动引用时）**：
1. 创建类的实例时（new、反射、反序列化）。
2. 调用某个类的静态方法时。
3. 使用某个类或接口的静态Field或对该Field赋值时。
4. 使用反射来强制创建某个类或接口对应的java.lang.Class对象，如Class.forName("Person")
5. 初始化某个类的子类时，此时该子类的所有父类都会被初始化。
6. 直接使用java.exe运行某个主类时。

## 四、反射
- 什么是反射？**JAVA反射机制是在运行状态中，对于任意一个类，都能够知道这个类的所有属性和方法；对于任意一个对象，都能够调用它的任意一个方法和属性；这种动态获取的信息以及动态调用对象的方法的功能称为java语言的反射机制。**
![](./java面试题/4-0.png)
- 反射的使用？**在Java中，Class类与`java.lang.reflect`类库一起对反射技术进行了全力的支持。在反射包中，我们常用的类主要有 Constructor类表示的是Class 对象所表示的类的构造方法，利用它可以在运行时动态创建对象、 Field表示Class对象所表示的类的成员变量，通过它可以在运行时动态修改成员变量的属性值(包含private)、 Method表示Class对象所表示的类的成员方法，通过它可以动态调用对象的方法(包含private)Class类对象的获取**
```java  
 @Test
    public void classTest() throws Exception {
        // 获取Class对象的三种方式
        logger.info("根据类名:  \t" + User.class);
        logger.info("根据对象:  \t" + new User().getClass());
        logger.info("根据全限定类名:\t" + Class.forName("com.test.User"));
        // 常用的方法
        logger.info("获取全限定类名:\t" + userClass.getName());
        logger.info("获取类名:\t" + userClass.getSimpleName());
        logger.info("实例化:\t" + userClass.newInstance());
    }
```
Constructor类及其用法
Field类及其用法
Method类及其用法

- getName、getCanonicalName与getSimpleName的区别?
`getSimpleName`：只获取类名
`getName`：类的全限定名，jvm中Class的表示，可以用于动态加载Class对象，例如`Class.forName`。
`getCanonicalName`：返回更容易理解的表示，主要用于输出（toString）或log打印，大多数情况下和getName一样，但是在内部类、数组等类型的表示形式就不同了。


## 五、什么是SPI机制？
**SPI（Service Provider Interface），是JDK内置的一种 服务提供发现机制，可以用来启用框架扩展和替换组件，主要是被框架的开发人员使用，比如`java.sql.Driver`接口，其他不同厂商可以针对同一接口做出不同的实现，MySQL和PostgreSQL都有不同的实现提供给用户，而Java的SPI机制可以为某个接口寻找服务实现。Java中SPI机制主要思想是将装配的控制权移到程序之外，在模块化设计中这个机制尤其重要，其核心思想就是 解耦。**SPI整体机制图如下：

![](./java面试题/5-0.png)

## 六、a = a + b 与 a += b 的区别
+= 隐式的将加操作的结果类型强制转换为持有结果的类型。如果两个整型相加，如 byte、short 或者 int，首先会将它们提升到 `int` 类型，然后在执行加法操作。
```java
byte a = 127;
byte b = 127;
b = a + b; // error : cannot convert from int to byte
b += a; // ok
```
(因为 a+b 操作会将 a、b 提升为 int 类型，所以将 int 类型赋值给 byte 就会编译出错)

## 七、Java异常类层次结构
`Throwable` 是 **Java 语言中所有错误与异常的超类**。 
`Error` 类及其子类：程序中无法处理的错误，表示运行应用程序中出现了严重的错误。Exception 程序本身可以捕获并且可以处理的异常。
`Exception` 这种异常又分为两类：运行时异常和编译时异常。

![](./java面试题/7-0.png)

## 八、Java 集合
 容器主要包括 Collection 和 Map 两种，Collection 存储着对象的集合，而 Map 存储着键值对(两个对象)的映射表。
### 1.Collection
#### 1）集合有哪些类？
- `Set` `TreeSet` 基于红黑树实现，支持有序性操作，例如根据一个范围查找元素的操作。但是查找效率不如 HashSet，HashSet 查找的时间复杂度为 O(1)，TreeSet 则为 O(logN)。**HashSet 基于哈希表实现**，支持快速查找，但不支持有序性操作。并且失去了元素的插入顺序信息，也就是说使用 Iterator 遍历 HashSet 得到的结果是不确定的。**LinkedHashSet 具有 HashSet 的查找效率，且内部使用双向链表维护元素的插入顺序**。
- `List` `ArrayList` 基于动态数组实现，支持随机访问。Vector 和 ArrayList 类似，但它是线程安全的。**LinkedList 基于双向链表实现，只能顺序访问，但是可以快速地在链表中间插入和删除元素。**不仅如此，LinkedList 还可以用作栈、队列和双向队列。
- `Queue` `LinkedList` 可以用它来实现双向队列。PriorityQueue 基于堆结构实现，可以用它来实现优先队列。
#### 2）ArrayList的底层？
ArrayList实现了List接口，是顺序容器，即元素存放的数据与放进去的顺序相同，允许放入null元素，**底层通过数组实现**。除该类未实现同步外，其余跟Vector大致相同。每个ArrayList都有一个容量(capacity)，表示底层数组的实际大小，容器内存储元素的个数不能多于当前容量。当向容器中添加元素时，如果容量不足，容器会自动增大底层数组的大小。前面已经提过，Java泛型只是编译器提供的语法糖，所以这里的数组是一个Object数组，以便能够容纳任何类型的对象。

#### 3）ArrayList自动扩容？
每当向数组中添加元素时，都要去检查添加后元素的个数是否会超出当前数组的长度，如果超出，数组将会进行扩容，以满足添加数据的需求。数组扩容通过`ensureCapacity(int minCapacity)`方法来实现。在实际添加大量元素前，我也可以使用ensureCapacity来手动增加ArrayList实例的容量，以减少递增式再分配的数量。
数组进行扩容时，会将老数组中的元素重新拷贝一份到新的数组中，每次数组容量的增长大约是其原容量的1.5倍。这种操作的代价是很高的，因此在实际使用时，我们应该尽量避免数组容量的扩张。当我们可预知要保存的元素的多少时，要在构造ArrayList实例时，就指定其容量，以避免数组扩容的发生。或者根据实际需求，通过调用ensureCapacity方法来手动增加ArrayList实例的容量。
![](./java面试题/8-1-2.png)

### 2.Map
#### 1）Map有哪些类？
- TreeMap 基于红黑树实现。
- **HashMap 1.7基于哈希表实现，1.8基于数组+链表+红黑树**。
- HashTable 和 HashMap 类似，但它是线程安全的，这意味着同一时刻多个线程可以同时写入 HashTable 并且不会导致数据不一致。它是遗留类，不应该去使用它。现在可以使用 `ConcurrentHashMap` 来支持线程安全，并且 ConcurrentHashMap 的效率会更高(1.7 ConcurrentHashMap 引入了分段锁, 1.8 引入了红黑树)。
- LinkedHashMap 使用双向链表来维护元素的顺序，顺序为插入顺序或者最近最少使用(LRU)顺序。

#### 2）JDK7 HashMap如何实现？
哈希表有两种实现方式，一种开放地址方式(Open addressing)，另一种是冲突链表方式(Separate chaining with linked lists)。Java7 HashMap采用的是冲突链表方式。

#### 3）JDK8 HashMap如何实现？
根据 Java7 HashMap 的介绍，我们知道，查找的时候，根据 hash 值我们能够快速定位到数组的具体下标，但是之后的话，需要顺着链表一个个比较下去才能找到我们需要的，时间复杂度取决于链表的长度，为 O(n)。为了降低这部分的开销，在 Java8 中，当链表中的元素达到了 8 个时，会将链表转换为**红黑树**，在这些位置进行查找的时候可以**降低时间复杂度为 O(logN)**。

![](./java面试题/8-2-3.png)

#### 4）HashSet是如何实现的？
HashSet是对HashMap的简单包装，对HashSet的函数调用都会转换成合适的HashMap方法//HashSet是对HashMap的简单包装
```java
public class HashSet<E>
{
	......
	private transient HashMap<E,Object> map;//HashSet里面有一个HashMap
    // Dummy value to associate with an Object in the backing Map
    private static final Object PRESENT = new Object();
    public HashSet() {
        map = new HashMap<>();
    }
    ......
    public boolean add(E e) {//简单的方法转换
        return map.put(e, PRESENT)==null;
    }
    ......
}
```
#### 5）什么是WeakHashMap?
我们都知道**Java中内存是通过GC自动管理的**，GC会在程序运行过程中自动判断哪些对象是可以被回收的，并在合适的时机进行内存释放。GC判断某个对象是否可被回收的依据是，是否有有效的引用指向该对象。如果没有有效引用指向该对象(基本意味着不存在访问该对象的方式)，那么该对象就是可回收的。这里的有效引用 并不包括弱引用。也就是说，虽然弱引用可以用来访问对象，但进行垃圾回收时弱引用并不会被考虑在内，仅有弱引用指向的对象仍然会被GC回收。
**WeakHashMap 内部是通过弱引用来管理entry的，弱引用的特性对应到 WeakHashMap 上意味着什么呢？**
WeakHashMap 里的`entry`可能会被GC自动删除，即使程序员没有调用`remove()`或者`clear()`方法。WeakHashMap 的这个特点特别适用于需要缓存的场景。在缓存场景下，由于内存是有限的，不能缓存所有对象；对象缓存命中可以提高系统效率，但缓存MISS也不会造成错误，因为可以通过计算重新得到。
