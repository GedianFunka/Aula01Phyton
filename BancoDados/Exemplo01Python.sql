create database escolas1;

use escolas1;

create table alunos(
	id int primary key auto_increment,
	nome varchar(100) not null,
    turma varchar(20),
    nota decimal(4,2)
    );
    
insert into alunos (nome, turma, nota) values 
('Gedian', '3ADS', 9.99),
('Kauã', '2ADS', 9.69),
('Weslley', '1ADS', 9.24);

select * from alunos;   

drop table if exists alunos;
