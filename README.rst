Gross Salary Calculator for Odoo (Egypt Payroll 2025)
======================================================

This module allows HR departments to calculate **gross salary from net salary** in compliance with the **Egyptian tax law (2025)**.

Features
--------

- Convert **Net to Gross** salary using accurate tax and insurance deductions.
- Supports **income tax slabs** with precise rounding (down to 10 piastres).
- Includes **Martyrs Fund contribution** and **social insurance** rules.
- Optional checkboxes to exclude **insurance**, **tax**, or **Martyrs Fund** from gross salary calculation.
- Easily integrated into Odoo Payroll structure.
- Works seamlessly with salary rules and contracts.

Compatible with:
----------------
- Odoo 13.0 to 18.0 (Community & Enterprise)

Egyptian Tax Formula (2025)
---------------------------
The logic inside the module is based on the official Egyptian income tax brackets and deduction rules, including:

- Social insurance (11%)
- Tax exemption (EGP 20,000 annually)
- Sliding tax brackets
- Martyrs Fund 0.05%

How it works
------------

If your company agrees with employees on the net salary (the amount received in hand),  
this module calculates the gross salary (before deductions) automatically.

How to use
----------

1. Go to **Odoo > Human Resources > Contracts**
2. Open an existing contract or create a new one.

You will see new fields:

- **Net Salary**: Enter the amount the employee should receive.
- **Gross Salary**: Calculated automatically — the salary before deductions.
- **Net Salary Fields**: Optionally, select other components to be included in the net.

**Example**:  
If you enter a net salary of 20,000 EGP,  
the system calculates social insurance, income tax, martyrs fund,  
and tells you the required gross salary.

Why this is useful
------------------
- Ensures the employee receives the exact agreed amount.
- Deductions are calculated correctly.
- Payroll and reports stay accurate.
