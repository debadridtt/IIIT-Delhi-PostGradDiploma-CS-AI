-- 2a.

select a.Gender, count(a.Gender) as count from (select * from Passenger where Distance >= 600) a group by a.Gender;

-- 2b.

select min(Price) from Price where Bus_Type = 'Sleeper';

-- 2c.

select Passenger_name from Passenger where Passenger_name like 'S%';

-- 2d.

select p.Passenger_name, p.Boarding_City, p.Destination_City, p.Bus_Type, f.Price
from 
Passenger p
left join 
Price f
on p.Bus_type=f.Bus_type and p.Distance=f.Distance;

-- 2e.

select p.Passenger_name, f.Price 
from (select * from Passenger where Distance=1000 and Bus_Type='Sitting') p
left join
Price f
on p.Distance=f.Distance and p.Bus_Type=f.Bus_Type; 

-- 2f.

select Price 
from Price 
where 
Distance=(select Distance from Passenger where Boarding_City='Panaji' and Destination_City='Bengaluru');

-- 2g.

select distinct(Distance) from Passenger order by Distance desc;

-- 2h.

select Passenger_name, Distance*100/sum(Distance) over() as percent_distance_travel from Passenger;
