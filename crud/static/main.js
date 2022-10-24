(function(win,doc){
    'use strict';

    if(doc.querySelector('.btnDeletar')){
        let btnDeletar = doc.querySelectorAll('.btnDeletar');
        for(let i=0; i < btnDeletar.length; i++){
            btnDeletar[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este contato?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    alert('Operação realizada com sucesso!');
                    result.classList.add('alert');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);