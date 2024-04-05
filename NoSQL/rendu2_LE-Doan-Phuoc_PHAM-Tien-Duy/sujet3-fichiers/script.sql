.mode csv

DROP TABLE IF EXISTS twitter_network;

CREATE TABLE twitter_network (
    followed INTEGER NOT NULL,
    follower INTEGER NOT NULL
);

.import social_network.csv twitter_network

.schema twitter_network

SELECT 'nb total de relations friend/follower: ' || COUNT(*) AS total_relations FROM twitter_network;

SELECT 'nb users qui ont au moins un follower: ' || COUNT(DISTINCT followed) AS users_with_followers FROM twitter_network;

SELECT 'nb utilisateurs qui suivent au moins qqn: ' || COUNT(DISTINCT follower) AS users_followings FROM twitter_network;

SELECT 'nb max de followers per utilisateur : ' || MAX(followers_count) || ' -- exemple utilisateur avec nb max de followers : ' || user_id 
FROM (SELECT followed AS user_id, COUNT(*) AS followers_count FROM twitter_network GROUP BY followed) ORDER BY followers_count DESC LIMIT 1;

SELECT 'nb min de followers per utilisateur : ' || MIN(followers_count) || ' -- exemple utilisateur avec min de followers : ' || user_id 
FROM (SELECT followed AS user_id, COUNT(*) AS followers_count FROM twitter_network GROUP BY followed) ORDER BY followers_count ASC LIMIT 1;