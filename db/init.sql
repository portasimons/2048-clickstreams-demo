CREATE TABLE default.user_events (
	user_name String,
	event_type LowCardinality(String),
	event_time DateTime64(3, 'UTC'),
	user_address IPv4,
	is_mobile Boolean
)
ENGINE = MergeTree
ORDER BY (event_type, user_name, event_time);

CREATE TABLE default.personal_records (
	user_name String,
	event_time DateTime64(3, 'UTC'),
	score UInt32 
)
ENGINE = ReplacingMergeTree(event_time)
ORDER BY (user_name);