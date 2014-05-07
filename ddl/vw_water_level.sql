create view vw_water_level 
as
select * from sensor_readings 
where id = 
(select max(id) 
from sensor_readings 
where sensor_type = 'water_level')