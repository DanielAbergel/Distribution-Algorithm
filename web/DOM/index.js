var namesArr=[];
var itemsArr=[];

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

}

function insertItems(){
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
  container.innerHTML="<h1>step4:</h1><h2>Every participant has to evaluate his interest of every item by dollars</h2>";
  for (i=0;i<numOFpeople;i++){
    for(var j=0;j<itemsArr.length;++j){
      // slider();
      slider(namesArr[i],itemsArr[j]);
      // slider("ayelet");
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
document.getElementById("rescaleBtn").style.display="none";
  var sumOfNamesRates;
  for (i=0;i<namesArr.length;i++){
    sumOfNamesRates=0;
    for (j=0;j<itemsArr.length;j++){
      sumOfNamesRates+=parseInt(document.getElementById('output'+namesArr[i]+itemsArr[j]).value);

    }
    for (j=0;j<itemsArr.length;j++){
      document.getElementById('output'+namesArr[i]+itemsArr[j]).value=""+ Math.round((parseInt(document.getElementById('input'+namesArr[i]+itemsArr[j]).value)/sumOfNamesRates)*100)+"$";
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

}

function algoChoser(){
  document.getElementById("container").style.display="none";
  document.getElementById("lastStepBtn").style.display="none";
  document.getElementById("radio-btn").style.display="inline";
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
  label.innerHTML = name+" rate for "+item;
  label.classList.add("label");

  var form=document.createElement("form");
  form.name="registrationForm";
  form.className ="mainForm";
  form.style.border = "thin solid #000000";
  form.style.margin="10px";
  form.style.marginLeft ="200px";
  form.style.marginRight ="200px";

  var input = document.createElement("input");
  input.type="range";
  input.name="ageInputName";
  input.id="input"+name+item;
  input.value="50";
  input.min="0";
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
  output.value="50$";
  document.getElementById("container").appendChild(form);

}
function updateTextInput(inputId,outputId){
  // console.log("aaa");
  var val= document.getElementById(inputId).value;
  console.log(val);
  var x =document.getElementById(outputId);
  x.value=val+"$";
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

  json=JSON.stringify({"values":mat,"problem": document.getElementById("alg2").checked ? "EnvyFree" : "Proportional","agents":namesArr,"items":itemsArr,"num_of_agents":mat.length,"num_of_items":mat[0].length});

  // console.log(json);
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
  console.log(document.getElementById("alg2").checked);//alg1=false.  alg2=true
  document.getElementById("table-div").style.display="inline";
  var ResultTable=document.getElementById("results-table");
  for (var i = 0; i <namesArr.length; i++) {
    var row = ResultTable.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = namesArr[i];
    var itemsStr="";
    for (var j = 0; j < mat[i].length; j++) {
      itemsStr+=Math.round(parseInt(mat_result[i][j]))+"% of the "+itemsArr[j]+"<br>";
    }
    cell2.innerHTML = itemsStr;
  }
var participantActual;// the actual sum of his profit.
var participantRational;//how much the participant had to get if we split equally.
var ExplenationTable=document.getElementById("explenation-table");
  for (i = 0; i <namesArr.length; i++) {
    participantActual=0;
    participantRational=0;
    for (var k = 0; k < mat_result[i].length; k++) {
      participantActual+=((mat_result[i][k]/100)*parseInt(mat[i][k]));
      participantRational+=mat[i][k];
    }
    var row1 = ExplenationTable.insertRow();
    var cell = row1.insertCell(0);
    // var cell2 = row.insertCell(1);
    cell.innerHTML = namesArr[i]+": The total value of the items you received, according to your evaluation, is "+ participantActual +"$. This is at least 1/"+namesArr.length+" of the total value of your rates which is "+(participantRational/namesArr.length);
  }
}


// function transpose(a) {
//
//   // Calculate the width and height of the Array
//   var w = a.length || 0;
//   var h = a[0] instanceof Array ? a[0].length : 0;
//
//   // In case it is a zero matrix, no transpose routine needed.
//   if(h === 0 || w === 0) { return []; }
//
//   /**
//   * @var {Number} i Counter
//   * @var {Number} j Counter
//   * @var {Array} t Transposed data is stored in this array.
//   */
//   var i, j, t = [];
//
//   // Loop through every item in the outer array (height)
//   for(i=0; i<h; i++) {
//
//     // Insert a new row (array)
//     t[i] = [];
//
//     // Loop through every item per item in outer array (width)
//     for(j=0; j<w; j++) {
//
//       // Save transposed data.
//       t[i][j] = a[j][i];
//     }
//   }
//
//   return t;
// }
