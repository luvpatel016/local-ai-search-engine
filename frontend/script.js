const uploadButton = document.getElementById("uploadButton"); 
const searchButton = document.getElementById("searchButton");
const searchInput = document.getElementById("searchInput");
const fileInput = document.getElementById("fileInput");
const results = document.getElementById("results");

uploadButton.addEventListener("click", function () {

    const file = fileInput.files[0];

    const formData = new FormData();

    formData.append("file", file);

    fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
});

searchButton.addEventListener("click", function () { 
    
    const query = searchInput.value;
    
    fetch(
    "http://127.0.0.1:8000/search?query=" +
    encodeURIComponent(query)
)
    .then(response => response.json())
    .then(data => {
        results.innerHTML = "<p>" + data.query_received + "</p>";
    });
});