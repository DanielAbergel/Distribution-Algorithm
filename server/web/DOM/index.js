var namesArr=[];
var itemsArr=[];
var emailCheck=false;
var count=0;

// this function will create 2 Selectpicker with for loop and a button that called "MOVE TO STEP 2"
function addS(){
  // peopleOPT & itemOPT - Selectpicker variables
  var peopleOPT = document.getElementById("peopleSelect");
  var itemOPT = document.getElementById("itemSelect");
  // for loop that open the number of people Selectpicker (between 2 to 4)
  for (var i = 2; i <= 4; i++) {
    var pOption = document.createElement("option");
    pOption.text = i;
    peopleOPT.add(pOption);
  }
// for loop that open the number of items Selectpicker (between 1 to 18)
  for (var j = 1; j <= 18; j++) {
    var iOption = document.createElement("option");
    iOption.text = j;
    itemOPT.add(iOption);
  }
// create the button "move to step 2" when its clicked the insertNames function will call
  var selectBtn = document.createElement("BUTTON");
  selectBtn.id="selectBtn";
  selectBtn.innerHTML = "MOVE TO STEP 2";
  selectBtn.onclick=insertNames;
  // css styling to "MOVE TO STEP 2" button
  selectBtn.classList.add("btn-secondary");
  selectBtn.classList.add("btn");
  selectBtn.classList.add("myButtons");
// add to document.body a child (selectBtn button)
  document.body.appendChild(selectBtn);

}
// insert the clients name to the filed nameInput
function insertNames(){
  //checks if the email div is exist. if yes it check that the input is not null.
  var check = document.getElementById("emailId");
  if(check){
  if(document.getElementById("emailInput").value==""&&emailCheck){
    alert("You have to fill all of the fields");
    return false;
  }
  document.getElementById("emailId").style.display="none";
}
if(count==0){
  // filed the var defaultNames with default names
  var defaultNames=["Alice","Bob","Carol","Dave"];
  // This command delete the selectStep class
  document.getElementById("selectStep").style.display="none";
  // This command delete the selectStep createElement
  document.getElementById("selectBtn").style.display="none";

  // Entering the value that chosen into the variable numOFpeople
  var numOFpeople=document.getElementById("peopleSelect").value;
// create a div called divP
  var divP = document.createElement("div");
  divP.id="divP";
// insert text to divP
  divP.innerHTML="<h1>step2:</h1><h2>Insert the participants names</h2>";
// this for loop create divs elements (Name number +i)
  for (i=1;i<=numOFpeople;i++){
    var divPpart = document.createElement("div");
// css styling to the div "divPpart"
    divPpart.classList.add("input-style");
// add to divPpart a child (text - Name number +i)
    divPpart.appendChild(document.createTextNode("Name number "+i));
// create an input text element
    var nameInput = document.createElement("input");
    nameInput.id = "name"+i;
    // take the names from defaultNames array to nameInput
    nameInput.value=defaultNames[i-1];
    // add to divPpart a child (text - that found in nameInput "name+i")
    divPpart.appendChild(nameInput);
    // add to divP a child (div - contains divPpart that create in this for loop)
    divP.appendChild(divPpart);
    // add to divP a child (br - downline)
    divP.appendChild(document.createElement("br"));
  }


// create a button element, the name is insertNamesBtn and when it's clicked it's called insertItems function
  var insertNamesBtn = document.createElement("BUTTON");
  insertNamesBtn.id="insertNamesBtn";
  // the text on the button
  insertNamesBtn.innerHTML = "MOVE TO STEP 3";
  //the function that calld when insertNamesBtn clicked
  insertNamesBtn.onclick=insertItems;
  // css styling to the button "insertNamesBtn"
  insertNamesBtn.classList.add("btn-secondary");
  insertNamesBtn.classList.add("btn");
  insertNamesBtn.classList.add("myButtons");
  // add to container a child (divP - <h1>step2:</h1><h2>Insert the participants names</h2)
  container.appendChild(divP);
  // add to document.body a child (insertNamesBtn - button that call the function insertItems)
  container.appendChild(insertNamesBtn);

  var numberOFpeople=document.getElementById("peopleSelect").value;
  //checks if number of people is 4. if it is so we activate the insertEmail function.
  if(numberOFpeople=="4"&&count==0){
    insertEmail();
    return;
  }
}else{
  document.getElementById("divP").style.display="inline";
  document.getElementById("insertNamesBtn").style.display="inline";
}

}
//if number of people is 4. if it is so we activate the insertEmail function and let the user insert email address.
function insertEmail(){
  count++;
  emailCheck=true;
  document.getElementById("divP").style.display="none";
  document.getElementById("insertNamesBtn").style.display="none";
  document.getElementById("emailId").style.display="inline";

  var insertNamesBtn = document.createElement("BUTTON");
  insertNamesBtn.id="mailBtn";
  insertNamesBtn.innerHTML = "MOVE TO STEP 2";
  insertNamesBtn.onclick=insertNames;
  insertNamesBtn.classList.add("btn-secondary");
  insertNamesBtn.classList.add("btn");
  insertNamesBtn.classList.add("myButtons");
  document.getElementById("emailId").appendChild(insertNamesBtn);
}

