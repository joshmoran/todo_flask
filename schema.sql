drop table if exists pending_tasks;
pending_tasks
create table pending_tasks (
  id integer primary key autoincrement unique,
  name text not null,
  priority varchar(6) not null,
  due_time time not null,
  due_date date not null
);

drop table if exists completed_tasks;

create table completed_tasks (
  id integer primary key autoincrement unique,
  name text not null,
  priority varchar(6) not null,
  due_time time not null,
  due_date date not null
);

--  Values for Tasks
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Feed Cats', 'HIGH', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Clean the house', 'LOW', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Do a wash load', 'MEDIUM','2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Potatoes', 'HIGH', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Milk', 'MEDIUM', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Bread', 'LOW', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Complete Assignment', 'HIGH', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Create a Health and Safety Poster', 'MED', '2024-12-30', '12:05:32' );
insert into pending_tasks ( name, priority, due_date, due_time ) values ( 'Work', 'LOW', '2024-12-30', '12:05:32'  );

-- Vales for Lists 
insert into lists ( name ) values ( 'default'), ('shopping' ), ( 'work' );

-- Values for time_refer
insert into time_refer ( date, time, task_id, list_id ) values ( , 1, 1 );
insert into time_refer ( date, time, task_id, list_id ) values ( , 2, 1 );
insert into time_refer ( date, time, task_id, list_id ) values ( , 3, 1 );
insert into time_refer ( date, time, task_id, list_id ) values ( , 1, 2 );
insert into time_refer ( date, time, task_id, list_id ) values ( , 2, 2 );
insert into time_refer ( date, time, task_id, list_id ) values ( '2024-12-30', '12:05:32', 3, 2 );
insert into time_refer ( date, time, task_id, list_id ) values ( '2024-12-30', '12:05:32', 1, 3 );
insert into time_refer ( date, time, task_id, list_id ) values ( '2024-12-30', '12:05:32', 2, 3 );
insert into time_refer ( date, time, task_id, list_id ) values ( '2024-12-30', '12:05:32', 3, 3 );


 "select * from time_refer where list_id = 1 full outer join tasks on time_refer.tasks_id = tasks.id and  full outer join lists on time_refer.list_id = lists.list_id 


 select * from time_refer  full join tasks on time_refer.task_id = tasks.id full outer join lists on time_refer.list_id = lists.list_id where time_refer.list_id = 1;