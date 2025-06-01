
from odoo import models, fields, api
from decimal import Decimal, ROUND_HALF_UP, getcontext

getcontext().prec = 12

class HrContract(models.Model):
    _inherit = 'hr.contract'

    selected_components = fields.Many2many(
        comodel_name='ir.model.fields',
        domain=[('model', '=', 'hr.contract')],
        string='Net Salary Fields'
    )

    net_salary = fields.Float(
        string='Net Salary',
        compute='_compute_net_salary',
        digits=(16, 2)
    )

    gross_salary = fields.Float(
        string='Gross Salary',
        compute='_compute_gross_salary',
        digits=(16, 2)
    )

    @api.depends('selected_components')
    def _compute_net_salary(self):
        for contract in self:
            total = 0.0
            for field_rec in contract.selected_components:
                try:
                    total += getattr(contract, field_rec.name, 0.0) or 0.0
                except AttributeError:
                    continue
            contract.net_salary = round(total, 2)

    def compute_annual_tax(self, income):
        income = Decimal(income)
        if income > 1200000:
            tax = 300000 + (income - 1200000) * Decimal('0.275')
        elif income > 900000:
            tax = 90000 + (income - 400000) * Decimal('0.25')
        elif income > 800000:
            tax = 85000 + (income - 400000) * Decimal('0.25')
        elif income > 700000:
            tax = 81500 + (income - 400000) * Decimal('0.25')
        elif income > 600000:
            tax = 78750 + (income - 400000) * Decimal('0.25')
        elif income > 400000:
            tax = 74750 + (income - 400000) * Decimal('0.25')
        elif income > 200000:
            tax = 29750 + (income - 200000) * Decimal('0.225')
        elif income > 70000:
            tax = 3750 + (income - 70000) * Decimal('0.20')
        elif income > 55000:
            tax = 1500 + (income - 55000) * Decimal('0.15')
        elif income > 40000:
            tax = (income - 40000) * Decimal('0.10')
        else:
            tax = Decimal('0.00')
        return tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @api.depends('selected_components')
    def _compute_gross_salary(self):
        for contract in self:
            # 
            total = 0.0
            for field_rec in contract.selected_components:
                try:
                    total += getattr(contract, field_rec.name, 0.0) or 0.0
                except AttributeError:
                    continue
            net_salary = Decimal(total).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            if not net_salary:
                contract.gross_salary = 0.0
                continue

            target_net = net_salary
            low = target_net
            high = target_net * Decimal('2.0')
            tolerance = Decimal('0.01')
            max_iter = 100
            result = Decimal('0.0')

            for _ in range(max_iter):
                guess = (low + high) / 2
                insurance_salary = min(guess, Decimal('14500'))
                insurance = insurance_salary * Decimal('0.11')
                martyrs_tax = guess * Decimal('0.0005')

                gross_annual = guess * Decimal('12')
                insurance_annual = insurance * Decimal('12')
                taxable_annual = gross_annual - insurance_annual - Decimal('20000')
                taxable_annual = max(taxable_annual, Decimal('0.0'))

                tax_annual = contract.compute_annual_tax(taxable_annual)
                tax_monthly = tax_annual / Decimal('12')

                net = guess - insurance - tax_monthly - martyrs_tax

                if abs(net - target_net) <= tolerance:
                    result = guess
                    break

                if net < target_net:
                    low = guess
                else:
                    high = guess

            contract.net_salary = float(net_salary)
            contract.gross_salary = float(result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
