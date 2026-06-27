1. Context
Most Saas companies need a reliable way to manage plans, customer, subscriptions, invoices, payments, and ledger events. 

Subledger is simplified billing backedn. 

You are building a clean backend foundation that is easy to understand , test, and extend. 

Models : 
--------
class Plans : 
class customer : 
class subscriptions
class invoices
class payments
class ledger


Learnings : 
----------

Low level desing 
solid principles
Repository Pattern
service Layer
Dependency management
production basics


suggested relationship : 

customer has many subscription  and many LedgerEntries.
Plan has many subscription
subscription has many invoices
invoices has many paymentAttempts and LedgerEntries

