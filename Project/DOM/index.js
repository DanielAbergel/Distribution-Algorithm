
var namesArr;
var itemsArr;
function getDetails() {
  var people = document.getElementById("peopleInput").value;
  var items = document.getElementById("itemsInput").value;
  namesArr=people.split(',');
  itemsArr=items.split(',');
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
    for (j=0;j<numOFitems;j++){
      // Append a node with it's text
      container.appendChild(document.createTextNode(namesArr[i]+" rate for "+itemsArr[j]));
      // Create an <input> element, set its type and name attributes
      var input = document.createElement("input");
      input.type = "number";
      input.id = "rate"+i+j;
      container.appendChild(input);
      // Append a line break
      container.appendChild(document.createElement("br"));
    }
  }
  // var button= document.createElement("input");
  // button.type = "submit";
  // button.name = "button";
  // container.appendChild(button);
  var btn = document.createElement("BUTTON");   // Create a <button> element
  btn.innerHTML = "send";                   // Insert text
  btn.setAttribute("id", "btnId");
  document.body.appendChild(btn);
  document.getElementById("btnId").onclick = setMat;

}

function setMat(){
  var mat=new Array(namesArr.length);
  for(var i=0;i<namesArr.length;++i){
    mat[i]=new Array(itemsArr.length);
  }
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      mat[i][j]=document.getElementById('rate'+i+j).value;
    }
  }
  for (i=0;i<namesArr.length;i++){
    for (j=0;j<itemsArr.length;j++){
      console.log(mat[i][j]);
    }
  }

}
