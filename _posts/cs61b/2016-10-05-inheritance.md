---
layout: page
title: "Inheritance"
description: "A look at inheritance as implemented and used in Java"
permalink: /cs61b/inheritence/
category: cs61b
# tags will also be used as html meta keywords.
tags:
  - cs61b
  - java
  - inheritence
show_meta: true
comments: true
mathjax: true
gistembed: true
published: true
noindex: false
nofollow: false
---

Java is an object oriented programming language. What does that mean? We have classes, which define a type of structure. We have things called objects, which are basically containers of data. All objects are an instance of some class. They have fields, which contain data and can interact with each other through methods.

So what is inheritance? Inheritance is a hierarchy of objects essentially. Basically, it defines a is-a relationship. So a simple example would be like this.

Let's say we have some class called Animal. Then we can have a subclass called Dog that inherits from Animal. All Dogs are Animals. Not all Animals are Dog. Anything an Animal can do, a Dog can go and better. So let's say we have these snippets of Java code

~~~
{}{}
public class Animal {
    public int legs;    

    public void move() {
        System.out.println("Animals move.");
    }

}

public class Dog extends Animal {
    public String breed;

    public void move() {
        System.out.println("Dogs can move too.");
    }

    public void bark() {
        System.out.println("Hi I'm a " + breed);
    }

}

~~~

So Dog is a subclass of Animal. It inherits from Animal and has everything that Animal has. Notice how we didn't redeclare the legs field. That doesn't mean that a Dog doesn't have legs. It does because it inherits it. Also we have overridden move in the subclass. That means when you have a Dog, it'll move like how a Dog should move, not how a generic Animal would. Dogs can also bark and have a breed, while Animals cannot. So like I said, Dogs are not only Animals, they are more.

This is a pretty cursory glance at inheritance. You can get a much better understanding from the Java documentation.