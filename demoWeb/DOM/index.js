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
  document.body.appendChild(selectBtn);

}

function insertNames(){
  document.getElementById("selectStep").style.display="none";
  document.getElementById("selectBtn").style.display="none";

  var numOFpeople=document.getElementById("peopleSelect").value;
  var divP = document.createElement("div");
  divP.id="divP";
  for (i=1;i<=numOFpeople;i++){
    var divPpart = document.createElement("div");
    divPpart.classList.add("input-style");
    divPpart.appendChild(document.createTextNode("Name number "+i));
    var nameInput = document.createElement("input");
    nameInput.id = "name"+i;
    divPpart.appendChild(nameInput);
    divP.appendChild(divPpart);
    divP.appendChild(document.createElement("br"));
  }

  var insertNamesBtn = document.createElement("BUTTON");
  insertNamesBtn.id="insertNamesBtn";
  insertNamesBtn.innerHTML = "MOVE TO STEP 3";
  insertNamesBtn.onclick=insertItems;
  container.appendChild(divP);
  document.body.appendChild(insertNamesBtn);

}

function insertItems(){
  var numOFpeople=document.getElementById("peopleSelect").value;
  for (var i = 1; i <= numOFpeople; i++) {
    namesArr.push(document.getElementById("name"+i).value);
  }
  document.getElementById("divP").style.display="none";
  document.getElementById("insertNamesBtn").style.display="none";
  var numOFitems=document.getElementById("itemSelect").value;
  var divI = document.createElement("div");
  divI.id="divI";

  for (i=1;i<=numOFitems;i++){
    var divIpart = document.createElement("div");
    divIpart.classList.add("input-style");
    divIpart.appendChild(document.createTextNode("Item number "+i));
    var itemInput = document.createElement("input");
    itemInput.id = "item"+i;
    divIpart.appendChild(itemInput);
    divI.appendChild(divIpart);
    divI.appendChild(document.createElement("br"));
  }
  var insertItemsBtn = document.createElement("BUTTON");
  insertItemsBtn.id="insertItemsBtn";
  insertItemsBtn.innerHTML = "MOVE TO STEP 4";
  insertItemsBtn.onclick=getDetails;
  container.appendChild(divI);
  document.body.appendChild(insertItemsBtn);


}
function getDetails() {
  document.getElementById("insertItemsBtn").style.display="none";
  var numOFpeople=document.getElementById("peopleSelect").value;
  var numOFitems=document.getElementById("itemSelect").value;

  for (var j = 1; j <= numOFitems; j++) {
    itemsArr.push(document.getElementById("item"+j).value);
  }
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
  for (i=0;i<numOFpeople;i++){
    for(var j=0;j<itemsArr.length;++j){
      // slider();
      slider(namesArr[i],itemsArr[j]);
      // slider("ayelet");
    }
  }
  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "LAST STEP";                   // Insert text
  btn.setAttribute("id", "btnId");
  document.body.appendChild(btn);
  document.getElementById("btnId").onclick = setMat;
}

function algoChoser(){
  
}

function slider(name,item){
  var label=document.createElement("label");
  label.innerHTML = name+" rate for "+item;
  label.classList.add("label");

  var form=document.createElement("form");
  form.name="registrationForm";
  form.className ="mainForm";

  var input = document.createElement("input");
  input.type="range";
  input.name="ageInputName";
  input.id="input"+name+item;
  input.value="50";
  input.min="0";
  input.classList.add('input');

  var output = document.createElement("output");
  output.name="ageOutputName";
  output.id="output"+name+item;
  output.classList.add('output');

  input.oninput=()=>updateTextInput(input.id,output.id);

  form.appendChild(label);
  form.appendChild(input);
  form.appendChild(output);
  output.value="50";
  document.getElementById("container").appendChild(form);

}
function updateTextInput(inputId,outputId){
  // console.log("aaa");
  var val= document.getElementById(inputId).value;
  console.log(val);
  var x =document.getElementById(outputId);
  x.value=val;
}

function setMat(){
  document.getElementById("btnId").style.display="none";
  var mat=new Array(namesArr.length);
  for(var i=0;i<namesArr.length;++i){
    mat[i]=new Array(itemsArr.length);
  }
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      mat[i][j]=parseInt(document.getElementById('input'+namesArr[i]+itemsArr[j]).value);
    }
  }
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      console.log(mat[i][j]);
    }
  }

  json=JSON.stringify({"values":mat,"num_of_agents":mat.length,"num_of_items":mat[0].length});

  // console.log(json);
  var xhr = new XMLHttpRequest();
  var url = "http://127.0.0.1:5000/calculator";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var jsona = JSON.parse(xhr.responseText);
      // console.log(jsona);
    }
  };
  var data = json;
  xhr.send(data);



  showChart(mat);
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

function showChart(mat){
  // mat=transpose(mat);
  result(mat);
}

function result(mat){
  document.getElementById("table-div").style.display="inline";
  var table=document.getElementById("my-table");
  for (var i = 0; i <namesArr.length; i++) {
    var row = table.insertRow();
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML = namesArr[i];
    var itemsStr="";
    for (var j = 0; j < mat[i].length; j++) {
      itemsStr+=mat[i][j]+"% of the "+itemsArr[j]+"<br>";
    }
    cell2.innerHTML = itemsStr;
  }

}


function transpose(a) {

  // Calculate the width and height of the Array
  var w = a.length || 0;
  var h = a[0] instanceof Array ? a[0].length : 0;

  // In case it is a zero matrix, no transpose routine needed.
  if(h === 0 || w === 0) { return []; }

  /**
  * @var {Number} i Counter
  * @var {Number} j Counter
  * @var {Array} t Transposed data is stored in this array.
  */
  var i, j, t = [];

  // Loop through every item in the outer array (height)
  for(i=0; i<h; i++) {

    // Insert a new row (array)
    t[i] = [];

    // Loop through every item per item in outer array (width)
    for(j=0; j<w; j++) {

      // Save transposed data.
      t[i][j] = a[j][i];
    }
  }

  return t;
}
