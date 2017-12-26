* select task_result->'_audit'->'started_at' as start_time, all_details->'ecosystem' as ecosystem from worker_results cross join jsonb_array_elements(worker_results.task_result->'result') all_results cross join jsonb_array_elements(all_results->'details') all_details where worker='GraphAggregatorTask' and external_request_id='<req id>';

* select task_result->'_audit'->'started_at' as start_time from worker_results;

* select now() - '2017-12-26T06:21:43.921451Z';

* select EXTRACT(DAY FROM age(now(), '2017-12-22T06:21:43.921451Z')) <=7; returns true or false

* select task_result->'_audit'->'started_at' as start_time from worker_results where EXTRACT(DAY FROM age(now(), to_timestamp(task_result->'_audit'->>'started_at'))) <=7;

* select task_result->'_audit'->'started_at' as start_time from worker_results where EXTRACT(DAY FROM age(to_timestamp(task_result->'_audit'->>'started_at', 'YYYYMMDDD:H:M:S'))) <=7;

* select age(to_timestamp(task_result->'_audit'->>'started_at', 'YYYYMMDDD:H:M:S')) as start_time from worker_results;

* select age(to_timestamp(task_result->'_audit'->>'started_at', 'YYYYMMDDDTH:M:SZ')) as start_time from worker_results;

* select age(to_timestamp(task_result->'_audit'->>'started_at','YYYY-MM-DDThh24:mi:ss')) as start_time from worker_results;

* select task_result->'_audit'->'started_at' as start_time, all_details->'ecosystem' as ecosystem, all_details->'_resolved' as deps from worker_results cross join jsonb_array_elements(worker_results.task_result->'result') all_results cross join jsonb_array_elements(all_results->'details') all_details where worker='GraphAggregatorTask' and EXTRACT(DAY FROM age(to_timestamp(task_result->'_audit'->>'started_at','YYYY-MM-DDThh24:mi:ss'))) <=7
