var namesArr=[];
var itemsArr=[];
var emailCheck=false;
function addS(){
  var peopleOPT = document.getElementById("peopleSelect");
  var itemOPT = document.getElementById("itemSelect");
  for (var i = 2; i <= 4; i++) {
    var pOption = document.createElement("option");
    pOption.text = i;
    peopleOPT.add(pOption);
  }

  for (var j = 1; j <= 18; j++) {
    var iOption = document.createElement("option");
    iOption.text = j;
    itemOPT.add(iOption);
  }

  var selectBtn = document.createElement("BUTTON");
  selectBtn.id="selectBtn";
  selectBtn.innerHTML = "MOVE TO STEP 2";
  selectBtn.onclick=insertNames;
  selectBtn.classList.add("btn-secondary");
  selectBtn.classList.add("btn");
  selectBtn.classList.add("myButtons");

  document.body.appendChild(selectBtn);

}

function insertNames(){
  var defaultNames=["Alice","Bob","Carol","Dave"];
  document.getElementById("selectStep").style.display="none";
  document.getElementById("selectBtn").style.display="none";
  // var check = document.getElementById("rescaleBtn");
  // if(check){
  //
  // }

  var numOFpeople=document.getElementById("peopleSelect").value;
  var divP = document.createElement("div");
  divP.id="divP";
  divP.innerHTML="<h1>step2:</h1><h2>Insert the participants names</h2>";
  for (i=1;i<=numOFpeople;i++){
    var divPpart = document.createElement("div");
    divPpart.classList.add("input-style");
    divPpart.appendChild(document.createTextNode("Name number "+i));
    var nameInput = document.createElement("input");
    nameInput.id = "name"+i;
    nameInput.value=defaultNames[i-1];
    divPpart.appendChild(nameInput);
    divP.appendChild(divPpart);
    divP.appendChild(document.createElement("br"));
  }



  var insertNamesBtn = document.createElement("BUTTON");
  insertNamesBtn.id="insertNamesBtn";
  insertNamesBtn.innerHTML = "MOVE TO STEP 3";
  insertNamesBtn.onclick=insertItems;
  insertNamesBtn.classList.add("btn-secondary");
  insertNamesBtn.classList.add("btn");
  insertNamesBtn.classList.add("myButtons");
  container.appendChild(divP);
  // document.getElementById("divP").innerHTML="<h1>step2:</h1><h2>Insert the participants names</h2>";
  // var text2=
  document.body.appendChild(insertNamesBtn);

  var numberOFpeople=document.getElementById("peopleSelect").value;
  if(numberOFpeople=="4"){
    insertEmail();
    return;
  }

}
function insertEmail(){
  emailCheck=true;
  document.getElementById("divP").style.display="none";
  document.getElementById("insertNamesBtn").style.display="none";
  document.getElementById("emailId").style.display="inline";

  var insertNamesBtn = document.createElement("BUTTON");
  insertNamesBtn.id="mailBtn";
  insertNamesBtn.innerHTML = "MOVE TO STEP 2";
  insertNamesBtn.onclick=insertItems;
  insertNamesBtn.classList.add("btn-secondary");
  insertNamesBtn.classList.add("btn");
  insertNamesBtn.classList.add("myButtons");
  // container.appendChild(divP);
  // document.getElementById("divP").innerHTML="<h1>step2:</h1><h2>Insert the participants names</h2>";
  // var text2=
  document.getElementById("emailId").appendChild(insertNamesBtn);
}
function insertItems(){
  var check = document.getElementById("emailId");
  if(check){
  if(document.getElementById("emailInput").value==""&&emailCheck){
    alert("You have to fill all of the fields");
    return false;
  }
  document.getElementById("emailId").style.display="none";
}
  var numOFpeople=document.getElementById("peopleSelect").value;
  for (var i = 1; i <= numOFpeople; i++) {
    if(document.getElementById("name"+i).value==""){
      alert("You have to fill all of the fields");
      return false;
    }
    namesArr.push(document.getElementById("name"+i).value);
  }
  defaultItems=["Armchair","Bed","Chair","Desk","Easy chair","Futon","Game table","Hammock","Iron","Jeep","Kitchen island","Lamp","Mattress","Nightstand","Office chair","Pillow","Quill","Rug"];
  document.getElementById("divP").style.display="none";
  document.getElementById("insertNamesBtn").style.display="none";
  var numOFitems=document.getElementById("itemSelect").value;
  var divI = document.createElement("div");
  divI.id="divI";
  divI.innerHTML="<h1>step3:</h1><h2>Insert the items names</h2>";
  for (i=1;i<=numOFitems;i++){
    var divIpart = document.createElement("div");
    divIpart.classList.add("input-style");
    divIpart.appendChild(document.createTextNode("Item number "+i));
    var itemInput = document.createElement("input");
    itemInput.id = "item"+i;
    itemInput.value=defaultItems[i-1];
    divIpart.appendChild(itemInput);
    divI.appendChild(divIpart);
    divI.appendChild(document.createElement("br"));
  }
  var insertItemsBtn = document.createElement("BUTTON");
  insertItemsBtn.id="insertItemsBtn";
  insertItemsBtn.innerHTML = "MOVE TO STEP 4";
  insertItemsBtn.onclick=getDetails;
  insertItemsBtn.classList.add("btn-secondary");
  insertItemsBtn.classList.add("btn");
  insertItemsBtn.classList.add("myButtons");
  container.appendChild(divI);
  document.body.appendChild(insertItemsBtn);


}
function getDetails() {

  var numOFpeople=document.getElementById("peopleSelect").value;
  var numOFitems=document.getElementById("itemSelect").value;

  for (var j = 1; j <= numOFitems; j++) {
    if(document.getElementById("item"+j).value==""){
      alert("You have to fill all of the fields");
      return false;
    }
    itemsArr.push(document.getElementById("item"+j).value);
  }
  document.getElementById("insertItemsBtn").style.display="none";
  addFields();
}

