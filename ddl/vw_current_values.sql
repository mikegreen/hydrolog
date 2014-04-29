CREATE 
VIEW `vw_current_values` AS
    select 
        `sensor_readings`.`sensor_type` AS `sensor_type`,
        `sensor_readings`.`sensor_value` AS `sensor_value`,
        `sensor_readings`.`reading_ts` AS `reading_ts`
    from
        `sensor_readings`
    order by `sensor_readings`.`id` desc
    limit 4 /* this is to get only the latest insert assuming 4 sensors, will need updating as add/remove sensors */
    /* need to find a better way, I know */