-- Lists all shows in that have at least one genre linked.
-- order: ascending
SELECT
    s.`title`,
    g.`genre_id`
FROM
    `tv_shows` AS s
    INNER JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
ORDER BY
    s.`title`,
    g.`genre_id`;