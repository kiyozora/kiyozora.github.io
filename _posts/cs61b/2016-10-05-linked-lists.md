---
layout: page
title: "Linked Lists"
description: "An introduction to LinkedLists, beginning from unencapsulated singly linked lists to encapsulated doubly linked lists with sentinels"
permalink: /cs61b/linkedlists/
category: cs61b
# tags will also be used as html meta keywords.
tags:
  - cs61b
  - java
  - data structures
  - linked lists
show_meta: true
comments: true
mathjax: true
gistembed: true
published: true
noindex: false
nofollow: false
---

== The Base for Linked Data Structures-A Node
The linked list is essentially our first new data structure. Arrays are nice and all, but they do have their limitations. Probably the most obvous of this is that arrays have a fixed length. If we reach capacity then we're out of luck. Also, if we ever want to add things to the middle of an array based list, then we will have to scooch everything over to the right, and if we were to remove something, we must move it over to the left.

 The linked list is the first data structure that we're going to build from scratch. The base of a linked list is the Node. Nodes also make up the base for other data structures include trees and graphs which we'll get to later. The Node class for our basic linked list will look like the following:

~~~
{Node.java}{}
public class Node {

  public Object item;
  public Node next;

}
~~~

So what is a node. It's basically a box that holds something and knows where the next node in the list is. So how can we use this to make a list? By linking a chain of these Nodes together. For instance, if we have the following code

~~~
{}{}
Node link1 = new Node();
Node link2 = new Node();
Node link3 - new Node();

link1.item = "Hey";
link2.item = "Hi";
link3.item = "Hello";

link1.next = link2;
link2.next = link3;
~~~

What just happened? Well we made 3 of our Nodes, and gave each of them a String to hold. Then we just linked them together by setting their next references. Notice that I didn't set the referece of link3's next. That means that it doesn't reference anything, and in Java, that is null.

So this is the basic structure of a Linked List. It's a recursive data structure. Each Node is in itself a valid list. But there are a few problems with what we have right now. For one, to say that our Nodes are lists themselves is a bit weird. In addition, our nodes aren't protected in any way. Also, how can we represent an empty list? null? If we do that, then we get NullPointer exceptions.

But we can get around this by defining a wrapper class, a class to actually represent our Linked List. This class will then use our Nodes in order to be a list. But what's great about this is that now people don't need to worry about our Nodes. As you'll see, we'll be changing up what our Nodes have and can do, but the outside world won't need to worry about it. It's abstracted away!

So let's add our wrapper class. I'll also add a constructor to the Node class.

~~~
{SList.java}{}
public class SList {

  private Node head;
  private int size;

  public SList() {
    head = null;
    size = 0;
  }
}
~~~
~~~
{Node constructor}{}
  public Node(Object item, Node next) {
    this.item = item;
    this.next = next;
  }
~~~

This version of the Linked List, the SList is called so because it is singly-linked. That is, all the Nodes in our list only have one reference, their next reference. 

Now we can think about the operations that our SList should be able to do. Well, the most ovious thing is that we want to be able to insert things into our list. So let's add an insert method. For now we'll only add things to the front of our SList. The code will look something like this

~~~
{Inserting into the front of a linked list}{}

public void insertFront(Object item) {
  head = new Node(item, head);
  size++;
}
~~~

So how do we make a list now? Well unlike before when we handled the Nodes directly, now we can just go through the SList class. So inserting into the list can be like this

~~~
{}{}
SList l = new SList();
l.insertFront(1);
l.insertFront(10);
l.insertFront(7);
~~~

So this is great right. We can add things to the front of a list really easily and quickly. If we did this using an array, we'd have to move everything first. But there are some disadvantages to our list as of now. One is that we can only add things to the beginning quickly. How would we add things to the end? Well in order to do that we can modify our SList class with a tail reference optimization. Basically in addition to the head pointing to the beginning of the list, we will have the tail pointing to the end of our list.

~~~
{SList.java with tail and insertBack}{}
public class SList {

  private Node head;
  private Node tail;
  private int size;

  public SList() {
    head = null;
    tail = null;
    size = 0;
  }

