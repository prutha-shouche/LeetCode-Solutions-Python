select id,
case
    when p_id is null then 'Root'
    when id not in (select distinct p_id from Tree where p_id is not null) then 'Leaf'
    else 'Inner'
end
as type
from Tree
order by id;


Explaination:
So here I am just trying to select:-

All points where there is no parent as 'Root'
Points whose id is not there in the parent id column, which means they are not parent to any other point as 'Leaf'
Rest of the points must be 'Inner'
Since all the inputs are valid trees, not having any other conditions
