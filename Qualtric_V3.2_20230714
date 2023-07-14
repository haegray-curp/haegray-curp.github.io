let lines = new Array();
let boxIds = new Array();
let highlightedPhrases = new Array();
let causalRelationships = new Array();
let taggedText = "";

Qualtrics.SurveyEngine.addOnload(function()
{
	/*Place your JavaScript here to run when the page loads*/

});



Qualtrics.SurveyEngine.addOnReady(function()
{
// Remember when we started
var startTimer = new Date().getTime();
var qid = "${lm://Field/4}";
var id_CE = 0;
var boxToArrowMap = {};
let thisQ = this;
var isMergeMode = false;
var isArrowMode = false;
//thisQ.hideNextButton();
	
//Bucket Configurations
var bucketName = "causalnarratives";
var bucketRegion = "us-east-1";
const encoder = new TextEncoder();
var s3 = new AWS.S3({apiVersion: '2006-03-01',
						 accessKeyId: "AKIAWYK37YKXVINWVHEI",
						 secretAccessKey: "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"
						});

var customNext =document.getElementById("NextButton").cloneNode(true);
customNext.id = "CustomNextButton";
jQuery(customNext).appendTo("#Buttons");
jQuery("#NextButton").hide();
jQuery(customNext).css({
    "border": "none",
    "color": "#fff",
    "font-size": "16px",
    "padding": "8px 20px",
    "-webkit-border-radius": "4px",
    "-moz-border-radius": "4px",
    "-ms-border-radius": "4px",
    "-o-border-radius": "4px",
    "border-radius": "4px",
    "cursor": "pointer",
    "margin": "0",
    "text-align": "center",
    "text-decoration": "none",
    "-webkit-appearance": "none",
    "transition": "background .3s",
    "background-color": "#007ac0"
});

var id_prefix = "${e://Field/PROLIFIC_PID}"+"_"+qid+"_" ;
// Define an array to keep track of previous states
var undoStackText = [];
var undoStackMain = [];
var undoStackName=[];
document.getElementById('main').id =id_prefix +'main'
var selectedToDel = null;
var initialState =document.getElementById(id_prefix +'main').clone().childElementCount;

//----------------------------------------------------------------------------------------------------------------------
//---------------For Deleting Elements----------------------------------
//----------------------------------------------------------------------------------------------------------------------


function selectElement(target){
    if( !jQuery(target).hasClass("ui-selected")) 
         {
             if(target.id.indexOf("li")>=0){ jQuery("li").removeClass("ui-selected"); jQuery(target).addClass("ui-selected");}
			 else{ jQuery(target).addClass("ui-selected").siblings().removeClass("ui-selected");}
             selectedToDel = target;

             return 0;

         }
    else
    {
        event.preventDefault();
        jQuery(target).removeClass("ui-selected");
        return 0;
        

    }
 }
 
  jQuery("li").click(function(){selectElement(this);});

  jQuery(".instr").click(function()
  {
	  swal({   title: "Instructions",   
    text: "1)Your objective is to identify the primary causal structures by highlighting the phrases corresponding to each event and dragging and dropping them into boxes. \n2)You can use arrows to create your own causal graph as appropriate. \n 3)You can drag and drop multiple phrases into the same box if more than one phrase describes the same event \n 4)Simply select the phrase or arrow you want to delete and click 'Delete' to remove the phrase or arrow \n5)once you submit your answer, there is no option to return or revise"});
  });

 jQuery(document).on('click',"#btnDel",function () {
      if(selectedToDel == null) {return;}
    else
    {       
        if(selectedToDel.id.indexOf('arrow')<0)
        {
			if(selectedToDel.id.indexOf('li')>=0)
			{
					var textRm = selectedToDel.innerText.replace(/(\r\n|\n|\r)/gm, "");
					console.log(textRm);
					jQuery(".textHigh:contains('"+textRm+"')").removeClass("textHigh");

					if(selectedToDel.parentNode.childElementCount==1)
					{

						selectedToDel = selectedToDel.parentNode.parentNode.parentNode;
							console.log(boxToArrowMap[selectedToDel.id]);

							for (let idx in boxToArrowMap[selectedToDel.id])

							{
								var arr_id = "arrow_"+boxToArrowMap[selectedToDel.id][idx]._id;
								if(document.getElementById(arr_id))
								{
									jQuery("#"+arr_id).remove();


									for (let i=0;i<lines.length;i++)
										{
											if(lines[i]._id == boxToArrowMap[selectedToDel.id][idx]._id)
											{lines.splice(i, 1);}
										}
								}

							}
						//selectedToDel = selectedToDel.parentNode;
					}
			}
			
			else
			{
				console.log(selectedToDel.className)
			}

        }
        else{                
            
            for (let i=0;i<lines.length;i++)
            {
                if(lines[i]._id == selectedToDel.id.substring(6))
                {lines.splice(i, 1);}
            }
        }
        console.log("Removing " + selectedToDel.id);
        jQuery(selectedToDel).remove();
        
    }

 })
	
//----------------------------------------------------------------------------------------------------------------------
//---------------Make boxes Drggable----------------------------------
//----------------------------------------------------------------------------------------------------------------------
function boxDraggable(){

    jQuery( ".OuterboxCE" )
    .draggable(
        {
            cancel : '.lport,.rport,.tport,.bport', 
            containment: jQuery(".box-container"),
        
            drag: function(event,ui){

                console.log("Moving1: "+event.target.id);
				for (let i=0;i<lines.length;i++)
                {
					if(document.getElementById("arrow_"+lines[i]._id)){
						lines[i].position();
					}
                    
                };
				
			}
    })
    };

jQuery(document).ready(boxDraggable());



//----------------------------------------------------------------------------------------------------------------------
//---------------For drag and Drop - Text and drawing arrows----------------------------------
//----------------------------------------------------------------------------------------------------------------------
function createTextBox(){
	
    jQuery(".Disclaim").remove();
    id_CE = id_CE+1;
   
	var outerBox = document.createElement('div');
    outerBox.setAttribute('class','OuterboxCE');
	outerBox.setAttribute('id','Par_CE_'+qid+id_CE.toString());
	

    var ele = document.createElement('div');
    ele.setAttribute('class','boxCE rounded');
	ele.setAttribute('id','CE_'+qid+id_CE.toString());
	

	var txtChild = document.createElement('ul');
    ele.appendChild(txtChild);
    outerBox.appendChild(ele)

    return outerBox;
	
    };

function expandToWord(range)
    {
        if (range.collapsed)
        {
            return;
        }
    
        while (range.startOffset > 0 && range.toString()[0].match(/\w/))
        {
            console.log(range.startOffset);
            range.setStart(range.startContainer, range.startOffset - 1);
        }
    
        while (range.endOffset < range.endContainer.length && range.toString()[range.toString().length - 1].match(/\w/))
        {
            console.log(range.endOffset);
            range.setEnd(range.endContainer, range.endOffset + 1);
        }
        return range;
    };

function highlightRange(range) {

    range = expandToWord(range)
    var newNode = document.createElement("span");
    newNode.setAttribute(
       "style",
        "display: inline;"
    );
    newNode.setAttribute(
        "class",
         "textHigh"
     );
    range.surroundContents(newNode);
 
    return [range.toString(),range.startOffset.toString(),range.endOffset.toString()];

};
document.addEventListener("dragover", function(event) {
    event.preventDefault();
});
document.addEventListener("dragenter", function(event) {
    event.preventDefault();
});
document.addEventListener("dropover", function(event) {
    event.preventDefault();
});

document.addEventListener("dragstart" ,function(event) {

    event.dataTransfer.setData("text/plain", event.target.id+";"+event.target.className+";"+event.dataTransfer.getData("text"));
    
});

//----------------------------------------------------------------------------------------------------------------------
//---------------New Arrow Drawing----------------------------------
//----------------------------------------------------------------------------------------------------------------------

	
function getClosestElementOfClass(classname, x, y) {
  var closestElement = null;
  var closestDistance = Number.MAX_VALUE;

  $("." + classname).each(function() {
    var $element = $(this);
    var elementPosition = $element.offset();
    var elementX = elementPosition.left + $element.width() / 2;
    var elementY = elementPosition.top + $element.height() / 2;
    var distance = Math.sqrt(Math.pow(x - elementX, 2) + Math.pow(y - elementY, 2));

    if (distance < closestDistance) {
      closestDistance = distance;
      closestElement = $element;
    }
  });

  return closestElement;
}

	
function mergeToggle()
	
	{
				if(isMergeMode)
				{   		
					isMergeMode = false;

					ele1 = document.getElementById("btnMerge2")
					ele1.setAttribute("hidden", "hidden");
					ele2 = document.getElementById("btnMerge1")
					ele2.removeAttribute("hidden");
				}
		else
		{
				isMergeMode = true;
			ele1 = document.getElementById("btnMerge1")
			ele1.setAttribute("hidden", "hidden");
			ele2 = document.getElementById("btnMerge2")
			ele2.removeAttribute("hidden");
		}
	};
	
function drawToggle()
	
	{
				if(isArrowMode)
				{   		
					isArrowMode = false;

					ele1 = document.getElementById("btnDraw2")
					ele1.setAttribute("hidden", "hidden");
					ele2 = document.getElementById("btnDraw1")
					ele2.removeAttribute("hidden");
				}
		else
		{
				isArrowMode = true;
			ele1 = document.getElementById("btnDraw1")
			ele1.setAttribute("hidden", "hidden");
			ele2 = document.getElementById("btnDraw2")
			ele2.removeAttribute("hidden");
			document.body.style.cursor = "pointer";
		}
	};
	
	
jQuery(document).ready(function() {
    var startPoint = null;
    var selectedText = '';
    var src = null;
	
    // Listen for click events on the canvas or target area
    jQuery(document).click(function(event) {
		
		console.log(event.target);
      if (isArrowMode) {
        if (startPoint === null) {
			
					   	   	var givenElement = document.getElementById(id_prefix +'main');
      			var targetElement = event.target;
				while (targetElement !== null) {
					if (targetElement === givenElement) {
			
          // Set the starting point
          startPoint = getClosestElementOfClass("OuterboxCE",event.pageX,event.pageY)[0];
						return;
					}
					targetElement = targetElement.parentElement;
					
				}
			drawToggle();
			
				
        } else {
			
						
					   	   	var givenElement = document.getElementById(id_prefix +'main');
      			var targetElement = event.target;
				while (targetElement !== null) {
					if (targetElement === givenElement) {
          // Draw the arrow from starting point to endpoint
          var endPoint = getClosestElementOfClass("OuterboxCE", event.pageX, event.pageY )[0];
          line = new LeaderLine(startPoint, endPoint,{middleLabel: 'Causes'});
		  lines.push(line);
		  document.getElementsByClassName("leader-line")[lines.length-1].setAttribute("id","arrow_"+line._id);
			jQuery("#arrow_"+line._id.toString()).click(function(){selectElement(this);});


			if (boxToArrowMap[startPoint.id]) {
				boxToArrowMap[startPoint.id].push(line);
			} else {
				boxToArrowMap[startPoint.id] = [line];
			}

			if (boxToArrowMap[endPoint.id]) {
				boxToArrowMap[endPoint.id].push(line);
			} else {
				boxToArrowMap[endPoint.id] = [line];
			}

		
		console.log(boxToArrowMap);
					}
					targetElement = targetElement.parentElement;
				}
  
          // Reset the starting point
          startPoint = null;
			drawToggle();
					
		  
        }
      }
		else if(event.target.id == "btnDraw1")
	{
		startPoint = null;
		drawToggle();
		
	}
	else if(event.target.id == "btnMerge1")
	{
		src = null;
		mergeToggle();
		
	}
		
	else if (isMergeMode) 
{
   if(src === null)
   {
        var givenElement = document.getElementById(id_prefix +'main');
        var targetElement = event.target;
        while (targetElement !== null) {
            if (targetElement === givenElement) {
              // Click occurred in the hierarchy of the given element
              src = getClosestElementOfClass("OuterboxCE",event.pageX,event.pageY)[0];
              jQuery(src).addClass("selected").siblings().removeClass("selected");
              console.log("Click occurred within the hierarchy of the given element.");
              return;
            }
            targetElement = targetElement.parentElement;
          }
        src = null;
        mergeToggle();
   
   }
   else
   {
        var givenElement = document.getElementById(id_prefix +'main');
        var targetElement = event.target;
        while (targetElement !== null) {
            if (targetElement === givenElement) {
                
            dest = getClosestElementOfClass("OuterboxCE",event.pageX,event.pageY)[0];
            jQuery(dest).addClass("selected");
       
         if(src.id != dest.id)
         {
           src.children[0].children[0].innerHTML = src.children[0].children[0].innerHTML + dest.children[0].children[0].innerHTML;
           jQuery("li").click(function(){selectElement(this);});
           for (let i=0;i<lines.length;i++)
           {
               if(lines[i].start.id == dest.id)
               {
                   lines[i].start.id = src.id;
                   lines[i].position();
               }
               if(lines[i].end.id == dest.id)
               {
                   lines[i].end.id = src.id;
                   lines[i].position();
               }
               // Remove the arrow that was connecting the two boxes
               if((lines[i].start.id == src.id && lines[i].end.id == dest.id) || (lines[i].start.id == dest.id && lines[i].end.id == src.id))
               {
                   lines[i].remove();
                   lines.splice(i, 1);
                   i--; // Decrement i to account for the removed element
               }
           }
            jQuery(dest).siblings().removeClass("selected");
           jQuery(dest).remove();
         }
           src = null;
           mergeToggle();
            return;
            }
                
            targetElement = targetElement.parentElement;
          }
   
        mergeToggle();
   
   }
}
		
else if(event.target.nodeName.indexOf("P")==0 || event.target.nodeName.indexOf("H")==0)
    {
		const [completeText,start,end] = highlightRange(window.getSelection().getRangeAt(0));
		console.log("Highlightext text : "+ completeText);
		
		if(completeText.length > 1)
			
		{
        
        
		undoStackText.push(jQuery("#txt").clone());
		undoStackMain.push(jQuery("#" +id_prefix+"main").clone());
        var ele = createTextBox();
        
        // ele.style.position = "absolute";
        ele.style.left = event.pageX;
        ele.style.top = event.pageY;
		console.log(qid);
        var id_target = event.target.id;
        var eleChild = ele.getElementsByTagName("ul")[0];
        var txtChild = document.createElement('li');
        txtChild.setAttribute('id','li_'+start+"_"+end);
		txtChild.innerHTML = completeText;
        eleChild.appendChild(txtChild);
		console.log(eleChild);
		ele.children[0].children[0] = eleChild;
        
        document.getElementById(id_prefix +"main").appendChild(ele);
        jQuery(txtChild).click(function(){selectElement(this);});
        boxDraggable();
        undoStackName.push("txt+container");
		

    
			document.getSelection().removeAllRanges();
		}
		
		else
		{
			if(event.target.id.indexOf("arrow_")>=0)
			   {
				   selectElement(event.target);
			   }
		
		}
	}
		
    });
});


//----------------------------------------------------------------------------------------------------------------------
//---------------New Arrow Drawing ENDS----------------------------------
//----------------------------------------------------------------------------------------------------------------------
	
	
function JSalert(){
	swal({   title: "You cannot go to the previous question once you proceed",   
    text: "Are you sure there is no Causal Relationship?",   
    type: "warning",   
    showCancelButton: true,   
    confirmButtonColor: "#DD6B55",   
    confirmButtonText: "Yes, there is no Causal Relationship!",   
    cancelButtonText: "No, I want to check again!",   
    closeOnConfirm: false,   
    closeOnCancel: false }); 
    /* function(isConfirm){   
        if (isConfirm) 
    {   
        console.log("");   
        } 
        else {     
            swal("Hurray", "Account is not removed!", "error");   
            }}			);*/
};
	
//----------------------------------------------------------------------------------------------------------------------
//-------------------------------------------Export Final Output-------------------------------------------------
//----------------------------------------------------------------------------------------------------------------------

	
	
function exportFinalOutput() {
    highlightedPhrases = [];
    boxIds = [];
    //taggedText = jQuery("#txt").html();

    jQuery(".OuterboxCE").each(function() {
        let boxId = this.id;
        jQuery("#" + boxId + " ul li").each(function() {
            let highlightedPhrase = this.innerText;
            highlightedPhrases.push(highlightedPhrase);
            boxIds.push(boxId);
        });
    });

    causalRelationships = lines.map(line => {
        return {
            fromId: line.start.id,
            toId: line.end.id
        };
    });
	
	// Update taggedText with the final version
	taggedText = "";
	const finalText = document.getElementById('txt').innerHTML;
	const parser = new DOMParser();
	const doc = parser.parseFromString(finalText, 'text/html');
	const highlightedElements = doc.querySelectorAll('.textHigh');
	const finalOutput = document.createElement('div');
	function traverseDOM(node) {
		for (let child of node.childNodes) {
			if (child.nodeType === Node.ELEMENT_NODE) {
				if (child.classList.contains('textHigh') && !child.classList.contains('deleted')) {
					const newElement = document.createElement('highlighted');
					newElement.innerHTML = child.innerHTML;
					finalOutput.appendChild(newElement);
				} else {
					traverseDOM(child);
				}
			} else if (child.nodeType === Node.TEXT_NODE) {
				finalOutput.appendChild(child.cloneNode());
			}
		}
	}
	traverseDOM(doc.body);
	taggedText = finalOutput.innerHTML;
	var endTimer = new Date().getTime();
	

	var htmlResp = document.getElementById(id_prefix +'main').innerHTML ;
	// given certain loop, save data
	if (parseInt("${lm://Field/4}")==1){
    Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases1", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships1", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds1", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText1", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time1", (endTimer-startTimer));
	Qualtrics.SurveyEngine.setEmbeddedData("html1", htmlResp);
		
	} else if (parseInt("${lm://Field/4}")==2){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases2", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships2", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds2", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText2", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time2", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html2", htmlResp);
		
	} else if (parseInt("${lm://Field/4}")==3){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases3", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships3", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds3", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText3", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time3", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html3", htmlResp);
	} else if (parseInt("${lm://Field/4}")==4){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases4", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships4", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds4", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText4", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time4", (endTimer-startTimer));	
		Qualtrics.SurveyEngine.setEmbeddedData("html4", htmlResp);
	} else if (parseInt("${lm://Field/4}")==5){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases5", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships5", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds5", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText5", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time5", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html5", htmlResp);
	} else if (parseInt("${lm://Field/4}")==6){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases6", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships6", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds6", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText6", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time6", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html6", htmlResp);
	} else if (parseInt("${lm://Field/4}")==7){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases7", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships7", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds7", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText7", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time7", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html7", htmlResp);
	} else if (parseInt("${lm://Field/4}")==8){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases8", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships8", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds8", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText8", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time8", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html8", htmlResp);
	} else if (parseInt("${lm://Field/4}")==9){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases9", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships9", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds9", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText9", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time9", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html9", htmlResp);
	} else if (parseInt("${lm://Field/4}")==10){
	Qualtrics.SurveyEngine.setEmbeddedData("highlightedPhrases10", JSON.stringify(highlightedPhrases));
    Qualtrics.SurveyEngine.setEmbeddedData("causalRelationships10", JSON.stringify(causalRelationships));
    Qualtrics.SurveyEngine.setEmbeddedData("boxIds10", JSON.stringify(boxIds));
    Qualtrics.SurveyEngine.setEmbeddedData("taggedText10", taggedText);
	Qualtrics.SurveyEngine.setEmbeddedData("time10", (endTimer-startTimer));
		Qualtrics.SurveyEngine.setEmbeddedData("html10", htmlResp);
	}
	
	
	
	
}

	
jQuery("#CustomNextButton").on('click',function (event) {
	

	
	curState = document.getElementById(id_prefix +'main').childElementCount;
	console.log(curState);
    var boxesConnected = new Set(lines.map(line => line.start.id).concat(lines.map(line => line.end.id)));
    console.log(boxesConnected);
	var num_boxes = document.getElementsByClassName("OuterboxCE").length;
	
	//if(curState == 1)
	if(num_boxes<2)
	{

		swal({   title: "Are you sure there is no Causal Relationship?",   
    text: "You cannot go to the previous question once you proceed",   
    type: "warning",   
     buttons: {
						cancel: "No! I want to check again",
						defeat: "Yes, there is no Causal Relationship!",
					  }})
					.then((value) => {
					  switch (value) {

						case "defeat":
							  exportFinalOutput();
							  thisQ.clickNextButton();
							  break;
					  }
					});
	}
	else if(boxesConnected.size != num_boxes)
	{


		swal({   title: "Not all the text boxes have an arrow associated!",   
    text: "You cannot go to the previous question once you proceed",   
    type: "warning",   
     buttons: {
						cancel: "No! Stay on this page",
						defeat: "Yes! proceed.",
					  }})
					.then((value) => {
					  switch (value) {

						case "defeat":
							  exportFinalOutput();
							  thisQ.clickNextButton();
							  break;
					  }
					});
	}
	else {
		exportFinalOutput();
        jQuery("#CustomNextButton").hide();
        thisQ.clickNextButton();}
	
});
	
