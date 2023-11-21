-- list all records of the table having a name value.
-- order: descending
SELECT
    `score`,
    `name`
FROM
    `second_table`
WHERE
    `name` != ""
ORDER BY
    `score` DESC