function addFields(){
  // Number of inputs to create
  var numOFpeople = namesArr.length;
  var numOFitems = itemsArr.length;
  // Container <div> where dynamic content will be placed
  var container = document.getElementById("container");
  // Clear previous contents of the container
  while (container.hasChildNodes()) {
    container.removeChild(container.lastChild);
  }
  container.innerHTML="<h1>step4:</h1><h2>You got 1200 points. Split them between the items as you wish.</h2>";
  for (i=0;i<numOFpeople;i++){
    var personDiv= document.createElement("div");
    personDiv.id=namesArr[i]+"div";
    personDiv.style.margin = "10px";
    var label=document.createElement("label");
    label.innerHTML = namesArr[i]+"'s rates";
    personDiv.style.border = "thin solid #000000";
    container.appendChild(personDiv);
    personDiv.appendChild(label);



    for(var j=0;j<itemsArr.length;++j){
      slider(namesArr[i],itemsArr[j]);
      // slider(namesArr[i],itemsArr[j]);
    }

  }
  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "rescale";                   // Insert text
  btn.id="rescaleBtn";
  btn.classList.add("btn-secondary");
  btn.classList.add("btn");
  btn.classList.add("myButtons");
  document.body.appendChild(btn);
  document.getElementById("rescaleBtn").onclick = rescale;
}

