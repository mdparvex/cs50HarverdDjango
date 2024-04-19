let counter = 0;
function count(){
	let heading = document.querySelector('h1');
	counter ++;
	heading.innerHTML = counter;

	if(counter % 10 === 0){
		alert(`counter is ${counter}`);
	}
			
			
}
document.addEventListener('DOMContentLoaded', function(){
		document.querySelector('button').onclick = count;
	});