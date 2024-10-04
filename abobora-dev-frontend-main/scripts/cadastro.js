const form = document.getElementById("form");
const dadosInvalidos = document.querySelectorAll('.dadoInvalido');
const inputDatas = document.querySelectorAll('.inputData');

const emailCadastro = document.getElementById("emailCadastro");
const nomeCadastro = document.getElementById("nomeCadastro");
const senhaCadastro = document.getElementById("passwordCadastro");

const regexEmail = /^[^\s]+@[^\s]+\.[^\s]+$/;
const regexName =  /^(?!\s*$).{5,60}$/;
const regexPassword = /^[A-Za-z0-9]{8,14}$/; 

function setError(index){
    dadosInvalidos[index].classList.add('showError');
    inputDatas[index].classList.add('redBorder');
}

function hideError(index){
    dadosInvalidos[index].classList.remove('showError');
    inputDatas[index].classList.remove('redBorder');
}

function emailValidate(){
    if (!regexEmail.test(emailCadastro.value)){
        setError(0);
        return true;
    } else{
        hideError(0);
        return false;
    }
}

function nameValidate(){
    if(!regexName.test(nomeCadastro.value)){
        setError(1);
        return true;
    } else{
        hideError(1);
        return false;
    }
}

function passwordValidate(){
    if(!regexPassword.test(senhaCadastro.value)){
        setError(2);
        return true;
    } else{
        hideError(2);
        return false;
    }
}

function registerValidate(){
    if(emailValidate || nameValidate || passwordValidate){
        return true;
    }
    else{
        return false;
    }
}

form.addEventListener('submit', function(event){
    if(emailValidate() || nameValidate() || passwordValidate()){
        event.preventDefault();
    }
}) 