function rescale(){
  deleteBtn();

  var sumOfNamesRates;
  for (i=0;i<namesArr.length;i++){
    sumOfNamesRates=0;
    for (j=0;j<itemsArr.length;j++){
      sumOfNamesRates+=parseInt(document.getElementById('output'+namesArr[i]+itemsArr[j]).value);

    }
    for (j=0;j<itemsArr.length;j++){
      document.getElementById('output'+namesArr[i]+itemsArr[j]).value=""+ Math.round((parseInt(document.getElementById('input'+namesArr[i]+itemsArr[j]).value)/sumOfNamesRates)*100)+" points";
      document.getElementById('input'+namesArr[i]+itemsArr[j]).value=""+ Math.round((parseInt(document.getElementById('input'+namesArr[i]+itemsArr[j]).value)/sumOfNamesRates)*100);
      document.getElementById('input'+namesArr[i]+itemsArr[j]).disabled = true;
    }
  }
  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "LAST STEP";                   // Insert text
  btn.id="lastStepBtn";
  btn.classList.add("btn-secondary");
  btn.classList.add("btn");
  btn.classList.add("myButtons");
  // btn.marginTop="0px";
  document.body.appendChild(btn);
  document.getElementById("lastStepBtn").onclick = algoChoser;

  var btn_again = document.createElement("BUTTON");   // Create a <button> element
  btn_again.innerHTML = "rate again";                   // Insert text
  btn_again.id="rate-again";
  btn_again.classList.add("btn-secondary");
  btn_again.classList.add("btn");
  btn_again.classList.add("myButtons");

  // btn.marginTop="0px";
  document.body.appendChild(btn_again);
  document.getElementById("rate-again").onclick = rateAgain;

}
function rateAgain(){

  deleteBtn();
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      document.getElementById('input'+namesArr[i]+itemsArr[j]).disabled = false;
    }
  }

  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "rescale";                   // Insert text
  btn.id="rescaleBtn2";
  btn.classList.add("btn-secondary");
  btn.classList.add("btn");
  btn.classList.add("myButtons");
  document.body.appendChild(btn);
  document.getElementById("rescaleBtn2").onclick = rescale;
}

function algoChoser(){
  document.getElementById("container").style.display="none";
  document.getElementById("lastStepBtn").style.display="none";
  document.getElementById("rate-again").style.display="none";
  document.getElementById("radio-btn").style.display="inline";
  deleteBtn();
  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "SEND";                   // Insert text
  btn.id="sendBtn";
  btn.style.marginTop = "50px";
  btn.classList.add("btn-secondary");
  btn.classList.add("btn");
  btn.classList.add("myButtons");
  document.body.appendChild(btn);
  document.getElementById("sendBtn").onclick = setMat;
}

function slider(name,item){
  var label=document.createElement("label");
  label.innerHTML = item+"'s rate";
  label.classList.add("label");

  var form=document.createElement("form");
  form.name="registrationForm";
  form.className ="mainForm";
  form.style.margin="10px";
  form.style.marginLeft ="150px";
  form.style.marginRight ="150px";

  var input = document.createElement("input");
  input.type="range";
  input.name="ageInputName";
  input.id="input"+name+item;
  // input.value="600";
  input.min="0";
  input.max="1200";
  input.defaultValue="600";
  input.style.marginTop = "5px";
  input.classList.add('input');

  var output = document.createElement("output");
  output.name="ageOutputName";
  output.id="output"+name+item;
  output.classList.add('output');

  input.oninput=()=>updateTextInput(input.id,output.id);

  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(output);
  output.value="600 points";
  document.getElementById(name+"div").appendChild(form);

}
function updateTextInput(inputId,outputId){
  // console.log("aaa");
  var val= document.getElementById(inputId).value;
  console.log(val);
  var x =document.getElementById(outputId);
  x.value=val+" points";
}

function setMat(){
  document.getElementById("radio-btn").style.display="none";
  document.getElementById("sendBtn").style.display="none";
  var mat=new Array(namesArr.length);
  for(var i=0;i<namesArr.length;++i){
    mat[i]=new Array(itemsArr.length);
  }
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      mat[i][j]=parseInt(document.getElementById('input'+namesArr[i]+itemsArr[j]).value);
    }
  }
  email=document.getElementById(emailInput).value;
  json=JSON.stringify({"values":mat,"problem": document.getElementById("alg2").checked ? "EnvyFree" : "Proportional","agents":namesArr,"items":itemsArr,"num_of_agents":mat.length,"num_of_items":mat[0].length , "email": email });

  var loader =document.createElement("div");
  loader.id="loaderId";
  loader.classList.add("loader");
document.body.appendChild(loader);

 // result(mat,mat);
  console.log(json);
  var xhr = new XMLHttpRequest();
  var url = "http://161.35.20.108/calculator";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var responseText = JSON.parse(xhr.responseText);
      var mat_result = responseText.values;
      for (i=0;i<mat_result.length;i++){
        for (j=0;j<mat_result[0].length;j++){
          mat_result[i][j] = mat_result[i][j] * 100 ;
        }
      }
      console.log(mat_result);
      result(mat_result,mat);
    }
  };
  var data = json;
  xhr.send(data);
}

