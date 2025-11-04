# Implementation of Software Design Patterns illustrated through Banking and Financial System examples

Table of contents

## Creational Design Pattern

- [Factory Method Design Pattern](#)
- [Abstract Factory Method Design Pattern](#)
- [Singleton Method Design Pattern](#)
- [Prototype Method Design Pattern](#)
- [Builder Method Design Pattern](#)

## Structural Design Pattern:

- [Adapter Method Design Pattern](#)
- [Facade Method Design Pattern](#facade-method-design-pattern)
- [Proxy Method Design Pattern](#)

## Behavioral Design Pattern:

- [Chain Of Responsibility Method Design Pattern](#)
- [Command Method Design Pattern](#)
- [Observer Method Design Pattern](#)
- [Strategy Method Design Pattern](#)

## Creational Design Patterns

<!-- Factory Method Design Pattern -->

### <ins> Factory Method Design Pattern</ins>

`Defines an interface for creating objects, letting each factory decide which specific type of object to create.`<br />
**My Example: Creates different types of bank accounts through the same interface**

> <ins> Main idea:</ins>
> Factory Method → One abstract creator (AccountFactory), multiple concrete factories, one product type (Account).
> The abstract factory (AccountFactory) defines the create_account() factory method — but doesn’t decide which account to create.
> Each concrete factory (CurrentAccountFactory, SavingAccountFactory) implements create_account() differently so that the client code calls the same interface, but gets different results.
> Check out the example code [here &rarr;](/creational_design_patterns/factory_method_design_pattern.py)

![Facade Method UML diagramm](/assets/images/FactoryMethod.png)

<!-- Abstract Factory Method Design Pattern -->

### <ins> Abstract Factory Method Design Pattern</ins>

`Defines an interface for creating set of related objects, letting each bank factory decide which specific product to create.`<br />
**My Example: Creates different types of banking products -Accounts, Cards and loans through the same interface**

> <ins> Main idea:</ins>
> Abstract Factory Method → One abstract factory (BankFactory), multiple concrete factories(InvestmentBankFactory, CommercialBankFactory, RetailBankFactory), multiple product types (Account, Card, Loan).
> The abstract factory (BankFactory) defines creation method for each product type (create_account(), create_card() create_loan()), but doesn’t decide which exactly account, card, or loan to create.
> Each concrete factory implements these methods to produce a cohesive family of products appropriate for that bank, so client code calls the same interface but gets different results depending on the factory used.

> Check out the example code [here &rarr;](/creational_design_patterns/abstract_factory_method_design_pattern.py)

![Facade Method UML diagramm](/assets/images/AbstractFactoryMethod.png)

[Go to -> Creational Design Pattern](#creational-design-pattern)

## Structural Design Pattern

<!-- Adapter Method Design Pattern -->

### <ins>Adapter Method Design Pattern</ins>

`Acts as a bridge to connect incompatible interfaces or formats`<br />
**My Example: Integration of incompatible payment APIs (like PayPal and Stripe) under a unified interface process_payment() for the banking system.**

> <ins> Main idea:</ins>
> Helps integrate different payment APIs using a unified interface process_payment() as a technical method that executes the actual payment, while the client interacts with the system through the high-level transfer_money() method of banking application.
> Check out the example code [here &rarr;](/structural_design_patterns/adapter_method_design_pattern.py)

![Facade Method UML diagramm](/assets/images/AdapterMethod.png)

<!-- Facade Method Design Pattern -->

### <ins>Facade Method Design Pattern</ins>

`Provides a simple unified interface to a set of complex subsystems`<br />
**My Example: Money Transfer in a Banking System**

![Facade Method UML diagramm](/assets/images/FacadeMethod.jpg)

> <ins> Main idea:</ins>
> Instead of dealing with complex subsystems or components, the client only needs to call a single transfer_money() method, implemented as a Facade. The client doesn’t need to know all the individual methods, the underlying resources, or the correct sequence of calls.
> Check out the example code [here &rarr;](/structural_design_patterns/facade_method_design_pattern.py)

### <ins>Proxy Method Design Pattern</ins>

> [Go to -> Structural Design Pattern](#creational-design-pattern)

## Behavioral Design Patterns

[Go to -> Behavioral Design Pattern](#behavioral-design-pattern)