// insert the items name to the filed itemInput
function insertItems(){
document.getElementById("divP").style.display="none";
  var numOFpeople=document.getElementById("peopleSelect").value;
// validation to check if the num of people filds is whit some text
  for (var i = 1; i <= numOFpeople; i++) {
    if(document.getElementById("name"+i).value==""){
      alert("You have to fill all of the fields");
      return false;
    }
    // push the names that we filed into namesArr
    namesArr.push(document.getElementById("name"+i).value);
  }
  // filed the var defaultItems with default items
  defaultItems=["Armchair","Bed","Chair","Desk","Easy chair","Futon","Game table","Hammock","Iron","Jeep","Kitchen island","Lamp","Mattress","Nightstand","Office chair","Pillow","Quill","Rug"];
// This command delete the divP class
  // document.getElementById("divP").style.display="none";
// This command delete the insertNamesBtn class
  document.getElementById("insertNamesBtn").style.display="none";
// Entering the value that chosen into the variable numOFitems
  var numOFitems=document.getElementById("itemSelect").value;
// create a div called divI
  var divI = document.createElement("div");
  divI.id="divI";
  // insert text to divI
  divI.innerHTML="<h1>step3:</h1><h2>Insert the items names</h2>";
// this for loop create divs elements (Item number +i)
  for (i=1;i<=numOFitems;i++){
    var divIpart = document.createElement("div");
    // css styling to the div "divIpart"
    divIpart.classList.add("input-style");
    // add to divIpart a child (text - Item number +i)
    divIpart.appendChild(document.createTextNode("Item number "+i));
// create an input text element
    var itemInput = document.createElement("input");
    itemInput.id = "item"+i;
    // take the items from defaultItems array to itemInput
    itemInput.value=defaultItems[i-1];
    // add to divIpart a child (text - that found in itemInput "name+i")
    divIpart.appendChild(itemInput);
    // add to divI a child (div - contains divIpart that create in this for loop)
    divI.appendChild(divIpart);
    // add to divI a child (br - downline)
    divI.appendChild(document.createElement("br"));
  }
  // create a button element, the name is insertItemsBtn and when it's clicked it's called getDetails function
  var insertItemsBtn = document.createElement("BUTTON");
  insertItemsBtn.id="insertItemsBtn";
  // the text on the button
  insertItemsBtn.innerHTML = "MOVE TO STEP 4";
  //the function that calld when insertItemsBtn clicked
  insertItemsBtn.onclick=getDetails;
  // css styling to the button "insertNamesBtn"
  insertItemsBtn.classList.add("btn-secondary");
  insertItemsBtn.classList.add("btn");
  insertItemsBtn.classList.add("myButtons");
  // add to container a child (divP - <h1>step3:</h1><h2>Insert the items names</h2)
  container.appendChild(divI);
  // add to document.body a child (insertItemsBtn - button that call the function getDetails)
  document.body.appendChild(insertItemsBtn);


}
function getDetails() {
// Entering the values that chosen into the variables numOFpeople & numOFitems
  var numOFpeople=document.getElementById("peopleSelect").value;
  var numOFitems=document.getElementById("itemSelect").value;
// validation to check if the num of items filds is whit some text
  for (var j = 1; j <= numOFitems; j++) {
    if(document.getElementById("item"+j).value==""){
      alert("You have to fill all of the fields");
      return false;
    }
    // push the items that we filed into itemsArr
    itemsArr.push(document.getElementById("item"+j).value);
  }
  // This command delete the insertItemsBtn button
  document.getElementById("insertItemsBtn").style.display="none";
// call the function add fields
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
  // insert text to container
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
      //create slider component for each participant to item
      slider(namesArr[i],itemsArr[j]);
    }
  }
  // Create a rescale <button> element
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
  email=document.getElementById("emailInput").value;
  console.log(email);
  json=JSON.stringify({"values":mat,"problem": document.getElementById("alg2").checked ? "EnvyFree" : "Proportional","agents":namesArr,"items":itemsArr,"num_of_agents":mat.length,"num_of_items":mat[0].length , "email": email });

  var loader =document.createElement("div");
  loader.id="loaderId";
  loader.classList.add("loader");
document.body.appendChild(loader);

 // result(mat,mat);
  console.log(json);
  var xhr = new XMLHttpRequest();
  var url = "https://fairness-algorithm.herokuapp.com/calculator";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var responseText = JSON.parse(xhr.responseText);
      if(namesArr.length>3){
        window.location.replace("https://fairness-algorithm.herokuapp.com/email.html");
      }else{
        var html=responseText.url;
        window.location.replace(html);
      }
    }
  };
  var data = json;
  xhr.send(data);
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