function convertTOjson(mat){
  var json="{";
  for(i=0;i<mat.length;++i){
    json+=i+": [";
    for(j=0;j<mat[0].length;++j){
      json+=mat[i][j]+",";
    }
    json+="],";
  }
  json+="num_of_agents: "+mat.length+",num_of_items: "+mat[0].length+"}";
  return json;
}
/////////////////////////////////////////////////////////////////

// function showChart(mat){
//   // mat=transpose(mat);
//   result(mat);
// }

function result(mat_result,mat){
  // console.log(document.getElementById("meh").checked);
  document.getElementById("loaderId").style.display="none";
  console.log(document.getElementById("alg2").checked);//alg1=false.  alg2=true
  document.getElementById("table-div").style.display="inline";
  var ResultTable=document.getElementById("results-table");
  var thead = ResultTable.createTHead();
  let row = thead.insertRow();
  let th = document.createElement("th");
  let text = document.createTextNode("Items");
  th.appendChild(text);
  row.appendChild(th);
  // var i;
  for ( let i = 0; i <namesArr.length; i++) {
     th = document.createElement("th");
     text = document.createTextNode(namesArr[i]);
    th.appendChild(text);
    row.appendChild(th);
  }


  for ( let i = 0; i < itemsArr.length; i++) {
    let row = thead.insertRow();
    let th = document.createElement("th");
    let text = document.createTextNode(itemsArr[i]);
   th.appendChild(text);
   row.appendChild(th);
    for (let j = 0; j < namesArr.length; j++) {
      let th = document.createElement("th");
      let text = document.createTextNode(mat_result[j][i]);
     th.appendChild(text);
     row.appendChild(th);
    }
  }


  // var row = ResultTable.insertRow();
  // var cell1 = row.insertCell(0);
  // cell1.innerHTML = "Name";
  //  for (var i = 0; i <namesArr.length; i++) {
  //    cell1.innerHTML = namesArr[i];
  //    ResultTable.appendChild(cell1);
  //  }
  //   var row = ResultTable.insertRow();
  //   var cell1 = row.insertCell(0);
  //   var cell2 = row.insertCell(1);
  //   cell1.innerHTML = namesArr[i];
  //   var itemsStr="";
  //   for (var j = 0; j < mat[i].length; j++) {
  //     itemsStr+=Math.round(parseInt(mat_result[i][j]))+"% of the "+itemsArr[j]+"<br>";
  //   }
  //   cell2.innerHTML = itemsStr;
  // }



  // var participantActual;// the actual sum of his profit.
  // var participantRational;//how much the participant had to get if we split equally.
  // var ExplenationTable=document.getElementById("explenation-table");
  // for (i = 0; i <namesArr.length; i++) {
  //   participantActual=0;
  //   participantRational=0;
  //   for (var k = 0; k < mat_result[i].length; k++) {
  //     participantActual+=((mat_result[i][k]/100)*parseInt(mat[i][k]));
  //     participantRational+=mat[i][k];
  //   }
  //   var row1 = ExplenationTable.insertRow();
  //   var cell = row1.insertCell(0);
  //   // var cell2 = row.insertCell(1);
  //   cell.innerHTML = namesArr[i]+": The total value of the items you received, according to your evaluation, is "+ participantActual +" points. This is at least 1/"+namesArr.length+" of the total value of your rates which is "+(participantRational/namesArr.length);
  // }
}


function deleteBtn(){
  var element;
  var check = document.getElementById("rescaleBtn");
  if(check){
    element = document.getElementById("rescaleBtn");
    element.parentNode.removeChild(element);
  }
  check = document.getElementById("lastStepBtn");
  if(check){
    element = document.getElementById("lastStepBtn");
    element.parentNode.removeChild(element);
  }
  check = document.getElementById("rate-again");
  if(check){
    element = document.getElementById("rate-again");
    element.parentNode.removeChild(element);
  }
  check = document.getElementById("rescaleBtn2");
  if(check){
    element = document.getElementById("rescaleBtn2");
    element.parentNode.removeChild(element);
  }
}
