create table teachers (
    id serial primary key,
    name varchar(100) not null,
    expertise varchar(100) not null
);

create table courses (
    id serial primary key,
    name varchar(100) not null,
    hours int not null,
    teacher_id int,
    constraint fk_course_teacher foreign key (teacher_id) REFERENCES teachers (id)
);

