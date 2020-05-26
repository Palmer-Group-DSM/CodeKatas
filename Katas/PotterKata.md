# Potter
In the magical world of code katas, there is a captivating series of 5 books about a wizard. This wizard's name is Harry. The series follows his extraordinary adventures and people love reading it! Thankfully, the publisher has set a generous pricing model, so that many people can get their own copy of the books.

> Pricing Model:

**Any one book within the series has an individual price of $8.00 each.**

If you buy more than one book at a time to create a set, you will get a percentage discount on the book.

| Sale Description | Discount Value |
| ---------------- | ----- |
| Buy **1** book within the series  | No discount |
| Buy **2** different books within the series | **5%** discount |
| Buy **3** different books within the series  | **10%** discount |
| Buy **4** different books within the series  | **20%** discount |
| Buy all **5** books within the series  | **25%** discount |

### Here is the catch:
> If you buy multiple books with the same title, then you buy the books at their individual price of $8.00.

### For example:

```
Given a shopping cart
When I buy 3 different books
Then my total is 21.60 dollars

```

```
Given a shopping cart
When I buy 3 of the same book 
Then my total is 24 dollars

```

### **Your goal is to create a program that calculates the price of any possible combination of books in a shopping cart and gives the best discount available.** 



