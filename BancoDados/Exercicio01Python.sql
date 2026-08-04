create database loja;

use loja;

create table produtos(
	id int auto_increment primary key,
    nome varchar(100) not null,
    preco decimal(10,2) not null,
    quantidade int,
    categoria varchar(50)
    );
    
    insert into produtos(nome, preco, quantidade, categoria) values
    ('Celular', '2500.00', 10, 'Eletrônico'),
    ('Computador', '5000.00', 20, 'Eletrônico'),
    ('Banana', '2.99', 50, 'Alimentos'),
    ('Feijão', '5.99', 10, 'Alimentos'),
    ('Camiseta', '69.99', 50, 'Vestuário');
    
    select * from produtos;
    
    -- Select com filtro
    select nome, preco from produtos;
    
	-- Filtro where
    select * from produtos
    where categoria = 'Eletrônico';
    
    select * from produtos
    where preco < 100;
    
    select * from produtos
    where quantidade < 0;
    
    -- Busca com like
    select * from produtos where nome like 'C%';
    select * from produtos where nome like '%dor';
    select * from produtos where nome like '%eij%';
    
    select * from produtos where categoria = 'Eletrônico' and preco < 3000;
    select * from produtos where categoria = 'Eletrônico' or preco < 5;
    
    -- Ordenando 
    select nome, preco from produtos
    order by preco; -- Crescente
    
    select nome,preco from produtos
    order by preco desc
    limit 3;
    
    select count(*) from produtos;
    select avg(preco) from produtos;
    select max(preco), min(preco) from produtos;
    select sum(preco*quantidade) from produtos;
    
    select * from produtos 
    where categoria = 'Vestuario';
    
    select nome, preco from produtos
    where preco > 50;
    
    select * from produtos
	where preco between 20 and 2600;
    
    select * from produtos 
    where nome like '%r';
    
    select * from produtos
    order by preco desc;
    
    
    select * from produtos 
    order by preco
    limit 2;
    
    -- Update e Delete
    update produtos
    set preco = 3000.00
    where id = 1;
    
    update produtos
    set quantidade = quantidade - 10
    where id = 2;
    
    set sql_safe_updates = 0;
    
    update produtos
    set preco = preco * 0.85
    where categoria = 'Eletrônico';
    
    update produtos
    set quantidade = quantidade + 10
    where quantidade < 20;
    
    delete from produtos
    where id = 5;
    
    insert into produtos(nome, preco, quantidade, categoria) values
    ('Camisetas', '69.99', 0, 'Vestuário');
    
    delete from produtos
    where quantidade = 0;
    
    select * from produtos;