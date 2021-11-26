var fs=require('fs');
var data=fs.readFileSync('materias.json', 'utf8');
var words=JSON.parse(data);
var materias = words.filter((x) =>  x.situacao === 'A cursar' & x.carga_horaria === 60 );

materias.forEach(f => {
    console.log(f.nome_disciplina);
});

