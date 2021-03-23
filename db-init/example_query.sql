SELECT v.make,
    c.name,
    q.question
FROM vehicle v
    JOIN category c ON v.category = c.id
    JOIN category_question cq ON cq.category = c.id
    JOIN question q ON cq.question = q.id
WHERE v.id = 1