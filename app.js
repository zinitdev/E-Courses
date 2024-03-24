async function loadCategories() {
	let res = await fetch('http://127.0.0.1:8000/categories/');
	let data = await res.json();

	let results = await data.results;

	let menu = document.getElementById('menu');

	for (const i in results) {
		menu.innerHTML += `<li>${results[i].url} - ${results[i].name}</li>`;
	}
}

window.onload = () => {
	loadCategories();
};
