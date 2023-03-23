SELECT c.name
FROM customers c
INNER JOIN legal_person lp ON c.id = lp.id_customers
WHERE lp.cnpj IS NOT NULL;