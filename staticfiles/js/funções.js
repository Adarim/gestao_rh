
function mostraimg(el, el2, el3) {
        console.log(el, el2);
        var ver = document.getElementById(el3);
        var img= document.getElementById(el);
        if(el2 == 'fecha') {
            ver.style.visibility='hidden';
            ver.style.height=0;
        } else {
            img.src=el2;
            ver.style.visibility='visible';
            ver.style.height='370px';
        }
    }

function mensag(el) {
        window.alert(el);
    }


function utilHE(id) {
        console.log(id);
        token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        var ver = document.getElementById('he');
        var ver2 = document.getElementById('he2');
        $.ajax({
                type: 'POST',
                    url: '/horas-extras/utilizouHE/' + id + '/',
                data:  {
                    csrfmiddlewaretoken:  token
                },
                success: function(result) {
                console.log(result);
                ver.style.visibility='visible';
                ver2.style.visibility='visible';
                $("#mensagem").text(result.mensagem);
                $("#horatu").text(result.horas);
                }
        });
}

function Nao_utilHE(id) {
        console.log(id);
        token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        var ver = document.getElementById('he');
        var ver2 = document.getElementById('he2');
        $.ajax({
                type: 'POST',
                    url: '/horas-extras/naoutilizouHE/' + id + '/',
                data:  {
                    csrfmiddlewaretoken:  token
                },
                success: function(result) {
                console.log(result);
                ver.style.visibility='visible';
                ver2.style.visibility='visible';
                $("#mensagem").text(result.mensagem);
                $("#horatu").text(result.horas);
                }
        });
}


function apaga(id,wurl,tit,wtit){

bootbox.confirm({
  message: 'Confirma a Exclusão do ' + tit + ':  '  + wtit +'?',
  callback: function(confirmacao){

    if (confirmacao) {
             $.ajax({
           url: wurl + id + '/',
//           type: "POST",
//           data: id,
////            success: function(result) {
////            $("#ID").text(result.id);
////            }
            });
         bootbox.alert(tit + ' excluído com sucesso.');
         location.reload ();}
    else
      bootbox.alert('Operação cancelada.');

  },
  buttons: {
    cancel: {label: 'Cancelar',className:'btn-default'},
    confirm: {label: 'EXCLUIR',className:'btn-danger'}

  }
});
}

function utiliza(id,wurl,tit,wtit){
let  mens =  'Confirma a Liberação do ' + tit + ':  '  + wtit +'?'
let  mens2 = 'LIBERAR HORAS'
if( wurl == '/horas-extras/marca/' ){
mens =  'Confirma a Utilização do ' + tit + ':  '  + wtit +'?';
mens2 = 'UTILIZAR HORAS';
}
bootbox.confirm({  message: mens ,
  callback: function(confirmacao){

    if (confirmacao) {
             $.ajax({
           url: wurl + id + '/',
//           type: "POST",
//           data: id,
////            success: function(result) {
////            $("#ID").text(result.id);
////            }
            });
//      bootbox.alert(tit + ' excluído com sucesso.');
      }
    else
      bootbox.alert('Operação cancelada.');
      location.reload ();
  },
  buttons: {
    cancel: {label: 'Cancelar',className:'btn-default'},
    confirm: {label: mens2,className:'btn-danger'}
  }
});
}





(function(win,doc){
        'use strict';

        if(doc.querySelector('.btnDel')){
            let btnDel = doc.querySelectorAll('.btnDel');
            for(let i=0; i < btnDel.length; i++){
                btnDel[i].addEventListener('click', function(event){
                 if(bootbox.confirm('Deseja Excluir o Registro de Hora-Extra?')){
                  bootbox.alert('Registro de Hora-Extra excluído com sucesso.');
                  return True;
                 }else{
                        event.preventDefault();
                        }

                })
            }
        }
}
)

$(function(){
    $('.mask-fone').mask('(00) 00000-0000');
});
