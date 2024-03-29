select
    name as type,
    case
        when type = 'A' then 20.0
        when type = 'B' then 70.0
        when type = 'C' then 530.5 end
    as price
from products
order by products.type, id desc;