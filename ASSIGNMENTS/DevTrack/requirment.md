A person who files issues.

id - unique integer

name - full name

email - contact email

team - e.g. backend, frontend, devops

Issue

A bug report or task filed by a Reporter.

id - unique integer

title - short summary

description - full details

status - one of: open, in_progress, resolved, closed

priority - one of: low, medium, high, critical

reporter_id - ID of the Reporter who filed this

created_at - optional, use str(datetime.now())

Relationship:  One Reporter can file many Issues. This is a 1:many relationship - store reporter_id inside the Issue, not the other way around.

OOP design

Model both entities as Python classes before writing any Django code.

Part A - BaseEntity, validate(), and to_dict()