jQuery("#btnExit").on('click',function (event) {
	

	Qualtrics.SurveyEngine.setEmbeddedData("exit",1);
	curState = document.getElementById(id_prefix +'main').childElementCount;
	console.log(curState);
    var boxesConnected = new Set(lines.map(line => line.start.id).concat(lines.map(line => line.end.id)));
    console.log(boxesConnected);
	var num_boxes = document.getElementsByClassName("OuterboxCE").length;
	
	//if(curState == 1)
	if(num_boxes<2)
	{

		swal({   title: "Are you sure there is no Causal Relationship?",   
    text: "You cannot go to the previous question once you proceed",   
    type: "warning",   
     buttons: {
						cancel: "No! I want to check again",
						defeat: "Yes, there is no Causal Relationship!",
					  }})
					.then((value) => {
					  switch (value) {

						case "defeat":
							  exportFinalOutput();
							  thisQ.clickNextButton();
							  break;
					  }
					});
	}
	else if(boxesConnected.size != num_boxes)
	{


		swal({   title: "Not all the text boxes have an arrow associated!",   
    text: "You cannot go to the previous question once you proceed",   
    type: "warning",   
     buttons: {
						cancel: "No! Stay on this page",
						defeat: "Yes! proceed.",
					  }})
					.then((value) => {
					  switch (value) {

						case "defeat":
							  exportFinalOutput();
							  thisQ.clickNextButton();
							  break;
					  }
					});
	}
	else {
		exportFinalOutput();
        //jQuery("#CustomNextButton").hide();
       thisQ.clickNextButton();
	}
	
});
 

});

Qualtrics.SurveyEngine.addOnUnload(function()
{
	/* Q1 Place your JavaScript here to run when the page is unloaded
	document.removeEventListener('drop',fn_drop, false); */
	 for (let i=0;i<lines.length;i++)
                {
                    lines[i].remove();
                };


});
