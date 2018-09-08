function count() {
	var form = document.getElementById("formid1");
	var count = 0;
	for(var i=0; i<form.children.length; i+=1){
		if(form.children[i].checked){
			count += 1;
			//count++;
		}
	}
	//console.log(count);
	alert(count);
};

/*
function count2(){
	var forms = document.getElementsByClassName("mycheckbox");
	var count = 0;
	console.log(forms);
	Array(forms).forEach( function (box){
	    console.log(box);
	//forms.forEach( (box) => {
		if(box.checked){
			count++;
		}
	});
	alert(count);
}
*/