  public void insertBack(Object item) {
    tail.next = new Node(item, null);
    tail = tail.next;
    size++;
}
~~~

But there are two operations that we naturally expect Lists to support that we don't currently have, and that's the get method and the remove method. What the logic for getting? Well unfortunately you can't index into a Linked List. The only thing that you can index into is an array. So we'll have to walk through the list in order to get something.

~~~
{get}{}
  public Object get(int index) {
    Node curr = head;
    for (int i = 0; i < index; i++) {
      curr = curr.next;
    }
    return curr.item;
  }
~~~

Now what about removal? Well removal from the beginning from a list is easy. All we have to do is set the head to become its next and the tail can remain untouched. But how about removing from the end of the list? It seems easy right? After all we have the tail pointer. But there's a problem. In order to remove from the end, we'd have to set the tail to the Node /previous/ to it. But how can we get to that Node? Well as of right now, the only way we can do that is again walk through our list until we reach it. Our nodes don't have access to the previous node; it's a singly linked list. But can fix that and have our list evolve. So introducing the Doubly linked list.

~~~
{New and improved Node class}{}
public class Node {

  public Object item;
  public Node next;
  public Node prev;

  public Node(Object item, Node next, Node prev) {
    this.item = item;
    this.next = next;
    this.prev = prev;
  }
}
~~~

~~~
{DList.java}{}
public class DList {

  private Node head;
  private Node tail;
  private int size;

  public DList() {
    head = null;
    tail = null;
    size = 0;
  }

  public void insertFront(Object item) {
    head = new Node(item, head, null);
    head.next.prev = head;
    size++;
  }

  public void insertBack(Object item) {
    tail = new Node(item, null, tail);
    tail.prev.next = tail;
    size++;
  }

  public void removeFront() {
    head = head.next;
    head.prev.next = null;
    head.prev = null;
    size--;
  }

  public void removeBack() {
    tail = tail.prev;
    tail.next.prev = null;
    tail.next = null;
    size--
  }

  public int size() {
    return size;
  }

}
~~~

Now our nodes know what is in before and after it. And because of that, removal from the back can now be in constant time. Of course now we have to do a bit more book keeping then when we only had single lists, but we are able to gain speed out of it.

I'm going to pause a bit to talk about invariants. We'll return to this more when talk about ADTs, but it deserves a bit of mentioning now. An *invariant* is something that is true about a data structure or code, assuming that everything is bug free. Basically, no matter how anyone tries to screw up your data structure, the invariants should still remain the same.

Some of the invariants that we have in our new DList is that the head instance variable will always point to the beginning of the list, the tail instance variable will always point to the end of the list, and that the size variable is always correct.

One last thing that I want to mention that we have not covered in depth this semester of CS61B (Fall 2015), is of an even further improvement on our linked list. Right now our DList looks pretty sweet. It does great things, but in our code there can be special cases. We can get around this through a *sentinel* node. Basically what happens is that our DList will have a special Node that will not hold anything. It's sole purpose will be to represent the head and tail of our list. Because of it, our code can be simpler, there will never be a case of null. Also there only has to be one reference, the reference to our sentinel. We don't need a reference to the tail anymore because our sentinel will know where it is.

It may seem like there is a lot of book keeping in the code, but it is clean and it does make sense. I do suggest drawing out an example and seeing what is happening to the references. I do a lot of cleaning up to make sure that old nodes get garbage collected.

~~~
{DList with a sentinel}{}
public class DList {

  private Node sentinel;
  private int size;

  public DList() {
    sentinel = new Node(null, null, null);
    sentinel.next = sentinel;
    sentinel.prev = sentinel;
    size = 0;
  }

  public void insertFront(Object item) {
    sentinel.next = new Node(item, sentinel.next, sentinel);
    sentinel.next.next.prev = sentinel.next;
    size++;
  }

  public void insertBack(Object item) {
    sentinel.prev = new Node(item, sentinel, sentinel.prev);
    sentinel.prev.prev.next = sentinel.prev;
    size++;
  }

  public void removeFront() {
    sentinel.next = sentinel.next.next;
    sentinel.next.prev.prev = null;
    sentinel.next.prev.next = null;
    sentinel.next.prev = sentinel;
    size--;
  }

  public void removeBack() {
    sentinel.prev = sentinel.prev.prev;
    sentinel.prev.next.prev = null;
    sentinel.prev.next.next = null;
    sentinel.prev.next = sentinel;
    size--
  }

  public int size() {
    return size;
  }

}
~~~

