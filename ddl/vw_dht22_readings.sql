CREATE 
VIEW `vw_dht22_readings` AS
    select 
        cast((`sensor_readings`.`reading_ts` + interval 3 hour)
            as date) AS `reading_date`,
        date_format((`sensor_readings`.`reading_ts` + interval 3 hour),
                '%Y-%m-%d %H:%i') AS `reading_ts`,
        avg((case `sensor_readings`.`sensor_type`
            when 'temp_air' then `sensor_readings`.`sensor_value`
        end)) AS `air_temp_value`,
        avg((case `sensor_readings`.`sensor_type`
            when 'humidity' then `sensor_readings`.`sensor_value`
        end)) AS `humidity_value`
    from
        `sensor_readings`
    where
        (`sensor_readings`.`sensor_value` > 10)
    group by date_format((`sensor_readings`.`reading_ts` + interval 3 hour), /* adjust to eastern time */ 
            '%Y-%m-%d %H:%i')
    order by 1