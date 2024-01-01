function h_deposit() {
  var input_value=document.getElementById("deposit").value;

  var con_I_value = con_number(input_value);
  var deposit_amount=document.getElementById("deposit_amount").innerText;

  var con_D_value = con_number(deposit_amount);
  var sum = con_D_value + con_I_value;
  
  document.getElementById("deposit_amount").innerText = sum;

  var t_amount =document.getElementById("total_amount").innerText;
  var con_T_value = con_number(t_amount);

  var totalsum =con_I_value + con_T_value;

  document.getElementById("total_amount").innerText = totalsum;

  document.getElementById("deposit").value = "";
}

function con_number(value) {
  return parseFloat (value);
};

function h_withdraw() {
  var w_value=document.getElementById("withdraw").value;

  var con_I_val = con_number(w_value);

  var withdraw_amount=document.getElementById("withdraw_amount").innerText;

  var con_D_val = con_number(withdraw_amount);

  var sum2 = con_D_val + con_I_val;
  
  document.getElementById("withdraw_amount").innerText = sum2;

  var to_amount =document.getElementById("total_amount").innerText;
  var con_T_value = con_number(to_amount);

  var totalsu =con_T_value - con_I_val;

  document.getElementById("total_amount").innerText = totalsu;

  document.getElementById("withdraw").value = "";

};