-- listall records in the table with a score >= 10
-- order: descending
SELECT
    `score`,
    `name`
FROM
    `second_table`
WHERE
    `score` >= 10
ORDER BY
    `score` DESC;