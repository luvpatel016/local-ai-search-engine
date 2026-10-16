const uploadButton = document.getElementById("uploadButton"); 
const searchButton = document.getElementById("searchButton");
const searchInput = document.getElementById("searchInput");

uploadButton.addEventListener("click", function () { 
    console.log("Upload button clicked");
});

searchButton.addEventListener("click", function () { 
    const query = searchInput.value;
    console.log(query);
});