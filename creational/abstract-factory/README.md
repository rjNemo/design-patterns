# Abstract Factory

## Summary

Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

## Problem

Imagine that you’re creating a furniture shop simulator. Your code consists of classes that represent:

A family of related products, say: `Chair` + `Sofa` + `CoffeeTable`.

Several variants of this family. For example, products `Chair` + `Sofa` + `CoffeeTable` are available in these variants: `Modern`, `Victorian`, `ArtDeco`.

You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.

Also, you don’t want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs very often, and you wouldn’t want to change the core code each time it happens.

## Solution

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. For example, all chair variants can implement the `Chair` interface; all coffee table variants can implement the `CoffeeTable` interface, and so on.

## How to Implement

1. Map out a matrix of distinct product types versus variants of these products.

1. Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.

1. Declare the abstract factory interface with a set of creation methods for all abstract products.

1. Implement a set of concrete factory classes, one for each product variant.

1. Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.

1. Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.
