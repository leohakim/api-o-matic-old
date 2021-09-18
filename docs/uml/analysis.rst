Analysis
========

Domain Model
------------

.. image:: images/domain_model.png
    :scale: 80

Use Cases
---------

.. image:: images/use_cases.png
    :scale: 80

Classes Diagram
---------------

.. image:: images/classes.png
    :scale: 80

Rules
-----

* A bit is the minimal unity of information

* Any Bit in system has to be refreshed at most every 10 minutes

* A byte can contain 0..N Bits

* A registered user can create at most 100 Bits

* When create a new Bit, check for Source, if exists return the existing Bit, else create a new one.

* Source.unique_id is the unique identifier of that resource, in XPATH case: "//*[@id="Capa_1-2"]/path[1]"

* same user can't have 2 Bytes with same name

* same byte can't have 2 equals bits
